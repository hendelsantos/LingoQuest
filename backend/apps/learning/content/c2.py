"""Conteúdo do nível C2 — LingoQuest.

Nível de maestria: nuance de aspecto, futuros raros, gradação modal,
retórica, pontuação como significado, fronting, armadilhas PT-EN,
idioms de conversa educada e cirurgia de registro.
"""

COURSE = {
    "slug": "c2-mastery",
    "title": "C2 Mastery",
    "description": (
        "O estágio final da jornada: nuance de aspecto e modalidade, retórica, "
        "pontuação como significado, registro e armadilhas de tradução para "
        "operar o inglês com a precisão de um nativo educado."
    ),
    "level": "C2",
}

UNITS = [
    {
        "title": "The Architecture of English",
        "position": 1,
        "description": (
            "Os mecanismos profundos do inglês: nuance de aspecto, futuros raros "
            "e gradação modal em nível de precisão nativa."
        ),
        "lessons": [
            {
                "slug": "c2-aspect-nuance",
                "title": "Subtle Tense Distinctions",
                "skill": "Grammar",
                "summary": (
                    "Aspecto em lente de aumento: intenções adiadas, planos frustrados e as "
                    "camadas de tempo que separam 'I saw', 'I've seen' e 'I'd seen' na narrativa."
                ),
                "theory": (
                    "No topo da proficiência, o que separa o nativo não é o tempo verbal, mas o "
                    "aspecto — a lente através da qual o falante enquadra o evento. 'I've been "
                    "meaning to call you' comunica intenção continuada e adiada, com um quê de "
                    "culpa; 'I saw it' ancora o evento num passado concluído, enquanto 'I've seen "
                    "it' o apresenta como experiência vital relevante agora. O pluperfect ('I'd "
                    "seen') recua ainda mais: sinaliza evento anterior a outro marco passado — "
                    "essencial em narrativa para dar camadas de tempo. E 'was to have finished' é "
                    "a joia rara: um arranjo planejado que não se concretizou, algo que o "
                    "português precisa de uma frase inteira para expressar ('era para ter "
                    "terminado'). Confundir 'I'd seen' com 'I've seen' desmonta a cronologia da "
                    "história — o leitor nativo sente, mesmo sem saber nomear a regra."
                ),
                "example": (
                    "I've been meaning to call you for weeks. She was to have signed off by "
                    "Friday, yet the audit dragged on. When the sequel finally opened, I "
                    "realised I'd seen the original years before — I had simply forgotten."
                ),
                "key_points": [
                    "I've been meaning to... = intenção adiada e continuada",
                    "was to have + particípio = plano frustrado",
                    "I saw / I've seen / I'd seen: ponto, experiência, anterioridade",
                    "Pluperfect cria camadas de tempo em narrativa",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Um amigo abre a conversa: 'I've been meaning to tell you...' O que essa construção sinaliza?",
                        "choices": [
                            "Uma decisão tomada há poucos minutos",
                            "Uma promessa solene sobre o futuro",
                            "Uma intenção continuada que ficou adiada — havia vontade há tempos",
                            "Uma informação que ele acabou de esquecer",
                        ],
                        "correct_index": 2,
                        "explanation": "'I've been meaning to' é present perfect continuous de intenção: a vontade existe desde há e continua não executada, quase com pedido de desculpas. É uma das construções mais 'nativas' que existem — 'I want to tell you' soa abrupto em comparação.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "'She was to have finished the report by Friday, but the data arrived late.' O que 'was to have finished' comunica?",
                        "choices": [
                            "Uma ação concluída pontualmente na sexta",
                            "Um arranjo passado que não se concretizou",
                            "Uma obrigação que ainda vale para o futuro",
                            "Uma hipótese remota, sem data definida",
                        ],
                        "correct_index": 1,
                        "explanation": "'Was to have + particípio' é o passado de um 'be to' frustrado: o plano existia, o desfecho não. O português precisa de 'era para ter terminado' — em inglês, uma única forma condensa arranjo, expectativa e fracasso.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Complete a narrativa: 'When the curtain fell, the critic realised he ___ the play years before.'",
                        "correct": "had seen",
                        "accepted": ["had seen"],
                        "explanation": "O pluperfect recua atrás do marco passado ('the curtain fell'): a percepção acontece no passado, mas o ver a peça é anterior. 'Saw' colapsaria a linha do tempo; 'had seen' cria as camadas de flash-back que a narrativa pede.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: I've / been / meaning / to / ask / you / something",
                        "correct": "I've been meaning to ask you something.",
                        "explanation": "A construção 'I've been meaning to' pede infinitivo depois: intenção continuada adiada. O erro típico é 'I am meaning to ask', que soa como 'estou querendo dizer agora' — tempo errado, nuance perdida.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "The guests were to have arrived by dusk.",
                        "explanation": "'Were to have arrived' repete o arranjo frustrado, agora no plural. Se ouvir 'were to arrive', sem 'have', trata-se de arranjo neutro relatado — o 'have' é a sílaba que carrega a frustração.",
                    },
                ],
            },
            {
                "slug": "c2-futurity-nuance",
                "title": "Be About To, Be Due To",
                "skill": "Grammar",
                "summary": (
                    "Quatro futuros, quatro câmeras: 'be to' oficial, 'about to' iminente, 'due to' "
                    "programado e 'bound to' inevitável — precisão que o 'going to' não entrega."
                ),
                "theory": (
                    "O português resolve quase todo futuro com 'ir + infinitivo' e deixa o contexto "
                    "carregar a nuance; o inglês de nível C2 exige que você escolha a estrutura que "
                    "já embute o significado. 'Be to' marca arranjo oficial, determinação ou "
                    "instrução — é o futuro dos anúncios institucionais: 'The President is to visit "
                    "Havana.' 'Be about to' comprime a iminência: o evento está na soleira da "
                    "porta, não 'em breve'. 'Be due to' aponta um horário previsto, consultável "
                    "num quadro de chegadas ou numa agenda. E 'be bound to' declara "
                    "inevitabilidade, quase sempre com resignação ou ironia. São quatro câmeras "
                    "distintas sobre o mesmo evento futuro; escolher errado não quebra a gramática, "
                    "mas entrega imediatamente que o falante não pensa como nativo."
                ),
                "example": (
                    "The minister is to announce the reforms on Monday. Hurry — the last tram is "
                    "about to leave! The flight is due to land at 6:40. Talk to her now; she's "
                    "bound to say yes in the end."
                ),
                "key_points": [
                    "be to = arranjo oficial, tom de manchete",
                    "be about to = iminência imediata",
                    "be due to = horário previsto, timetable",
                    "be bound to = inevitabilidade sem relógio",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Manchete: 'The Chancellor is to raise tariffs next quarter.' Qual é o efeito de 'is to'?",
                        "choices": [
                            "Iminência de segundos: o fato já está acontecendo",
                            "Horário previsto em tabela oficial",
                            "Inevitabilidade resignada do fato",
                            "Anúncio oficial de arranjo ou decisão já tomada",
                        ],
                        "correct_index": 3,
                        "explanation": "'Be to' é o futuro dos comunicados formais: arranjo, determinação ou instrução institucional. É por isso que manchetes o adoram — transmite autoridade oficial, não simples marcação de tempo.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Segundo o painel de chegadas: 'The flight from Oslo is ___ to land at 22:15.'",
                        "correct": "due",
                        "accepted": ["due"],
                        "explanation": "'Due to' aponta horário previsto, verificável em timetable. 'About to' seria iminência absurda horas antes; 'bound to' é inevitabilidade sem relógio. O painel de aeroporto pede 'due' — previsão programada.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "'She's bound to complain about the seating.' Qual é o grau transmitido?",
                        "choices": [
                            "Compromisso oficial dela de reclamar depois",
                            "Quase inevitável — pode apostar que ela reclamará",
                            "Reclamação agendada para hora marcada",
                            "Possibilidade remota, dita com esperança",
                        ],
                        "correct_index": 1,
                        "explanation": "'Bound to' declara inevitabilidade, frequentemente com resignação ou ironia. É mais forte que 'likely' e não envolve horário ('due to') nem arranjo institucional ('be to') — é uma aposta quase certa.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: The / show / is / about / to / begin",
                        "correct": "The show is about to begin.",
                        "explanation": "'Be about to' é iminência pura: o evento está na soleira. Não combine com marcadores de tempo longo — 'about to begin tomorrow' é a assinatura clássica do não-nativo.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "The committee is to meet behind closed doors.",
                        "explanation": "'Is to meet' = reunião oficialmente determinada; 'behind closed doors' reforça o tom institucional e sigiloso. Repare: nem 'will' nem 'going to' apareceriam num comunicado assim.",
                    },
                ],
            },
            {
                "slug": "c2-modality-shades",
                "title": "The Finest Modal Degrees",
                "skill": "Grammar",
                "summary": (
                    "O dial modal em casas decimais: 'may well', 'might just', 'could conceivably', "
                    "o 'shall' dos contratos e o 'will' do hábito exasperante."
                ),
                "theory": (
                    "A modalidade em inglês é um dial de precisão milimétrica, e no C2 você opera "
                    "as casas decimais. 'May well' expressa probabilidade robusta — mais que 'may', "
                    "menos que 'will'. 'Might just' sugere possibilidade mínima, dita com "
                    "relutância ou para acalmar alguém. 'Could conceivably' abre espaço apenas no "
                    "plano hipotético: 'não é impossível conceber'. Em contratos, 'shall' não é um "
                    "futuro elegante, é obrigação vinculante — trocar por 'will' enfraquece "
                    "juridicamente o documento. E o 'will/won't' característico ('He will insist on "
                    "arriving late') descreve hábitos marcantes, muitas vezes irritantes, quase "
                    "sempre com tom de lamento. Onde o português usa 'pode' para tudo, o inglês "
                    "força você a declarar, na forma verbal, o grau exato da sua aposta."
                ),
                "example": (
                    "The supplier shall notify the buyer within fourteen days. She may well be the "
                    "strongest candidate we've interviewed. He might just agree to a compromise, "
                    "though I wouldn't bank on it. My brother will leave his keys in the door; he "
                    "simply won't learn."
                ),
                "key_points": [
                    "may well = probabilidade robusta",
                    "might just = possibilidade mínima, com relutância",
                    "shall = obrigação vinculante em contrato",
                    "will/won't = hábito característico, quase sempre exasperante",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Você redige uma cláusula com obrigação vinculante. Qual é a forma canônica?",
                        "choices": [
                            "The supplier might not amend the schedule unilaterally.",
                            "The supplier may well not amend the schedule unilaterally.",
                            "The supplier shall not amend the schedule unilaterally.",
                            "The supplier could conceivably not amend the schedule unilaterally.",
                        ],
                        "correct_index": 2,
                        "explanation": "Em linguagem contratual, 'shall' cria obrigação vinculante da parte mencionada. 'Might not', 'may well not' e 'could conceivably not' especulam sobre probabilidade — juridicamente vazias onde se precisa de dever.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual frase expressa o MAIOR grau de confiança no resultado?",
                        "choices": [
                            "She might just win the case.",
                            "She may well win the case.",
                            "She could conceivably win the case.",
                            "She might not win the case.",
                        ],
                        "correct_index": 1,
                        "explanation": "'May well' = probabilidade robusta, quase certeza sem chegar a 'will'. 'Might just' é a possibilidade mínima, dita a contragosto; 'could conceivably' vive só no hipotético; 'might not' nem é aposta a favor.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Hábito característico no presente: 'Even now, in his eighties, my grandfather ___ insist on correcting everyone's grammar.'",
                        "correct": "will",
                        "accepted": ["will"],
                        "explanation": "'Will' habitual característico descreve traço marcante (muitas vezes exasperante), ancorado no presente por 'even now'. 'Would' faria o hábito morar no passado — aqui, ele claramente persiste.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: The / board / may / well / refuse / the / offer",
                        "correct": "The board may well refuse the offer.",
                        "explanation": "'May well' antepõe o reforço ao verbo: 'may well refuse', nunca 'well may refuse'. É probabilidade alta sem a certeza arrogante de 'will' — o tom exato de um conselho de administração.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "He might just forgive you this once.",
                        "explanation": "'Might just' = possibilidade mínima com relutância; 'this once' limita o perdão a uma exceção. Juntos, transmitem: 'não conte com isso, mas há uma fresta' — nuance que 'may forgive' não captura.",
                    },
                ],
            },
        ],
    },
    {
        "title": "Style & Rhetoric",
        "position": 2,
        "description": (
            "Estilo como significado: retórica dos grandes discursos, pontuação que decide "
            "identidade e ordem de palavras que cria foco."
        ),
        "lessons": [
            {
                "slug": "c2-rhetoric",
                "title": "The Rhetorical Toolbox",
                "skill": "Vocabulary",
                "summary": (
                    "Os dispositivos dos grandes discursos: anáfora, quiasmo, trícolono, antítese "
                    "e pergunta retórica — ritmo como argumento."
                ),
                "theory": (
                    "Retórica é arquitetura sonora: os grandes discursos não usam palavras "
                    "difíceis, usam estruturas que o cérebro grava. A anáfora repete a abertura "
                    "de cláusulas sucessivas para criar urgência incantatória ('I have a "
                    "dream...'). O chiasmus espelha as ideias em A-B/B-A ('ask not what your "
                    "country can do for you — ask what you can do for your country'), forçando o "
                    "ouvinte a inverter a própria perspectiva. O tricolon arma a frase em três "
                    "tempos — o ritmo mais memorável do inglês. A antítese encosta opostos ('the "
                    "best of times, the worst of times') para condensar tensão em simetria. E a "
                    "pergunta retórica invade o palco do ouvinte sem esperar resposta. "
                    "Reconhecer o dispositivo é compreender o argumento por baixo das palavras — "
                    "é onde o C2 deixa de ser vocabulário e vira leitura crítica."
                ),
                "example": (
                    "'We came, we saw, we conquered' builds a tricolon. 'That's one small step "
                    "for man, one giant leap for mankind' balances antithesis. 'Do we really have "
                    "a choice?' poses a rhetorical question that answers itself."
                ),
                "key_points": [
                    "Anaphora: repetir a abertura, virar martelo",
                    "Chiasmus: A-B / B-A, inverter a perspectiva",
                    "Tricolon: três tempos, ritmo memorável",
                    "Antithesis: opostos gêmeos condensam tensão",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "'Ask not what your country can do for you; ask what you can do for your country.' Qual é o dispositivo dominante?",
                        "choices": [
                            "Chiasmus — as ideias se espelham em ordem invertida",
                            "Anaphora — repetição na abertura de cada cláusula",
                            "Tricolon — três elementos em ritmo crescente",
                            "Euphemism — suavização de um pedido incômodo",
                        ],
                        "correct_index": 0,
                        "explanation": "O chiasmus cruza a estrutura A-B/B-A: país→você, depois você→país. O espelhamento força o ouvinte a inverter sua perspectiva — exatamente o objetivo retórico da posse de JFK.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "'We shall fight on the beaches, we shall fight on the landing grounds, we shall fight in the fields...' O dispositivo é:",
                        "choices": [
                            "Chiasmus, com espelhamento ABBA das ideias",
                            "Antítese entre praia e campo",
                            "Anaphora, com efeito de martelo incantatório",
                            "Hipérbole acumulada em paradoxo",
                        ],
                        "correct_index": 2,
                        "explanation": "Cada cláusula abre com 'we shall fight': a anáfora transforma argumento em pulso. O efeito não é informar, é hipnotizar — Churchill sabia que ritmo convence mais que lógica.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "O lema francês 'liberty, equality, fraternity' é o exemplo escolar de um ___. (termo técnico)",
                        "correct": "tricolon",
                        "accepted": ["tricolon"],
                        "explanation": "Tricolon é a estrutura de três tempos — o ritmo mais memorável do inglês ('of the people, by the people, for the people'). Três itens soam completos; quatro, já parecem lista de compras.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: It / was / the / worst / of / times",
                        "correct": "It was the worst of times.",
                        "explanation": "É a antítese de Dickens em miniatura: 'best of times' contra 'worst of times'. Encostar opostos em frases gêmeas condensa a tensão de toda uma era em duas cláusulas.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "Government of the people, by the people, for the people.",
                        "explanation": "O tricolon de Gettysburg triplica 'the people' em três preposições: origem, meio e destino. A forma carrega a tese — democracia como pertencimento, dita em dez palavras.",
                    },
                ],
            },
            {
                "slug": "c2-punctuation-meaning",
                "title": "Punctuation Is Meaning",
                "skill": "Writing",
                "summary": (
                    "Vírgula que muda a identidade, travessão que rouba a cena e ponto e vírgula "
                    "que equilibra: pontuação como significado."
                ),
                "theory": (
                    "Em inglês, pontuação é gramática de significado, não enfeite. A vírgula "
                    "decide identidade: 'My sister, who lives in Lisbon, is a chef' (vírgulas = "
                    "informação acessória: tenho uma irmã só) contra 'My sister who lives in "
                    "Lisbon is a chef' (sem vírgulas = oração restritiva: tenho várias, e "
                    "especifico qual). O travessão interrompe dramaticamente e promove o "
                    "intercalado a foco — é o gesto da mão que sobe; em registro marcado, quase "
                    "teatral. O ponto e vírgula equilibra duas orações independentes de igual "
                    "peso — o conectivo elegante do escrito, sinalizando ligação sem "
                    "subordinação. E atenção à armadilha brasileira: o português tolera comma "
                    "splice ('eu fui, ele ficou'); em inglês formal, juntar duas orações "
                    "independentes só com vírgula é erro grave que envergonha até o nativo "
                    "apressado."
                ),
                "example": (
                    "My sister, who lives in Lisbon, is a chef. (única irmã) My sister who lives "
                    "in Lisbon is a chef. (irmãs várias) His excuse — flimsy as it was — was "
                    "accepted. Two options remained; neither appealed."
                ),
                "key_points": [
                    "Vírgula = acessório; sem vírgula = restritivo",
                    "Travessão interrompe e promove o intercalado a foco",
                    "Ponto e vírgula equilibra orações irmãs",
                    "Comma splice é erro grave em inglês formal",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "'My brother who lives in Leeds hates football.' O que a ausência de vírgulas permite inferir?",
                        "choices": [
                            "Tenho um irmão só, e o dado é acessório",
                            "Meu irmão acabou de se mudar para Leeds",
                            "O falante odeia futebol tanto quanto o irmão",
                            "Tenho mais de um irmão — a oração identifica qual",
                        ],
                        "correct_index": 3,
                        "explanation": "Sem vírgulas, a oração é restritiva: restringe 'brother' entre vários. Com vírgulas ('My brother, who lives in Leeds,'), o dado seria acessório — e implicaria irmão único. A pontuação muda os fatos da família.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "'She rewrote the clause; the client signed without a word.' O que o ponto e vírgula transmite?",
                        "choices": [
                            "A segunda ação causou a primeira",
                            "As duas orações têm peso igual e ligação estreita",
                            "O autor hesita entre as duas ideias",
                            "Uma lista de três itens está por vir",
                        ],
                        "correct_index": 1,
                        "explanation": "O ponto e vírgula equilibra orações independentes irmãs: nem subordina (como a vírgula exigiria 'and'), nem separa por completo (como o ponto faria). É o equilíbrio discreto do escrito elegante.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Complete com UMA palavra: 'The verdict — ___ everyone had predicted — split the room.'",
                        "correct": "as",
                        "accepted": ["as"],
                        "explanation": "Os travessões isolam um comentário em tom de aparte; 'as' retoma 'the verdict' e introduz a previsão. O travessão promove o intercalado a foco dramático — a vírgula seria mais morna, os parênteses, mais frios.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras (com a pontuação): The / deadline / passed; / nobody / so / much / as / flinched.",
                        "correct": "The deadline passed; nobody so much as flinched.",
                        "explanation": "Ponto e vírgula + 'so much as' negativo enfático: o equilíbrio formal destaca que ninguém esboçou reação. 'So much as flinched' sem negação explícita ganha força do contexto severo.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "The winners, however, saw it differently.",
                        "explanation": "'However' intercalado exige vírgulas dos dois lados — mais rígido que o 'entretanto' português, que admite flexibilidade. No ditado, ouvir a entonação de aparte é metade da resposta.",
                    },
                ],
            },
            {
                "slug": "c2-word-order-emphasis",
                "title": "Fronting & Focus",
                "skill": "Grammar",
                "summary": (
                    "Quebre a ordem SVO de propósito: fronting, clivagem em wh- e inversão com "
                    "'so' e negativas — o foco mora na posição."
                ),
                "theory": (
                    "A ordem canônica sujeito-verbo-objeto é o neutro; o nativo a quebra de "
                    "propósito quando quer apontar o dedo. Frontar o objeto ('This I must see') "
                    "ergue o elemento ao palco — dramático, quase literário. A clivagem em wh- "
                    "('What surprised me was the silence') isola a informação-nova e a entrega "
                    "embrulhada no fim, posição de foco máximo. Com 'so/such' anteposto, a "
                    "inversão é obrigatória ('So absurd was it that...'), e o efeito é de ênfase "
                    "formal elevada, voz de editorial. Negativas curtas à frente ('Little did she "
                    "know', 'Not once did he apologise') fazem o mesmo pelo mistério e pela "
                    "indignação. O português até conhece inversões ('Isso eu quero ver'), mas em "
                    "inglês essas construções carregam registro e ironia — usá-las errado soa "
                    "arcaico; usá-las bem soa magistral."
                ),
                "example": (
                    "This I must see. What surprised me was the silence, not the noise. So absurd "
                    "was the claim that nobody even responded. Little did he realise the deal was "
                    "already dead."
                ),
                "key_points": [
                    "This I must see: frontar o objeto enfatiza",
                    "What... was...: clivagem entrega o foco no fim",
                    "So + adjetivo + inversão: ênfase editorial",
                    "Little did she know: suspense narrativo",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "'What impressed the jury most was her candour.' O que a clivagem realiza?",
                        "choices": [
                            "Põe 'the jury' em foco como surpresa",
                            "Transforma a frase em pergunta educada",
                            "Põe 'her candour' em foco como informação-nova",
                            "Sinaliza que a franqueza era esperada",
                        ],
                        "correct_index": 2,
                        "explanation": "A wh-cleft pré-anuncia a moldura ('what impressed...') e entrega o quadro no fim ('her candour'). O ouvinte recebe primeiro a pergunta implícita, depois a resposta — o foco fica garantido na posição final.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Complete a inversão: 'So fierce ___ the competition that three firms withdrew.'",
                        "correct": "was",
                        "accepted": ["was"],
                        "explanation": "Com 'so + adjetivo' anteposto, a inversão é obrigatória: 'So fierce was...'. A ordem neutra ('the competition was so fierce that') existe, mas a invertida carrega a ênfase de editorial — decisão de estilo, não só de gramática.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "'This I must see.' O que a anteposição do objeto comunica?",
                        "choices": [
                            "Cortesia interrogativa disfarçada de afirmação",
                            "Ênfase dramática: o objeto sobe ao palco da frase",
                            "Erro de ordem em inglês contemporâneo",
                            "Dúvida sobre já ter visto a coisa",
                        ],
                        "correct_index": 1,
                        "explanation": "Frontar o objeto é arrego retórico: 'This' recebe o holofote antes do verbo. O paralelo português 'Isso eu tenho que ver' existe, mas o inglês reserva a construção para momentos de ênfase literária ou ironia",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: Little / did / she / know / what / awaited / her",
                        "correct": "Little did she know what awaited her.",
                        "explanation": "Adverbial negativo à frente força inversão: 'did she know', nunca 'she knew'. É a fórmula clássica de suspense narrativo — abrir um capítulo com ela cria cheiro de história.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "Not once did he apologise for the delay.",
                        "explanation": "'Not once' à frente + inversão ('did he'): a negação enfática substitui 'He never apologised'. A entonação carrega indignação — 'never' simples seria neutro demais para o tom.",
                    },
                ],
            },
        ],
    },
    {
        "title": "Translation Traps & Final Mastery",
        "position": 3,
        "description": (
            "As armadilhas finais e a síntese: tradução PT-EN sem falsos amigos, idioms cultos, "
            "cirurgia de registro e o desafio supremo."
        ),
        "lessons": [
            {
                "slug": "c2-translation-traps",
                "title": "PT–EN: Mind the Gap",
                "skill": "Vocabulary",
                "summary": (
                    "As bifurcações que o dicionário não conta: faz 2 anos, pretender, mesmo, "
                    "eventualmente, ou...ou — escolher, nunca transferir."
                ),
                "theory": (
                    "Traduzir é escolher, nunca transferir. 'Faz dois anos' bifurca: ponto no "
                    "passado → 'two years ago'; duração até agora → 'for two years'. 'Informar' "
                    "se reparte em 'tell' (cotidiano, direto) e 'inform' (formal, oficial, com "
                    "'of'). 'Mesmo' é camaleão: 'even' (até mesmo), 'the same' (o mesmo), "
                    "'really' (mesmo!, enfático). 'Ou...ou' vira 'either...or' — e 'neither...nor' "
                    "no negativo. 'Pretender' jamais é 'pretend' (fingir): é 'intend'. E a mais "
                    "traiçoeira de todas: 'eventualmente' em português é 'occasionally' ou "
                    "'possibly', enquanto 'eventually' em inglês significa 'finalmente, depois de "
                    "muita espera'. A dupla ser/estar também espreita: 'He is being difficult' "
                    "(comportamento temporário) contra 'He is difficult' (caráter). Dominar essas "
                    "bifurcações é o que distingue o C2: o nativo percebe a escolha certa mesmo "
                    "sem saber nomear a regra."
                ),
                "example": (
                    "I moved to Canada two years ago and have lived there ever since. He intends "
                    "to hand in his notice before June. She told me the news herself; the agency "
                    "later informed us of the delay. Either you sign, or you walk away."
                ),
                "key_points": [
                    "faz 2 anos = ago (ponto) / for 2 years (duração)",
                    "pretender = intend; pretend = fingir",
                    "eventualmente = occasionally; eventually = finalmente",
                    "ou...ou = either...or; nem...nem = neither...nor",
                    "tell = cotidiano; inform = formal + of",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Traduza: 'Eventualmente, poderemos viajar no inverno.'",
                        "choices": [
                            "We will eventually travel in the winter.",
                            "We eventually travel in the winter.",
                            "We may occasionally travel in the winter.",
                            "We may travel in the winter eventually.",
                        ],
                        "correct_index": 2,
                        "explanation": "'Eventualmente' em português = de vez em quando / possivelmente → 'occasionally'. 'Eventually' inglês = finalmente, após longa espera — um dos falsos amigos mais caros para brasileiros em reuniões e e-mails.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Como se traduz o verbo em 'Ela pretende abrir uma cafeteria'?",
                        "choices": [
                            "She pretends to open a coffee shop.",
                            "She intends to open a coffee shop.",
                            "She claims to open a coffee shop.",
                            "She manages to open a coffee shop.",
                        ],
                        "correct_index": 1,
                        "explanation": "'Pretender' = 'intend' (ter a intenção). 'Pretend' é fingir; 'claim' é afirmar; 'manage' é conseguir com esforço. O erro clássico inverte completamente o sentido — ela passaria a estar fingindo.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "'Conheci essa cidade faz dois anos.' Qual tradução é precisa?",
                        "choices": [
                            "I have visited this city for two years.",
                            "I know this city since two years.",
                            "I visited this city two years before.",
                            "I visited this city two years ago.",
                        ],
                        "correct_index": 3,
                        "explanation": "'Faz dois anos' como ponto no passado → 'two years ago'. 'For two years' seria duração ('conheço há dois anos' = present perfect + for); 'since' exige ponto de partida com present perfect, não com past simple.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Complete: '___ you apologise or you leave this room.'",
                        "correct": "Either",
                        "accepted": ["Either", "either"],
                        "explanation": "'Ou...ou' correlativo é 'either...or' — o 'either' anteposto é obrigatório em inglês padrão. O português dispensa o primeiro 'ou'; o inglês, não. No negativo, a dupla vira 'neither...nor'.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: I / shall / inform / you / of / any / changes",
                        "correct": "I shall inform you of any changes.",
                        "explanation": "'Informar' formal/escrito é 'inform' + objeto + 'of'. No dia a dia, 'tell': 'I'll tell you about any changes'. A escolha do verbo já define o registro da frase inteira — shall formaliza, inform sela.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "He is being incredibly difficult today.",
                        "explanation": "'Is being difficult' = comportamento temporário (o 'estar sendo' do português). 'He is difficult' descreveria caráter permanente. O progressive com 'be + adjetivo' captura o traço do momento — nuance de ser/estar.",
                    },
                ],
            },
            {
                "slug": "c2-idiom-mastery",
                "title": "Cultural Literacy",
                "skill": "Vocabulary",
                "summary": (
                    "Idioms da conversa educada e a noção de registro: quando usá-los e quando o "
                    "formal pede 'at the latest possible moment'."
                ),
                "theory": (
                    "Idioms são a moeda cultural corrente: quem não os gasta com fluidez fica de "
                    "fora da conversa educada. 'At the eleventh hour' é a última hora possível, "
                    "com o suspense do prazo esgotando. 'A blessing in disguise' nomeia o mal que "
                    "vira bem — o famoso 'tudo aconteceu por um motivo'. 'Cut corners' acusa a "
                    "economia que sacrifica qualidade ou etapas. 'Throw in the towel' é desistir "
                    "com a dignidade do boxeador que joga a toalha. 'Read between the lines' é o "
                    "ato fino de captar o subtexto não escrito. Atenção ao registro: todos são "
                    "informais-educados; num white paper, o nativo trocaria por 'at the latest "
                    "possible moment' ou 'ultimately beneficial'. E nunca traduzam literalmente: "
                    "as imagens raramente coincidem com as do português — cada língua pinta o "
                    "mesma ideia com metáfora própria."
                ),
                "example": (
                    "The audit found they had cut corners on the wiring. The deal was rescued at "
                    "the eleventh hour. Her rejection turned out to be a blessing in disguise: it "
                    "pushed her into the startup. Read between the lines of that memo — "
                    "redundancies are coming."
                ),
                "key_points": [
                    "at the eleventh hour = última hora possível",
                    "a blessing in disguise = mal que vira bem",
                    "cut corners = sacrificar qualidade por economia",
                    "read between the lines = captar o subtexto",
                    "throw in the towel = desistir (a toalha do boxe)",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "'The contract was signed at the eleventh hour.' Quando assinaram?",
                        "choices": [
                            "Onze horas depois do prazo encerrado",
                            "De manhã cedo, antes de todos",
                            "No último momento possível, esgotando o prazo",
                            "Após negociação longa e exaustiva",
                        ],
                        "correct_index": 2,
                        "explanation": "'At the eleventh hour' = na última hora viável, quando já parecia perdido. Vem da parábola dos trabalhadores da vinha (Mateus 20): os últimos contratados chegam às onze horas — e recebem igual.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "'Losing that client was a blessing in disguise.' O que o falante quer dizer?",
                        "choices": [
                            "Foi pura sorte desde o início",
                            "O mal virou bem: a perda trouxe benefício inesperado",
                            "A perda foi um sacrifício planejado",
                            "O cliente era um problema financeiro",
                        ],
                        "correct_index": 1,
                        "explanation": "'Blessing in disguise' = bênção disfarçada de desgraça. É o 'tudo aconteceu por um motivo' do português — e 'in disguise' é a imagem que memoriza: o bem vestido de mal.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Complete a collocation: 'His letter says more than it seems — you have to read between the ___.'",
                        "correct": "lines",
                        "accepted": ["lines"],
                        "explanation": "'Read between the lines' = captar o subtexto não escrito. A imagem é literal: o sentido mora no espaço em branco entre uma linha e outra — o que o autor não disse, mas insinuou.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: They / had / to / cut / corners / on / quality",
                        "correct": "They had to cut corners on quality.",
                        "explanation": "'Cut corners' = economizar sacrificando qualidade ou etapas. Sempre plural: 'corners'. É acusação — ninguém 'cuts corners' como elogio; o audit report é o habitat natural da expressão.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "After three failed rounds, we threw in the towel.",
                        "explanation": "'Throw in the towel' = desistir, com a imagem do boxeador que arremessa a toalha ao ringue. Equivalente funcional ao português 'bater a bandeira branca' — jamais 'jogar a toalha' literalmente.",
                    },
                ],
            },
            {
                "slug": "c2-register-surgery",
                "title": "Rewriting for Any Audience",
                "skill": "Writing",
                "summary": (
                    "O mesmo conteúdo em três bisturis: jurídico, corporativo e casual — "
                    "transitar entre registros sem costura visível."
                ),
                "theory": (
                    "Cirurgia de registro: o mesmo conteúdo sob três bisturis. O jurídico "
                    "nominaliza, apaga pessoas e usa 'shall', 'hereunder', 'aforementioned' — a "
                    "autoridade vem da impessoalidade. O corporativo mistura formalidade com "
                    "calor: 'we are committed to', 'we kindly request', voz ativa com polimento. "
                    "O casual contrai, usa phrasal verbs e discourse markers ('look', 'hang on') "
                    "— a confiança substitui a cerimônia. O C2 não é saber os três; é transitar "
                    "entre eles sem costura visível, reescrevendo em segundos conforme o leitor "
                    "muda. O brasileiro costuma traduzir o registro formal do português ('aos "
                    "cuidados de', 'no que tange') literalmente, produzindo um inglês burocrático "
                    "que não existe — o erro clássico do contrato traduzido que nenhum nativo "
                    "assina sem sorrir."
                ),
                "example": (
                    "Legal: The tenant shall not sublet the premises without prior written "
                    "consent. / Corporate: We would ask that you refrain from subletting at this "
                    "stage. / Casual: Look, don't go subletting the place without running it by "
                    "us first, okay?"
                ),
                "key_points": [
                    "Jurídico: shall, hereunder, nominalização",
                    "Corporativo: we are committed to, kindly request",
                    "Casual: contrações, phrasal verbs, 'look'",
                    "O verbo escolhido já define o registro",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "'Please be advised that the aforementioned clause has been rescinded.' Qual é o registro?",
                        "choices": [
                            "Corporativo cordial de e-mail interno",
                            "Casual entre colegas de equipe",
                            "Jurídico-burocrático, típico de documentos formais",
                            "Jornalístico de tabloide popular",
                        ],
                        "correct_index": 2,
                        "explanation": "'Please be advised', 'aforementioned' e 'rescinded' são assinaturas do jurídico-burocrático. Um e-mail corporativo diria 'we're writing to let you know'; um casual, 'heads-up: that clause is gone'.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Reescreva 'Sorry, we messed up' em registro corporativo:",
                        "choices": [
                            "Our bad — the service fell over on us.",
                            "We apologise for the shortfall in service delivery.",
                            "We messed up the service, regrettably so.",
                            "Mistakes were made by the service team, oops.",
                        ],
                        "correct_index": 1,
                        "explanation": "O corporativo troca o phrasal verb 'messed up' por nominalização ('shortfall'), usa 'apologise' e impessoaliza. Mantém a culpa admitida, mas embalada — é isso que 'corporate polish' significa.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Registro jurídico: 'The hirer shall ___ the owner against any claims arising hereunder.'",
                        "correct": "indemnify",
                        "accepted": ["indemnify"],
                        "explanation": "'Indemnify' = indenizar/compensar, verbo-totem do contrato em inglês. 'Hereunder' = 'sob este contrato' (o 'na cláusula presente' do juridiquês). Juntos, marcam registro legal inequívoco.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: We've / got / your / back / the / whole / way",
                        "correct": "We've got your back the whole way.",
                        "explanation": "O casual usa contração ('we've'), possessivo idiomático ('got your back' = te apoiamos) e ritmo de fala. Nenhum advogado escreveria assim — e é exatamente esse o ponto do registro.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "We are committed to supporting our clients throughout the transition.",
                        "explanation": "Sem contrações, 'committed to + gerúndio', 'throughout': o vocabulário do corporativo médio. 'Committed to support' (infinitivo) também existe, mas o gerúndio é o padrão das cartas de missão e valores.",
                    },
                ],
            },
            {
                "slug": "c2-final-challenge",
                "title": "The Final Boss",
                "skill": "Review",
                "summary": (
                    "O desafio final: aspecto, futuros, modalidade, inversão, pontuação, falsos "
                    "amigos e registro numa única prova exigente."
                ),
                "theory": (
                    "O desafio final junta todas as ferramentas do nível: aspecto fino, futuros "
                    "precisos, modalidade em casas decimais, inversões retóricas, "
                    "pontuação-significado, armadilhas PT–EN, idioms e cirurgia de registro. Nada "
                    "aqui é isolado — uma única frase pode exigir três decisões simultâneas de "
                    "registro, tempo e ênfase. Erros comuns no topo da curva: usar 'due to' onde "
                    "o sentido pede 'bound to'; esquecer a inversão depois de 'Not until'; cair "
                    "no falso amigo 'eventually'; pôr vírgula numa oração restritiva. Trate cada "
                    "questão como um mini-exame C2 real: leia a frase inteira, identifique o "
                    "registro, antecipe a armadilha e só então escolha. Se errar, volte à lição "
                    "de origem — o mapa do nível inteiro já está na sua cabeça agora."
                ),
                "example": (
                    "So persuasive was her closing argument that even the sceptics read between "
                    "the lines and caved. We were to have signed at noon; the wire transfer, "
                    "however, landed at the eleventh hour."
                ),
                "key_points": [
                    "Inversão após negativa anteposta é obrigatória",
                    "shall vs may well: obrigação vs probabilidade",
                    "due to obedece ao timetable; bound to, não",
                    "Revisão: escolha pelo registro, não pela regra",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Qual frase usa a inversão correta e natural?",
                        "choices": [
                            "Not until the audit the board acted.",
                            "Not until the audit acted the board.",
                            "Not until the audit did the board act.",
                            "Not until did the audit the board act.",
                        ],
                        "correct_index": 2,
                        "explanation": "Advérbio negativo à frente ('Not until...') exige inversão do sujeito: 'did the board act'. A ordem neutra seria 'The board did not act until the audit' — correta, mas sem a ênfase da frente.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual redação cria obrigação vinculante num contrato?",
                        "choices": [
                            "The vendor may well deliver the full dataset by the third quarter.",
                            "The vendor might just deliver the full dataset by the third quarter.",
                            "The vendor is about to deliver the full dataset by the third quarter.",
                            "The vendor shall deliver the full dataset by the third quarter.",
                        ],
                        "correct_index": 3,
                        "explanation": "'Shall' contratual = obrigação vinculante da parte. 'May well' é probabilidade, 'might just' é possibilidade mínima, 'about to' é iminência — nenhuma obriga juridicamente quem assina.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Falso amigo à espreita: 'She ___ to retire next year.' (pretender)",
                        "correct": "intends",
                        "accepted": ["intends"],
                        "explanation": "'Pretender' = 'intend'. 'She pretends to retire' significaria que ela finge que vai se aposentar — sentido completamente outro. Em revisão de documentos, esse erro é demitível.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Segundo o programa oficial: 'The keynote is ___ to start at nine sharp.'",
                        "correct": "due",
                        "accepted": ["due"],
                        "explanation": "'Due to' = horário previsto, consultável no programa. 'About to' às nove em ponto seria redundante; 'bound to' não tem relógio. O programa define, o 'due' obedece.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: I've / been / meaning / to / say / this",
                        "correct": "I've been meaning to say this.",
                        "explanation": "O fecho clássico do C2: intenção continuada adiada, finalmente executada. Se você montou a frase sem hesitar, o aspecto do inglês já é reflexo seu.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "What struck the committee was her sheer composure.",
                        "explanation": "Wh-cleft em ação: 'her sheer composure' chega como informação-nova no fim, a posição de foco. 'Sheer' intensifica substantivo com elegância que 'pure' não alcança.",
                    },
                ],
            },
        ],
    },
]


from .advanced_extension import add_c2_conversations  # noqa: E402

add_c2_conversations(UNITS)
