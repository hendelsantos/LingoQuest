# API

Prefixo planejado: `/api/v1/`. O contrato completo está na [especificação](../SPEC.md).

Disponível:

| Método | Rota | Autenticação | Finalidade |
|---|---|---|---|
| GET | `/health/` | pública | liveness mínimo, sem consulta ou segredo |
| GET | `/api/schema/` | somente desenvolvimento | schema OpenAPI |
| GET | `/api/docs/` | somente desenvolvimento | Swagger UI |
| GET | `/api/v1/auth/csrf/` | pública | cria cookie CSRF e retorna o token mascarado |
| POST | `/api/v1/auth/login/` | pública + CSRF | inicia sessão HttpOnly com e-mail e senha |
| POST | `/api/v1/auth/logout/` | sessão + CSRF | invalida a sessão atual |
| GET | `/api/v1/auth/me/` | sessão | retorna identidade e papel salvos no servidor |
| POST | `/api/v1/auth/staff/invitations/` | administrador + CSRF | envia convite de aluno ou professor |
| POST | `/api/v1/auth/invitations/accept/` | pública + CSRF | usa convite uma vez e cria a conta e o perfil |
| POST | `/api/v1/auth/password-reset/` | pública + CSRF | responde genericamente e envia link quando aplicável |
| POST | `/api/v1/auth/password-reset/confirm/` | pública + CSRF | valida link de uso único e troca a senha |
| GET | `/api/v1/demo/courses/a1-foundations/outline/` | pública | trilha demonstrativa publicada |
| GET | `/api/v1/demo/lessons/{slug}/` | pública | teoria, exemplo e questões sem gabarito |
| POST | `/api/v1/demo/lessons/{slug}/answer/` | pública | corrige uma escolha e devolve feedback |

O namespace `/demo/` é deliberadamente separado dos futuros endpoints autenticados. Ele serve à
avaliação pública do produto; o progresso desse modo fica no navegador. O backend nunca inclui
`is_correct`, explicação ou alternativa correta no payload inicial da lição.

As mutações de identidade exigem `X-CSRFToken`, inclusive login, convite e recuperação. O cliente
obtém o valor em `/api/v1/auth/csrf/`, usa `credentials: "same-origin"` e nunca armazena credenciais
de autenticação no `localStorage`. Convites persistem somente o hash do token e expiram em três dias.

Erros futuros seguirão `{"code":"...","detail":"...","fields":{}}`. IDs públicos serão UUID,
datas ISO 8601 com offset e dinheiro será string decimal. A especificação OpenAPI publicada deve
ser tratada como contrato verificável, não documentação manual paralela.

