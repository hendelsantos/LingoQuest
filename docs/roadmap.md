# Roadmap de engenharia orientado a resultados

Cada fase termina em um incremento demonstrável, testes e documentação. Uma fase não começa com
pendências críticas de autorização, integridade ou build na anterior.

| Fase | Resultado demonstrável | Gate |
|---|---|---|
| 0 — Fundação | API/DB/web executam, landing real, CI e arquitetura registradas | health, lint, testes e build verdes |
| 1 — Identidade | admin convida; usuário aceita, entra e sai | CSRF, papéis e desativação testados |
| 2A — Currículo | admin publica A1 Foundations e aluno matriculado vê trilha | seed idempotente, gabarito não vaza |
| 2B — Missão | aluno responde, recarrega, conclui e recebe XP uma vez | concorrência e revisão testadas |
| 3 — Ciclo humano | professor vê evidências, atribui tarefa e agenda aula externa | aluno alheio invisível; conflito de agenda |
| 4 — Operação do piloto | caderno, entregas, presença e painel mínimo | piloto de seis semanas operável |
| 5 — Financeiro manual | assinatura, competência, baixa e auditoria | valores decimais e isolamento testados |
| 6 — Vídeo | sala LiveKit homologada, mantendo fallback externo | janela/token/cancelamento testados |
| 7 — Pagamento | Asaas sandbox e webhook idempotente | duplicata/fraude/inconsistência testadas |
| 8 — Staging | HTTPS, E2E, logs, backup/restauração e go-live | checklist assinado antes de dados reais |

## Próxima entrega: Fase 1

Fluxo vertical:

1. administrador autenticado cria convite de aluno;
2. e-mail de desenvolvimento mostra link de uso único;
3. aluno define senha, entra e recebe sessão HttpOnly;
4. `/auth/me/` direciona para layout do papel correto;
5. logout invalida a sessão;
6. usuário desativado perde acesso inclusive com sessão existente.

Testes obrigatórios: CSRF ausente, token expirado/reutilizado, papel enviado pelo cliente, login
inativo, enumeração na recuperação e acesso de aluno a rota administrativa.

## Disciplina de entrega

- manter PRs/commits pequenos por fluxo vertical;
- não misturar integração LiveKit/Asaas antes do núcleo manual correspondente;
- registrar decisão em ADR antes de mudar autorização ou modelo de implantação;
- revisar as métricas do piloto a cada fase e cortar funcionalidade que não reduz risco comercial,
  pedagógico ou operacional.

