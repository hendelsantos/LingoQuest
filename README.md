# LingoQuest — English Academy

Escola digital de inglês que combina missões curtas, acompanhamento humano e operação
acadêmica em uma única plataforma. A [especificação](SPEC.md) é a fonte inicial de verdade.

## Estado atual

Fundação publicada e primeiro fluxo educacional demonstrável:

- monorepo com Django REST Framework e Next.js;
- PostgreSQL como único banco suportado;
- usuário customizado criado antes da primeira migration;
- health check, OpenAPI em desenvolvimento, landing e ambiente do aluno responsivos;
- currículo demonstrativo A1–C2 com 112 missões e 570 questões;
- Missão 2.0 em todo o A1, com ativação, produção, revisão cumulativa e retomada espaçada;
- avaliações A1 inicial/final paralelas e categorias de erro para orientar o estudo;
- teoria, diálogos, áudio de referência, quatro tipos de exercício e correção no servidor;
- painel e trilha demonstrativos com progresso salvo no navegador;
- laboratório de aula ao vivo com câmera local real, controles de mídia e exercício interativo;
- identidade por convite para alunos e professores, login por sessão, logout e recuperação de senha;
- áreas protegidas por papel para aluno, professor e administração;
- matrícula persistida com gestão administrativa e currículo autenticado isolado por aluno;
- configurações separadas para desenvolvimento, testes e produção;
- testes, lint, typecheck, build e CI;
- frontend, backend e PostgreSQL publicados no Railway com deploy automático pela `main`.

Tentativas, progresso e XP associados à conta, pagamentos e videoconferência entre duas contas
**ainda não estão implementados**. O laboratório usa somente os dispositivos locais e
informa quando não existe um professor conectado; o modo público não simula esses recursos.

Produção: <https://frontend-production-a0b865d3.up.railway.app/><br>
Login: <https://frontend-production-a0b865d3.up.railway.app/login><br>
Demonstração pública: <https://frontend-production-a0b865d3.up.railway.app/demo><br>
Laboratório da sala: <https://frontend-production-a0b865d3.up.railway.app/demo/live>

## Pré-requisitos

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- Node.js 20.9+
- Docker com Docker Compose

## Executar localmente

1. Crie a configuração local e substitua `CHANGE_ME` por uma senha exclusivamente local:

   ```bash
   cp .env.example .env
   ```

2. Instale as dependências e suba o PostgreSQL:

   ```bash
   make install
   make db-up
   ```

3. Aplique as migrations e execute a API:

   ```bash
   cd backend
   uv run python manage.py migrate
   uv run python manage.py runserver 127.0.0.1:8000
   ```

4. Em outro terminal, execute a interface:

   ```bash
   cd frontend
   npm run dev
   ```

Interface: <http://localhost:3000>  
Health: <http://localhost:3000/health/>  
OpenAPI (desenvolvimento): <http://127.0.0.1:8000/api/docs/>

O navegador acessa a API por `/api/*` na origem do Next.js. O rewrite usa
`NEXT_INTERNAL_API_BASE_URL` apenas no servidor e preserva cookies/CSRF na mesma origem.

Crie o primeiro administrador sem senha padrão e use a área `/school/invitations` para convidar
as demais contas:

```bash
cd backend
uv run python manage.py createsuperuser
```

Para popular ou atualizar o currículo completo localmente:

```bash
cd backend
uv run python manage.py seed_demo
```

## Qualidade

```bash
make check
make test
cd frontend && npm run build
```

O backend nunca usa SQLite, nem mesmo nos testes. Defina `DATABASE_URL` apontando para um
PostgreSQL isolado ao executar a suíte fora do ambiente local.

## Organização

```text
backend/       Django, DRF, domínio e integrações server-side
frontend/      Next.js App Router e design system
docs/          análise de produto, arquitetura, ADRs e roadmap
Especificação/ documento original fornecido
SPEC.md        atalho versionado para a especificação original
```

Leia [análise de produto](docs/product-analysis.md), [arquitetura](docs/architecture.md),
[plano de evolução e implantação](docs/product-evolution-plan.md),
[plano de evolução pedagógica](docs/pedagogical-evolution-plan.md) e
[roadmap de entrega](docs/roadmap.md) antes de ampliar o escopo.

