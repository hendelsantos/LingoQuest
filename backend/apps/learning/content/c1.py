COURSE = {
    "slug": "c1-advanced",
    "title": "C1 Advanced",
    "description": (
        "O nível avançado do LingoQuest: nuance modal, estruturas sofisticadas, "
        "registro e estilo para brasileiros que querem um inglês de nativo educado."
    ),
    "level": "C1",
}

UNITS = [
    {
        "title": "Precision & Nuance",
        "position": 1,
        "description": "Nuances modais, subjuntivo e cláusulas de particípio para dizer exatamente o que se quer dizer.",
        "lessons": [
            {
                "slug": "c1-modality-nuance",
                "title": "Must Have Been...: Deduction in the Past",
                "skill": "Grammar",
                "summary": "Deduções no passado com must have, can't have e might have, além de needn't have vs. didn't need to.",
                "theory": (
                    "No C1, o que separa o fluente do proficiente é a precisão das deduções. "
                    "'Must have + particípio' expressa conclusão quase certa sobre o passado — a dúvida "
                    "praticamente desapareceu — e 'can't have' é o espelho disso: impossibilidade. "
                    "'Might/may/could have' mantêm a porta aberta. Já 'needn't have + particípio' é diferente de "
                    "'didn't need to': o primeiro diz 'fez, mas era desnecessário'; o segundo só afirma que não "
                    "havia necessidade, sem dizer se a ação ocorreu. Cuidado com o clássico brasileiro: obrigação "
                    "no passado é 'had to', nunca 'must have', que os lusófonos usam por influência do 'deve ter'. "
                    "'Be supposed to' indica expectativa ou combinado — e ganha tom de crítica quando frustrado."
                ),
                "example": "She must have left already — her coat's gone. You needn't have cooked; we ate on the way here.",
                "key_points": [
                    "must have + particípio = certeza quase total",
                    "can't have + particípio = impossibilidade",
                    "needn't have = fez à toa; didn't need to = não era preciso",
                    "was supposed to = expectativa frustrada",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "O anfitrião cozinhou para 20 pessoas, mas só 8 apareceram. Qual frase comunica 'a ação ocorreu, mas era desnecessária'?",
                        "choices": [
                            "You didn't need to cook so much.",
                            "You needn't have cooked so much.",
                            "You mustn't have cooked so much.",
                            "You can't have cooked so much.",
                        ],
                        "correct_index": 1,
                        "explanation": "'Needn't have + particípio' pressupõe ação realizada e desnecessária. 'Didn't need to' não diz se ele cozinhou; e para dedução negativa não existe 'mustn't have' — usa-se 'can't have'.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "A casa está escura e ninguém atende a porta. They ___ (dedução quase certa) have gone out.",
                        "correct": "must",
                        "accepted": ["must"],
                        "explanation": "'Must have + particípio' é a conclusão quase certa sobre o passado, como o nosso 'deve ter saído'. Não confunda com obrigação passada, que é 'had to'.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Você viu seu colega embarcar. Qual frase expressa impossibilidade: 'ele não pode ter perdido o voo'?",
                        "choices": [
                            "He might have missed the flight.",
                            "He should have missed the flight.",
                            "He can't have missed the flight.",
                            "He must have missed the flight.",
                        ],
                        "correct_index": 2,
                        "explanation": "'Can't have + particípio' é a dedução negativa forte: 'é impossível que...'. 'Must have' afirmaria o contrário; 'might have' deixaria a porta aberta; 'should have' é crítica, não dedução.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "O combinado era meio-dia e já são três horas. The train ___ (expectativa frustrada) to arrive at noon, but it's already three.",
                        "correct": "was supposed",
                        "explanation": "'Was supposed to' comunica expectativa frustrada — 'era para ter chegado ao meio-dia'. Equivale ao português 'era para...', com tom implícito de crítica.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: forgotten / can't / have / he / meeting / the",
                        "correct": "He can't have forgotten the meeting.",
                        "explanation": "Ordem canônica da dedução: sujeito + can't + have + particípio. 'He can't have forgotten the meeting.' — impossibilidade afirmada com confiança.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva exatamente a frase que você ouviu.",
                        "correct": "You needn't have worried about the tickets.",
                        "explanation": "'Needn't have worried' = preocupou-se sem necessidade. Repare na pronúncia conectada de 'needn't have', que soa quase 'needn-tav' na fala rápida.",
                    },
                ],
            },
            {
                "slug": "c1-subjunctive",
                "title": "Unreal Past & Subjunctive",
                "skill": "Grammar",
                "summary": "I'd rather you didn't, it's time we went e o subjuntivo com suggest e insist: passado que fala do presente.",
                "theory": (
                    "O inglês tem dois 'passados irreais'. Primeiro, o unreal past: 'I'd rather you didn't', "
                    "'It's time we went' e 'if it weren't for...' usam o passado para falar do agora — o passado "
                    "aqui é distância psicológica, não tempo. Segundo, o subjuntivo mandativo: após suggest, "
                    "insist, demand, recommend e urge, usa-se o verbo base para qualquer pessoa — 'I suggest he "
                    "go', nunca 'goes'. O português ajuda e atrapalha: 'sugiro que ele vá' também é subjuntivo, "
                    "mas o brasileiro tende a trocar por indicativo ('he goes') ou por 'that he would go'. Note "
                    "ainda 'It's high time', que acrescenta urgência crítica a uma situação já atrasada."
                ),
                "example": "I'd rather you didn't mention this to anyone. It's high time we made a decision.",
                "key_points": [
                    "I'd rather you didn't + verbo",
                    "It's (high) time + sujeito + passado",
                    "suggest/insist/demand + verbo base",
                    "if it weren't for... = se não fosse por...",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Complete: 'The board insisted that the CEO ___ present at the hearing.'",
                        "choices": ["is", "be", "was", "would be"],
                        "correct_index": 1,
                        "explanation": "Após insist, suggest, demand, recommend e urge, o subjuntivo mandativo usa o verbo base para qualquer pessoa: 'that the CEO be'. 'Is' e 'was' são indicativo — erro clássico do brasileiro.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "O táxi já está esperando lá embaixo. It's time we ___ (verbo leave) — the taxi is waiting.",
                        "correct": "left",
                        "explanation": "'It's time + sujeito + passado' é unreal past: passado gramatical para um presente real. 'It's time we left' = precisamos ir agora; 'it's time we go' soa de aprendiz.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual frase soa como conselho crítico e urgente sobre o presente?",
                        "choices": [
                            "It's high time you find a new job.",
                            "It's high time you found a new job.",
                            "It's high time you will find a new job.",
                            "It's high time you would find a new job.",
                        ],
                        "correct_index": 1,
                        "explanation": "'High' intensifica a urgência, mas o passado irreal permanece: 'you found'. A crítica implícita é 'isso já devia ter acontecido' — urgência com passado, não com futuro.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Você prefere que seu colega fique quieto por enquanto: I'd rather you ___ (negativo de tell) anyone about this.",
                        "correct": "didn't tell",
                        "explanation": "'I'd rather + sujeito diferente + passado simples' expressa preferência sobre a ação de outro: 'prefiro que você não conte'. Com o mesmo sujeito, seria 'I'd rather not tell'.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: time / we / it's / this / talked / about",
                        "correct": "It's time we talked about this.",
                        "explanation": "A estrutura é inalterável: 'It's time' + sujeito ('we') + verbo no passado ('talked'). O passado marca irrealidade — a conversa ainda não aconteceu —, não tempo.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e digite a frase que você ouviu.",
                        "correct": "If it weren't for you, we'd never have met.",
                        "explanation": "'If it weren't for...' = 'se não fosse por...'. Note a contração 'we'd' e o 'were' subjuntivo fixo, mesmo com sujeito singular — 'wasn't' seria informal demais aqui.",
                    },
                ],
            },
            {
                "slug": "c1-participle-clauses",
                "title": "Compact & Elegant: Participle Clauses",
                "skill": "Grammar",
                "summary": "Comprima duas ideias em uma frase elegante com cláusulas de particípio — e evite o dangling participle.",
                "theory": (
                    "Cláusulas de particípio comprimem duas ideias em uma frase elegante: 'Walking home, I had "
                    "an idea' substitui 'While I was walking home, I had an idea'. O particípio presente (-ing) "
                    "marca voz ativa ou simultaneidade; o particípio passado marca voz passiva: 'the letters "
                    "written in ink'. 'Having been + particípio' situa uma ação passiva antes da principal. O "
                    "erro típico é o dangling participle: 'Walking home, the rain started' — a chuva não "
                    "caminha! O sujeito da cláusula precisa ser o sujeito da oração principal. Em escrita "
                    "formal, essa estrutura elimina redundância e eleva o registro de uma vez."
                ),
                "example": "Sealed in airtight jars, the jam keeps for years. Having studied under three masters, she cooks with quiet authority.",
                "key_points": [
                    "particípio presente (-ing) = voz ativa",
                    "particípio passado = voz passiva",
                    "having been + particípio = passiva anterior",
                    "sujeito da cláusula = sujeito da frase principal",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Complete: '___ in small batches, the cheese keeps its full flavor.'",
                        "choices": ["Making", "Made", "Having made", "To make"],
                        "correct_index": 1,
                        "explanation": "O queijo é fabricado — voz passiva —, logo particípio passado: 'Made in small batches'. '-ing' marcaria voz ativa, como se o queijo se fabricasse a si mesmo.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: home / walking / I / a / had / idea / brilliant",
                        "correct": "Walking home, I had a brilliant idea.",
                        "explanation": "A cláusula de particípio abre a frase seguida de vírgula, e o sujeito ('I') vem logo depois: quem caminha é quem tem a ideia. É isso que evita o dangling participle.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "___ (have/spend) ten years in Japan, he negotiates like a local.",
                        "correct": "Having spent",
                        "explanation": "'Having + particípio' marca ação concluída antes da principal. 'Spending ten years in Japan...' daria ideia de simultaneidade — impossível entre passar anos e negociar.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual frase evita o erro de dangling participle?",
                        "choices": [
                            "Opening the window, a cold breeze came in.",
                            "Opening the window, I let a cold breeze in.",
                            "Opened the window, the breeze came in.",
                            "Being opened the window, a breeze came in.",
                        ],
                        "correct_index": 1,
                        "explanation": "Quem abre a janela é 'I', então 'I' deve ser o sujeito principal. Na primeira opção, a brisa estaria abrindo a janela — erro clássico, gramaticalmente possível e semanticamente cômico.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "O romance foi escrito em 1847: The novel, ___ (write) in 1847, still feels startlingly modern.",
                        "correct": "written",
                        "explanation": "Voz passiva: o romance foi escrito, não escreveu. 'Written in 1847' substitui 'which was written in 1847' — condensação elegante típica de texto formal.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "Having been warned twice, he finally changed.",
                        "explanation": "'Having been warned' = passiva + anterioridade: 'por ter sido avisado'. A sequência having + been + particípio condensa uma cláusula inteira em quatro palavras.",
                    },
                ],
            },
            {
                "slug": "c1-negotiating",
                "title": "Reaching Agreement: The Art of Negotiating",
                "skill": "Conversation",
                "summary": "Negocie em inglês com diplomacia: concessões, condições e a arte de recusar sem quebrar a relação.",
                "theory": (
                    "Negociar em inglês exige diplomacia: raramente se diz 'no' seco. Padrões como 'I'm afraid "
                    "that won't work for us', 'We'd be willing to..., provided that...' e 'Let's meet halfway' "
                    "abrandam posições sem abrir mão delas. Condições vêm embaladas em 'as long as' e 'unless'; "
                    "concessões, em 'in exchange for'. O brasileiro costuma ser direto demais — 'I don't agree' "
                    "soa abrupto; prefira 'I see your point, however...'. E ouça o que não é dito: 'That's our "
                    "best offer' dito com hesitação quase sempre ainda é negociável."
                ),
                "example": "In exchange for a longer commitment, we could revisit the annual fee.",
                "key_points": [
                    "I'm afraid that won't work for us",
                    "provided that / as long as = desde que",
                    "in exchange for = em troca de",
                    "let's meet halfway = vamos ao meio-termo",
                ],
                "dialogue": [
                    {"speaker": "Ana", "line": "Thanks for making time, Mike. We'd love to license your platform, but the annual fee is honestly beyond our budget."},
                    {"speaker": "Mike", "line": "I hear you. What if we tiered the pricing instead of cutting it?"},
                    {"speaker": "Ana", "line": "That's interesting. We'd be willing to sign a two-year contract, provided that the second year comes at a discount."},
                    {"speaker": "Mike", "line": "Two years is a big commitment. I'm afraid I can't do that without something in return."},
                    {"speaker": "Ana", "line": "Fair enough. In exchange for the discount, we could feature your platform as our preferred partner in all our materials."},
                    {"speaker": "Mike", "line": "That would give us real exposure... Let's meet halfway: fifteen percent off, and you keep the case study rights."},
                    {"speaker": "Ana", "line": "Deal — as long as the discount applies from month one, not after renewal."},
                    {"speaker": "Mike", "line": "Agreed. I'll send the revised terms today, and we can finalize by Friday."},
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Como recusar uma proposta com diplomacia, sem dizer 'no' seco?",
                        "choices": [
                            "That's a terrible offer.",
                            "I'm afraid that won't work for us.",
                            "No, absolutely not.",
                            "You must be joking.",
                        ],
                        "correct_index": 1,
                        "explanation": "'I'm afraid that won't work for us' recusa com cortesia: o 'I'm afraid' amortece o golpe e 'won't work' critica a proposta, não a pessoa. Negociação é preservar a relação enquanto se defende o interesse.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Concessão condicional: We'd be willing to extend the contract, ___ that you guarantee exclusivity.",
                        "correct": "provided",
                        "accepted": ["provided"],
                        "explanation": "'Provided that' introduz condição formal — 'desde que'. Equivale a 'as long as', mas soa mais contratual, perfeito para mesas de negociação e cláusulas de acordo.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "O que significa a proposta 'Let's meet halfway'?",
                        "choices": [
                            "Vamos desistir da negociação.",
                            "Vamos encontrar um termo intermediário.",
                            "Vamos marcar a reunião em outro local.",
                            "Vamos deixar a decisão para depois.",
                        ],
                        "correct_index": 1,
                        "explanation": "'Meet halfway' propõe compromisso: cada lado cede um pouco e o acordo acontece no meio. É o gesto clássico de quem quer fechar sem que ninguém perca a face.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Troca de concessões: ___ exchange for the discount, we'll feature your brand in our campaigns.",
                        "correct": "In",
                        "explanation": "'In exchange for' apresenta a moeda de troca: 'em troca de'. É o padrão para explicitar o que cada lado ganha ao ceder algo — transparência que acelera acordos.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: discount / as / as / the / long / applies / month / from / one",
                        "correct": "As long as the discount applies from month one.",
                        "explanation": "'As long as' abre a condição: 'desde que o desconto valha desde o primeiro mês'. A ordem é conjunção + condição + resto — sem inversão, diferente das estruturas enfáticas.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e digite a frase de negociação que você ouviu.",
                        "correct": "We could live with fifteen percent off.",
                        "explanation": "'We could live with...' sinaliza aceitação relutante: 'não é o ideal, mas fecha'. Essa nuance de voz — meio cética, meio conciliadora — vale ouro em negociação.",
                    },
                ],
            },
        ],
    },
    {
        "title": "Sophisticated Structures",
        "position": 2,
        "description": "Inversão, cleft, elipse e nominalização: as estruturas que dão sofisticação ao inglês avançado.",
        "lessons": [
            {
                "slug": "c1-inversion",
                "title": "Never Have I Seen: Inversion for Emphasis",
                "skill": "Grammar",
                "summary": "Inversão com advérbios negativos para ênfase dramática: Never have I seen, No sooner had..., So... was...",
                "theory": (
                    "Inversão é ênfase dramática: 'Never have I seen such a mess' soa mais forte que 'I have "
                    "never seen such a mess'. A regra: advérbio negativo ou restritivo no início (never, rarely, "
                    "seldom, no sooner, not only, under no circumstances) força a ordem auxiliar + sujeito, como "
                    "numa pergunta. 'No sooner had we sat down than the show began' pede o par fixo 'than'; "
                    "'Not only did she win, but she also broke a record' exige a estrutura paralela 'but... "
                    "also'. Atenção: advérbios comuns como 'always' e 'often' não provocam inversão. O erro "
                    "típico do brasileiro é manter a ordem declarativa — 'Never I have seen' —, que soa "
                    "estrangeiro até em texto informal."
                ),
                "example": "Rarely had the city seen such a turnout. So intense was the heat that the marathon was cancelled.",
                "key_points": [
                    "Never/Rarely + auxiliar + sujeito + verbo",
                    "No sooner had... than...",
                    "Not only did..., but... also...",
                    "So + adjetivo + was + sujeito + that...",
                ],
                "questions": [
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: have / I / never / such / seen / a / mess",
                        "correct": "Never have I seen such a mess.",
                        "explanation": "Advérbio negativo na frente puxa a inversão: 'Never + have + I + particípio'. É a estrutura de pergunta aplicada à ênfase dramática — o choque mora na ordem das palavras.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Complete: 'No sooner ___ the door than the phone rang.'",
                        "choices": ["we had closed", "had we closed", "we closed", "did we close"],
                        "correct_index": 1,
                        "explanation": "'No sooner' exige 'had + sujeito + particípio', e o par fixo é 'than': mal fechamos a porta e o telefone tocou. A ordem declarativa ('we had closed') cancela toda a ênfase.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Ênfase dupla: Not only ___ (arrive) late, but he also forgot the slides.",
                        "correct": "did he arrive",
                        "explanation": "'Not only' no início exige auxiliar + sujeito + verbo base: 'did he arrive'. E o par 'but... also' completa a estrutura — chegar atrasado E ainda esquecer os slides.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual frase com 'so/such... that' invertida está correta?",
                        "choices": [
                            "So convincing was her argument that everyone agreed.",
                            "So convincing her argument was that everyone agreed.",
                            "Such convincing was her argument that everyone agreed.",
                            "So convincingly was her argument that everyone agreed.",
                        ],
                        "correct_index": 0,
                        "explanation": "Com 'so + adjetivo' na frente, inverte-se: 'So convincing was her argument that...'. 'Such' exigiria 'a + substantivo'; 'convincingly' seria advérbio, que não descreve 'argument' aqui.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "Rarely does she accept interviews.",
                        "explanation": "Advérbio restritivo na frente + inversão com 'does': 'raramente ela aceita'. A ênfase sugere que recusar entrevistas é quase regra para ela — força que a ordem comum não teria.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual advérbio NÃO provoca inversão quando colocado no início da frase?",
                        "choices": ["Never", "Rarely", "Always", "Seldom"],
                        "correct_index": 2,
                        "explanation": "Só advérbios negativos ou restritivos disparam a inversão. 'Always' é frequência comum: 'Always I have loved...' permanece declarativo (ou soa poético) — sem auxiliar à frente do sujeito.",
                    },
                ],
            },
            {
                "slug": "c1-cleft-sentences",
                "title": "It Was You Who...: Cleft Sentences",
                "skill": "Grammar",
                "summary": "Cleft sentences para ênfase cirúrgica: It was you who..., What I need is..., All I did was...",
                "theory": (
                    "Cleft sentences existem para destacar um único elemento da frase: 'It was John who paid' "
                    "responde a 'quem pagou?'; 'What I need is time' joga 'time' para o final, onde o inglês "
                    "põe o peso informativo. Há três padrões: it-cleft (It + be + destaque + who/that), "
                    "what-cleft (What + ideia conhecida + be + destaque) e all-cleft (All I did was + verbo "
                    "base). O português tem 'Foi o João que pagou', então a lógica é familiar — mas o brasileiro "
                    "costuma omitir o 'who/that' ou produzir 'What I need it is time', com o 'it' extra. Em "
                    "conversa, clefts são ouro: corrigem informações ('It wasn't me who said that') e suavizam "
                    "críticas com precisão."
                ),
                "example": "What gets me is the silence, not the noise. It wasn't the money that bothered her; it was the principle.",
                "key_points": [
                    "It was John who paid",
                    "What I need is time",
                    "All I did was + verbo base",
                    "nunca 'What I need it is...' (sem 'it' extra)",
                ],
                "questions": [
                    {
                        "type": "FILL_IN",
                        "prompt": "Destaque 'a break': ___ I really need is a break, not another meeting.",
                        "correct": "What",
                        "explanation": "What-cleft: 'What + ideia conhecida + be + destaque'. A frase responde 'o que você precisa?', jogando 'a break' para o final — a posição de destaque natural do inglês.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: was / it / who / you / broke / the / vase",
                        "correct": "It was you who broke the vase.",
                        "explanation": "It-cleft para acusar com precisão: 'It + was + you + who + verbo'. O destaque 'you' fica isolado entre 'was' e 'who' — impossível não ouvir quem quebrou o vaso.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Complete: 'All I did ___ suggest a different approach.'",
                        "choices": ["was", "is", "were", "did"],
                        "correct_index": 0,
                        "explanation": "All-cleft minimiza a ação para se defender: 'All I did was + verbo base' — 'eu só sugeri'. Sem 'to' e sem flexão no verbo seguinte, é estrutura fechada.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Em 'She loves the mountains', qual cleft enfatiza 'the mountains'?",
                        "choices": [
                            "It is she that loves the mountains.",
                            "It is the mountains that she loves.",
                            "What she is loves the mountains.",
                            "It was the mountains what she loves.",
                        ],
                        "correct_index": 1,
                        "explanation": "O it-cleft move o elemento em destaque para logo após 'It is': 'It is the mountains that she loves'. A primeira opção destacaria 'she'; 'what' no lugar de 'that' é marca de registro popular.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e digite a frase enfática que você ouviu.",
                        "correct": "What surprised me was the price.",
                        "explanation": "What-cleft com 'surprised': o espanto é informação conhecida; 'the price' é a novidade, plantada no final. Repare na entonação, que cresce até 'price' e cai no fechamento.",
                    },
                ],
            },
            {
                "slug": "c1-ellipsis-substitution",
                "title": "Saying Less, Meaning More: Ellipsis & Substitution",
                "skill": "Grammar",
                "summary": "Elipse e substituição para soar nativo: so do I, neither have I, one/ones, do so.",
                "theory": (
                    "Elipse e substituição mantêm o fluxo sem repetir: 'so do I' e 'neither have we' devolvem "
                    "concordância; 'one/ones' substituem contáveis ('the fresh ones'); 'do so' substitui "
                    "verbos-ação em registro formal ('they did so immediately'). A pegadinha clássica: 'So do "
                    "I' concorda com o interlocutor, mas 'So I do' confirma algo que disseram sobre você — a "
                    "ordem muda o sentido. Brasileiros abusam de 'me too', que funciona, mas soa limitado em "
                    "contexto profissional. Domine também 'I think so', 'I hope not' e a elipse após 'and/but/"
                    "or' ('She can stay, but I can't') — o que o inglês pode omitir, ele omite."
                ),
                "example": "— I love Ethiopian food. — So do I. — I couldn't eat another bite. — Neither could I.",
                "key_points": [
                    "So do I / Neither have I = concordância",
                    "So I do = confirmação sobre si mesmo",
                    "one/ones substituem contáveis",
                    "do so = ação completa, registro formal",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "— I've never tried oysters. — Qual resposta concorda ('eu também nunca')?",
                        "choices": ["So have I.", "Neither have I.", "Neither do I.", "So do I."],
                        "correct_index": 1,
                        "explanation": "Frase negativa pede 'Neither + auxiliar da frase + sujeito': 'Neither have I'. 'Neither do I' trocaria o auxiliar (o verbo é 'have tried'); 'So have I' concordaria com uma afirmação positiva.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Registro formal: Cutting costs won't be easy, but we must ___ (fazer isso) before June.",
                        "correct": "do so",
                        "explanation": "'Do so' substitui a ação inteira ('cut costs') em registro formal — comum em relatórios e atas. Na fala do dia a dia, 'do it' é o equivalente neutro.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Complete: 'These cookies are stale; I'd like fresh ___.'",
                        "choices": ["one", "ones", "them", "some of one"],
                        "correct_index": 1,
                        "explanation": "'Ones' substitui um plural contável ('cookies'): biscoitos frescos, outros biscoitos. 'One' seria singular; 'them' se referiria aos mesmos biscoitos velhos, não a novos.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: so / would / I / do / never",
                        "correct": "I would never do so.",
                        "explanation": "Aqui não há inversão: 'never' está no meio da frase, não no início. A substituição 'do so' fecha a ideia — 'eu jamais faria isso' — em registro formal e econômico.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "— You speak French, don't you? — Qual resposta confirma algo dito sobre você mesmo?",
                        "choices": ["So do I.", "So I do.", "Neither do I.", "So I am."],
                        "correct_index": 1,
                        "explanation": "'So do I' concorda com o interlocutor; 'So I do' confirma algo que disseram sobre você: 'de fato falo'. A posição do sujeito inverte o sentido — pegadinha clássica de exame.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a resposta que você ouviu.",
                        "correct": "Neither would I, to be honest.",
                        "explanation": "Concordância com negativa no condicional: 'Neither + would + I'. O aposto 'to be honest' é típico da fala espontânea e soa natural, nunca ensaiado — repare na entonação de fechamento.",
                    },
                ],
            },
            {
                "slug": "c1-nominalisation",
                "title": "From Verbs to Concepts: Nominalisation",
                "skill": "Grammar",
                "summary": "Transforme verbos em conceitos e eleve o registro: they decided → the decision.",
                "theory": (
                    "Nominalização é o motor da escrita formal: transformar verbos e adjetivos em substantivos "
                    "— 'they decided' vira 'the decision', 'prices rose' vira 'the rise in prices'. O efeito é "
                    "densidade e impessoalidade, típicos de relatórios, atas e textos acadêmicos; os "
                    "conectores mudam junto: 'because' cede lugar a 'due to/owing to', 'so' a 'therefore'. "
                    "'The implementation of the policy requires funding' soa institucional; 'They implemented "
                    "the policy and needed money' soa como relato de bastidor. O alerta: excesso de "
                    "nominalização cria texto pesado e vago — use para condensar ideias, não para esconder o "
                    "agente quando ele importa."
                ),
                "example": "The company's decision to downsize preceded a sharp rise in unemployment claims.",
                "key_points": [
                    "they decided → the decision",
                    "because → due to + substantivo",
                    "so → therefore",
                    "nominalize para condensar, não para esconder",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Qual versão tem o registro mais formal, típico de relatório?",
                        "choices": [
                            "The government analyzed the data carefully.",
                            "The careful analysis of the data was carried out by the government.",
                            "The government did a careful look at the data.",
                            "Someone in the government went over the data.",
                        ],
                        "correct_index": 1,
                        "explanation": "A nominalização ('the careful analysis') somada à voz passiva ('was carried out') cria o tom impessoal do relatório. A primeira opção é gramaticalmente correta, mas soa como conversa de corredor.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "O anúncio da chegada: The ___ (arrive) of the train was announced with a delay.",
                        "correct": "arrival",
                        "explanation": "'Arrival' nominaliza 'arrive': a ação vira conceito e assume o posto de sujeito. Padrão onipresente em avisos, horários e textos institucionais.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Complete com o conector formal: '___ the strike, no buses were running.'",
                        "choices": ["Because", "Due to", "Owing", "Since"],
                        "correct_index": 1,
                        "explanation": "'Due to' + substantivo substitui 'because' + oração no registro formal. 'Because' e 'since' exigem oração com verbo; 'owing' sozinho não existe — o par é 'owing to'.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: in / prices / rise / the / resulted / shortage / a / in",
                        "correct": "The rise in prices resulted in a shortage.",
                        "explanation": "Nominalize o verbo (rose → rise) e a cadeia muda: 'the rise in prices resulted in a shortage'. Duas ações viram dois conceitos encadeados — denso, formal, elegante.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase de relatório que você ouviu.",
                        "correct": "The implementation of the policy requires funding.",
                        "explanation": "'Implementation' nominaliza 'implement': a ação vira substantivo e a frase ganha o tom institucional de documentos oficiais e papers — sem agente, sem roteiro, só conceito.",
                    },
                ],
            },
        ],
    },
    {
        "title": "Register & Style",
        "position": 3,
        "description": "Registro formal vs. informal, hedging e coesão: escreva e fale como um profissional.",
        "lessons": [
            {
                "slug": "c1-register-switching",
                "title": "Who Are You Talking To? Register Switching",
                "skill": "Grammar",
                "summary": "Escolha a palavra certa para a ocasião: obtain vs. get, require vs. need, phrasal vs. verbo latino.",
                "theory": (
                    "Registro é escolha de vocabulário conforme a situação: 'get' vira 'obtain', 'need' vira "
                    "'require', 'buy' vira 'purchase', 'help' vira 'assist'. A regra prática: verbos de origem "
                    "latina pertencem ao registro formal (contratos, e-mails para clientes, papers); phrasal "
                    "verbs ('put off', 'find out') pertencem ao informal. O brasileiro avançado erra nos dois "
                    "sentidos: soa frio demais com amigos ('I require your assistance to move the sofa') ou "
                    "informal demais no trabalho ('Can you gimme the report?'). Em e-mails profissionais, "
                    "prefira 'I would appreciate' a 'I want'; em contratos, 'the party shall' a 'the party "
                    "will' — shall obriga, will apenas prevê."
                ),
                "example": "We require further documentation; please assist us by submitting the invoices. (Formal) / Can you help me out with the invoices? (Informal)",
                "key_points": [
                    "get → obtain, buy → purchase, help → assist",
                    "phrasal verb = informal; verbo latino = formal",
                    "shall obriga em contratos; would suaviza pedidos",
                    "registro alto: clientes, contratos e papers",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Qual frase pertence a um e-mail formal?",
                        "choices": [
                            "We need to get more info on this.",
                            "Further information is required before we proceed.",
                            "Can you grab some details for us?",
                            "We gotta find out more about it.",
                        ],
                        "correct_index": 1,
                        "explanation": "O registro formal troca 'get' por 'require/obtain' e prefere a voz passiva impessoal ('is required'). As outras são coloquiais — 'gotta' nem caberia num e-mail informal profissional.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Versão formal de 'Can you help me with this?': Could you ___ me with this matter?",
                        "correct": "assist",
                        "explanation": "'Assist' é o par latino de 'help': formal e impessoal, padrão em atendimento e correspondência. 'Help' é neutro; 'assist' eleva o registro da frase inteira de uma vez.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Substituto formal do phrasal verb em 'We put off the meeting':",
                        "choices": [
                            "We postponed the meeting.",
                            "We delayed-off the meeting.",
                            "We hold off the meeting.",
                            "We pushed the meeting off.",
                        ],
                        "correct_index": 0,
                        "explanation": "Phrasal verbs ('put off', 'hold off') são informais; o verbo latino 'postpone' é o equivalente de contrato e e-mail sério. Mesma informação, registro diferente — 'delayed-off' nem existe.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Agora o contrário, o par informal de 'purchase': I just need to ___ a new laptop this weekend.",
                        "correct": "buy",
                        "explanation": "'Purchase' é formal (notas fiscais, contratos); 'buy' é a escolha natural na fala. Saber descer o registro é tão importante quanto elevá-lo — formalidade em excesso soa distante.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase de encerramento formal que você ouviu.",
                        "correct": "Your assistance in this matter would be appreciated.",
                        "explanation": "Fórmula clássica de correspondência: 'assistance' (não 'help'), 'matter' (não 'thing'), condicional 'would be' (não 'will be'). Registro alto de ponta a ponta.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual par segue a direção informal → formal corretamente?",
                        "choices": ["need → require", "require → need", "obtain → get", "inquire → ask"],
                        "correct_index": 0,
                        "explanation": "A seta aponta sempre para o lado latino: need → require, get → obtain, ask → inquire. Invertê-la rebaixa o registro — erro comum quando se traduz literalmente do português.",
                    },
                ],
            },
            {
                "slug": "c1-hedging-stance",
                "title": "Softening Your Claims: Hedging & Stance",
                "skill": "Vocabulary",
                "summary": "Hedging e stance para claims defensáveis: appears to, tends to, arguably, admittedly.",
                "theory": (
                    "Hedging é o seguro da escrita acadêmica e profissional: 'appears to', 'tends to', "
                    "'arguably', 'to some extent' protegem suas afirmações de exceções — dizer 'Social media "
                    "destroys attention' convida à refutação; 'appears to affect attention' é defensável. Já "
                    "os stance adverbs sinalizam sua atitude diante do conteúdo: 'surprisingly', 'admittedly', "
                    "'understandably', 'predictably' avaliam sem alterar o fato. O erro do brasileiro é a "
                    "generalização absoluta, herança do 'os brasileiros são...' — em inglês avançado, claims "
                    "absolutos parecem ingênuos ou arrogantes. Hedging não é fraqueza: é precisão intelectual, "
                    "a marca de quem conhece os limites dos próprios dados."
                ),
                "example": "The data arguably point to a modest effect, though the sample admittedly remains small.",
                "key_points": [
                    "appears to / tends to = hedge de evidência",
                    "arguably / to some extent = hedge de escopo",
                    "surprisingly / admittedly = stance",
                    "claim absoluto soa ingênuo em inglês",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Qual frase apresenta um claim de forma defensável em texto acadêmico?",
                        "choices": [
                            "Social media destroys teenagers' attention spans.",
                            "Social media appears to affect teenagers' attention spans.",
                            "Social media obviously harms everyone equally.",
                            "Social media will always damage concentration.",
                        ],
                        "correct_index": 1,
                        "explanation": "'Appears to' protege o claim: você afirma uma tendência observável, não uma lei universal. Absolutos como 'destroys', 'obviously' e 'always' convidam refutação imediata.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Indicação de tendência: The results ___ to support the hypothesis, but more studies are needed.",
                        "correct": "tend",
                        "explanation": "'Tend to' suaviza a generalização: 'em geral, apontam para'. É o hedge favorito de papers — reconhece exceções sem abdicar da conclusão central.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Complete: '___, no one predicted such demand — the app went viral overnight.'",
                        "choices": ["Predictably", "Surprisingly", "Understandably", "Admittedly"],
                        "correct_index": 1,
                        "explanation": "O stance adverb 'surprisingly' avalia o fato como inesperado. 'Predictably' diria o oposto; 'understandably' e 'admittedly' caberiam em contextos de empatia ou concessão, não de espanto.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Hedge de escopo: The policy, ___ speaking, achieved its goals in urban areas.",
                        "correct": "broadly",
                        "accepted": ["broadly", "generally"],
                        "explanation": "'Broadly speaking' (ou 'generally speaking') delimita o alcance do claim: vale em geral, com espaço para exceções. É precisão intelectual, não covardia — o oposto do claim absoluto.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase acadêmica que você ouviu.",
                        "correct": "The findings tend to confirm earlier studies.",
                        "explanation": "Note 'tend to confirm': nem 'prove' (forte demais), nem 'might suggest' (fraco demais) — o meio-termo exato de um claim bem calibrado, típico de abstracts.",
                    },
                ],
            },
            {
                "slug": "c1-cohesion-writing",
                "title": "Writing That Flows: Cohesion & Coherence",
                "skill": "Writing",
                "summary": "Coesão de nível profissional: cadeias de referência, topic sentences e estrutura dado-novo.",
                "theory": (
                    "Texto que flui não repete: cria cadeias de referência. 'This growth', 'such measures', "
                    "'the latter', 'these findings' retomam o já dito e encadeiam o novo — é a estrutura "
                    "given-new: comece a frase com informação conhecida e termine com a novidade, que recebe o "
                    "peso. Cada parágrafo abre com uma topic sentence que anuncia a ideia central; as demais "
                    "frases sustentam-na sem abrir novas frentes. Conectores como 'moreover' e 'furthermore' "
                    "ajudam, mas o excesso denuncia texto costurado às pressas — a coesão de verdade vem da "
                    "repetição controlada, dos pronomes e dos demonstrativos, não de cola sintática."
                ),
                "example": "Remote work boosts retention. This benefit, however, comes at the cost of weaker mentorship.",
                "key_points": [
                    "this + substantivo retoma o já dito",
                    "the former / the latter para duas opções",
                    "topic sentence abre cada parágrafo",
                    "dado conhecido primeiro, novidade no fim",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Qual seria uma boa topic sentence para um parágrafo sobre os desafios do trabalho remoto?",
                        "choices": [
                            "Remote work also brings challenges that companies often underestimate.",
                            "For example, my cousin works from home.",
                            "It's hard, really hard, in many ways.",
                            "Furthermore, moreover, in addition.",
                        ],
                        "correct_index": 0,
                        "explanation": "A topic sentence anuncia a ideia central e cria expectativa de desenvolvimento. As outras não orientam: exemplo solto não substitui anúncio, vagueza não informa, e empilhar conectores revela texto sem planejamento.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Duas opções foram propostas: contratar localmente ou realocar a equipe. ___ (a segunda mencionada) would be far more costly.",
                        "correct": "The latter",
                        "explanation": "'The latter' retoma a segunda de duas opções; 'the former', a primeira. Evita repetir 'realocar a equipe' e mantém a cadeia de referência limpa — coesão por economia.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Coesão sem repetição: 'Sales grew twelve percent. ___ was driven almost entirely by exports.'",
                        "choices": ["This growth", "The growth of it", "That it grew", "It grew"],
                        "correct_index": 0,
                        "explanation": "'This + substantivo' cria cadeia de referência: retoma 'grew' como conceito ('this growth') e avança. Repetir 'sales grew' ou usar 'the growth of it' denunciaria texto amador.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: paragraph / a / with / begin / clear / sentence / topic / a",
                        "correct": "Begin a paragraph with a clear topic sentence.",
                        "explanation": "A regra de ouro da coesão: cada parágrafo abre com a frase-âncora que anuncia a ideia. O leitor agradece — e o seu texto ganha um esqueleto visível de ponta a ponta.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "The latter option deserves closer consideration.",
                        "explanation": "'The latter option' retoma a segunda alternativa já mencionada, e 'closer consideration' a encadeia — coesão por referência, sem nenhum conector: é isso que separa o C1 do B2.",
                    },
                ],
            },
        ],
    },
    {
        "title": "C1 Fluency Lab",
        "position": 4,
        "description": "Colocações precisas, apresentações com signposting e o desafio final que reúne todo o nível.",
        "lessons": [
            {
                "slug": "c1-collocation-precision",
                "title": "The Perfect Word: Collocation Precision",
                "skill": "Vocabulary",
                "summary": "Colocações exatas que separam o fluente do nativo: utterly ridiculous, painfully shy, meet a deadline.",
                "theory": (
                    "Colocação é casamento de palavras: algumas combinam, outras não. 'Utterly ridiculous', "
                    "'painfully shy', 'highly unlikely', 'bitterly cold', 'deeply concerned', 'fully aware' — o "
                    "advérbio certo muda com o adjetivo, e não há regra lógica, apenas uso. No campo "
                    "verbo-substantivo: 'meet a deadline' (não 'reach'), 'pose a challenge', 'raise awareness', "
                    "'make progress'. O brasileiro traduz literalmente e produz 'strongly ridiculous' ou 'make "
                    "a research' — gramaticalmente possível, mas estranho ao ouvido nativo. A saída é tratar "
                    "colocações como blocos prontos, aprendidas em pacote, nunca palavra por palavra: cada "
                    "colocação nova deve entrar no seu repertório como uma unidade indivisível."
                ),
                "example": "She was painfully shy, yet her argument was utterly convincing — and highly original.",
                "key_points": [
                    "utterly ridiculous / absurd",
                    "painfully shy, bitterly cold, deeply concerned",
                    "highly unlikely / effective / successful",
                    "meet a deadline, pose a challenge",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Qual advérbio collocaciona com 'ridiculous' para intensificá-lo?",
                        "choices": ["utterly", "bitterly", "strongly", "heavily"],
                        "correct_index": 0,
                        "explanation": "'Utterly ridiculous' é casamento consagrado. 'Bitterly' casa com cold/disappointed; 'strongly', com verbos como believe; 'heavily', com rain. Colocação não se traduz — memoriza-se em bloco.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Ela cora quando alguém olha para ela: She's ___ shy — public speaking terrifies her.",
                        "correct": "painfully",
                        "explanation": "'Painfully shy' = timidez quase dolorosa, intensidade máxima. 'Very shy' comunica menos; 'painfully' carrega a avaliação emocional junto com o grau — mais palavra, muito mais sentido.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Complete: 'It's ___ unlikely that the board will approve the merger.'",
                        "choices": ["utterly", "highly", "bitterly", "deeply"],
                        "correct_index": 1,
                        "explanation": "'Highly unlikely' é a colocação para probabilidade. 'Utterly' prefere ridiculous/absurd; 'deeply', concerned/touched. Cada adjetivo tem seu advérbio de confiança — sem lógica, só uso.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Verbo + substantivo: 'The new regulation will ___ a challenge for small exporters.'",
                        "choices": ["make", "do", "pose", "give"],
                        "correct_index": 2,
                        "explanation": "'Pose a challenge' é a colocação padrão; 'make a challenge' é tradução literal que nenhum nativo produziria. Guarde como bloco: pose a challenge / a threat / a question.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "We must meet the deadline at all costs.",
                        "explanation": "'Meet a deadline', nunca 'reach' ou 'hit'. E 'at all costs' fecha a frase com determinação. Colocações verbo-substantivo são as mais cobradas em ambientes corporativos.",
                    },
                ],
            },
            {
                "slug": "c1-presentations",
                "title": "Owning the Stage: Presentations & Signposting",
                "skill": "Conversation",
                "summary": "Apresente com signposting profissional: to begin with, moving on, to put it simply, to sum up.",
                "theory": (
                    "Uma apresentação é um mapa: o público precisa saber onde está a todo momento. "
                    "Signposting faz isso: 'To begin with', 'Moving on to', 'Let's turn to', 'To put it "
                    "another way', 'To sum up'. Sinalizar transições dá ritmo e autoridade — em vez de virar "
                    "slides em silêncio, você guia a audiência pela mão. Abra com um mapa ('I'll cover three "
                    "points'), sinalize cada curva e feche recapitulando. Brasileiros costumam apenas ler "
                    "slides; o apresentador de C1 conduz: 'That brings us to...', 'If there's time, I'll touch "
                    "on...'. Na dúvida, sinalize mais do que menos — ninguém nunca se perdeu por excesso de "
                    "clareza."
                ),
                "example": "To begin with, I'll outline the problem. Moving on, I'll share our data. To sum up, we need a decision today.",
                "key_points": [
                    "To begin with... abre o mapa",
                    "Moving on to... sinaliza transição",
                    "To put it simply... reformula",
                    "To sum up... fecha com síntese",
                ],
                "dialogue": [
                    {"speaker": "Dana", "line": "Good morning, everyone. To begin with, I'd like to thank you all for joining at such short notice."},
                    {"speaker": "Carlos", "line": "Happy to be here, Dana. How long will this take?"},
                    {"speaker": "Dana", "line": "About twenty minutes. I'll cover three things: last quarter's results, the new pipeline, and one risk we can't ignore."},
                    {"speaker": "Carlos", "line": "Perfect. Fire away."},
                    {"speaker": "Dana", "line": "So, moving on to the numbers — revenue grew twelve percent, driven mostly by renewals."},
                    {"speaker": "Carlos", "line": "Sorry to interrupt — does that include the Asia contracts?"},
                    {"speaker": "Dana", "line": "Good question. It doesn't, and I'll touch on Asia in a moment. Now let's turn to the pipeline, which is where things get interesting."},
                    {"speaker": "Carlos", "line": "Before you do, could you put that growth figure another way for the board?"},
                    {"speaker": "Dana", "line": "Of course. To put it simply: for every dollar we made last year, we made a dollar twelve this year."},
                    {"speaker": "Dana", "line": "To sum up, we're healthy, we're growing, but we must fix the retention gap before June."},
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Você terminou o primeiro tópico e quer anunciar o próximo. Qual signpost você usa?",
                        "choices": ["To sum up, ...", "Moving on to ...", "To begin with, ...", "As I was saying, ..."],
                        "correct_index": 1,
                        "explanation": "'Moving on to' sinaliza transição para o próximo tópico. 'To sum up' encerra tudo; 'to begin with' abre; 'as I was saying' retoma algo que foi interrompido — cada um tem seu momento exato.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Sinalize a mudança de slide: Let's ___ on to the numbers for last quarter.",
                        "correct": "move",
                        "explanation": "'Let's move on to...' é o signpost de transição mais versátil: anuncia a próxima estação e dá ao público o tempo de trocar de contexto mental junto com você.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual frase você usa para reformular uma ideia complicada em termos mais simples?",
                        "choices": ["To put it simply, ...", "To be fair, ...", "Moving on, ...", "First of all, ..."],
                        "correct_index": 0,
                        "explanation": "'To put it simply/another way' reformula: a mesma ideia em palavras mais acessíveis. É o signpost favorito de quem apresenta números para não especialistas — e salva apresentações.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: sum / to / up / results / the / solid / were",
                        "correct": "To sum up, the results were solid.",
                        "explanation": "'To sum up' abre o fechamento: anuncia que nada novo virá, só síntese. O público relaxa e absorve o recado final — exatamente o que você quer nas últimas frases.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase de abertura que você ouviu.",
                        "correct": "To begin with, let's look at the numbers.",
                        "explanation": "'To begin with' marca o ponto de partida do mapa da apresentação. Ouça a entonação descendente no fim — é frase completa, não pergunta; a vírgula dá a pausa natural após o signpost.",
                    },
                ],
            },
            {
                "slug": "c1-final-challenge",
                "title": "The C1 Gauntlet: Final Challenge",
                "skill": "Review",
                "summary": "O desafio final do C1: inversão, cleft, modais, colocação e particípios em um teste misto exigente.",
                "theory": (
                    "O C1 se prova no conjunto: dedução modal precisa ('can't have known'), unreal past ('I'd "
                    "rather you didn't'), inversão dramática ('Not only did she...'), cleft para ênfase ('It "
                    "was the manager who...'), colocações exatas ('bitterly cold') e particípios bem presos ao "
                    "seu sujeito ('Having spent years in diplomacy...'). Revise os padrões sem traduzir: quanto "
                    "menos você passar pelo português, mais fluente soa — e mais rápido reage na conversa. Este "
                    "desafio mistura tudo de propósito: cada erro aqui aponta exatamente qual lição revisar. "
                    "Respire, confie no que já absorveu e observe a nuance de cada frase antes de responder."
                ),
                "example": "Not only did she meet the deadline, but she also revised the whole appendix.",
                "key_points": [
                    "revisão: modal + particípio, cleft, inversão",
                    "colocações vêm em blocos prontos",
                    "particípio sempre preso ao sujeito certo",
                    "ênfase C1: estrutura a serviço do sentido",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Seu amigo ligou às 3h da manhã 'só para avisar que chegaria de madrugada'. Você reclama: 'You ___ called me at three!'",
                        "choices": ["needn't have", "didn't need to", "mustn't have", "couldn't have"],
                        "correct_index": 0,
                        "explanation": "Ele ligou (ação realizada) sem necessidade: 'needn't have + particípio'. 'Didn't need to' não afirmaria que a ligação ocorreu — e aqui ela aconteceu, dolorosamente.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Preferência sobre a ação de outro: I'd rather you ___ (negativo de leave) before we settle this.",
                        "correct": "didn't leave",
                        "explanation": "'I'd rather + sujeito diferente + passado simples': 'prefiro que você não saia'. Se o sujeito fosse o mesmo, seria 'I'd rather not leave' — a estrutura muda junto com o sujeito.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: also / not / she / did / early / she / but / only / helped / arrive",
                        "correct": "Not only did she arrive early, but she also helped.",
                        "explanation": "'Not only' abre com inversão ('did she arrive') e o par 'but... also' devolve a ordem normal na segunda parte. Duas regras de ênfase em uma única frase — puro C1.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase enfática que você ouviu.",
                        "correct": "It was the manager who approved the refund.",
                        "explanation": "It-cleft para corrigir atribuição: o destaque 'the manager' fica isolado entre 'was' e 'who' — ênfase cirúrgica que a ordem comum não conseguiria.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Colocação: a noite estava ___ cold.",
                        "choices": ["utterly", "highly", "bitterly", "painfully"],
                        "correct_index": 2,
                        "explanation": "'Bitterly cold' é o casamento clássico para frio intenso. 'Utterly' vai com ridiculous; 'highly', com unlikely; 'painfully', com shy. Bloco fechado — sem sinônimos improvisados.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Cláusula de particípio com anterioridade: ___ spent years in diplomacy, she negotiated with finesse.",
                        "correct": "Having",
                        "explanation": "'Having spent' marca ação concluída antes da principal. Sem o 'having', 'Spending years...' sugeriria simultaneidade impossível entre passar anos na diplomacia e negociar agora.",
                    },
                ],
            },
        ],
    },
]
