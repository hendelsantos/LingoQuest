# LingoQuest — English Academy

**Especificação de produto, requisitos e implementação do MVP**  
Versão 1.0 · 15/11/2026 · MH Software  
Documento de referência para desenvolvimento orientado por IA no VS Code.

> **Objetivo:** construir uma escola digital de inglês com identidade visual própria, aprendizado gamificado, aulas com professores, caderno individual e gestão administrativa e financeira. O software deve funcionar de ponta a ponta, com dados persistidos, contas reais e permissões verificadas no backend.

Protótipo visual aprovado: [LingoQuest](https://lingoquest-english-academy.attentivelark2.chatgpt.site).  
Referência de direção visual: [Construct](https://www.construct.net/en). O objetivo é reinterpretar a linguagem visual, sem copiar marca, código ou personagens de terceiros.

---

## 1. Instruções para iniciar com um agente de programação

Abra uma pasta vazia no VS Code, coloque este arquivo na raiz como `SPEC.md` e use o agente de sua preferência (GitHub Copilot, Claude Code, Codex ou equivalente). Envie a instrução abaixo:

```text
Leia integralmente SPEC.md. Você é o engenheiro responsável pelo MVP
LingoQuest. Construa um monorepo com Django REST Framework, PostgreSQL e
Next.js TypeScript, seguindo os requisitos, regras, contratos da API e
critérios de aceite. Primeiro examine a pasta, crie um plano e implemente
somente a Fase 0 do roadmap. Use código organizado, migrations,
testes de autorização e documentação de execução. Não inclua segredos,
não invente integrações e não simule sucesso de pagamentos ou vídeo.
Ao terminar uma fase, execute os testes e informe arquivos modificados,
comandos utilizados, resultados e próximos passos. Avance em pequenos
commits somente depois de verificar cada fase. Preserve o design aprovado.
Não substitua requisitos por funcionalidades desconectadas ou mockups.
```

**Contrato de trabalho:** este documento é a fonte inicial de verdade. Antes de alterar arquitetura, regras de autorização ou escopo, registrar a decisão em `docs/adr/`. A aplicação não deve depender do ChatGPT Sites para sua operação. A MH Software será proprietária do repositório e controlará o deployment.

## 2. Visão do produto

### 2.1 Proposta de valor

LingoQuest combina três experiências em um só lugar:

1. Aprender inglês por missões curtas, com feedback imediato e progressão.
2. Estudar com professores por aulas individuais ou em grupo, acompanhadas de atividades personalizadas.
3. Administrar uma escola digital: alunos, agenda, matrículas, planos e mensalidades.

**Público inicial:** brasileiros adultos que precisam aprender inglês do zero ou reforçar a base para trabalhar, viajar e conversar; professores particulares e pequenos cursos. A linguagem deve ser acolhedora, mas não infantilizada. Começar com português brasileiro na interface e conteúdo em inglês, aumentando a exposição ao idioma conforme o progresso.

**Hipótese a validar:** a união de estudo autônomo e acompanhamento humano melhora a frequência de estudo e reduz o esforço administrativo do professor.

### 2.2 Perfis de acesso

| Perfil | Responsabilidade | Não pode |
|---|---|---|
| Visitante | Conhecer a escola, consultar planos, entrar em sua conta | Acessar dados privados |
| Aluno | Estudar, resolver missões, anotar, entregar tarefas, entrar nas próprias aulas e consultar cobranças | Acessar informações de outros alunos, administrar pagamentos ou publicar aulas |
| Professor | Gerenciar suas próprias turmas e aulas, atribuir tarefas, corrigir entregas e acompanhar estudantes vinculados | Administrar finanças, alterar permissões ou acessar cadernos privados |
| Administrador | Gerenciar usuários, cursos, conteúdo, matrículas, professores, agenda, planos e finanças | Acessar senhas, tokens e dados de cartão; acessar anotações privadas por padrão |

No MVP, uma instalação atende uma escola. A estrutura de domínio deve permitir futuramente adaptar-se a múltiplas escolas; **não implementar multi-tenancy, subcontas, marketplace nem sistema de royalties agora**. Os papéis são atribuídos no backend, não por um botão que altera o privilégio do usuário. O seletor de perfis do protótipo era apenas demonstrativo.

### 2.3 Resultados esperados e indicadores iniciais

| Indicador | Definição |
|---|---|
| Alunos ativos | Matrículas ativas na data de consulta |
| Ativação | Alunos novos que completaram a primeira missão em até 7 dias / novos matriculados |
| Retenção semanal | Alunos que realizaram ao menos uma atividade válida em duas semanas consecutivas / ativos na semana anterior |
| Progresso do curso | Lições obrigatórias aprovadas / lições obrigatórias publicadas na trilha matriculada |
| Presença em aulas | Participantes com presença confirmada / participantes esperados em aulas realizadas |
| Receita recebida | Soma de cobranças confirmadas como pagas no período pela data de confirmação |
| Financeiro em aberto | Soma das cobranças pendentes ou vencidas, sem incluir cancelamentos |

Não declarar que uma missão garante fluência ou certificação oficial. Os níveis A1–C2 são uma estrutura de organização inspirada no CEFR; não atribuir proficiência oficial sem avaliação apropriada.

## 3. Escopo e limites do primeiro MVP

| Módulo | Entrega obrigatória | Evolução posterior |
|---|---|---|
| Site público | Landing page, metodologia, planos, login responsivo | Blog, SEO avançado, campanhas |
| Identidade | Login, logout, convite, recuperação de senha, perfis e permissões | OAuth social, MFA para todos |
| Aprendizado | Curso A1 inicial com 8 missões publicadas e 24 perguntas, feedback e reprodução de áudio | A2–C2 completos, áudio humano, avaliações adaptativas |
| Gamificação | XP, missões concluídas, conquistas e progressão | Sequência diária, moedas, avatar editável, ranking opt-in |
| Caderno digital | Criar, listar, editar, excluir e pesquisar notas privadas | Flashcards e revisão espaçada |
| Aulas | Agenda individual/grupo, controle de acesso, presença manual, link HTTPS; sala integrada LiveKit mediante credenciais | Gravação, quadro branco, transcrição e grupos avançados |
| Atividades | Professor cria tarefa, aluno envia resposta escrita, professor corrige | Upload de arquivos, rubricas avançadas |
| Gestão | Alunos, professores, matrícula, turmas, conteúdo e relatórios básicos | Gestão de leads e comunicação em massa |
| Financeiro | Planos, cobranças, vencimentos, baixa manual auditada; integração Asaas sandbox como incremento | Cobranças em produção, recorrência automática, split |
| Segurança | Permissões por objeto, CSRF, validação, proteção contra abuso, logs e backups | Auditorias especializadas e controles corporativos |

**MVP utilizável:** começar com funcionalidades manuais reais, depois habilitar vídeo nativo e pagamentos em sandbox. O sistema deve funcionar mesmo quando LiveKit e Asaas estiverem desativados. Nenhum botão deve fingir que uma cobrança ou uma aula foi realizada.

## 4. Arquitetura técnica proposta

### 4.1 Stack

| Camada | Escolha | Motivo |
|---|---|---|
| Backend | Python 3.12+, Django 5.2 LTS, Django REST Framework | ORM, migrations, autenticação, admin, permissões e bom suporte à evolução |
| Banco | PostgreSQL | FKs, constraints, transações, concorrência e integridade financeira |
| Frontend | Next.js App Router + TypeScript | Landing page, dashboard, componentes e rotas organizadas |
| UI | Tailwind CSS, componentes próprios acessíveis, Lucide icons | Identidade visual consistente e reaproveitamento |
| Data fetching | `fetch` tipado; TanStack Query opcional | Carregamento, cache e invalidação após mutations |
| Validação | DRF serializers; Zod/form validation no frontend | Contratos claros; backend é definitivo |
| Documentação API | drf-spectacular / OpenAPI | Facilita integração, testes e evolução do contrato |
| Vídeo | LiveKit + SDK web e SDK de servidor Python | Sala de vídeo/áudio integrada sem desenvolver infraestrutura WebRTC própria |
| Pagamentos | Asaas (sandbox primeiro) | Pix, cartão/checkout hospedado, cobranças e eventos |
| Tarefas | Comandos Django + scheduler confiável; Celery/Redis somente quando necessário | Reduz complexidade operacional inicial |
| Testes | pytest/pytest-django, DRF APIClient, Vitest, Playwright | Cobrem regras, API, componentes e fluxo real |
| Hospedagem | Railway (backend, frontend e PostgreSQL); domínio próprio com HTTPS | Adequado à infraestrutura já usada pela MH Software |

Fixar versões compatíveis no lockfile (Python e npm) e confirmar bibliotecas na documentação oficial durante a implementação. Evitar misturar Django templates e React para as mesmas telas. Django Admin deve ser um backoffice técnico protegido; os usuários da escola utilizarão a interface Next.js.

### 4.2 Fluxo de arquitetura

```mermaid
flowchart TD
    U[Aluno / Professor / Admin] --> W[Next.js - Web]
    W -->|API JSON / sessão| A[Django REST Framework]
    A --> P[(PostgreSQL)]
    A -->|Token de sala| L[LiveKit]
    W <-->|Vídeo e áudio| L
    A -->|Cobrança| G[Asaas]
    G -->|Webhook autenticado| A
```

- A sessão e as autorizações são controladas exclusivamente pelo Django.
- O frontend nunca consulta diretamente PostgreSQL, API administrativa do Asaas ou segredo do LiveKit.
- O servidor Django valida a relação entre usuário, matrícula, turma, aula, tarefa ou cobrança antes de qualquer leitura ou alteração.
- As integrações são adaptadores, não dependências do núcleo de aprendizado.
- Implementar um **monólito modular**, não microserviços. Utilizar transações sempre que uma resposta, XP, matrícula ou evento de pagamento alterar registros relacionados.
- Em produção, servir frontend e API sob uma origem pública única, por exemplo `https://english.mhsoftware.com.br` com `/api/v1/*` encaminhado ao Django. O subdomínio é uma sugestão, não uma configuração já realizada. Priorizar domínio único para simplificar cookies e CSRF. Localmente usar proxy/rewrite do Next.js para `/api/v1/*`.

## 5. Estrutura do repositório

```text
lingoquest/
├── SPEC.md
├── README.md
├── .gitignore
├── .env.example
├── docker-compose.yml
├── Makefile                         # alvos opcionais para Linux
├── docs/
│   ├── adr/
│   ├── architecture.md
│   └── api.md
├── backend/
│   ├── manage.py
│   ├── pyproject.toml
│   ├── config/
│   │   ├── settings/
│   │   │   ├── base.py
│   │   │   ├── development.py
│   │   │   └── production.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── apps/
│   │   ├── accounts/
│   │   ├── learning/
│   │   ├── gamification/
│   │   ├── notebook/
│   │   ├── classroom/
│   │   ├── assignments/
│   │   ├── billing/
│   │   └── audit/
│   ├── tests/
│   └── integrations/
│       ├── livekit.py
│       └── asaas.py
└── frontend/
    ├── package.json
    ├── src/
    │   ├── app/
    │   │   ├── (public)/
    │   │   ├── (student)/app/
    │   │   ├── (teacher)/teacher/
    │   │   └── (admin)/dashboard/
    │   ├── components/
    │   │   ├── ui/
    │   │   ├── layout/
    │   │   ├── mascot/
    │   │   └── learning/
    │   ├── features/
    │   ├── lib/
    │   │   ├── api.ts
    │   │   ├── auth.ts
    │   │   └── types.ts
    │   └── styles/
    ├── public/
    │   ├── brand/
    │   └── characters/
    └── tests/
```

Organização por domínio no Django: `models.py`, `serializers.py`, `views.py`, `urls.py`, `permissions.py`, `services.py` e `tests/`. Extrair serviços apenas quando houver lógica de negócio real. Fazer `get_queryset()` restringir o universo de dados antes de filtros, paginação ou serialização. Evitar importações circulares.

## 6. Modelo de dados

Convenções: chaves primárias UUID em objetos expostos pela API; `created_at` e `updated_at`; UTC no banco, exibição em `America/Sao_Paulo`; timestamps ISO 8601 com fuso na API. Preços e valores financeiros usam `DecimalField(max_digits=12, decimal_places=2)`, enviados como strings decimais. Nunca usar `float` para cálculos de dinheiro.

### 6.1 Contas e matrículas

| Modelo | Campos essenciais | Restrições |
|---|---|---|
| `User` | id, email, name, role, is_active, is_staff, password, last_login | E-mail normalizado e único, `role` ADMIN/TEACHER/STUDENT; senha com hash do Django, nunca armazenar senha em texto |
| `StudentProfile` | user (1:1), target_level, placement_level, timezone, learning_goal | Student role; nível A1–C2; sem dados desnecessários |
| `TeacherProfile` | user (1:1), bio, is_available | Teacher role |
| `Invitation` | recipient_email, role, token_hash, expires_at, used_at, invited_by | Token aleatório, validade limitada e uso único |
| `Enrollment` | student, course, status, enrolled_at, ended_at | ACTIVE/PAUSED/COMPLETED/CANCELLED; único por aluno e curso |
| `TeacherStudent` | teacher, student, assigned_at, active | Único por par; garante acesso autorizado a alunos individuais |
| `Group` | name, teacher, course, active | Professor dono; várias matrículas |
| `GroupMember` | group, enrollment, joined_at, left_at | Único por grupo e matrícula; matrícula do mesmo curso |

Criar `User` customizado antes da primeira migration (`AUTH_USER_MODEL = 'accounts.User'`). Preferir `AbstractUser` adaptado para autenticação por e-mail, com manager customizado e normalização consistente. `is_staff` representa acesso ao Django Admin e não é sinônimo de papel professor.

### 6.2 Domínio pedagógico

| Modelo | Campos essenciais | Restrições |
|---|---|---|
| `Course` | slug, title, description, level, status, version | slug único; níveis A1–C2; DRAFT/PUBLISHED/ARCHIVED |
| `Unit` | course, title, position, description | ordem única por curso |
| `Lesson` | unit, slug, title, summary, theory, example, estimated_minutes, position, xp_reward, passing_percent, required, status | ordem única por unidade; xp_reward >= 0; passing_percent 0–100 |
| `Question` | lesson, type, prompt, position, explanation, weight | MCQ inicialmente; weight > 0; ordem única por lição |
| `Choice` | question, text, position, is_correct | Exatamente uma correta em MCQ; validar ao publicar |
| `LessonAttempt` | student, lesson, status, started_at, submitted_at, correct_count, total_questions, score_percent, passed | IN_PROGRESS/SUBMITTED/ABANDONED; servidor calcula pontuação |
| `AttemptAnswer` | attempt, question, selected_choice, is_correct, answered_at | Única por tentativa/pergunta; choice pertence à mesma pergunta |
| `LessonProgress` | student, lesson, best_score, first_passed_at, completed, last_attempt_at | Único por aluno/lição; progresso não regrede após aprovação |
| `XPEvent` | student, source_type, source_id, amount, created_at | Ledger imutável; único por aluno, origem e identificador da origem |
| `Achievement` | code, name, description, icon, required_lesson_count | code único |
| `StudentAchievement` | student, achievement, unlocked_at | Único por aluno e conquista |

Uma lição publicada com tentativas existentes não deve ter perguntas/correção alteradas no lugar. No MVP, bloquear alterações estruturais após a primeira tentativa; para corrigir ou atualizar, duplicar/versionar a lição e publicar nova versão com política de migração explícita. Conservar tentativa histórica.

### 6.3 Caderno, tarefas e sala de aula

| Modelo | Campos essenciais | Restrições |
|---|---|---|
| `Note` | student, title, body, tags, updated_at | Dono exclusivo; título até 120 caracteres; corpo até 5.000 |
| `Assignment` | teacher, title, instructions, due_at, created_at, status | DRAFT/PUBLISHED/ARCHIVED |
| `AssignmentRecipient` | assignment, student, enrollment | Um por aluno/tarefa; vínculo válido com professor no momento da criação |
| `Submission` | recipient, answer_text, submitted_at, status, grade, feedback, reviewed_at, reviewed_by | Uma por destinatário; DRAFT/SUBMITTED/REVIEWED; nota opcional 0–100 |
| `ClassSession` | teacher, title, description, starts_at, ends_at, group (nullable), mode, external_url, room_name, status | mode EXTERNAL/LIVEKIT; SCHEDULED/CANCELLED/COMPLETED; término > início; room_name único |
| `ClassParticipant` | session, student, enrollment, attendance_status | Um por participante; EXPECTED/PRESENT/ABSENT; matrícula e professor autorizados |

Para aula individual, criar sessão sem grupo e exatamente um participante; para aula em grupo, registrar os participantes elegíveis ao agendar. Não usar `group_id` informado pelo frontend como autorização suficiente. Uma alteração de grupo posterior não inclui ninguém numa aula antiga automaticamente.

### 6.4 Financeiro

| Modelo | Campos essenciais | Restrições |
|---|---|---|
| `Plan` | slug, name, description, monthly_price, is_active, live_class_type | Preço > 0; exibição no site público |
| `Subscription` | student, plan, status, started_at, ended_at | ACTIVE/PAUSED/CANCELLED; apenas uma ativa por aluno no MVP |
| `Invoice` | student, subscription, period, amount, due_date, status, source, external_id, paid_at, payment_url | PENDING/PAID/OVERDUE/CANCELLED/REFUNDED; source MANUAL/ASAAS; período por mensalidade (competência YYYY-MM) com unicidade por subscription e period; valor original imutável após cobrança; identificador do provedor único quando existente |
| `PaymentEvent` | provider, event_id, event_type, invoice (nullable), received_at, processed_at, processing_status, error_code | Único por provider/event_id; persistência mínima do evento, sem dados sensíveis |
| `AuditLog` | actor (nullable), action, object_type, object_id, request_id, created_at, metadata | Append-only pela aplicação; metadados permitidos, sem tokens ou respostas completas |

Criar índices em FKs e consultas frequentes: matrícula por estudante/status, aulas por teacher/starts_at, aulas do participante, cobranças por student/status/due_date, tarefas por professor/prazo e notas por aluno/updated_at. Usar `PROTECT` em relações com histórico financeiro; preferir desativação/arquivamento de usuários e cursos em vez de apagar dados históricos.

### 6.5 Relacionamentos principais

```mermaid
erDiagram
    USER ||--o{ ENROLLMENT : student
    COURSE ||--o{ ENROLLMENT : receives
    COURSE ||--o{ UNIT : contains
    UNIT ||--o{ LESSON : contains
    LESSON ||--o{ QUESTION : contains
    QUESTION ||--o{ CHOICE : offers
    USER ||--o{ LESSON_ATTEMPT : attempts
    LESSON ||--o{ LESSON_ATTEMPT : receives
    LESSON_ATTEMPT ||--o{ ATTEMPT_ANSWER : records
    USER ||--o{ LESSON_PROGRESS : owns
    LESSON ||--o{ LESSON_PROGRESS : measures
    USER ||--o{ NOTE : owns
    USER ||--o{ CLASS_SESSION : teaches
    CLASS_SESSION ||--o{ CLASS_PARTICIPANT : includes
    USER ||--o{ CLASS_PARTICIPANT : attends
    ASSIGNMENT ||--o{ ASSIGNMENT_RECIPIENT : assigns
    ASSIGNMENT_RECIPIENT ||--o| SUBMISSION : receives
    USER ||--o{ SUBSCRIPTION : subscribes
    PLAN ||--o{ SUBSCRIPTION : defines
    SUBSCRIPTION ||--o{ INVOICE : generates
```

## 7. Requisitos funcionais e regras de negócio

### RF-01 — Identidade, convite e autenticação (P0)

- Visitante navega pelo site, conhece os planos e acessa login.
- Administrador cria convite para professor ou aluno; usuário aceita uma única vez, define senha válida e conclui perfil.
- Login com e-mail e senha; logout real que invalida sessão. Convites e recuperação por e-mail via SMTP configurável (backend de console em desenvolvimento). Não enviar senhas.
- Responder de forma genérica à recuperação de senha para evitar enumeração de usuários. Limitar tentativas de login, convite e recuperação.
- Usuário desativado não poderá autenticar; verificar usuário ativo nas requisições. Não confiar no papel enviado pelo cliente.
- Preferir `SessionAuthentication` com cookie de sessão `HttpOnly` e `Secure` em produção. Não armazenar tokens de autenticação em `localStorage`.
- Endpoint CSRF fornece token mascarado; o cliente envia `X-CSRFToken` com POST, PATCH, PUT e DELETE. Aplicar proteção CSRF explicitamente inclusive nas views públicas de login/reset/convite. Obter novo token após login. Cookies `SameSite=Lax` em origem única; `credentials: 'same-origin'`.
- Se a configuração de produção depender de proxy, validar `Host`, origem e `X-Forwarded-Proto` apenas quando inseridos pelo proxy confiável. Não habilitar CORS irrestrito para resolver erros de sessão.

### RF-02 — Curso, currículo e missões (P0)

- Aluno matriculado enxerga somente cursos publicados aos quais tem acesso.
- A1 contém oito missões; níveis A2–C2 aparecem na apresentação como planejados, não clicáveis como cursos disponíveis.
- Professor observa progresso apenas de estudantes vinculados; administrador gerencia publicação e conteúdo no backoffice.
- Cada lição contém título, habilidade, teoria em português, exemplos em inglês e quatro estados: não iniciada, em andamento, concluída e revisão.
- O estudante pode acessar/revisar qualquer missão publicada da sua trilha inicial. A interface sugere a primeira missão não concluída; após as oito, recomenda revisão.
- Administrador pode publicar somente uma lição com perguntas válidas, uma alternativa correta por questão e critérios de aprovação configurados. Se houver tentativas, bloquear mudanças incompatíveis.

### RF-03 — Execução de uma missão (P0)

Fluxo: abrir lição → ler teoria → ouvir exemplo → iniciar tentativa → responder → receber explicação → concluir → receber progresso/XP.

1. Backend inicia tentativa autorizada e retorna perguntas e alternativas **sem `is_correct`, gabarito ou explicação antecipada**.
2. Enviar apenas identificadores da questão e alternativa. Backend confirma pertencimento e grava resposta. Resposta já submetida retorna o resultado anterior ou conflito; aluno não muda resposta após confirmação.
3. Backend devolve feedback e explicação apenas após a resposta confirmada.
4. Ao finalizar, confirmar que todas as questões obrigatórias foram respondidas. Calcular pontuação no servidor e persistir.
5. Aprovação de cada missão A1: pelo menos 2 acertos em 3 questões, todas com peso 1. Para o seed, usar `passing_percent=66` e comparar a fração exata antes do arredondamento visual (2/3 = 66,666…%). Outras lições podem configurar limiar e pesos; quando houver pesos, usar soma dos pesos corretos / soma total.
6. Em falha, permitir nova tentativa. Em revisão, novas tentativas melhoram `best_score`, mas não repetem XP.
7. Ao recarregar ou trocar de dispositivo, recuperar tentativa em andamento e progresso. Retomada deve respeitar respostas já confirmadas.

Implementação crítica: ao finalizar, usar `transaction.atomic()` e bloqueio apropriado ou constraint + tratamento de conflito. Uma requisição duplicada não deve emitir dois `XPEvent`. A resposta de finalização repetida retorna o resultado consolidado.

### RF-04 — Gamificação (P0)

| Ação | Regra |
|---|---|
| Primeira aprovação de uma missão A1 | +60 XP uma única vez |
| Revisão já aprovada | 0 XP adicional |
| Tentativa reprovada ou incompleta | 0 XP |
| Conquista First Steps | Após 1 missão aprovada |
| Grammar Explorer | Após 3 missões aprovadas do A1 |
| English Adventurer | Após 5 missões aprovadas do A1 |
| A1 Champion | Após 8 missões aprovadas do A1 |

XP é a soma de `XPEvent.amount`, não um valor confiado ao navegador. Progresso inicial = 100 × lições obrigatórias distintas concluídas / total de lições obrigatórias publicadas. Com oito lições concluídas, XP inicial = 480 e progresso A1 = 100%. Não prometer ganho de XP em botões ou tela se o backend não confirmou. O conceito de nível de idioma não deve ser confundido com pontuação do jogo.

### RF-05 — Caderno digital individual (P0)

- Aluno cria anotações livres com título, conteúdo, tags e data, edita, pesquisa e exclui as próprias notas. Ordenação pela última atualização. Exibir confirmação antes de remover.
- Notas são privadas; professor e outros alunos não podem ler por ID nem por listagem. Anotações não são tarefas entregues. Se futuramente compartilhar uma nota, usar recurso específico e explícito.
- Caderno apresenta seção separada de atividades do professor, status e feedback. Persistir notas no banco; não usar dados locais como fonte de verdade.

### RF-06 — Atividades personalizadas (P0)

- Professor vinculado cria tarefa individual ou para turma, com título, instrução e prazo. Publicar materializa os destinatários válidos.
- Aluno recebe a tarefa, pode salvar rascunho e enviar resposta escrita. Depois de enviar, resposta fica bloqueada a menos que professor a devolva formalmente para nova tentativa (fora da primeira entrega se não implementado).
- Professor autor da tarefa visualiza entregas dos destinatários e corrige com texto e nota opcional. Aluno recebe feedback apenas sobre a própria resposta.
- Prazo vencido deve ser indicado; no MVP, aceitar envio atrasado com `submitted_at > due_at` sinalizado. Não contar rascunho como entrega.

### RF-07 — Agenda e aulas ao vivo (P0 agenda; P1 vídeo nativo)

- Administrador agenda qualquer aula; professor agenda apenas aulas próprias para alunos vinculados ou suas turmas.
- Campos: título, professor responsável, descrição, início, fim, modalidade, participantes. Data/hora selecionada no fuso da escola e enviada em ISO com offset.
- Validar conflitos de horário do professor e de participantes ativos: intervalos sobrepõem-se quando `new_start < existing_end AND new_end > existing_start`. Aulas canceladas não bloqueiam agenda. Usar transação e bloqueio das linhas relevantes (ou constraint adequada) para evitar dupla reserva concorrente.
- Aluno vê apenas aulas em que é participante. Professor vê somente as próprias; admin vê todas.
- `EXTERNAL`: link HTTPS inserido pelo professor, com validação de URL e sem redirecionamento open redirect do backend. Mostrar botão Entrar na hora adequada. Não fazer requisição server-side ao link fornecido.
- Sala integrada LiveKit: `LIVEKIT`, `room_name` gerado de forma opaca no servidor; nunca usar nome de aluno ou e-mail como nome de sala.
- Permitir entrada de participante e professor no intervalo de 10 minutos antes do começo até 15 minutos após o término enquanto aula estiver SCHEDULED. Após cancelar ou terminar, negar novos tokens; encerrar/remover participantes pela API do provedor quando vídeo nativo estiver ativo. Professor/admin podem marcar presença e encerrar aula.
- Não gravar áudio ou vídeo por padrão; gravação fica fora do MVP até definir consentimento, retenção, proteção e custo.

**Integração LiveKit (incremento após agenda):**

1. Frontend pede `POST /api/v1/classes/{id}/join/`.
2. Django verifica autenticação, vínculo, estado e janela de horário.
3. Para aula EXTERNAL, retorna link validado; para LIVEKIT, usando SDK oficial server-side, retorna URL pública LiveKit e token assinado de TTL curto (ex.: 5 minutos), identidade opaca e permissão apenas para a sala autorizada.
4. Frontend monta sala responsiva usando SDK/componentes React, com câmera, microfone, seleção de dispositivos, lista de participantes e saída; pedir permissão somente após ação do usuário. Compartilhamento de tela para professor se a ferramenta suportar.
5. Fim da aula encerra a sessão; modo sem credenciais fica em EXTERNAL. Nunca mostrar câmera fictícia ou afirmar que participantes estão conectados sem confirmação do SDK.

### RF-08 — Gestão institucional (P0)

- Dashboard administrativo com alunos ativos, aulas agendadas, tarefas pendentes, recebimentos e valores em aberto. Datas e fórmulas explícitas conforme seção 2.3; dados reais, sem valores estáticos disfarçados.
- CRUD controlado de usuários, matrículas, professores, vínculos, turmas e planos. Administrador pode pausar ou reativar matrícula. Desativação mantém histórico.
- Professor dispõe de lista de alunos vinculados e acompanhamento de progresso/última atividade, seus horários e entregas.
- Busca de alunos por nome/e-mail, filtro de nível e status; paginação server-side. Exportar CSV administrativo opcional após MVP (se incluído, prevenir fórmulas CSV iniciadas por `=`, `+`, `-` ou `@`).
- Recebimentos e ajustes críticos, convites, alteração de matrículas e cancelamentos geram eventos de auditoria.

### RF-09 — Planos, cobranças e mensalidades (P0 manual; P1 sandbox)

Planos ilustrativos configuráveis pelo administrador (não valores comerciais definitivos):

| Plano | Valor de referência | Benefício |
|---|---:|---|
| Explorer | R$ 39,00/mês | Missões e caderno digital |
| Plus | R$ 149,00/mês | Missões e aulas em grupo |
| Mentor | R$ 299,00/mês | Missões e aulas individuais |

- Admin cria/edita planos ativos, atribui assinatura ao aluno, gera cobrança manual por competência e data de vencimento. Preço do plano pode mudar sem modificar cobranças já emitidas.
- Aluno vê exclusivamente as próprias cobranças e vencimentos. Professor não vê financeiro.
- `PENDING` quando emitida; `OVERDUE` quando vencida (exibir calculado no backend ou atualizar por tarefa diária); `PAID` após registro de recebimento; `CANCELLED` ou `REFUNDED` por ação autorizada e auditável. Não apagar cobrança.
- Baixa manual exige confirmação do administrador, motivo/comprovante de referência e data; apenas cobranças MANUAL podem ser baixadas manualmente. Cobrança ASAAS recebe confirmação do provedor; divergências exigem conciliação e log, não edição arbitrária.
- Recalcular valores de totais do banco, sem depender de dados do frontend. Recebimento parcial e parcelamento ficam fora do MVP.
- Inadimplência inicialmente gera sinalização. Suspensão da matrícula é decisão explícita do administrador; não cancelar progresso automaticamente. Futuramente aplicar regras de acesso conforme plano e política informada no contrato comercial.

**Integração Asaas em sandbox:**

1. Usar cliente HTTP server-side, timeout, validação e ambiente selecionado por configuração. Nunca misturar chaves ou dados sandbox/produção.
2. Criar/associar cliente com dados mínimos de teste necessários; registro de cobrança com referência interna única. Persistir `external_id`, link hospedado e status. Se timeout na criação, reconciliar pela referência antes de tentar novamente, evitando duplicata.
3. Aluno usa checkout/link de pagamento do provedor. Não coletar nem armazenar cartão na aplicação.
4. Receber webhook público com verificação do token/autenticação de acordo com a documentação atual do Asaas. CSRF isento **apenas nesse endpoint**, protegido pelo segredo do webhook e validação do evento; não usar sessão de aluno.
5. Persistir `PaymentEvent` por identificador externo, rejeitar/ignorar duplicatas de maneira idempotente e tratar eventos fora de ordem. Buscar status atual da cobrança no provedor em inconsistência. Conferir ID, valor e titular antes de confirmar.
6. Testar cobrança, confirmação simulada, repetição do webhook, evento incorreto, retentativa e expiração no sandbox. A resposta 2xx só indica evento devidamente recebido/registrado; erros transitórios permitem reprocessamento. Não usar transações reais para teste.
7. Antes de habilitar produção: acesso à conta do estabelecimento, aprovação comercial, políticas de cobrança, segurança, homologação e checklist financeiro.

## 8. Contrato REST API

Prefixo `/api/v1/`. JSON UTF-8. IDs UUID, datas ISO 8601, preços como strings em BRL. Listas paginadas com `count`, `next`, `previous`, `results`; tamanho padrão 20, máximo 100. Filtros e ordenação com allowlist. Documentar OpenAPI em `/api/schema/` e Swagger em rota restrita a staff/desenvolvimento.

### 8.1 Autenticação e público

| Método / rota | Acesso | Resultado |
|---|---|---|
| `GET /health/` | Infraestrutura | Status mínimo, sem segredos |
| `GET /api/v1/auth/csrf/` | Público | Cookie CSRF e token mascarado |
| `POST /api/v1/auth/login/` | Público + CSRF | Cria sessão, perfil/papel e novo CSRF |
| `POST /api/v1/auth/logout/` | Autenticado + CSRF | Encerra sessão |
| `GET /api/v1/auth/me/` | Autenticado | Perfil da sessão e papel |
| `POST /api/v1/auth/invite/accept/` | Público + CSRF | Valida convite, cria senha e ativa conta |
| `POST /api/v1/auth/password/reset/` | Público + CSRF | Resposta genérica, envia link quando aplicável |
| `POST /api/v1/auth/password/confirm/` | Público + CSRF | Valida token, redefine senha |
| `GET /api/v1/public/plans/` | Público | Planos visíveis |

Exemplo de `GET /auth/me/`:

```json
{
  "id": "a1111111-1111-4111-8111-111111111111",
  "name": "Aluno Exemplo",
  "email": "aluno@example.com",
  "role": "STUDENT",
  "is_active": true
}
```

### 8.2 Aluno e aprendizado

| Método / rota | Resultado |
|---|---|
| `GET /api/v1/me/dashboard/` | Dados do aluno logado: XP, progresso, próxima lição, tarefas e aulas |
| `GET /api/v1/me/enrollments/` | Matrículas do usuário |
| `GET /api/v1/courses/{id}/outline/` | Curso autorizado com unidades e lições publicadas e progresso do usuário |
| `GET /api/v1/lessons/{id}/` | Teoria e exemplos sem gabarito |
| `POST /api/v1/lessons/{id}/attempts/` | Iniciar ou recuperar uma tentativa em curso |
| `GET /api/v1/attempts/{id}/` | Tentativa e questões do próprio aluno; feedback somente das questões já respondidas |
| `POST /api/v1/attempts/{id}/answers/` | Confirmar alternativa e retornar feedback |
| `POST /api/v1/attempts/{id}/finish/` | Finalizar, calcular score/XP e retornar resultado |
| `GET /api/v1/me/achievements/` | Conquistas desbloqueadas e requisitos |
| `GET, POST /api/v1/me/notes/` | Listar/criar notas privadas |
| `GET, PATCH, DELETE /api/v1/me/notes/{id}/` | Consultar, editar, excluir nota própria |
| `GET /api/v1/me/assignments/` | Tarefas destinadas ao aluno |
| `GET, PATCH /api/v1/me/assignments/{id}/submission/` | Consultar/salvar rascunho |
| `POST /api/v1/me/assignments/{id}/submit/` | Enviar resposta final |
| `GET /api/v1/me/classes/` | Aulas do aluno |
| `GET /api/v1/me/invoices/` | Mensalidades próprias |

Exemplo de corpo da validação de resposta:

```json
{
  "question_id": "b2222222-2222-4222-8222-222222222222",
  "choice_id": "c3333333-3333-4333-8333-333333333333"
}
```

Resposta após confirmação:

```json
{
  "is_correct": true,
  "correct_choice_id": "c3333333-3333-4333-8333-333333333333",
  "explanation": "Use am com I.",
  "answered_count": 1,
  "total_questions": 3
}
```

Finalização:

```json
{
  "correct_count": 3,
  "total_questions": 3,
  "score_percent": 100,
  "passed": true,
  "xp_earned": 60,
  "xp_total": 60,
  "new_achievements": ["FIRST_STEPS"]
}
```

### 8.3 Professor, administrador e integrações

| Método / rota | Autorização |
|---|---|
| `GET /api/v1/staff/students/` | Admin: todos; professor: vinculados |
| `GET /api/v1/staff/students/{id}/progress/` | Admin ou professor vinculado |
| `GET, POST /api/v1/staff/groups/` | Admin; professor suas turmas |
| `GET, PATCH /api/v1/staff/groups/{id}/` | Admin ou professor responsável |
| `POST /api/v1/staff/groups/{id}/members/` | Admin ou professor autorizado |
| `GET, POST /api/v1/staff/classes/` | Admin ou professor para aulas próprias |
| `GET, PATCH /api/v1/staff/classes/{id}/` | Admin ou professor responsável |
| `POST /api/v1/staff/classes/{id}/cancel/` | Admin ou professor responsável |
| `POST /api/v1/staff/classes/{id}/complete/` | Admin ou professor responsável |
| `POST /api/v1/staff/classes/{id}/attendance/` | Admin ou professor responsável |
| `POST /api/v1/classes/{id}/join/` | Participante, professor da aula ou admin quando autorizado |
| `GET, POST /api/v1/staff/assignments/` | Admin ou professor para estudantes elegíveis |
| `GET, PATCH /api/v1/staff/assignments/{id}/` | Admin ou professor autor |
| `POST /api/v1/staff/assignments/{id}/publish/` | Admin ou professor autor |
| `GET /api/v1/staff/assignments/{id}/submissions/` | Admin ou professor autor |
| `POST /api/v1/staff/submissions/{id}/review/` | Professor autor ou admin pedagógico |
| `GET /api/v1/admin/dashboard/` | Admin |
| `GET, POST /api/v1/admin/users/` | Admin (convite/criação controlada) |
| `GET, PATCH /api/v1/admin/users/{id}/` | Admin |
| `GET, POST /api/v1/admin/enrollments/` | Admin |
| `PATCH /api/v1/admin/enrollments/{id}/` | Admin |
| `GET, POST /api/v1/admin/teacher-students/` | Admin |
| `GET, POST /api/v1/admin/courses/` | Admin ou Django Admin interno equivalente |
| `GET, POST /api/v1/admin/plans/` | Admin |
| `GET, PATCH /api/v1/admin/plans/{id}/` | Admin |
| `GET, POST /api/v1/admin/subscriptions/` | Admin |
| `GET, PATCH /api/v1/admin/subscriptions/{id}/` | Admin; preservar histórico |
| `GET, POST /api/v1/admin/invoices/` | Admin |
| `GET /api/v1/admin/invoices/{id}/` | Admin |
| `POST /api/v1/admin/invoices/{id}/mark-paid/` | Admin; manual e auditado |
| `POST /api/v1/admin/invoices/{id}/cancel/` | Admin; validar origem/estado e conciliar provedor |
| `POST /api/v1/webhooks/asaas/` | Segredo do webhook, sem sessão |

Padrão de erro sugerido: `{"code":"LESSON_NOT_AVAILABLE","detail":"Esta lição não está disponível.","fields":{}}`. Utilizar 400 para validação, 401 para ausência de autenticação quando aplicável, 403 para ação não autorizada, 404 quando objeto está fora do queryset autorizado, 409 para conflito de estado/concorrência e 429 para limite de requisições. DRF SessionAuthentication pode emitir 403 em certas falhas de autenticação; documentar o comportamento efetivamente implementado e testá-lo. Nunca retornar stack trace ao cliente.

## 9. Design system e direção artística

### 9.1 Identidade

**Marca:** LingoQuest — English Academy.  
**Slogan:** Small steps. Big adventures.  
**Direção:** tecnologia educacional moderna, amigável e minimalista; inspirada na energia visual de jogos e software criativo. Evitar excesso de gradientes, emojis decorativos e aparência de painel genérico.

| Token | Cor | Uso |
|---|---|---|
| `brand-900` | `#123638` | Sidebar, CTA escuro, navegação |
| `brand-800` | `#173B38` | Botões e destaques |
| `accent` | `#C9EC7D` | XP, destaque e item ativo |
| `surface` | `#FFFFFF` | Cards |
| `background` | `#F7F9F4` | Fundo geral |
| `ink` | `#18332E` | Texto principal |
| `muted` | `#63736A` | Texto secundário |
| `border` | `#DCE5D8` | Divisões e contornos |
| `lavender` | `#EBE6F5` | Aulas ao vivo |
| `warm` | `#F6E1BA` | Recompensas |

Tipografia sugerida: Inter ou fonte de sistema equivalente, títulos sem serifa com tracking levemente negativo. Espaçamento base 4/8 px. Cards com borda sutil e raio 16–24 px. CTA principal com raio 10–12 px. Usar contraste WCAG AA como alvo; validar cores em texto pequeno e estados de interação.

### 9.2 Personagem Finn

Finn é um pequeno explorador digital original com corpo verde-petróleo, visor verde-lima, olhos simples e expressão acolhedora. Criar assets SVG próprios em `frontend/public/characters/` e um componente reutilizável `FinnMascot`.

Estados iniciais: `idle`, `welcome`, `thinking`, `celebrate`, `encourage`. No MVP, 2–3 ilustrações SVG são suficientes. Usar animações CSS discretas apenas em celebrações, respeitando `prefers-reduced-motion`. Não carregar assets de terceiros sem licença. Finn ajuda a orientar; não deve interromper o aprendizado com animações constantes.

Mensagens curtas: “Hello!”, “Nice work!”, “Keep going!”, “Mission complete!”. Feedback de erro neutro e informativo, sem humilhar o aluno. Não bloquear acesso por animação.

### 9.3 Navegação pública e painéis

| Rota frontend | Tela | Elementos |
|---|---|---|
| `/` | Landing page | Hero com Finn, CTA, metodologia, benefícios, planos, FAQ, rodapé |
| `/login` | Login | E-mail, senha, recuperação |
| `/invite` | Aceitar convite | Token + criação de senha |
| `/app` | Dashboard aluno | Hero, próximo desafio, XP, progresso, aula e caderno |
| `/app/learn` | Trilha | A1 ativo, A2–C2 planejados, unidades e cards de missão |
| `/app/learn/[lessonId]` | Lição | Teoria, exemplo, áudio e quiz em passos |
| `/app/notebook` | Caderno | Busca, lista, editor, tarefas e entregas |
| `/app/live` | Agenda | Próximas aulas, histórico, horários e botão entrar |
| `/app/live/[classId]` | Sala | Pré-teste/dispositivos e experiência LiveKit quando habilitada |
| `/app/achievements` | Conquistas | Badges, XP, progresso, desbloqueios |
| `/app/billing` | Minhas mensalidades | Plano, vencimentos, status, link seguro |
| `/app/settings` | Perfil | Nome e preferências |
| `/teacher` | Dashboard professor | Aulas, tarefas pendentes, alunos vinculados |
| `/teacher/students` | Alunos | Lista e progresso de vinculados |
| `/teacher/classes` | Aulas | Agenda e formulário de agendamento |
| `/teacher/assignments` | Tarefas | Criar, publicar e avaliar respostas |
| `/dashboard` | Dashboard admin | KPIs e atalhos |
| `/dashboard/students` | Gestão de alunos | Lista, convite, matrícula, status |
| `/dashboard/teachers` | Gestão de professores | Convites, disponibilidade e vínculos |
| `/dashboard/groups` | Turmas | Criar, vincular membros e professor |
| `/dashboard/courses` | Conteúdo | Visão curricular e atalho para backoffice editorial |
| `/dashboard/classes` | Agenda geral | Agendar, cancelar, acompanhar aulas |
| `/dashboard/billing` | Financeiro | Planos, assinaturas, cobranças e filtros |

Os layouts devem ter sidebar de aproximadamente 230 px no desktop, topbar com breadcrumb e XP no ambiente do aluno, hero verde-claro e cards espaçados. Na mobile, usar menu compacto acessível (drawer ou navegação adaptável), sem rolagem horizontal. Formulários devem ter labels associadas, mensagens de erro, foco visível e estados de loading/empty/error/success. O dashboard administrativo usa a mesma identidade, sem mascote excessivo.

### 9.4 Wireframe lógico — dashboard do aluno

```text
┌──────────────────┬───────────────────────────────────────────────┐
│ LQ LingoQuest    │ LingoQuest / Seu espaço     XP          Perfil │
│                  ├───────────────────────────────────────────────┤
│ Visão geral      │ Small steps. Big adventures.         [Finn]   │
│ Trilha de inglês │ Continue sua próxima missão →                 │
│ Meu caderno      ├─────────────┬─────────────┬───────────────────┤
│ Aulas ao vivo    │ XP          │ Missões     │ Progresso A1      │
│ Conquistas       ├─────────────┴─────────────┼───────────────────┤
│ Minhas faturas   │ Your learning path        │ Live classroom    │
│                  │ Hello, World!               │ Próxima aula       │
│ Perfil / Sair    │ The Verb To Be              │ Mini challenge     │
│                  │ A, An & The                 │ Meu caderno        │
└──────────────────┴───────────────────────────┴───────────────────┘
```

Implementar primeiro a versão desktop e conferir em 390 × 844, 768 × 1024 e 1440 × 900. Nenhum layout ou botão deve depender apenas do mouse. Campos e textos de status não dependem exclusivamente da cor.

## 10. Conteúdo inicial — A1 Foundations

O agente deve criar um comando `python manage.py seed_demo` idempotente, que cria o curso, duas unidades, oito missões e 24 perguntas abaixo. Em desenvolvimento, pode incluir contas e relacionamentos fictícios por opção `--with-demo-users` (senha vinda de variável de ambiente ou gerada e exibida apenas no terminal do desenvolvedor; jamais usar senha padrão em produção). Não criar usuários de demonstração ao fazer deploy de produção.

### 10.1 Lições

| Unidade | Slug | Nome | Habilidade | Objetivo e exemplo |
|---|---|---|---|---|
| Welcome | `hello` | Hello, World! | Speaking | Apresentar-se: `Hello! My name is Alex. Nice to meet you.` |
| Welcome | `tobe` | The Verb To Be | Grammar | Am/is/are: `I am a student. She is a teacher. We are friends.` |
| Welcome | `articles` | A, An & The | Grammar | Artigos: `I have an apple and a book. The book is blue.` |
| Everyday English | `routine` | My Daily Routine | Grammar | Simple Present: `I work every day. He works in a factory.` |
| Everyday English | `family` | People & Family | Vocabulary | Possessivos: `This is my sister. Her name is Jane.` |
| Everyday English | `time` | What Time Is It? | Listening | Horários: `It is seven thirty. I start work at eight.` |
| Everyday English | `questions` | Ask Me Anything | Speaking | Wh-questions: `Where do you live? What do you do?` |
| Everyday English | `review` | Mission: Real Life | Review | Combinar conteúdos: `Hello! I am Lucas. I live in Brazil and I work every day.` |

Exibir teoria clara antes dos desafios: `I am`, `he/she/it is`, `you/we/they are`; artigos `a/an` conforme o som inicial, `the` específico; Simple Present com terceira pessoa e uso de `do/does`; possessivos `my/your/his/her/our/their`; preposição `at` para horário; perguntas `what/where/when/who/why/how`.

### 10.2 Banco de perguntas inicial

Alternativas abaixo usam letras A/B/C. A coluna gabarito é **somente para o seed e o backend**, não pode entrar no bundle do frontend. `Choice.is_correct` guarda o gabarito e `Question.explanation` a explicação.

| Lição | Pergunta | A | B | C | Gabarito e explicação |
|---|---|---|---|---|---|
| hello | Como dizer bom dia? | Good night | Good morning | Goodbye | B — saudação da manhã |
| hello | My name ___ Alex. | am | are | is | C — terceira pessoa singular |
| hello | Prazer em conhecer você. | Nice to meet you | See you tomorrow | How old are you? | A — expressão de apresentação |
| tobe | I ___ happy. | is | am | are | B — I usa am |
| tobe | They ___ at school. | am | is | are | C — They usa are |
| tobe | She ___ not tired. | is | are | am | A — She usa is |
| articles | ___ orange | a | an | is | B — som vocálico |
| articles | I have ___ dog. | an | a | am | B — som consonantal |
| articles | Já falamos sobre o livro. ___ book is blue. | An | A | The | C — objeto específico |
| routine | She ___ English. | study | studies | studying | B — terceira pessoa, y vira ies |
| routine | ___ you work here? | Does | Do | Is | B — You usa do |
| routine | He ___ like coffee. | do not | does not | are not | B — negativa com does not |
| family | Meu livro | My book | Your book | His book | A — My = meu/minha |
| family | She loves ___ own family. | his | her | their | B — her se refere a she |
| family | We live with ___ parents. | our | your | my | A — our = nosso |
| time | 7:30 em inglês | Seven thirteen | Seven thirty | Seventy-three | B — thirty = trinta |
| time | I wake up ___ six. | in | on | at | C — at para horário |
| time | Como perguntar as horas? | What time is it? | How old are you? | Where is it? | A — pergunta correta |
| questions | ___ do you live? | Where | When | Who | A — Where = onde |
| questions | ___ is your birthday? | What | When | Where | B — When = quando |
| questions | ___ are you? | Who | Why | How | C — How are you? |
| review | I ___ from Brazil. | am | are | is | A — I am |
| review | He ___ at eight. | work | works | working | B — He works |
| review | ___ do you study English? Because I love it. | What | Why | When | B — Why pergunta motivo |

**Áudio no MVP:** para ouvir exemplos, usar `SpeechSynthesisUtterance` em inglês `en-US`, somente após clique, com opção de velocidade reduzida quando suportada. Informar quando não há voz apropriada no navegador. Isso oferece áudio de referência, não avaliação de pronúncia. Exercícios de fala e escuta com gravação/análise são evolução posterior.

## 11. Segurança, privacidade e confiabilidade

- Adotar menor privilégio; autorização server-side tanto nas listas quanto nos objetos. Testar horizontal privilege escalation (IDOR) de aluno A tentando acessar aluno B e professor não vinculado.
- Não expor senha, token, segredo, gabarito antecipado, e-mail de outros alunos, notas privadas ou dados de cartão nem em erros/logs.
- HTTPS em produção; cookies seguros; CSRF, validação de origem e `ALLOWED_HOSTS` restrito. `DEBUG=False`, `SECRET_KEY` em segredo do ambiente e nunca no Git.
- A senha usa validadores Django e hashing padrão seguro do framework. Recuperação usa tokens comprovados do Django. Evitar autenticação caseira.
- Aplicar throttling e limites de tamanho em endpoints sensíveis; queries paginadas e índices. Configurar proteção de login no proxy ou aplicação para uso real.
- Sanitizar conteúdo exibido. Para teoria e notas inicialmente texto simples/Markdown seguro, sem HTML arbitrário. Nunca usar `dangerouslySetInnerHTML` com entrada do usuário.
- Proteger painel de administração, evitar credenciais de teste, registrar alterações críticas e erros sem PII desnecessária. Considerar MFA administrativo antes de abrir produção.
- Para operar no Brasil, preparar aviso de privacidade, termos, canais para solicitação de dados, política de retenção e tratamento adequado às obrigações LGPD com revisão profissional. Restringir piloto inicial a adultos; menores requerem fluxo específico de responsáveis.
- Sem gravação de vídeo no MVP. Se futuramente houver gravação, tratar consentimento/aviso, retenção, acesso e exclusão.
- Logs estruturados com request_id; endpoint health; backup automatizado do PostgreSQL conforme plano de hospedagem e teste de restauração em ambiente isolado. Monitorar erros 5xx, falhas de webhook e indisponibilidade.
- Nunca colocar chaves em variáveis `NEXT_PUBLIC_*`. Elas são acessíveis pelo cliente; somente informações genuinamente públicas podem usar esse prefixo.

## 12. Ambiente de desenvolvimento no VS Code

Pré-requisitos: Git, Python, Node.js LTS compatível com Next.js, npm, Docker + Docker Compose (para PostgreSQL), VS Code. Extensões sugeridas: Python, Pylance, ESLint, Prettier, Docker. Usar terminal integrado.

### 12.1 Criar o repositório do zero

```bash
mkdir lingoquest
cd lingoquest
git init
```

Copie este arquivo como `SPEC.md`. O agente deverá criar as pastas e arquivos de configuração. Os comandos abaixo são referência de bootstrap a partir de uma pasta vazia; não repetir `startproject` se ele já foi criado pelo agente.

```bash
mkdir backend
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install 'Django>=5.2,<5.3' djangorestframework 'psycopg[binary]' django-environ drf-spectacular gunicorn pytest pytest-django
django-admin startproject config .
cd ..
npx create-next-app@latest frontend --ts --tailwind --eslint --app --src-dir --use-npm
```

No Windows PowerShell, para criar/ativar o ambiente virtual: `py -3.12 -m venv .venv` e `.\.venv\Scripts\Activate.ps1`. Se o agente já configurou dependências com `pyproject.toml`, preferir instalar pelo arquivo e lockfile gerado, sem instalar pacotes avulsos manualmente. Validar e fixar versões compatíveis antes de criar o primeiro commit.

**Importante:** criar `accounts.User`, configurar `AUTH_USER_MODEL`, registrar apps e configurar PostgreSQL **antes** de executar a primeira migration. Não construir em SQLite para depois descobrir incompatibilidades do banco alvo.

### 12.2 Docker Compose (exemplo — apenas banco local)

```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: lingoquest
      POSTGRES_USER: lingoquest
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    ports:
      - '127.0.0.1:5432:5432'
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U lingoquest -d lingoquest']
      interval: 5s
      timeout: 3s
      retries: 10
volumes:
  postgres_data:
```

O banco é persistido em volume. Não executar `docker compose down -v` para reiniciar a aplicação; isso apaga dados locais. Usar senha local exclusiva, sem copiar senha de trabalho ou produção.

### 12.3 Configuração de ambiente

Criar `.env.example` versionado sem segredos; o `.env` real fica no `.gitignore`. Exemplo de nomes (os valores de segredo devem ser gerados/preenchidos localmente):

```dotenv
DJANGO_SETTINGS_MODULE=config.settings.development
DJANGO_SECRET_KEY=
DJANGO_DEBUG=true
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_CSRF_TRUSTED_ORIGINS=http://localhost:3000
DATABASE_URL=postgresql://lingoquest:CHANGE_ME@127.0.0.1:5432/lingoquest
POSTGRES_PASSWORD=CHANGE_ME
APP_BASE_URL=http://localhost:3000
NEXT_INTERNAL_API_BASE_URL=http://127.0.0.1:8000
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
DEFAULT_FROM_EMAIL=no-reply@example.com
LIVEKIT_ENABLED=false
LIVEKIT_URL=
LIVEKIT_API_KEY=
LIVEKIT_API_SECRET=
ASAAS_ENABLED=false
ASAAS_ENV=sandbox
ASAAS_API_KEY=
ASAAS_WEBHOOK_TOKEN=
DEMO_PASSWORD=
```

`CHANGE_ME` é placeholder, não senha utilizável em produção. A senha embutida na DATABASE_URL deve corresponder a POSTGRES_PASSWORD e ser corretamente codificada quando houver caracteres especiais. O agente deve implementar carregamento explícito do `.env` da raiz no Django, e configuração server-only do frontend (ex.: `frontend/.env.local` com apenas `NEXT_INTERNAL_API_BASE_URL`), mantendo todas versões reais ignoradas. Para teste inicial, backend de e-mail console apenas em desenvolvimento.

### 12.4 Inicializar e executar após as fases 0 e 1 do roadmap

No terminal da raiz:

```bash
docker compose up -d db
```

No terminal do backend, após configurar o usuário customizado:

```bash
cd backend
source .venv/bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:8000
```

Após a Fase 2, executar também `python manage.py seed_demo` em outro terminal com o ambiente virtual ativo, para popular o curso A1. O comando não existe antes dessa fase.

Em outro terminal:

```bash
cd frontend
npm install
npm run dev
```

URLs locais esperadas: `http://localhost:3000` (interface) e `http://127.0.0.1:8000/admin/` (Django Admin interno). O frontend deve chamar `/api/v1/...` na mesma origem dele, por meio de proxy/rewrite. Não chamar diretamente `http://127.0.0.1:8000` pelo navegador para operações de sessão. Testar cookie e CSRF pelo proxy local, inclusive login e logout.

### 12.5 Comandos de qualidade previstos

```bash
# Backend (com o venv ativo e na pasta backend)
python manage.py check
python manage.py makemigrations --check --dry-run
pytest -q

# Frontend (na pasta frontend; scripts devem ser configurados pelo agente)
npm run lint
npm run typecheck
npm run test
npm run build
npx playwright test
```

CI deve usar ambiente isolado e banco PostgreSQL de teste, com migrations executadas. Se um teste não puder rodar por ausência de credenciais, marcar como teste de integração pendente e testar a interface do adaptador com mocks explícitos; jamais declarar que o provedor real foi validado.

## 13. Implementação por fases — backlog executável

Prioridades: P0 = necessário para MVP; P1 = integração real em homologação; P2 = evolução. Cada fase deve terminar com teste, código funcional e instruções no README. Evitar trabalhar em todo o projeto simultaneamente sem um fluxo vertical verificável.

| Fase | Implementação | Critério de saída |
|---|---|---|
| 0 — Fundação | Monorepo, dependências, Docker PostgreSQL, configurações, OpenAPI, UI tokens, `.env.example`, CI | Backend/DB/Next executam localmente; health e build passam |
| 1 — Identidade | User customizado, migrations, login, logout, CSRF, convite, reset, perfis e layouts protegidos | Contas reais dos três papéis; tentativa indevida negada; nenhuma senha padrão |
| 2 — Aprendizado | Curso/units/lessons, seed 8×3, API de tentativas, feedback, XP, cards, Finn, trilha e dashboard aluno | Aluno conclui missão e ganha 60 XP; recarga mantém dados; gabarito oculto até responder |
| 3 — Gestão acadêmica | Cadastro de estudantes/professores, matrículas, vínculos, turmas, agenda manual, dashboard professor e admin | Admin matricula aluno, professor vê aluno vinculado e agenda aula; aluno vê apenas sua aula |
| 4 — Caderno e tarefas | Notas privadas, busca/edição/exclusão, tarefa individual/grupo, submissão e correção | Professor publica, aluno entrega, professor corrige, aluno visualiza feedback; isolamento testado |
| 5 — Financeiro manual | Planos, assinatura, cobrança, status e baixa auditada, painel financeiro | R$ 39,00 + R$ 149,00 soma R$ 188,00 exatos; cobrança de terceiros invisível; sem duplicação por período |
| 6 — Videoconferência | Adaptador LiveKit e sala nativa; fallback externo | Dois participantes autorizados entram na sala de homologação; não autorizado/cancelado não recebe token; mic/câmera e saída funcionam |
| 7 — Pagamento sandbox | Adaptador Asaas, link de cobrança, webhook idempotente, conciliação | Cobrança sandbox criada e pagamento simulado confirma uma vez; evento falso rejeitado; interface deixa claro sandbox |
| 8 — Qualidade e deploy | Testes E2E, responsividade, segurança, logs, backup/restauração, documentação, Railway | Staging funciona em HTTPS, teste ponta a ponta, sem credenciais versionadas; checklist de go-live documentado |

Fases 0–5 formam o núcleo inicial operacional. Fases 6–7 completam a experiência de vídeo e integração financeira em homologação. Não ligar cobrança em produção até completar homologação e requisitos comerciais. Em piloto, use apenas usuários e dados fictícios antes de cadastrar pessoas reais.

## 14. Plano de testes e critérios de aceite globais

| ID | Cenário | Resultado obrigatório |
|---|---|---|
| AC01 | Aluno entra com credencial válida | Sessão válida e redirecionamento ao painel do aluno |
| AC02 | Aluno tenta chamar API admin | Bloqueado no Django, independentemente da UI |
| AC03 | Professor tenta ler progresso de aluno não vinculado | Resposta negada, sem vazamento de metadados |
| AC04 | Aluno solicita nota ou cobrança de outro usuário por ID | 404/403 e nenhum dado retornado |
| AC05 | Inicia lição A1 | Perguntas sem gabarito antes da resposta |
| AC06 | Completa duas questões corretas de três | Aprovado; 60 XP na primeira aprovação; progresso salvo |
| AC07 | Finaliza novamente a mesma tentativa de forma concorrente | Apenas um registro XP; mesmo progresso final |
| AC08 | Faz revisão de lição aprovada | XP permanece inalterado; best_score pode melhorar |
| AC09 | Reprova com um acerto | 0 XP adicional, permite nova tentativa |
| AC10 | Conclui todas as oito missões | 480 XP, 100%, quatro conquistas iniciais desbloqueadas |
| AC11 | Cria nota, edita e recarrega | Dados persistidos; outra conta não vê a nota |
| AC12 | Professor vinculado publica tarefa | Apenas os destinatários recebem; entrega e correção salvas |
| AC13 | Testa agenda sobreposta para professor | Conflito rejeitado; cancelamento libera horário |
| AC14 | Participante entra antes da janela ou em aula cancelada | Join negado; nenhuma credencial fornecida |
| AC15 | Admin registra mensalidade e marca como paga | Status, data, totais e auditoria consistentes |
| AC16 | Cliente repete criação da mensalidade para a mesma competência | Constraint impede duplicação |
| AC17 | Webhook sandbox duplicado ou fora de ordem | Sem dupla baixa; estado reconciliado corretamente |
| AC18 | Webhook sem segredo válido | Rejeitado; nenhuma alteração financeira |
| AC19 | POST autenticado sem CSRF | Rejeitado (exceto endpoint webhook com autenticação própria) |
| AC20 | Usuário é desativado e tenta utilizar sessão existente | Acesso bloqueado |
| AC21 | Navega em 390px e com teclado | Sem overflow indevido; interação, labels e foco funcionam |
| AC22 | Credenciais LiveKit/Asaas não configuradas | Core funciona; opção indisponível ou fallback honesto |
| AC23 | Erro de conexão durante salvamento ou pagamento | Feedback real, sem falsa confirmação ou duplicação |
| AC24 | Acesso a HTTPS em staging | Cookies e CSRF funcionam; sem segredos vazados no bundle ou log |

Separar testes unitários (cálculo e regras), integração DB/API, testes de isolamento entre usuários, integrações simuladas de provedor e E2E com contas reais de ambiente de teste. O teste de vídeo real exige acesso a dois navegadores/participantes e conta LiveKit; pagamento real não faz parte da homologação sandbox.

## 15. Hospedagem e passagem para produção

1. Criar repositório privado (GitHub ou equivalente) e versionar apenas código e configuração não secreta.
2. Criar ambientes de desenvolvimento, staging e produção separados. Provisionar PostgreSQL e serviços backend/frontend no Railway. Utilizar rede privada entre frontend/proxy e backend quando disponível; expor somente rotas necessárias.
3. Definir comandos de build/start para cada serviço. Backend: instalar dependências, migrations controladas no release, `collectstatic`, servidor WSGI/ASGI de produção (ex.: Gunicorn para WSGI). Nunca usar `runserver` em produção. Frontend: `npm ci`, `npm run build`, `npm run start`.
4. Configurar variáveis, HTTPS, cookies, origem confiável e domínio escolhido. Validar proxy de `/api/v1/*`, cabeçalhos encaminhados e acesso do webhook autenticado. Proteger backoffice Django.
5. Executar `python manage.py check --deploy` com settings de produção. Corrigir avisos aplicáveis, testar logs, tratamento de erros, health e recursos estáticos.
6. Configurar backup, alerta e rotina de recuperação; fazer teste de restauração em staging e documentar rollback de release e estratégia de migrations.
7. Criar primeiro administrador de forma segura; rodar seed pedagógico sem contas demo. Validar login, convites e recuperação com e-mail real configurado.
8. Validar integração de vídeo e pagamentos em homologação. Produção Asaas permanece desligada até aprovação do responsável e revisão de segurança/financeiro.
9. Pilotar com grupo pequeno de alunos voluntários, coletar feedback e revisar conteúdo com um professor de inglês.

Custos dependerão de hospedagem, volume de dados, minutos/participantes de vídeo e taxas de cobrança. Não assumir que o plano atual do Railway ou do provedor cobre o uso do SaaS; verificar os preços oficiais antes de iniciar operação comercial.

## 16. Evolução pós-MVP

- **Pedagogia:** ampliar A1, criar A2–C2, teste de nivelamento, listening com compreensão real, fases de speaking e writing, revisão espaçada de vocabulário e diagnóstico de erros recorrentes. Professor revisa e aprova conteúdo gerado por IA.
- **Tutor IA:** feedback contextual, diálogo, simulação de entrevistas e inglês para trabalho. Implementar limites de uso, privacidade, revisão pedagógica, transparência da correção e custo por aluno. Não enviar dados de uma turma ou caderno privado a modelos sem base e autorização adequadas.
- **Gamificação:** Finn evolui ao avançar; mapa visual por regiões, desafios diários, revisão espaçada, moedas cosméticas, itens e streak. Não usar design coercitivo.
- **Aulas:** quadro branco, materiais privados, gravação autorizada, transcrição e resumo para o aluno, notificação de agenda. Agendamento de reposição e gestão de disponibilidade.
- **Financeiro:** recorrência automatizada, conciliação, alertas, gestão de contratos, cupons e relatórios. Não improvisar emissão fiscal ou obrigações legais.
- **SaaS para escolas:** multi-tenancy com isolamento testado, identidade por escola, gestão de marca, planos B2B, owner/admin por organização e cobrança da plataforma. Decidir modelo econômico antes de implementar.
- **Aplicativo:** PWA instalável ou futura versão Flutter consumindo a mesma API; autenticação mobile deverá receber arquitetura de segurança própria.
- **Inglês corporativo:** módulos de reuniões, relatórios, chão de fábrica, compras, engenharia e área técnica. Pode ser um diferencial alinhado à experiência da MH Software no ambiente industrial.

## 17. Definição de pronto (Definition of Done)

Uma funcionalidade só está concluída quando:

- [ ] Requisito implementado com backend e interface conectados; nenhum mock apresentado como funcionalidade real.
- [ ] Migration e constraints revisadas; dados de teste persistem após recarga.
- [ ] Permissões positivas e negativas testadas; IDOR e vazamento evitados.
- [ ] API documentada; loading, vazio, sucesso e falha têm tratamento adequado.
- [ ] Testes relevantes executados com resultado registrado; build passa.
- [ ] Responsividade e acessibilidade básicas verificadas.
- [ ] Segredos não versionados; alterações relevantes auditadas.
- [ ] README inclui comandos reproduzíveis e pré-requisitos; limitações explícitas.
- [ ] Não houve alteração de escopo ou deploy real sem decisão documentada.

**Primeiro objetivo prático:** implementar o fluxo vertical admin cria convite → aluno aceita e entra → matrícula A1 → executa missão → recebe XP → retorna ao painel com progresso salvo. Só depois avançar para os demais módulos. Este fluxo comprova identidade, permissões, persistência, API e interface em conjunto.

## 18. Referências técnicas oficiais

- Django 5.2 — [Customizing authentication](https://docs.djangoproject.com/en/5.2/topics/auth/customizing/), [deployment checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/).
- Django REST Framework — [Authentication](https://www.django-rest-framework.org/api-guide/authentication/), [Permissions](https://www.django-rest-framework.org/api-guide/permissions/), [Testing](https://www.django-rest-framework.org/api-guide/testing/), [AJAX/CSRF/CORS](https://www.django-rest-framework.org/topics/ajax-csrf-cors/).
- LiveKit — [Access tokens & grants](https://docs.livekit.io/frontends/reference/tokens-grants/), [Connecting](https://docs.livekit.io/intro/basics/connect/).
- Asaas — [Sandbox](https://docs.asaas.com/docs/sandbox), [Webhook](https://docs.asaas.com/docs/receba-eventos-do-asaas-no-seu-endpoint-de-webhook), [Testando no Sandbox](https://docs.asaas.com/docs/testando-no-sandbox).

---

**Visão final:** uma escola digital que seja divertida para estudar, simples para ensinar e eficiente para administrar. Começar pelo núcleo funcional, evoluir em pequenos incrementos verificados e preservar a identidade aprovada no protótipo.
