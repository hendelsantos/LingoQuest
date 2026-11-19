# Análise de produto e oportunidade

## Parecer executivo

A proposta é forte quando posicionada como uma **escola digital acompanhada**, não como um
clone de aplicativo de idiomas. O diferencial defensável é o ciclo:

```text
missão curta → evidência de dificuldade → orientação do professor → aula semanal → nova prática
```

Aplicativos de autoestudo competem por hábito; marketplaces competem por oferta de professores.
O LingoQuest pode competir pela continuidade entre os dois: o professor chega à aula sabendo o
que o aluno estudou, errou e precisa praticar.

O documento original é tecnicamente consistente e cuidadoso com autorização, idempotência e
integridade financeira. Ele é mais amplo que um primeiro lançamento comercial. O risco principal
não é tecnologia: é construir muitos módulos antes de provar aprendizagem, retenção e margem.

## O que deve ser validado primeiro

1. Adultos iniciantes estudam ao menos três vezes por semana quando existe acompanhamento humano?
2. O professor consegue preparar uma aula melhor em menos tempo usando o progresso da plataforma?
3. O formato em grupo retém alunos sem perder a sensação de acompanhamento?
4. O aluno aceita pagar de forma recorrente depois de quatro a seis semanas de piloto?

O primeiro fluxo vertical da especificação continua correto: convite → matrícula A1 → missão →
XP → painel. Em seguida, a prioridade comercial deve ser fechar o ciclo com uma tarefa e uma aula
real, antes de ampliar dashboards administrativos.

## Pedagogia: gamificar sem esvaziar o aprendizado

As 112 missões e 570 questões demonstram amplitude e validam o motor, mas não comprovam sozinhas
que a plataforma “ensina inglês”. Um piloto pedagógico minimamente confiável deve ter:

- diagnóstico inicial curto e avaliação final equivalente, sem chamar o resultado de certificação;
- prática distribuída em três a cinco contatos semanais;
- recuperação ativa e revisão espaçada, em vez de apenas releitura;
- produção de escrita e fala observada pelo professor;
- registro das categorias de erro para definir a aula seguinte;
- objetivos observáveis por ciclo, como “apresentar-se por 60 segundos” ou “perguntar e responder
  sobre rotina”, não apenas concluir cards.

XP, conquistas e Finn devem reforçar esforço, domínio e retomada. Evitar punições por erro, rankings
públicos e streaks que gerem ansiedade. A mensagem central é progresso, não vício de uso.

## Modelo comercial e capacidade do primeiro professor

Os valores da especificação são hipóteses, não preços aprovados. A conta abaixo usa **R$ 50 por
hora-aula como premissa ilustrativa**, quatro encontros por mês e não inclui impostos, aquisição,
suporte, preparação, faltas, vídeo ou meios de pagamento.

| Oferta | Receita mensal | Custo direto ilustrativo | Contribuição antes dos demais custos |
|---|---:|---:|---:|
| Explorer, autoestudo | R$ 39 | baixo e variável | alta, após recuperar custo de conteúdo |
| Plus, grupo de 4 a R$ 149 | R$ 596 por turma | R$ 200 | R$ 396 (66%) |
| Mentor, individual a R$ 299 | R$ 299 | R$ 200 | R$ 99 (33%) |

Com 4,33 semanas médias por mês, o custo real seria um pouco maior e a margem individual cairia.
Por isso:

- o plano em grupo deve ser a oferta principal do piloto;
- o individual precisa de preço maior, encontro mais curto, pacote limitado ou posicionamento
  premium para sustentar margem;
- o plano de R$ 39 pode funcionar como entrada, mas exige conteúdo suficiente para retenção;
- não criar marketplace nem repasse automático agora; um professor e agenda manual reduzem risco.

Como referência de mercado, a página oficial da Cambly exibiu em novembro de 2026 valores por aula
de 30 minutos que variavam por compromisso e modalidade, e a Preply permite professores com preços
individuais em uma faixa ampla. Isso confirma que “aula humana” não é uma commodity de custo quase
zero; preço e ocupação precisam ser validados em entrevistas e pré-venda, não copiados. Fontes:
[Cambly](https://www.cambly.com/en/subscribe?currency=BRL&lang=pt) e
[Preply](https://preply.com/pt/online/professores--ingl%C3%AAs).

O relatório EF EPI 2025 também associa inglês a colaboração profissional e mostra diferenças
relevantes entre setores e funções. Isso sustenta testar, depois do A1 geral, um nicho de inglês para
trabalho técnico/industrial — especialmente coerente com a experiência da MH Software — sem
transformar essa inferência em promessa de mercado. Fonte:
[EF EPI 2025](https://www.ef.com.br/assetscdn/cefcom-epi-site/reports/2025/ef-epi-2025-brazilian-portuguese.pdf).

## Lacunas que precisam de decisão antes do piloto pago

| Tema | Lacuna | Decisão recomendada |
|---|---|---|
| Direito à aula | `Plan.live_class_type` não controla quantidade | Definir encontros/mês, duração, grupo e política de excedente |
| Cancelamento | Não há antecedência, reposição ou no-show | Política manual explícita antes de automatizar |
| Acompanhamento | Nota do aluno é privada; falta registro pedagógico do professor | Criar observação pedagógica separada e auditável numa fase futura |
| Currículo | Amplitude A1–C2 sem revisão integral de professor ou avaliação equivalente | Validar primeiro o A1 em piloto e não tratar conclusão como certificação oficial |
| Métrica de aprendizagem | KPIs medem uso, não ganho | Adicionar avaliação inicial/final e rubrica de fala/escrita |
| Conteúdo | Revisão pedagógica ainda não tem responsável | Professor aprova toda publicação e versionamento |
| Dados | LGPD citada, mas faltam políticas operacionais | Definir retenção, atendimento ao titular e termos antes de dados reais |

## Piloto recomendado

- 20 a 30 adultos, durante seis semanas;
- turmas de 3 a 5 alunos, uma aula semanal;
- onboarding assistido e suporte manual;
- cobrança manual ou lista de espera nas duas primeiras semanas;
- entrevista na entrada, semana 3 e saída;
- metas: ativação em 7 dias, três práticas/semana, presença, retenção até a semana 6,
  ganho na avaliação e intenção de renovação;
- critério de avanço: evidência de aprendizagem e renovação, não apenas cadastros ou XP.

## Conclusão

Existe oportunidade real se o LingoQuest entregar **acompanhamento estruturado a um preço entre o
app impessoal e a tutoria individual premium**. O caminho econômico mais promissor começa com
grupos pequenos e operação deliberadamente manual. A tecnologia deve primeiro aumentar a qualidade
e a capacidade do professor; só depois deve tentar escalar aquisição, pagamentos e múltiplas escolas.

