# API

Prefixo planejado: `/api/v1/`. O contrato completo está na [especificação](../SPEC.md).

Disponível na Fase 0:

| Método | Rota | Autenticação | Finalidade |
|---|---|---|---|
| GET | `/health/` | pública | liveness mínimo, sem consulta ou segredo |
| GET | `/api/schema/` | somente desenvolvimento | schema OpenAPI |
| GET | `/api/docs/` | somente desenvolvimento | Swagger UI |

Erros futuros seguirão `{"code":"...","detail":"...","fields":{}}`. IDs públicos serão UUID,
datas ISO 8601 com offset e dinheiro será string decimal. A especificação OpenAPI publicada deve
ser tratada como contrato verificável, não documentação manual paralela.

