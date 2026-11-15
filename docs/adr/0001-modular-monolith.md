# ADR 0001 — Monólito modular com Django e Next.js

- Status: aceito
- Data: 2026-11-15

## Contexto

O MVP precisa validar aprendizagem acompanhada, uma operação com um professor e pagamentos/vídeo
opcionais. Segurança por objeto, transações e velocidade de mudança são mais importantes que escala
organizacional prematura.

## Decisão

Usar Django REST Framework como autoridade do domínio, PostgreSQL como fonte de verdade e Next.js
como cliente web. Organizar o backend por módulos de negócio e integrar LiveKit/Asaas por adaptadores.
Usar sessão HttpOnly e mesma origem pública. Implantar frontend e backend como serviços isolados do
mesmo monorepo.

## Consequências

- regras e transações permanecem consistentes e testáveis em um processo;
- deploy possui apenas dois artefatos de aplicação e um banco;
- módulos precisam respeitar limites para evitar um monólito acoplado;
- tarefas assíncronas, cache e serviços separados serão adicionados somente com evidência;
- futura multi-tenancy exigirá ADR e migração explícita, não um campo opcional espalhado.

