COURSE = {
    "slug": "b2-upper-intermediate",
    "title": "B2 Upper-Intermediate",
    "description": (
        "Consolide seu inglês de nível intermediário avançado: narre histórias com "
        "precisão temporal, domine condicionais e estruturas complexas e soe natural "
        "com colocações, phrasal verbs e idiomas do dia a dia."
    ),
    "level": "B2",
}

UNITS = [
    {
        "title": "Narrative Mastery",
        "position": 1,
        "description": "Aprenda a contar histórias no passado com precisão temporal, combinando os tempos narrativos como um falante nativo.",
        "lessons": [
            {
                "slug": "b2-past-perfect",
                "title": "Before & After",
                "skill": "Grammar",
                "summary": "Use o past perfect (had + particípio) para marcar a ação que aconteceu antes de outra no passado.",
                "theory": (
                    "O past perfect é o 'passado do passado': ele marca uma ação que terminou "
                    "ANTES de outra ação também no passado. Formamos com had + particípio para "
                    "todas as pessoas, então não há conjugação nova para decorar. Em português, "
                    "resolvemos isso com 'já' ou 'antes de' e usamos dois verbos no passado "
                    "('cheguei e o trem já tinha saído' ou simplesmente 'saiu'); em inglês, o "
                    "had deixa a ordem cronológica explícita: 'When I got to the station, the "
                    "train had left.' Advérbios como already, never e just ficam entre had e o "
                    "particípio: 'She had just left.' Erro típico do brasileiro: usar dois past "
                    "simples e deixar o ouvinte sem saber o que veio primeiro."
                ),
                "example": "When I got home, Ana had already cooked dinner and the kids had gone to bed.",
                "key_points": [
                    "had + particípio = ação anterior a outro passado",
                    "already / never / just entre 'had' e o particípio",
                    "It was the first time (that) I had... = sempre past perfect",
                    "By the time + passado, ... had + particípio",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "When I got to the station, the train ___.",
                        "choices": ["had already left", "has already left", "already left", "was already leaving"],
                        "correct_index": 0,
                        "explanation": "A chegada à estação está no passado ('when I got'), e o trem partiu antes dela: ação anterior a outro passado exige past perfect (had + already + particípio). 'Has already left' é presente e 'was leaving' indicaria partida em curso no momento da chegada.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "It was the first time I ___ snow in my life.",
                        "choices": ["had ever seen", "ever saw", "have ever seen", "was ever seeing"],
                        "correct_index": 0,
                        "explanation": "Depois de 'It was the first time...', o inglês pede past perfect: a experiência de ver neve aconteceu antes do momento passado em que você fez a observação. 'Have ever seen' (presente) é o erro clássico de quem traduz 'é a primeira vez que vejo' literalmente.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "By the time we arrived at the theater, the show ___ (to start).",
                        "correct": "had started",
                        "explanation": "'By the time' marca o evento de referência no passado (nossa chegada); o espetáculo começou antes dele, então usamos had + particípio, não o past simple.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: had / she / left / before / I / called",
                        "correct": "She had left before I called.",
                        "explanation": "Duas ações no passado: ela sair (antes) e eu ligar (depois). A ação mais antiga leva past perfect ('had left') e a mais recente, past simple ('called').",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "I had never seen snow before that trip.",
                        "explanation": "Repare no padrão: 'had never seen' (past perfect com never entre had e o particípio) + 'before that trip' como referência no passado.",
                    },
                ],
            },
            {
                "slug": "b2-past-perfect-continuous",
                "title": "What Had Been Happening",
                "skill": "Grammar",
                "summary": "Use had been + -ing para ações em progresso com duração antes de outro evento no passado.",
                "theory": (
                    "O past perfect continuous (had been + verbo com -ing) descreve uma ação que "
                    "estava em andamento durante um período antes de outro evento no passado, "
                    "dando ênfase à duração: 'She had been waiting for an hour when the bus "
                    "finally arrived.' A diferença para o past perfect simples é de foco: 'The "
                    "road was wet because it had rained' olha o resultado concluído, enquanto "
                    "'...because it had been raining all night' destaca a atividade e quanto "
                    "tempo ela durou. O erro típico do brasileiro é parar no past continuous "
                    "('was waiting'), traduzindo 'estava esperando'; mas quando existe um "
                    "segundo ponto no passado e a ideia é 'já fazia tempo que...', o correto é "
                    "had been + -ing, geralmente acompanhado de for ou since."
                ),
                "example": "Her eyes were red because she had been crying right before the interview.",
                "key_points": [
                    "had been + -ing = duração antes de um evento no passado",
                    "had done foca o resultado; had been doing foca a atividade",
                    "Costuma vir com for / since para medir a duração",
                    "Efeito visível no passado + had been -ing explica a causa",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Her eyes were red. She ___ before the interview.",
                        "choices": ["had been crying", "has been crying", "was crying", "cried"],
                        "correct_index": 0,
                        "explanation": "O choro aconteceu durante um período antes da entrevista (o evento passado de referência), e o resultado visível (olhos vermelhos) aparece no passado. Isso pede had been + -ing. 'Was crying' indicaria choro exatamente no momento, o que conflita com a sequência da história.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "When the concert was canceled, some fans ___ in line since dawn.",
                        "choices": ["had been waiting", "were waiting", "have been waiting", "waited"],
                        "correct_index": 0,
                        "explanation": "'Since dawn' mede a duração de uma espera que começou antes do cancelamento (também no passado). Duração anterior a um ponto passado = past perfect continuous. 'Have been waiting' é presente e não conversa com 'was canceled'.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "They ___ (to wait) for over an hour when the bus finally arrived.",
                        "correct": "had been waiting",
                        "explanation": "'For over an hour' mede a duração da espera, que começou antes e continuou até a chegada do ônibus (passado). Portanto: had been + waiting.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: been / working / she / had / all / day",
                        "correct": "She had been working all day.",
                        "explanation": "A estrutura é had + been + verbo com -ing: 'She had been working all day' — ela trabalhava há o dia inteiro antes do momento passado que você tem em mente.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "He had been living there for ten years.",
                        "explanation": "Padrão clássico: had been living + for ten years. A moradia durou dez anos antes de outro evento no passado, como uma mudança ou uma visita.",
                    },
                ],
            },
            {
                "slug": "b2-narrative-tenses",
                "title": "Telling the Full Story",
                "skill": "Grammar",
                "summary": "Combine past simple, continuous e perfect para construir narrativas claras e naturais.",
                "theory": (
                    "Uma boa história no passado usa três ferramentas, cada uma com seu papel. O "
                    "past simple empurra a trama para frente, evento por evento: 'We arrived, "
                    "ordered dinner and paid the bill.' O past continuous pinta o cenário e as "
                    "ações em curso que formam o pano de fundo: 'It was raining when we left.' E "
                    "o past perfect esclarece o que já tinha acontecido antes daquele ponto: "
                    "'The kitchen had closed ten minutes earlier.' Antes de escolher o tempo, "
                    "pergunte: isso é a linha principal, o cenário ou o passado anterior? O erro "
                    "comum do brasileiro é usar o past continuous para tudo porque 'a história "
                    "estava acontecendo', o que deixa a narração confusa. Guarde também a dupla "
                    "clássica: while + continuous para o fundo, when + simple para o evento que "
                    "interrompe."
                ),
                "example": "I was cooking dinner when the lights went out, and we realized we had forgotten to pay the bill.",
                "key_points": [
                    "Past simple = eventos principais, na ordem",
                    "Past continuous = cenário e ações interrompidas",
                    "Past perfect = o que veio antes daquele ponto da história",
                    "while + contínuo (fundo) / when + simple (interrupção)",
                    "Pergunte a si: trama, cenário ou passado anterior?",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "I ___ dinner when the phone rang.",
                        "choices": ["was cooking", "cooked", "had cooked", "had been cooking"],
                        "correct_index": 0,
                        "explanation": "A cozinha é a ação em curso (o cenário) e a campainha é o evento que interrompe: past continuous + when + past simple. 'Had cooked' diria que o jantar já estava pronto antes do telefonema, mudando a história.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "When I got home, I noticed that somebody ___ the window.",
                        "choices": ["had broken", "broke", "has broken", "was breaking"],
                        "correct_index": 0,
                        "explanation": "Duas ações no passado: eu notar (depois) e alguém quebrar o vidro (antes). A mais antiga leva past perfect — e é justamente ela que explica o estado que você notou ao chegar.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "When we finally found the restaurant, we ___ (to walk) around for twenty minutes.",
                        "correct": "had been walking",
                        "explanation": "A caminhada durou vinte minutos antes de encontrarmos o restaurante: duração anterior a um evento passado, com for medindo o tempo — past perfect continuous.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: the / sun / was / setting / as / we / drove / home",
                        "correct": "The sun was setting as we drove home.",
                        "explanation": "'Was setting' descreve o cenário em mudança, enquanto 'drove' é a ação principal da viagem. As marca as duas coisas acontecendo ao mesmo tempo.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "I was watching TV when the lights went out.",
                        "explanation": "Mais uma vez o padrão da interrupção: past continuous (ação em curso) + when + past simple (evento súbito). É a espinha dorsal de qualquer anedota.",
                    },
                ],
            },
            {
                "slug": "b2-telling-anecdotes",
                "title": "You Won't Believe This",
                "skill": "Conversation",
                "summary": "Conte histórias surpreendentes com ganchos, reações naturais e os tempos narrativos certos.",
                "theory": (
                    "Contar uma anedota em inglês tem receita. Abra com um gancho que promete "
                    "emoção: 'You won't believe what happened to me yesterday.' Monte o cenário "
                    "com past continuous ('I was walking home...'), use past perfect para o "
                    "contexto anterior ('I hadn't seen her in ten years') e past simple para os "
                    "eventos que empurram a história. Intercale reações genuínas — 'No way!', "
                    "'What happened next?', 'You're kidding!' — para mostrar que está engajado. "
                    "Para o brasileiro, dois cuidados: não traduzir 'você não vai acreditar' com "
                    "tom neutro (a entonação animada faz parte do significado) e não abusar de "
                    "'meu Deus' — 'Oh my gosh' é mais natural no dia a dia americano."
                ),
                "example": "So, to make a long story short, I missed the flight, lost my suitcase, and still had the best week of my life.",
                "key_points": [
                    "Gancho: 'You won't believe what happened...'",
                    "Cenário no continuous, trama no simple, contexto no perfect",
                    "Reações: 'No way!', 'What happened next?', 'You're kidding!'",
                    "'To make a long story short' resume antes do desfecho",
                    "'It's such a small world' reage a coincidências",
                ],
                "dialogue": [
                    {"speaker": "Ana", "line": "You won't believe what happened to me yesterday."},
                    {"speaker": "Mike", "line": "What? Tell me everything."},
                    {"speaker": "Ana", "line": "I was walking home when I ran into my old teacher from school."},
                    {"speaker": "Mike", "line": "No way! The one you hadn't seen in ten years?"},
                    {"speaker": "Ana", "line": "That one! We had been trying to find each other online for ages."},
                    {"speaker": "Mike", "line": "So what did you two do?"},
                    {"speaker": "Ana", "line": "We grabbed coffee and talked for three hours straight."},
                    {"speaker": "Mike", "line": "That's amazing! It really is such a small world."},
                    {"speaker": "Ana", "line": "Honestly, I'm still smiling about it."},
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Qual é a função de 'You won't believe what happened' ao iniciar uma conversa?",
                        "choices": [
                            "Apresentar uma novidade surpreendente e prender a atenção",
                            "Pedir desculpas por um atraso",
                            "Encerrar uma conversa formal",
                            "Fazer um convite para sair",
                        ],
                        "correct_index": 0,
                        "explanation": "Essa frase é um gancho clássico de anedota: ela promete algo surpreendente e cria expectativa, convidando o outro a perguntar 'What? Tell me everything!'. É exatamente como nativos abrem histórias pessoais.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "No diálogo, Ana diz: 'We had been trying to find each other online for ages.' Por que ela usa essa forma?",
                        "choices": [
                            "Para mostrar duração de uma ação antes do encontro",
                            "Para falar de um plano futuro",
                            "Para expressar uma hipótese irreal",
                            "Para fazer um pedido educado",
                        ],
                        "correct_index": 0,
                        "explanation": "'Had been trying... for ages' é past perfect continuous: uma tentativa que durou muito tempo antes do reencontro (o evento passado principal da história). É o tempo perfeito para dar profundidade temporal a uma anedota.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "I was walking home when I ___ (to run) into my old teacher.",
                        "correct": "ran",
                        "explanation": "'Run into someone' é o phrasal verb para encontrar alguém por acaso — perfeito para anedotas. Aqui ele é o evento que interrompe o cenário ('I was walking'), então vai para o past simple: ran.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: won't / believe / what / you / happened",
                        "correct": "You won't believe what happened.",
                        "explanation": "O gancho padrão de anedota: 'You won't believe what happened.' Guarde-o inteiro — abrir a história assim soa instantaneamente natural e nativo.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "It's such a small world.",
                        "explanation": "Expressão-fixada para reagir a coincidências: 'que mundo pequeno!'. Use-a quando algo improvável acontece, como reencontrar alguém do passado por acaso.",
                    },
                ],
            },
        ],
    },
    {
        "title": "Hypothetical English",
        "position": 2,
        "description": "Fale de arrependimentos, hipóteses e situações irreais no passado e no presente com condicionais e wish.",
        "lessons": [
            {
                "slug": "b2-third-conditional",
                "title": "If Only I Had Known",
                "skill": "Grammar",
                "summary": "Use a terceira condicional para falar de hipóteses impossíveis sobre o passado.",
                "theory": (
                    "A terceira condicional fala de um passado alternativo que não aconteceu — e "
                    "que não pode mais ser mudado. A forma é fixa: if + had + particípio (a "
                    "condição) e would have + particípio (o resultado): 'If I had known about the "
                    "traffic, I would have left earlier.' Em português dizemos 'se eu soubesse, "
                    "teria saído', e é aí que mora a armadilha: o brasileiro costuma misturar "
                    "'If I would have known', que soa errado para nativos, ou usar o presente "
                    "'would leave' para um resultado passado. Também vale contrair: 'If I'd "
                    "known... I'd have left...' — e na negativa, 'wouldn't have'."
                ),
                "example": "If we had booked earlier, the tickets would have been much cheaper.",
                "key_points": [
                    "if + had + particípio, would have + particípio",
                    "Nunca 'would' na cláusula do if",
                    "Forma contratada: If I'd known..., I'd have left",
                    "Negativa: wouldn't have + particípio",
                    "Passado impossível de mudar = sempre 3ª condicional",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "If I ___ about the traffic, I would have left earlier.",
                        "choices": ["had known", "knew", "have known", "would know"],
                        "correct_index": 0,
                        "explanation": "Condição passada irreal: if + past perfect (had known). 'Knew' é da segunda condicional (presente/futuro hipotético) e 'would know' quebra a regra de ouro: nunca 'would' depois de if.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "If we had booked earlier, the tickets ___ cheaper.",
                        "choices": ["would have been", "will be", "would be", "had been"],
                        "correct_index": 0,
                        "explanation": "A condição está no passado (had booked), então o resultado também é passado irreal: would have + particípio. 'Would be' é resultado de presente/futuro — o erro clássico de quem mistura as condicionais.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "She would have called you if she ___ (to have) your number.",
                        "correct": "had had",
                        "accepted": ["had had"],
                        "explanation": "Soa estranho, mas é correto: o primeiro had é o auxiliar do past perfect e o segundo é o verbo 'ter'. 'If she had had your number' = se ela tivesse tido seu número. Na fala, quase sempre vira 'if she'd had'.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: would / have / we / won / you / if / had / played",
                        "correct": "We would have won if you had played.",
                        "explanation": "A ordem também funciona invertida, mas a estrutura interna é sempre a mesma: 'would have + particípio' no resultado e 'had + particípio' no if. Duas metades, cada uma com sua forma.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "If they had left sooner, they wouldn't have missed the flight.",
                        "explanation": "Repare nas duas marcas da terceira condicional negativa: 'had left' no if e 'wouldn't have missed' no resultado. O passado não muda, mas a gente adora reescrevê-lo.",
                    },
                ],
            },
            {
                "slug": "b2-mixed-conditionals",
                "title": "Mixing Times",
                "skill": "Grammar",
                "summary": "Combine passado e presente em condicionais mistas: condições passadas com resultados atuais, e vice-versa.",
                "theory": (
                    "Nem toda hipótese mora no mesmo tempo. Na condicional mista, a condição e o "
                    "resultado estão em tempos diferentes. O mix mais comum é passado → presente: "
                    "'If I had studied medicine, I would be a doctor now' — a escolha foi no "
                    "passado, mas a consequência vive no seu presente. O caminho inverso também "
                    "existe, presente → passado: 'If I weren't so shy, I would have asked her out "
                    "last year' — minha timidez é de agora, mas o efeito apareceu no passado. "
                    "Como não existe equivalente direto em português, o brasileiro tende a "
                    "manter tudo no mesmo tempo. A dica é olhar para a linha do tempo de cada "
                    "metade separadamente e só depois montar a frase; 'now', 'today', 'last "
                    "year' são pistas valiosas."
                ),
                "example": "If I had taken that job in Lisbon, I would be living in Europe now.",
                "key_points": [
                    "Passado → presente: If I had..., I would... now",
                    "Presente → passado: If I were..., I would have...",
                    "Analise cada metade separadamente na linha do tempo",
                    "'now / today' → resultado presente; 'last year' → passado",
                    "A condição define o tempo do if, o resultado define o would",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "If she had saved money last year, she ___ on vacation right now.",
                        "choices": ["would be", "would have been", "will be", "is"],
                        "correct_index": 0,
                        "explanation": "A condição é passada (had saved), mas o resultado é presente: 'right now' não deixa dúvida. Mistura clássica: if + past perfect com would + verbo no presente. 'Would have been' ignoraria o 'right now'.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "If I weren't afraid of heights, I ___ the rooftop tour last summer.",
                        "choices": ["would have taken", "would take", "had taken", "took"],
                        "correct_index": 0,
                        "explanation": "Aqui a condição é um estado atual (I am afraid today) e o resultado é passado (last summer): if + past simple com would have + particípio. O medo é de agora, mas o tour perdido ficou no verão passado.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "If he ___ (to not stay up) so late last night, he wouldn't be so tired today.",
                        "correct": "hadn't stayed up",
                        "accepted": ["hadn't stayed up", "had not stayed up"],
                        "explanation": "A causa é passada (a noite passada) e o efeito é presente (cansaço hoje): if + past perfect negativo (hadn't stayed up) com would be... today. Padrão de condicional mista passado → presente.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: would / happier / now / she / be / if / had / listened",
                        "correct": "She would be happier now if she had listened.",
                        "explanation": "Resultado no presente ('would be... now') e condição no passado ('had listened'): essa é a cara da condicional mista mais comum. O 'now' é a pista que separa os tempos.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "If I had taken that job, I would be in Canada now.",
                        "explanation": "Decisão no passado, vida no presente: 'had taken' + 'would be... now'. É assim que nativos comentam escolhas antigas cujas consequências ainda sentem hoje.",
                    },
                ],
            },
            {
                "slug": "b2-wish-regrets",
                "title": "Wishes & Regrets",
                "skill": "Grammar",
                "summary": "Domine wish + past simple, wish + past perfect e wish + would, e saiba quando usar hope.",
                "theory": (
                    "Wish é o coração dos arrependimentos, e cada tempo atrás dele muda o "
                    "significado. Wish + past simple fala de um desejo pelo presente: 'I wish I "
                    "were taller' (queria ser — não sou). Wish + past perfect é arrependimento "
                    "pelo passado: 'I wish I had studied abroad' (queria ter estudado — não "
                    "estudei). Wish + would expressa irritação com algo que a outra pessoa faz e "
                    "você quer que mude: 'I wish you would stop smoking.' E atenção à dupla que "
                    "enlouquece brasileiros: hope é para desejos possíveis e positivos sobre o "
                    "futuro ('I hope you pass the exam'), enquanto wish + passado aponta para o "
                    "irreal ou o improvável. Na fala, 'If only...' tem o mesmo valor de wish, "
                    "com mais emoção."
                ),
                "example": "I wish I were better at math, and I really wish my neighbor would turn his music down.",
                "key_points": [
                    "wish + past simple = desejo irreal pelo presente",
                    "wish + past perfect = arrependimento pelo passado",
                    "wish + would = irritação com hábito alheio",
                    "hope = futuro possível e positivo; wish = irreal",
                    "'If only...' = wish com mais ênfase emocional",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "I wish I ___ taller.",
                        "choices": ["were", "am", "would be", "will be"],
                        "correct_index": 0,
                        "explanation": "Desejo irreal pelo presente: wish + past simple. Com 'I', a forma padrão é 'were' (subjuntivo), embora você ouça 'was' informal na fala. 'Would be' ficaria para irritação com algo que pode mudar — altura, infelizmente, não muda.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "I wish he ___ his music so loud. It drives me crazy!",
                        "choices": ["wouldn't play", "didn't play", "hadn't played", "doesn't play"],
                        "correct_index": 0,
                        "explanation": "Irritação com um hábito presente de outra pessoa que você quer que ela mude: wish + would (aqui na negativa, wouldn't). É o famoso 'wish + would' do vizinho barulhento — só se usa para ações que dependem de vontade alheia.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Your friend has an exam tomorrow. What do you say?",
                        "choices": ["I hope you pass!", "I wish you passed!", "I wish you had passed!", "I hoped you pass!"],
                        "correct_index": 0,
                        "explanation": "Passar na prova é possível e o exame é amanhã: usa-se hope + presente, nunca wish. 'Wish you passed' trataria o futuro como irreal; 'wish you had passed' já daria o resultado como perdido — péssimo presságio!",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "I wish I ___ (to study) harder for the test last week.",
                        "correct": "had studied",
                        "explanation": "Arrependimento pelo passado: wish + past perfect (had + particípio). 'Last week' confirma que o barco já navegou — resta imaginar como teria sido.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: wish / I / had / taken / more / photos",
                        "correct": "I wish I had taken more photos.",
                        "explanation": "Estrutura do arrependimento: I wish + had + particípio. Guarde o padrão 'I wish I had...' — é o jeito mais rápido de expressar 'queria ter...' em inglês.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "I wish we had more time together.",
                        "explanation": "Aqui o desejo é presente (não há had + particípio): wish + past simple 'had more time' = queria que tivéssemos mais tempo agora. Compare com 'I wish we had had more time' — esse sim seria passado.",
                    },
                ],
            },
            {
                "slug": "b2-talk-regrets",
                "title": "If I Could Go Back",
                "skill": "Conversation",
                "summary": "Converse sobre arrependimentos e segundas chances usando condicionais, wish e 'if only' com naturalidade.",
                "theory": (
                    "Falar de arrependimentos é um assunto que aproxima as pessoas — e em inglês "
                    "tem vocabulário próprio. Abra com uma pergunta ampla: 'If you could go back "
                    "and change one thing, what would it be?' Use 'I wish I had...' e 'If only "
                    "I had...' para o passado, e condicionais mistas para conectar escolhas "
                    "antigas à vida de hoje: 'If I had been braver, I would have applied.' Para "
                    "responder com empatia, vale 'That's honest', 'It's never too late' e "
                    "'You could still do it'. O brasileiro costuma traduzir 'se eu pudesse "
                    "voltar' como 'if I could go back' — está certíssimo —, mas lembre de "
                    "emendar a condicional: '...I would change...' para a frase ficar completa."
                ),
                "example": "If only I had learned to play the guitar when I was a kid!",
                "key_points": [
                    "'If you could go back, what would you change?' abre o papo",
                    "'I wish I had...' / 'If only I had...' = arrependimento",
                    "'It's never too late' tranquiliza o outro",
                    "Feche a condicional: 'If I had..., I would have...'",
                    "'I regret not + -ing' também expressa arrependimento",
                ],
                "dialogue": [
                    {"speaker": "Lucas", "line": "If you could go back and change one thing, what would it be?"},
                    {"speaker": "Emma", "line": "Definitely college. I wish I had studied abroad for a year."},
                    {"speaker": "Lucas", "line": "Really? Why didn't you?"},
                    {"speaker": "Emma", "line": "I was scared of being so far from my family. If I had been braver, I would have applied."},
                    {"speaker": "Lucas", "line": "That's honest. My big regret is not learning an instrument as a kid."},
                    {"speaker": "Emma", "line": "It's never too late, you know. You could still take lessons."},
                    {"speaker": "Lucas", "line": "If only I had the free time!"},
                    {"speaker": "Emma", "line": "We always find excuses, don't we?"},
                    {"speaker": "Lucas", "line": "Guilty as charged. Maybe next year I'll finally do it."},
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "No diálogo, Lucas diz: 'If only I had the free time!' O que ele quer dizer?",
                        "choices": [
                            "Ele gostaria de ter tempo livre, mas não tem",
                            "Ele tinha muito tempo livre no passado",
                            "Ele acabou de arrumar tempo livre",
                            "Ele está oferecido para ajudar Emma",
                        ],
                        "correct_index": 0,
                        "explanation": "'If only' funciona como 'wish', mas com mais emoção: 'If only I had the free time' = 'queria tanto que eu tivesse tempo'. Como o verbo está no past simple ('had'), o desejo é irreal no presente — ele não tem tempo.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Emma responde: 'It's never too late, you know.' Qual é o espírito dessa resposta?",
                        "choices": [
                            "Encorajar Lucas a começar agora",
                            "Criticar a preguiça dele",
                            "Mudar de assunto",
                            "Concordar que já era tarde demais",
                        ],
                        "correct_index": 0,
                        "explanation": "'It's never too late' é a frase clássica de incentivo: não importa a idade ou o tempo passado, você ainda pode começar. Ela suaviza o arrependimento e mantém a conversa positiva — um ótimo recurso de empatia.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "If I ___ (to be) braver back then, I would have applied for that job.",
                        "correct": "had been",
                        "explanation": "Condição no passado com resultado no passado: if + past perfect (had been) + would have applied. É a terceira condicional pura, a gramática oficial dos arrependimentos.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: what / would / change / you / if / could / go / back",
                        "correct": "What would you change if you could go back?",
                        "explanation": "A pergunta que abre esse tipo de conversa: 'What would you change if you could go back?' — second conditional (irreal) para convidar o outro a imaginar o passado de novo.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "It's never too late to start something new.",
                        "explanation": "Frase-feita de incentivo, muito útil ao falar de segundas chances. Guarde o padrão: 'It's never too late to + verbo'.",
                    },
                ],
            },
        ],
    },
    {
        "title": "Advanced Structures",
        "position": 3,
        "description": "Estruturas de nível avançado: causativas, passiva de relato, orações relativas complexas e padrões de verbos que confundem.",
        "lessons": [
            {
                "slug": "b2-causative",
                "title": "Getting Things Done",
                "skill": "Grammar",
                "summary": "Use have/get something done e have someone do para falar de serviços que você encomenda a outros.",
                "theory": (
                    "A estrutura causativa é essencial na vida adulta: cortar cabelo, consertar "
                    "carro, pintar casa — quando você não faz, alguém faz para você. O padrão "
                    "mais comum é have/get + objeto + particípio: 'I had my car repaired' ou "
                    "'I got my hair cut' — e o dono da ação não aparece. Com pessoa, muda a "
                    "regra: have + pessoa + verbo puro ('I had the mechanic check the brakes') "
                    "ou get + pessoa + to + verbo ('I got my brother to help me'). O erro "
                    "clássico do brasileiro vem do 'mandei consertar': 'I made my car repaired' "
                    "não existe — made é para obrigação. E atenção ao sentido: 'I had repaired "
                    "my car' significa que VOCÊ mesmo consertou antes de algo, coisa bem "
                    "diferente de 'I had my car repaired'."
                ),
                "example": "I need to get my laptop fixed and have the dentist take a look at my back tooth.",
                "key_points": [
                    "have/get + objeto + particípio = alguém faz para você",
                    "have + pessoa + verbo puro (sem to!)",
                    "get + pessoa + to + verbo",
                    "'I had my car repaired' ≠ 'I had repaired my car'",
                    "Não traduza 'mandei fazer' com 'make'",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Qual frase significa que ALGUÉM consertou o carro para você?",
                        "choices": [
                            "I had my car repaired.",
                            "I repaired my car.",
                            "I had repaired my car.",
                            "I made my car repaired.",
                        ],
                        "correct_index": 0,
                        "explanation": "Have + objeto + particípio é a causativa de serviço: você pagou/alguém consertou. 'I repaired my car' = você mesmo fez; 'I had repaired' = past perfect de algo que você fizera antes; e 'made my car repaired' é tradução literal do 'mandei' que não existe em inglês.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "The manager had the intern ___ the reports.",
                        "choices": ["prepare", "to prepare", "prepared", "preparing"],
                        "correct_index": 0,
                        "explanation": "Com pessoa depois de have, o verbo vem nu, sem to: 'had the intern prepare'. Se fosse get, aí sim entraria o to: 'got the intern to prepare'. 'Prepared' servira para objeto, não para pessoa.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "I finally got my visa ___ (to approve) last week.",
                        "correct": "approved",
                        "explanation": "Get + objeto + particípio: o visto foi aprovado (por outros, no consulado) para você. Quem realizou a ação não importa — a estrutura destaca quem se beneficia.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: had / I / my / phone / fixed / yesterday",
                        "correct": "I had my phone fixed yesterday.",
                        "explanation": "A ordem é fixa: sujeito + had + objeto + particípio. 'I had my phone fixed' — levei o celular e o técnico consertou. Trocar a ordem destrói o sentido causativo.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "They got their house painted last month.",
                        "explanation": "Aqui a causativa vem com get, comum na fala americana: 'got their house painted' — contrataram pintores. A ideia é a mesma do had, com registro mais informal.",
                    },
                ],
            },
            {
                "slug": "b2-passive-reporting",
                "title": "It Is Said That...",
                "skill": "Grammar",
                "summary": "Reporte informações sem citar a fonte com it is said/believed/reported that e 'is thought to...'.",
                "theory": (
                    "Jornais e conversas especulativas usam a passiva de relato para falar de "
                    "algo sem assumir quem disse: 'It is said that the house is haunted.' A "
                    "estrutura é it + is + verbo de relato + that + frase — e no passado, it was "
                    "reported/believed/said that. Há ainda uma versão elegante com infinitivo: "
                    "'He is thought to be in his forties' = acham que ele tem uns quarenta. "
                    "Para eventos já concluídos, o infinitivo perfeito assume: 'She is believed "
                    "to have left the country.' O brasileiro costuma recorrer ao indefinido "
                    "'they say that...', que existe, mas soa vago demais em contextos formais; "
                    "a passiva de relato é a escolha profissional de notícia, relatório e "
                    "fofoca chique."
                ),
                "example": "It is believed that the painting is a fake, and the forger is thought to have died in 1998.",
                "key_points": [
                    "It is said/believed/reported that + frase",
                    "Passado: It was reported that...",
                    "Versão com infinitivo: He is thought to be...",
                    "Passado dentro do infinitivo: to have left",
                    "Use quando a fonte é desconhecida ou irrelevante",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "___ that the company will open a new office in São Paulo.",
                        "choices": ["It is expected", "Is expected", "It expects", "Expecting it"],
                        "correct_index": 0,
                        "explanation": "A passiva de relato precisa do sujeito 'it' e do verbo no passivo: 'It is expected that...'. 'It expects' daria a empresa como sujeito que espera algo — uma ideia completamente diferente.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "The novelist ___ to be living in Portugal now.",
                        "choices": ["is said", "says", "is saying", "said"],
                        "correct_index": 0,
                        "explanation": "Aqui entra a versão com infinitivo: sujeito + is said + to be living. Equivale a 'People say that she is living in Portugal', sem citar quem diz. 'Says' faria a romancista mesma a fonte.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "___ (to believe) that the painting is a fake.",
                        "correct": "It is believed",
                        "explanation": "Comece com 'It is believed that...' — a manchete especulativa padrão. O 'it' é o sujeito-coringa: não é tradução de 'isso', mas parte fixa da estrutura.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: thought / he / is / to / be / in / his / forties",
                        "correct": "He is thought to be in his forties.",
                        "explanation": "A versão compacta da passiva de relato: pessoa + is thought + to be. Tradução mental: 'ele é pensado estar...' — na prática, 'acham que ele está/tem...'.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "It was reported that no one was injured.",
                        "explanation": "No passado, o relato inteiro recua: it was reported. Duas passivas juntas ('was reported', 'was injured') são a cara do jornalismo de acidentes e ocorrências.",
                    },
                ],
            },
            {
                "slug": "b2-relative-advanced",
                "title": "Beyond Basic Clauses",
                "skill": "Grammar",
                "summary": "Domine orações relativas não-definidoras (com vírgulas) e reduzidas (the man sitting there).",
                "theory": (
                    "Dois upgrades deixam suas relativas de nível B2. Primeiro, as não-definidoras: "
                    "informação extra entre vírgulas, que pode sair sem estragar a frase — 'My "
                    "sister, who lives in Rio, is visiting us.' Nelas, nunca use that, e who/which "
                    "são obrigatórios mesmo se o verbo for o da frase. Segundo, as reduzidas: "
                    "quando a oração tem who is/which is/that is, dá para cortar o pronome e o "
                    "verbo be, deixando só o particípio presente: 'the man sitting there' (= who "
                    "is sitting there) ou o particípio passado: 'the bridge built in 1930' (= "
                    "which was built). O brasileiro erra ao usar that com vírgula ('my sister, "
                    "that lives...') e ao manter o 'is' redundante ('the man who is sitting' "
                    "está certo, mas 'the man is sitting there is my boss' vira fratura exposta)."
                ),
                "example": "My new manager, who used to work in Tokyo, loved the report written by the intern.",
                "key_points": [
                    "Não-definidora: vírgulas + informação extra",
                    "Nunca 'that' depois de vírgula",
                    "Reduzida ativa: the man sitting there = who is sitting",
                    "Reduzida passiva: a bridge built in 1930 = which was built",
                    "A vírgula muda o sentido: 'my sister, who...' pressupõe irmã única",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "My sister, ___ lives in Rio, is visiting us this weekend.",
                        "choices": ["who", "that", "which", "whose"],
                        "correct_index": 0,
                        "explanation": "Com vírgulas (oração não-definidora), who é a escolha para pessoas e that é proibido. 'Which' é para coisas, e 'whose' indicaria posse — aqui falta quem vive, não de quem é.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "The man ___ next to you is my boss.",
                        "choices": ["sitting", "who sitting", "is sitting", "sit"],
                        "correct_index": 0,
                        "explanation": "É a relativa reduzida: 'the man sitting next to you' = 'the man who is sitting next to you'. Cortamos who + is e ficamos com o particípio presente. 'Is sitting' deixaria dois verbos principais brigando pela frase.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "The students ___ (to select) for the project will present it on Friday.",
                        "correct": "selected",
                        "explanation": "Relativa reduzida passiva: 'the students selected' = 'the students who were selected'. Sem quem/that, só o particípio passado — e o sentido passivo vem dele.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: the / bridge / built / in / 1930 / is / closed",
                        "correct": "The bridge built in 1930 is closed.",
                        "explanation": "'Built in 1930' reduz 'which was built in 1930'. A frase principal é 'the bridge is closed', e o detalhe histórico entra como adjetivo enxuto.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "The woman talking to the principal is my aunt.",
                        "explanation": "Mais uma reduzida ativa: 'the woman talking to...' = 'the woman who is talking to...'. Na fala corrida, o who is praticamente desaparece — ouvir e captar isso é sinal de B2 consolidado.",
                    },
                ],
            },
            {
                "slug": "b2-verb-patterns",
                "title": "Tricky Verb Patterns",
                "skill": "Grammar",
                "summary": "Diferencie stop/remember/try/forget + infinitivo (objetivo) de + -ing (processo ou memória).",
                "theory": (
                    "Alguns verbos mudam de sentido conforme vêm com infinitivo ou com -ing — e "
                    "aqui o português engana. Remember/forget + infinitivo é a tarefa a fazer: "
                    "'Remember to lock the door' (não esqueça de trancar). Com -ing, é memória "
                    "do passado: 'I remember locking the door' (lembro de ter trancado). Stop "
                    "+ -ing é abandonar um hábito: 'We stopped drinking coffee at night'; stop "
                    "+ infinitivo é pausar para fazer outra coisa: 'I stopped to buy bread' "
                    "(parei o carro a fim de comprar pão — em português 'parei para comprar', "
                    "logo o brasileiro quer 'stopped for buy'). Try + infinitivo é esforço "
                    "diante de dificuldade: 'I tried to open the jar'; try + -ing é experimentar "
                    "uma alternativa: 'Try restarting your phone'. São pequenos deslocamentos "
                    "que mudam a mensagem inteira."
                ),
                "example": "I remembered to cancel the subscription, but I'll never forget meeting the founder at that event.",
                "key_points": [
                    "remember/forget TO do = tarefa; DOING = memória",
                    "stop DOING = parar o hábito; stop TO do = pausar para",
                    "try TO do = esforçar-se; try DOING = experimentar",
                    "'Parei para comprar' = stopped TO buy",
                    "Traduzir do português sem pensar aqui é armadilha certa",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Remember ___ the lights before you leave the office.",
                        "choices": ["to turn off", "turning off", "turn off", "turned off"],
                        "correct_index": 0,
                        "explanation": "É uma tarefa futura: não esqueça de apagar as luzes. Verbo de obrigação + infinitivo: remember to turn off. 'Turning off' seria lembrança de um apagar já acontecido.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "We stopped ___ coffee at night because it kept us awake.",
                        "choices": ["drinking", "to drink", "drink", "drank"],
                        "correct_index": 0,
                        "explanation": "Abandonar um hábito: stop + -ing. 'Stopped to drink' significaria que você pausou outra atividade a fim de tomar café — praticamente o oposto da saúde do sono!",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "The printer isn't working. Try ___ it off and on again.",
                        "choices": ["turning", "to turn", "turn", "turned"],
                        "correct_index": 0,
                        "explanation": "Sugestão de experimento: tente a alternativa de desligar e ligar. Try + -ing propõe testar uma solução; 'try to turn' sugeriria esforço diante de dificuldade, como se o botão resistisse.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "On my way home, I stopped ___ (to buy) some bread.",
                        "correct": "to buy",
                        "explanation": "'Parei (o carro) para comprar pão': a parada tem um objetivo novo, então stop + infinitivo. O brasileiro traduz 'para comprar' e quer 'for buy' ou 'buying' — as duas erram.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: locking / I / remember / the / door",
                        "correct": "I remember locking the door.",
                        "explanation": "Memória de ação concluída: lembro-me de ter trancado a porta. O -ing aponta para o passado — a tranca já aconteceu na sua cabeça.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "Did you remember to water the plants?",
                        "explanation": "Pergunta sobre tarefa: você se lembrou de ( ter de) regar as plantas? Infinitivo 'to water' = obrigação da lista mental, não lembrança nostálgica do regador.",
                    },
                ],
            },
            {
                "slug": "b2-complaints",
                "title": "Sorting Out Problems",
                "skill": "Conversation",
                "summary": "Reclame com educação e eficiência em inglês: abra o assunto, descreva o problema e negocie a solução.",
                "theory": (
                    "Reclamar bem em inglês é quase uma arte: firme no problema, suave na forma. "
                    "Abra com um amortecedor: 'Excuse me, I'm afraid there's a problem with my "
                    "room' — o 'I'm afraid' aqui não é medo, é polidez. Descreva o problema com "
                    "fatos, não com acusações: 'The air conditioning isn't working' em vez de "
                    "'You gave me a terrible room'. Faça pedidos com as fórmulas mágicas: 'Would "
                    "it be possible to...?', 'Is there any chance I could...?', 'I'd appreciate "
                    "it if...'. E reaja à solução com 'That would be great' ou 'Thank you for "
                    "sorting this out'. O brasileiro amiúde traduz 'quero meu dinheiro de volta' "
                    "como 'I want my money back' — gramática certa, tom de briga; 'I'd like a "
                    "refund, please' abre as mesmas portas sem gritaria."
                ),
                "example": "I'm afraid there's a problem with my order — the soup is cold. Would it be possible to get a fresh one?",
                "key_points": [
                    "'I'm afraid there's a problem...' abre com polidez",
                    "Descreva fatos: 'It isn't working', não 'You ruined...'",
                    "Pedidos: 'Would it be possible to...?' / 'Is there any chance...?'",
                    "'I'd like a refund, please' > 'I want my money back'",
                    "Feche agradecendo: 'Thanks for sorting this out'",
                ],
                "dialogue": [
                    {"speaker": "Sofia", "line": "Excuse me, I'm afraid there's a problem with my room."},
                    {"speaker": "David", "line": "I'm sorry to hear that. What seems to be the issue?"},
                    {"speaker": "Sofia", "line": "The air conditioning isn't working, and the room gets really hot at night."},
                    {"speaker": "David", "line": "That does sound uncomfortable. I do apologize for the inconvenience."},
                    {"speaker": "Sofia", "line": "Is there any chance I could move to another room?"},
                    {"speaker": "David", "line": "Let me check... Yes, we have one available on the fourth floor, with a nice view."},
                    {"speaker": "Sofia", "line": "That would be great, as long as it's quieter too."},
                    {"speaker": "David", "line": "Absolutely. I'll have someone bring your luggage up right away."},
                    {"speaker": "Sofia", "line": "Thank you so much. I really appreciate your help."},
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Por que Sofia abre a reclamação com 'I'm afraid there's a problem with my room'?",
                        "choices": [
                            "Para suavizar a reclamação e soar educada",
                            "Para mostrar que ela está com medo do gerente",
                            "Para admitir que a culpa é dela",
                            "Para encerrar a conversa mais rápido",
                        ],
                        "correct_index": 0,
                        "explanation": "'I'm afraid' é um amortecedor fixo: prepara o ouvinte para uma notícia ruim sem agressividade. Não tem nada de medo real — é a polidez britânica e americana anunciando um problema.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "'Is there any chance I could move to another room?' é usado para...",
                        "choices": [
                            "Fazer um pedido educado deixando espaço para um 'não'",
                            "Exigir mudança imediata de quarto",
                            "Perguntar sobre a probabilidade de chuva",
                            "Pedir desculpas pelo incômodo",
                        ],
                        "correct_index": 0,
                        "explanation": "Essa fórmula embrulha o pedido em hipótese: 'haveria alguma chance de...?'. Ela mostra respeito pela situação do interlocutor e, por isso, costuma conseguir mais do que exigências diretas.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "___ it be possible to get a full refund?",
                        "correct": "Would",
                        "explanation": "'Would it be possible to...?' é a versão polida de 'Can I...?'. O would hipotético deixa o pedido em território de cortesia — ideal para reclamações em hotéis, lojas e restaurantes.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: to / I'm / sorry / hear / that",
                        "correct": "I'm sorry to hear that.",
                        "explanation": "A resposta empática padrão de quem recebe uma reclamação: sinto muito ouvir isso. Ela valida o problema antes de partir para a solução — passo 1 de qualquer bom atendimento.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "There seems to be a mistake on my bill.",
                        "explanation": "'There seems to be...' é outra abertura macia: aponta o erro sem culpar ninguém em especial. Perfeita para contestar contas, faturas e extratos com classe.",
                    },
                ],
            },
        ],
    },
    {
        "title": "Natural Fluency",
        "position": 4,
        "description": "Soe natural em inglês com colocações, phrasal verbs, idiomas, marcadores do discurso e debate de ideias.",
        "lessons": [
            {
                "slug": "b2-collocations",
                "title": "Words That Belong Together",
                "skill": "Vocabulary",
                "summary": "Aprenda combinações naturais de palavras (heavy rain, make a decision, catch a cold) que o inglês exige.",
                "theory": (
                    "Colocações são palavras que casam por costume: o inglês diz heavy rain, "
                    "nunca 'strong rain'; make a decision, não 'take a decision'; strong coffee, "
                    "não 'powerful coffee'. Não há lógica — há hábito de nativos, e é exatamente "
                    "esse hábito que separa o inglês fluente do inglês traduzido. Como em "
                    "português dizemos 'tomar uma decisão' e 'chuva forte', o brasileiro faz "
                    "escolhas erradas com muita confiança. A estratégia é tratar cada colocação "
                    "como uma unidade única, como se fosse uma palavra só: anote 'make a "
                    "decision' junto, repita junto e crie exemplos próprios. Faça uma pizza "
                    "de grupos: make (decisions, complaints, progress), take (a photo, a break, "
                    "a chance), do (homework, the dishes, business) e catch (a cold, a bus, "
                    "someone's eye)."
                ),
                "example": "We had heavy rain all morning, so I made the decision to take a break and do the paperwork later.",
                "key_points": [
                    "make a decision (não take!) — e make a complaint, make progress",
                    "heavy rain / strong coffee — adjetivo certo para cada substantivo",
                    "take a photo / take a break / take a chance",
                    "catch a cold / catch a bus",
                    "Aprende a colocação inteira, palavra por palavra nunca",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "It was ___ rain all morning, so we stayed inside.",
                        "choices": ["heavy", "strong", "hard", "big"],
                        "correct_index": 0,
                        "explanation": "Em inglês, chuva se mede com heavy: heavy rain, a heavy storm. 'Strong' é a tradução de 'forte' que soa estranha para nativos — forte fica para café, opiniões e vento (strong winds).",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "I need to ___ a decision by Friday.",
                        "choices": ["make", "take", "do", "give"],
                        "correct_index": 0,
                        "explanation": "O inglês faz decisões: make a decision. 'Take a decision' existe, mas é formal e mais britânico-jornalístico; no dia a dia americano, make é a colocação padrão — e 'do/give a decision' simplesmente não existem.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Let's ___ a photo in front of the fountain.",
                        "choices": ["take", "make", "do", "catch"],
                        "correct_index": 0,
                        "explanation": "Fotos se tiram com take: take a photo/take a picture. 'Make a photo' é a tradução literal de 'fazer uma foto' que nenhum nativo usa — e que entrega o falante tradutor na hora.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "I think I'm ___ (to catch) a cold — my throat really hurts.",
                        "correct": "catching",
                        "explanation": "Em inglês a gente 'pesca' um resfriado: catch a cold. Aqui, com 'I think I'm', o verbo vai para o presente contínuo: catching — o resfriado está chegando.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: a / complaint / she / made / formal",
                        "correct": "She made a formal complaint.",
                        "explanation": "Reclamações também se fazem: make a complaint. Guarde o combo do atendimento: faça a reclamação (make a complaint) e, se precisar, peça o reembolso (get a refund).",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "Could I have a strong coffee, please?",
                        "explanation": "Café forte é strong coffee. Note o contraste com a chuva: o mesmo 'forte' do português vira heavy (rain) e strong (coffee) — cada substantivo escolhe seu adjetivo.",
                    },
                ],
            },
            {
                "slug": "b2-phrasal-advanced",
                "title": "Phrasal Verbs in Real Life",
                "skill": "Vocabulary",
                "summary": "Use phrasal verbs de B2 (look into, put off, come up with, run out of) e domine separáveis e inseparáveis.",
                "theory": (
                    "Phrasal verbs são verbos + partícula com sentido novo: look into não é "
                    "'olhar dentro', é investigar. Em B2, os essenciais incluem put off (adiar), "
                    "come up with (inventar/ter uma ideia), run out of (acabar estoque) e turn "
                    "down (recusar ou abaixar volume). A parte mecânica que decide tudo: os "
                    "separáveis aceitam o objeto no meio — 'turn the music down' ou 'turn down "
                    "the music' — mas com pronome o lugar é obrigatoriamente o meio: 'turn it "
                    "down', nunca 'turn down it'. Já os inseparáveis mantêm a partícula colada: "
                    "'look into it', 'run out of them'. O brasileiro erra por causa do objeto "
                    "no fim herdado do português; a regra prática é decorar junto com o phrasal "
                    "se ele é separável ou não, como quem decora o gênero da palavra."
                ),
                "example": "They put off the meeting until Friday because we had run out of ideas to discuss.",
                "key_points": [
                    "look into = investigar; come up with = ter a ideia de",
                    "run out of = acabar (estoque/tempo); put off = adiar",
                    "Separável + pronome: turn it down (nunca turn down it)",
                    "Inseparáveis: look into it, run out of them",
                    "Aprenda junto se é separável ou inseparável",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "The committee promised to ___ the complaint carefully.",
                        "choices": ["look into", "look after", "look for", "look up"],
                        "correct_index": 0,
                        "explanation": "Look into = investigar, examinar a fundo — perfeito para comitês e reclamações. Look after é cuidar de alguém, look for é procurar algo perdido e look up é consultar (uma palavra, um endereço).",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "The music is too loud. Can you ___?",
                        "choices": ["turn it down", "turn down it", "turning it down", "turn down them"],
                        "correct_index": 0,
                        "explanation": "Turn down é separável, e com pronome o lugar é o meio: turn it down. 'Turn down it' é o erro clássico de quem aprendeu só 'turn down the music' e aplicou a mesma ordem ao pronome.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "We need to ___ a solution before Friday.",
                        "choices": ["come up with", "come up to", "come up for", "come up"],
                        "correct_index": 0,
                        "explanation": "Come up with é inseparável e significa criar/inventar: come up with a solution, an idea, a plan. É a colocação oficial de brainstorming em inglês — sem tradução palavra a palavra do 'chegar a'.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "We've ___ (to run out of) sugar — could you buy some on your way home?",
                        "correct": "run out of",
                        "explanation": "Run out of = o estoque acabou: run out of sugar, of time, of patience. Note o present perfect: 'we've run out of' conecta o agora com o estoque vazio.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: put / they / off / meeting / the / until / Friday",
                        "correct": "They put off the meeting until Friday.",
                        "explanation": "Put off = adiar, e aqui o objeto (the meeting) vem depois da partícula — ordem permitida porque é separável. Com pronome seria 'they put it off'.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "She came up with a brilliant idea.",
                        "explanation": "Ouça 'came up with' como um bloco único: teve/inventou uma ideia brilhante. Se tentar traduzir cada palavra, a frase se desmancha — phrasal verb se ouve inteiro.",
                    },
                ],
            },
            {
                "slug": "b2-idioms",
                "title": "Sounding Natural",
                "skill": "Vocabulary",
                "summary": "Use idiomas corriqueiros (piece of cake, under the weather, break the ice) para soar autenticamente fluente.",
                "theory": (
                    "Idiomas são expressões cujo sentido não vem das palavras: 'it's a piece of "
                    "cake' não fala de bolo, fala de facilidade. Em B2, os que mais rendem são "
                    "os do dia a dia: piece of cake (muito fácil), hit the books (estudar"
                    " firme), under the weather (meio doente), break the ice (quebrar o clima "
                    "de constrangimento), once in a blue moon (raramente) e cost an arm and a "
                    "leg (custar caríssimo). Duas dicas de professor: primeiro, idioma se usa "
                    "inteiro e com naturalidade — nada de 'as we say in English...'; segundo, "
                    "evite os idiomas antigos de livro (it's raining cats and dogs) que "
                    "nativos quase não dizem. E cuidado com a tentação de traduzir expressões "
                    "brasileiras: 'chutar o balde' não tem equivalente direto, e 'break the "
                    "bucket' renderia silêncio constrangedor."
                ),
                "example": "The final exam was a piece of cake because I had hit the books for two straight weeks.",
                "key_points": [
                    "a piece of cake = muito fácil",
                    "under the weather = meio doente, indisposto",
                    "hit the books = estudar firme",
                    "break the ice = quebrar o gelo (mesma imagem do PT!)",
                    "cost an arm and a leg = custar caríssimo",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Don't worry about the test — it'll be a piece of cake. O que o falante quer dizer?",
                        "choices": [
                            "O teste será muito fácil",
                            "O teste será muito longo",
                            "Haverá comida na prova",
                            "O teste será cancelado",
                        ],
                        "correct_index": 0,
                        "explanation": "Piece of cake = facilidade extrema, 'mamão com açúcar' americano. Como o sentido é figurado, traduzir literalmente 'pedaço de bolo' não leva a lugar nenhum — o idioma é a unidade de sentido.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "I'm feeling a bit under the weather today. Como a pessoa está?",
                        "choices": [
                            "Um pouco doente, indisposta",
                            "Molhada por causa da chuva",
                            "Muito animada e disposta",
                            "Confusa sobre o clima",
                        ],
                        "correct_index": 0,
                        "explanation": "Under the weather é o eufemismo padrão para 'meio doente' — perfeito para avisar o trabalho sem drama. A tradução literal 'debaixo do tempo' (opção molhada!) é a armadilha clássica do brasileiro.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "I'd better hit the books tonight — finals are next week. O que ela vai fazer?",
                        "choices": [
                            "Estudar bastante",
                            "Devolver livros na biblioteca",
                            "Ir dormir mais cedo",
                            "Bater nos livros de raiva",
                        ],
                        "correct_index": 0,
                        "explanation": "Hit the books = estudar firme, mergulhar nos livros. É o idioma por excelência da época de provas — e o 'hit' aqui é intensidade, não violência.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "That concert ticket cost ___ (idioma para 'muito caro').",
                        "correct": "an arm and a leg",
                        "explanation": "Cost an arm and a leg = custar caríssimo, 'custar os olhos da cara'. A imagem é de perder membros no preço — exagero típico do humor americano.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: to / we / break / needed / the / ice",
                        "correct": "We needed to break the ice.",
                        "explanation": "Break the ice = quebrar o clima inicial de constrangimento — felizmente, aqui a imagem coincide com a do português 'quebrar o gelo'. Rara bênção entre idiomas.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "We go hiking once in a blue moon.",
                        "explanation": "Once in a blue moon = raramente, 'de vez em quando nunca'. A lua azul é evento raro no céu — e o idioma herdou a raridade.",
                    },
                ],
            },
            {
                "slug": "b2-discourse-markers",
                "title": "Anyway, Actually & Mind You",
                "skill": "Vocabulary",
                "summary": "Organize sua fala com marcadores do discurso: anyway, actually, mind you, by the way, to be honest.",
                "theory": (
                    "Marcadores do discurso são as placas de sinalização da conversa — eles "
                    "mostram para onde a fala vira. Anyway retoma ou encerra um assunto: "
                    "'Anyway, where was I?' Actually corrige uma expectativa: 'Everyone thinks "
                    "he's shy. Actually, he does stand-up comedy.' Mind you acrescenta uma "
                    "observação contrária, quase um 'só que': 'The apartment is tiny. Mind you, "
                    "the rent is cheap.' By the way introduz informação lateral, fora do "
                    "assunto: 'By the way, your sister called.' To be honest antecede uma "
                    "opinião franca. O brasileiro conhece 'by the way' (a propósito), mas "
                    "costuma usar 'actually' com sentido de 'atualmente' — que em inglês é "
                    "currently. Dominar esses seis é subir de nível em fluência sem aprender "
                    "uma única regra nova de gramática."
                ),
                "example": "The hotel was far from the beach. Mind you, the price included breakfast, so we didn't mind.",
                "key_points": [
                    "anyway = retomar ou encerrar o assunto",
                    "actually = corrigir expectativa (não é 'atualmente'!)",
                    "mind you = 'só que...', observação contrária",
                    "by the way = informação lateral, fora do tópico",
                    "to be honest = opinião franca a caminho",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "The apartment is tiny. ___, the rent is really cheap.",
                        "choices": ["Mind you", "By the way", "Anyway", "Actually"],
                        "correct_index": 0,
                        "explanation": "Mind you adiciona uma observação que contrapesa a anterior: pequeno, sim, 'só que' o aluguel é barato. É o equilíbrio de argumentos em duas palavras.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "___, where was I before that phone call? Oh yes, the budget.",
                        "choices": ["Anyway", "Actually", "Mind you", "To be honest"],
                        "correct_index": 0,
                        "explanation": "Anyway é a placa de 'voltando ao assunto': retoma a linha do raciocínio após um desvio. É provavelmente o marcador mais frequente em reuniões e conversas longas.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Everyone says the movie is boring. ___, I laughed the whole time.",
                        "choices": ["Actually", "Anyway", "By the way", "Mind you"],
                        "correct_index": 0,
                        "explanation": "Actually apresenta um fato que corrige a expectativa criada: todo mundo diz chato, mas, na real, eu ri o tempo todo. É o contraste entre o senso comum e a sua experiência.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "___ the way, did I mention that I got promoted last month?",
                        "correct": "By",
                        "explanation": "By the way = 'a propósito', introduz algo fora do tópico corrente. A promoção não tem relação com o assunto anterior — por isso ela entra lateralmente, por essa porta.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: honest / be / to / wasn't / it / easy",
                        "correct": "To be honest, it wasn't easy.",
                        "explanation": "To be honest sinaliza franqueza: prepara o ouvinte para uma avaliação sem retoques. Perfeito para opiniões profissionais e feedback construtivo.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "By the way, I loved your presentation today.",
                        "explanation": "Repare como by the way chega de lado: o elogio não era o assunto da conversa, e o marcador anuncia isso. Elogio em segunda mão, em primeira velocidade.",
                    },
                ],
            },
            {
                "slug": "b2-debating",
                "title": "The Great Debate",
                "skill": "Conversation",
                "summary": "Debate ideias em inglês: apresente argumentos, reconheça o outro lado e rebata com polidez e firmeza.",
                "theory": (
                    "Debater em inglês é um balé de firmeza e cortesia. Apresente opinião com "
                    "discurso macio: 'I really think...', 'From my point of view...'. Discorde "
                    "sem quebrar o clima: 'I'm not sure I agree', 'I see your point, but...'. "
                    "Reconheça antes de rebater — a dupla mais valiosa do debate: 'That's a "
                    "fair point, but...' e 'Even so, ...'. E saiba recuar com elegância quando "
                    "vencido por um argumento: 'You've got a point there' ou 'Now that I can "
                    "agree with'. O brasileiro costuma traduzir 'mas eu acho que não' como 'but "
                    "I think no' — gramaticalmente assombroso; e erra por outro lado ao usar "
                    "'you're wrong', que soa agressivo demais. 'I'm afraid I disagree' entrega "
                    "a mesma discordância com passaporte diplomático."
                ),
                "example": "That's a fair point, but even so, I still think hybrid work wins in the long run.",
                "key_points": [
                    "Opine macio: 'I really think...' / 'From my point of view...'",
                    "Discorda educado: 'I'm not sure I agree'",
                    "Reconheça e rebata: 'That's a fair point, but...'",
                    "'Even so...' mantém a réplica depois da concessão",
                    "Ceda com classe: 'You've got a point there'",
                ],
                "dialogue": [
                    {"speaker": "Rafael", "line": "I really think remote work is better for most companies."},
                    {"speaker": "Jenny", "line": "I'm not sure I agree. Don't you think people collaborate better in person?"},
                    {"speaker": "Rafael", "line": "That's a fair point, but studies show remote teams can be just as productive."},
                    {"speaker": "Jenny", "line": "Even so, new employees learn much faster when they sit next to experienced colleagues."},
                    {"speaker": "Rafael", "line": "I see what you mean, though a good onboarding program can solve that."},
                    {"speaker": "Jenny", "line": "What about loneliness, though? Working from home can be really isolating."},
                    {"speaker": "Rafael", "line": "You've got a point there. Maybe a hybrid model is the best of both worlds."},
                    {"speaker": "Jenny", "line": "Now that I can agree with. Balance usually wins."},
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "'That's a fair point, but...' indica que o falante vai...",
                        "choices": [
                            "Reconhecer o argumento do outro e depois apresentar uma réplica",
                            "Concordar totalmente e encerrar o debate",
                            "Ignorar o que o outro acabou de dizer",
                            "Pedir para mudar de assunto imediatamente",
                        ],
                        "correct_index": 0,
                        "explanation": "Essa é a dupla concessão + contra-argumento: 'fair point' valida o argumento adversário e o 'but' anuncia que a resposta vem aí. Debater sem ceder terreno soa como ataque; ceder sem 'but' é capitulação.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "'I'm not sure I agree' é uma forma de...",
                        "choices": [
                            "Discordar com polidez",
                            "Expressar certeza absoluta",
                            "Pedir confirmação do que ouviu",
                            "Fazer um elogio disfarçado",
                        ],
                        "correct_index": 0,
                        "explanation": "É discordância embrulhada em dúvida: 'não tenho certeza se concordo' soa muito mais suave que 'you're wrong'. Em debate, o objetivo é vencer o argumento, não a pessoa — e a forma é metade da estratégia.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "___ you think remote work saves companies money? (perguntando a opinião de alguém)",
                        "correct": "Don't",
                        "explanation": "'Don't you think...?' é o convite ao debate: a pergunta negativa pressupõe concordância e puxa o outro para a discussão. Assim se abre uma discordância sem agressividade.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: got / you've / a / there / point",
                        "correct": "You've got a point there.",
                        "explanation": "A rendição elegante: 'You've got a point there' admite que o argumento adversário tocou em algo verdadeiro — e pode até virar a chave para um acordo, como no diálogo com o modelo híbrido.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "I see what you mean, but it depends.",
                        "explanation": "Outra dupla clássica: 'I see what you mean' mostra que você entendeu o argumento, e o 'but it depends' reabre a discussão com nuance. Debate adulto em nove palavras.",
                    },
                ],
            },
        ],
    },
]


from .advanced_extension import add_b2_review  # noqa: E402

add_b2_review(UNITS)
