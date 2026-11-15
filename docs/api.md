# API

Prefixo planejado: `/api/v1/`. O contrato completo está na [especificação](../SPEC.md).

Disponível:

| Método | Rota | Autenticação | Finalidade |
|---|---|---|---|
| GET | `/health/` | pública | liveness mínimo, sem consulta ou segredo |
| GET | `/api/schema/` | somente desenvolvimento | schema OpenAPI |
| GET | `/api/docs/` | somente desenvolvimento | Swagger UI |
| GET | `/api/v1/demo/courses/a1-foundations/outline/` | pública | trilha demonstrativa publicada |
| GET | `/api/v1/demo/lessons/{slug}/` | pública | teoria, exemplo e questões sem gabarito |
| POST | `/api/v1/demo/lessons/{slug}/answer/` | pública | corrige uma escolha e devolve feedback |

O namespace `/demo/` é deliberadamente separado dos futuros endpoints autenticados. Ele serve à
avaliação pública do produto; o progresso desse modo fica no navegador. O backend nunca inclui
`is_correct`, explicação ou alternativa correta no payload inicial da lição.

Erros futuros seguirão `{"code":"...","detail":"...","fields":{}}`. IDs públicos serão UUID,
datas ISO 8601 com offset e dinheiro será string decimal. A especificação OpenAPI publicada deve
ser tratada como contrato verificável, não documentação manual paralela.

