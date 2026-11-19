# Roadmap de engenharia orientado a resultados

Cada fase termina em um incremento demonstrável, testes e documentação. Uma fase não começa com
pendências críticas de autorização, integridade ou build na anterior.

## Prioridades atuais: Fase 3 e validação pedagógica

A Fase 2B concluiu a persistência do ciclo de estudo e liberou o início da Fase 3. Em paralelo,
a Missão 2.0 aplicada a todo o A1 ainda precisa de validação com alunos e professor antes de ser
tratada como método comprovado. O incremento inclui objetivo observável, produção autoral,
checkpoints cumulativos, avaliações paralelas, categorias de erro e recuperação em 1, 3, 7 e 21
dias. O plano e os critérios estão em [evolução pedagógica](pedagogical-evolution-plan.md).

| Fase | Resultado demonstrável | Gate |
|---|---|---|
| 0 — Fundação ✓ | API/DB/web executam, landing real, CI e arquitetura registradas | health, lint, testes e build verdes |
| 1 — Identidade ✓ | admin convida; usuário aceita, entra e sai | CSRF, papéis e desativação testados |
| 2A — Currículo ✓ | admin publica A1 Foundations e aluno matriculado vê trilha | seed idempotente, gabarito não vaza |
| 2B — Missão ✓ | aluno responde, recarrega, conclui e recebe XP uma vez | concorrência e revisão testadas |
| 3 — Ciclo humano | professor vê evidências, atribui tarefa e agenda aula externa | aluno alheio invisível; conflito de agenda |
| 4 — Operação do piloto | caderno, entregas, presença e painel mínimo | piloto de seis semanas operável |
| 5 — Financeiro manual | assinatura, competência, baixa e auditoria | valores decimais e isolamento testados |
| 6 — Vídeo | sala LiveKit homologada, mantendo fallback externo | janela/token/cancelamento testados |
| 7 — Pagamento | Asaas sandbox e webhook idempotente | duplicata/fraude/inconsistência testadas |
| 8 — Staging | HTTPS, E2E, logs, backup/restauração e go-live | checklist assinado antes de dados reais |

## Entrega concluída: Fase 1

Fluxo vertical:

1. administrador autenticado cria convite de aluno;
2. e-mail de desenvolvimento mostra link de uso único;
3. aluno define senha, entra e recebe sessão HttpOnly;
4. `/auth/me/` direciona para layout do papel correto;
5. logout invalida a sessão;
6. usuário desativado perde acesso inclusive com sessão existente.

Testes obrigatórios: CSRF ausente, token expirado/reutilizado, papel enviado pelo cliente, login
inativo, enumeração na recuperação e acesso de aluno a rota administrativa.

O fluxo também inclui recuperação de senha genérica, perfis mínimos de aluno/professor e layouts
protegidos em `/app`, `/teacher` e `/school`. A demonstração sem conta foi isolada em `/demo`.

## Entrega concluída: Fase 2A

O currículo publicado agora está vinculado a matrículas reais. O administrador cria e altera
matrículas em `/school/enrollments`; a API autenticada restringe cursos, lições e correção ao aluno
com matrícula ativa ou concluída. Matrícula pausada ou cancelada bloqueia o currículo com 404. A
interface da conta não lê o progresso local do preview nem simula XP.

## Entrega concluída: Fase 2B

Tentativas, respostas confirmadas, progresso e o ledger de XP agora são persistidos. A finalização
é idempotente, emite XP uma única vez na primeira aprovação e conserva o melhor resultado em
revisões. Recarregar ou trocar de dispositivo recupera a tentativa em andamento e respeita as
respostas já confirmadas.

## Próxima entrega: Fase 3

Criar o ciclo humano mínimo: vínculo professor-aluno, evidências de progresso autorizadas, tarefa
escrita e agenda de aula externa com bloqueio de conflitos. O professor deve enxergar somente seus
alunos, e nenhum vínculo informado pelo frontend pode servir como autorização.

## Disciplina de entrega

- manter PRs/commits pequenos por fluxo vertical;
- não misturar integração LiveKit/Asaas antes do núcleo manual correspondente;
- registrar decisão em ADR antes de mudar autorização ou modelo de implantação;
- revisar as métricas do piloto a cada fase e cortar funcionalidade que não reduz risco comercial,
  pedagógico ou operacional.

