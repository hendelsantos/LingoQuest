# LingoQuest — English Academy

Escola digital de inglês que combina missões curtas, acompanhamento humano e operação
acadêmica em uma única plataforma. A [especificação](SPEC.md) é a fonte inicial de verdade.

## Estado atual

Fundação publicada e primeiro fluxo educacional demonstrável:

- monorepo com Django REST Framework e Next.js;
- PostgreSQL como único banco suportado;
- usuário customizado criado antes da primeira migration;
- health check, OpenAPI em desenvolvimento, landing e ambiente do aluno responsivos;
- curso A1 Foundations com duas unidades, oito missões e 24 questões reais;
- teoria, exemplos, áudio de referência, quiz corrigido no servidor e feedback pedagógico;
- painel e trilha demonstrativos com progresso salvo no navegador;
- configurações separadas para desenvolvimento, testes e produção;
- testes, lint, typecheck, build e CI;
- frontend, backend e PostgreSQL publicados no Railway com deploy automático pela `main`.

Autenticação, matrícula persistida por aluno, pagamentos e vídeo **ainda não estão implementados**.
O modo público é identificado como demonstração e não simula esses recursos.

Produção: <https://frontend-production-a0b865d3.up.railway.app/><br>
Ambiente de aprendizado: <https://frontend-production-a0b865d3.up.railway.app/app>

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

Para popular ou atualizar o conteúdo A1 localmente:

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

Leia [análise de produto](docs/product-analysis.md), [arquitetura](docs/architecture.md) e
[roadmap de entrega](docs/roadmap.md) antes de ampliar o escopo.

