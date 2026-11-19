"""Conteúdo do nível A2 — A2 Everyday English.

Narrativas no passado, presente contínuo, planos futuros, comparações,
quantificadores, pedidos educados e introdução ao present perfect.
"""

COURSE = {
    "slug": "a2-everyday-english",
    "title": "A2 Everyday English",
    "description": (
        "Consolide o básico e ganhe independência: passado, presente contínuo, "
        "planos futuros, comparações e present perfect para conversar sobre a vida real."
    ),
    "level": "A2",
}

UNITS = [
    {
        "title": "The Past Is a Story",
        "position": 1,
        "description": (
            "Aprenda a contar o que aconteceu: verbos regulares e irregulares no passado, "
            "perguntas com did e uma conversa real sobre o fim de semana."
        ),
        "lessons": [
            {
                "slug": "a2-past-regular",
                "title": "Life Before Now",
                "skill": "Grammar",
                "summary": (
                    "Aprenda a formar o passado com verbos regulares (-ed) e as regras de "
                    "ortografia: studied, stopped e played."
                ),
                "theory": (
                    "O Simple Past é o tempo que usamos para contar coisas que já aconteceram "
                    "e terminaram — ontem, semana passada, em 2019. Com verbos regulares, a "
                    "formação é simples: acrescente -ed ao verbo. I work → I worked, we play → "
                    "we played. Só a ortografia pede atenção: verbos terminados em consoante + y "
                    "trocamos o y por ied (study → studied), e verbos curtos com uma vogal entre "
                    "consoantes dobram a última consoante (stop → stopped). Cuidado com um erro "
                    "comum: no português dizemos 'eu estudei ontem', e o 'estudei' já marca o "
                    "passado; em inglês, se a ação terminou, o verbo precisa do -ed. Na negativa "
                    "e na pergunta, o -ed sai e entra o did, como você verá nas próximas lições."
                ),
                "example": "I studied English every day last year. We watched a movie last night.",
                "key_points": [
                    "Verb + ed = passado (worked, played)",
                    "consoante + y → ied (study → studied)",
                    "vogal curta dobra a consoante (stop → stopped)",
                    "y depois de vogal não muda (play → played)",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Qual é a forma correta de 'study' no Simple Past?",
                        "choices": ["studied", "studyed", "studyd", "studies"],
                        "correct_index": 0,
                        "explanation": (
                            "Verbos terminados em consoante + y trocam o y por i e ganham ed: "
                            "study → studied. 'studies' é o presente (3ª pessoa). Se o y vem "
                            "depois de vogal, como em play, nada muda: played."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "They ___ (to play) soccer last Saturday.",
                        "correct": "played",
                        "explanation": (
                            "play termina em y depois de vogal (a), então o y fica: play → played. "
                            "A regra do ied só vale para consoante + y, como study → studied. "
                            "last Saturday confirma o tempo passado."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Complete: The bus ___ at the corner this morning.",
                        "choices": ["stopped", "stoped", "stops", "stoping"],
                        "correct_index": 0,
                        "explanation": (
                            "stop é curto, com uma vogal entre consoantes, então dobra o p antes "
                            "do ed: stopped. 'stoped' com uma só letra mudaria o som da vogal — "
                            "por isso a grafia dobra a consoante."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: a movie / we / watched / last night",
                        "correct": "We watched a movie last night.",
                        "explanation": (
                            "A ordem natural em inglês é sujeito + verbo + complemento + tempo: "
                            "We (sujeito) watched (passado de watch) a movie (o quê) last night "
                            "(quando). A expressão de tempo costuma fechar a frase."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "I worked all weekend on the project.",
                        "explanation": (
                            "worked é o passado regular de work: work + ed. Como a ação terminou "
                            "(all weekend), o verbo vai ao passado — o -ed é a marca disso."
                        ),
                    },
                ],
            },
            {
                "slug": "a2-past-irregular",
                "title": "Irregular Heroes",
                "skill": "Grammar",
                "summary": (
                    "Domine os verbos irregulares essenciais — went, had, saw, made, took — "
                    "para contar histórias reais."
                ),
                "theory": (
                    "Muitos verbos ingleses são 'rebeldes': em vez de ganharem -ed, eles mudam "
                    "completamente de forma no passado. São os famosos verbos irregulares, como "
                    "go → went, have → had, see → saw, make → made e take → took. Não existe "
                    "regra que os explique — a boa notícia é que os mais importantes aparecem o "
                    "tempo todo em histórias, então você os memoriza com o uso. Um alerta para "
                    "brasileiros: cuidado com 'goed' e 'taked', que não existem; e não confunda "
                    "o passado (went, saw) com o particípio (gone, seen), usado em outros tempos "
                    "verbais. A dica de ouro é aprender cada irregular como um par sempre junto, "
                    "como uma música: 'go — went', 'have — had', 'see — saw'."
                ),
                "example": "I went to the beach and saw my friends. We had a great time.",
                "key_points": [
                    "go → went",
                    "have → had / see → saw",
                    "make → made / take → took",
                    "Aprenda em pares: go — went",
                    "gone/seen são particípios, não passado",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Qual é o Simple Past de 'go'?",
                        "choices": ["went", "goed", "gone", "goes"],
                        "correct_index": 0,
                        "explanation": (
                            "go é irregular: seu passado é went, sem -ed. 'goed' não existe, "
                            "embora seja a tentativa mais comum de quem está aprendendo. gone é "
                            "o particípio, usado com have/has."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "She ___ (to have) a great time at the party.",
                        "correct": "had",
                        "explanation": (
                            "have é irregular: have → had. É o mesmo verbo de 'I have a car', "
                            "mas no passado. O contexto (at the party) e o sentido da frase "
                            "pedem a forma had."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "He ___ (to take) the bus to work yesterday.",
                        "correct": "took",
                        "explanation": (
                            "take → took, outro par irregular essencial. Cuidado com 'taked' "
                            "(não existe) e com taken, que é o particípio usado no Present "
                            "Perfect, não o passado simples."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: to the store / I / went / after class",
                        "correct": "I went to the store after class.",
                        "explanation": (
                            "Em inglês, o sujeito vem primeiro e as expressões de lugar e tempo "
                            "fecham a frase: I went (sujeito + verbo) to the store (lugar) "
                            "after class (tempo)."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "We saw a movie last Friday.",
                        "explanation": (
                            "saw é o passado irregular de see. A frase fala de last Friday, um "
                            "tempo já terminado, então o verbo vai para o passado — saw, e não "
                            "see ou seen."
                        ),
                    },
                ],
            },
            {
                "slug": "a2-past-questions",
                "title": "Did You...?",
                "skill": "Grammar",
                "summary": (
                    "Faça perguntas e negativas no passado com did/didn't e use expressões como "
                    "yesterday, last night e two days ago."
                ),
                "theory": (
                    "Para perguntar ou negar no passado, o inglês usa uma ajudinha: o passado "
                    "vai para o verbo auxiliar did (ou didn't), e o verbo principal volta à "
                    "forma base, sem -ed e sem forma irregular. Ou seja: 'Did you watch the "
                    "game?' e 'They didn't go to the party'. Aqui mora o erro mais comum dos "
                    "brasileiros: dizemos 'Did you went?' porque no português 'você foi' sempre "
                    "marca o passado no verbo. Em inglês, o passado aparece uma única vez, no "
                    "did — o verbo principal fica 'limpo'. Para responder, use 'Yes, I did' ou "
                    "'No, I didn't'. Combine com yesterday, last night, two days ago e last "
                    "week, que sinalizam passado."
                ),
                "example": "Did you watch the game yesterday? No, I didn't. I worked late.",
                "key_points": [
                    "Did + sujeito + verbo base?",
                    "didn't + verbo base (sem -ed)",
                    "Yes, I did. / No, I didn't.",
                    "yesterday, last night, two days ago",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Complete: ___ you watch the game yesterday?",
                        "choices": ["Did", "Do", "Does", "Was"],
                        "correct_index": 0,
                        "explanation": (
                            "Para perguntar sobre o passado, use did + sujeito + verbo base: Did "
                            "you watch...? Do/does são do presente, e was não forma perguntas "
                            "com verbos de ação."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "She didn't ___ (to watch) TV last night.",
                        "correct": "watch",
                        "explanation": (
                            "Depois de didn't, o verbo volta à forma base, sem -ed: didn't "
                            "watch. O passado já está marcado pelo didn't — o verbo não precisa "
                            "(nem pode) marcá-lo de novo."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual pergunta está correta em inglês?",
                        "choices": [
                            "Did you went home?",
                            "Did you go home?",
                            "Did you going home?",
                            "You did go home?",
                        ],
                        "correct_index": 1,
                        "explanation": (
                            "A regra é uma só: o passado aparece apenas no did; o verbo "
                            "principal fica na base. 'Did you went' repete o passado duas vezes, "
                            "erro clássico de quem traduz 'você foi' palavra por palavra."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: your mom / did / you / call / yesterday",
                        "correct": "Did you call your mom yesterday?",
                        "explanation": (
                            "A pergunta no passado segue a ordem Did + sujeito + verbo + "
                            "complemento: Did you call your mom yesterday? Note call na forma "
                            "base e o yesterday fechando a frase."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "I didn't work last Saturday.",
                        "explanation": (
                            "didn't work usa o verbo na base: o passado está todo no didn't. "
                            "last Saturday confirma a ação terminada, e a negativa é simples: "
                            "didn't + verbo puro."
                        ),
                    },
                ],
            },
            {
                "slug": "a2-weekend-story",
                "title": "How Was Your Weekend?",
                "skill": "Conversation",
                "summary": (
                    "Pratique uma conversa real sobre o fim de semana, com perguntas no passado "
                    "e reações naturais como 'That sounds fun!'."
                ),
                "theory": (
                    "Hora de juntar as peças! Nesta conversa você vai ouvir pessoas perguntando "
                    "sobre o fim de semana — uma das situações mais comuns do dia a dia em "
                    "inglês. As perguntas-chave são 'How was your weekend?' e 'What did you "
                    "do?'. Repare que a resposta usa o Simple Past para contar as ações: 'I went "
                    "to the beach', 'We made a cake'. Não traduza 'eu fui' palavra por palavra "
                    "com 'I was': 'was' é o passado de to be (estar/ser), enquanto 'fui' costuma "
                    "ser went. E para mostrar interesse, o nativo responde com pequenos "
                    "comentários: 'Nice!', 'That sounds fun!'. Deixe a conversa fluir e treine "
                    "contando também o seu fim de semana."
                ),
                "example": "How was your weekend? It was great!",
                "key_points": [
                    "How was your weekend?",
                    "What did you do?",
                    "I went to the beach.",
                    "Nice! / That sounds fun!",
                ],
                "dialogue": [
                    {"speaker": "Ana", "line": "Hi, Mike! How was your weekend?"},
                    {"speaker": "Mike", "line": "It was great, thanks! I went to the beach with some friends."},
                    {"speaker": "Ana", "line": "Nice! What did you do there?"},
                    {"speaker": "Mike", "line": "We played volleyball and had a barbecue. How about you?"},
                    {"speaker": "Ana", "line": "I visited my grandmother on Saturday. We made a chocolate cake together."},
                    {"speaker": "Mike", "line": "That sounds fun! Did you do anything else?"},
                    {"speaker": "Ana", "line": "Not much. On Sunday I just watched a series and rested."},
                    {"speaker": "Mike", "line": "Sounds relaxing! We should do something together next weekend."},
                    {"speaker": "Ana", "line": "Definitely! Let's talk during the week."},
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Segundo o diálogo, o que Mike fez no fim de semana?",
                        "choices": [
                            "Foi à praia com amigos",
                            "Visitou a avó",
                            "Ficou em casa descansando",
                            "Fez um bolo de chocolate",
                        ],
                        "correct_index": 0,
                        "explanation": (
                            "Mike diz 'I went to the beach with some friends' — went é o passado "
                            "irregular de go. As outras opções misturam as atividades de Ana no "
                            "diálogo, um exercício clássico de compreensão auditiva."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "O que Ana e a avó fizeram juntas no sábado?",
                        "choices": [
                            "Fizeram um bolo de chocolate",
                            "Assistiram a uma série",
                            "Jogaram vôlei",
                            "Foram à praia",
                        ],
                        "correct_index": 0,
                        "explanation": (
                            "Ana conta 'We made a chocolate cake together' — made é o passado "
                            "irregular de make. A série e o descanso foram no domingo, sem a "
                            "avó — leia com atenção."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "How ___ (to be) your weekend?",
                        "correct": "was",
                        "explanation": (
                            "A pergunta 'How was your weekend?' usa o passado de to be: was. "
                            "Como weekend é singular, a forma correta é was, e não were. É a "
                            "pergunta que abre qualquer conversa de segunda-feira."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: with my sister / I / went / to the beach",
                        "correct": "I went to the beach with my sister.",
                        "explanation": (
                            "Conte a história na ordem inglesa: I (sujeito) went (passado de go) "
                            "to the beach (lugar) with my sister (acompanhia) — sujeito, verbo, "
                            "lugar e por último as pessoas."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "We played volleyball all afternoon.",
                        "explanation": (
                            "played é o passado regular de play (o y depois de vogal não muda). "
                            "all afternoon indica tempo passado e terminado, por isso o verbo "
                            "vai ao passado."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "title": "Right Now & Big Plans",
        "position": 2,
        "description": (
            "Fale sobre o que está acontecendo agora e sobre o futuro: present continuous, "
            "going to e will, mais um diálogo combinando planos."
        ),
        "lessons": [
            {
                "slug": "a2-present-continuous",
                "title": "Happening Now",
                "skill": "Grammar",
                "summary": (
                    "Descreva o que está acontecendo agora com am/is/are + -ing e acerte a "
                    "ortografia de running e making."
                ),
                "theory": (
                    "O Present Continuous descreve ações que estão acontecendo agora, neste "
                    "momento — 'I'm studying English' (estou estudando inglês). A formação é "
                    "com o verbo to be + verbo com -ing: I am working, she is running, they are "
                    "making dinner. Aqui a ortografia pede cuidado: verbos terminados em e mudo "
                    "perdem o e antes do -ing (make → making), e verbos curtos dobram a última "
                    "consoante (run → running, sit → sitting). O erro clássico do brasileiro é "
                    "esquecer o to be e dizer só 'I working now', porque no português 'estou "
                    "trabalhando' já traz o 'estou' embutido. Em inglês, o am/is/are é "
                    "obrigatório — sem ele, a frase fica quebrada. Use com now, right now e at "
                    "the moment."
                ),
                "example": "She is running in the park right now. They are making dinner.",
                "key_points": [
                    "am/is/are + verbo-ing",
                    "run → running / make → making",
                    "now, right now, at the moment",
                    "O to be é obrigatório",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Complete: Look! The dog ___ in the garden.",
                        "choices": ["is running", "runs", "ran", "is sleep"],
                        "correct_index": 0,
                        "explanation": (
                            "A ação está acontecendo agora — o 'Look!' sinaliza isso — então "
                            "usamos o Present Continuous: is + running. runs descreve hábito, e "
                            "ran é passado simples."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "They ___ (to make) dinner right now.",
                        "correct": "are making",
                        "explanation": (
                            "Present Continuous = to be + -ing: they are making. E repare na "
                            "ortografia: make perde o e final antes do ing, dando making, e não "
                            "makeing."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual é a forma correta de 'make' no -ing?",
                        "choices": ["making", "makeing", "makking", "maked"],
                        "correct_index": 0,
                        "explanation": (
                            "Verbos terminados em e mudo perdem o e antes do -ing: make → "
                            "making. 'makking' dobra a consoante sem necessidade — isso só "
                            "acontece com verbos curtos como run → running."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: TV / my brother / is watching / right now",
                        "correct": "My brother is watching TV right now.",
                        "explanation": (
                            "A ordem do Continuous é sujeito + to be + verbo-ing: My brother is "
                            "watching TV right now. O 'right now' fecha a frase e reforça a "
                            "ideia de agora."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "She is cooking dinner right now.",
                        "explanation": (
                            "She is cooking usa a estrutura completa: to be + verbo-ing. O "
                            "'right now' confirma que a ação está em andamento neste exato "
                            "momento."
                        ),
                    },
                ],
            },
            {
                "slug": "a2-present-vs-continuous",
                "title": "Always vs Right Now",
                "skill": "Grammar",
                "summary": (
                    "Entenda de vez a diferença entre hábitos (Simple Present) e ações do "
                    "momento (Present Continuous)."
                ),
                "theory": (
                    "Os dois presentes do inglês têm funções diferentes, e essa é uma das "
                    "maiores dificuldades para brasileiros. O Simple Present descreve hábitos e "
                    "rotinas — 'I work downtown' (eu trabalho no centro, sempre). Já o Present "
                    "Continuous descreve o momento atual — 'I'm working from home today' (estou "
                    "trabalhando em casa hoje). O erro típico é usar o presente simples para "
                    "falar de agora, porque no português 'eu trabalho agora' pode significar "
                    "exatamente isso; em inglês, essa ideia exige 'I'm working now'. Palavras-"
                    "chave que ajudam: always, usually e every day puxam o Simple Present; now, "
                    "right now e today puxam o Continuous. Compare as duas frases da lição e "
                    "treine esse contraste até ficar automático."
                ),
                "example": "I usually work downtown, but today I'm working from home.",
                "key_points": [
                    "Hábito → Simple Present",
                    "Agora → Present Continuous",
                    "every day vs right now",
                    "I'm working now (não 'I work now')",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Complete: Be quiet! The baby ___ right now.",
                        "choices": ["is sleeping", "sleeps", "slept", "is sleep"],
                        "correct_index": 0,
                        "explanation": (
                            "'Be quiet!' indica ação imediata, acontecendo agora → Present "
                            "Continuous: is sleeping. 'sleeps' seria hábito geral, o que não "
                            "combina com um bebê dormindo neste momento."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Complete: My dad ___ coffee every morning.",
                        "choices": ["drinks", "is drinking", "drank", "drink"],
                        "correct_index": 0,
                        "explanation": (
                            "'every morning' marca rotina, então Simple Present: drinks — a "
                            "terceira pessoa do singular (he/she/it) ganha -s. O Continuous "
                            "aqui diria 'está bebendo agora', sem ideia de hábito."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Right now, I ___ (to study) for the test.",
                        "correct": "am studying",
                        "explanation": (
                            "'Right now' exige Present Continuous: I am studying. O erro típico "
                            "é dizer 'I study now', como no português 'estudo agora' — mas em "
                            "inglês o agora pede am + -ing."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: English / she / is learning / this year",
                        "correct": "She is learning English this year.",
                        "explanation": (
                            "'this year' é um período em curso, então a frase usa o Continuous: "
                            "She is learning English this year. A ordem é sujeito + to be + "
                            "verbo-ing + complemento."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "I'm working from home today.",
                        "explanation": (
                            "I'm working from home today usa o Continuous porque 'today' aqui é "
                            "o dia em curso, diferente do habitual. Se fosse hábito permanente, "
                            "a frase seria 'I work from home'."
                        ),
                    },
                ],
            },
            {
                "slug": "a2-going-to",
                "title": "Plans on the Horizon",
                "skill": "Grammar",
                "summary": "Use going to para falar de planos e intenções já pensados para o futuro.",
                "theory": (
                    "Para falar de planos e intenções já pensados, o inglês usa 'be going to + "
                    "verbo': 'I'm going to visit my cousins next month'. É a ideia de 'vou "
                    "visitar' — algo que você já decidiu antes de falar. A estrutura usa o to "
                    "be (am/is/are) + going to + verbo na forma base. Atenção a um erro comum: "
                    "dizer 'I will going to' ou 'I'm go to' — essas formas não existem. Em "
                    "perguntas, o to be vem primeiro: 'Are you going to travel?'. Nos Estados "
                    "Unidos, você também vai ouvir o informal 'gonna' em conversas rápidas, mas "
                    "na escrita e em contexto formal mantenha 'going to'. Combine com next "
                    "month, tomorrow e next year para situar o plano no futuro."
                ),
                "example": "I'm going to visit my cousins next month.",
                "key_points": [
                    "am/is/are going to + verbo base",
                    "Plano já pensado antes de falar",
                    "Are you going to travel?",
                    "tomorrow, next month, next year",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Complete: We ___ travel to Japan in December.",
                        "choices": ["are going to", "will going to", "go to", "are going"],
                        "correct_index": 0,
                        "explanation": (
                            "A estrutura é am/is/are + going to + verbo base: are going to "
                            "travel. 'will going to' e 'go to' sozinho não existem — o to be é "
                            "obrigatório antes de going to."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "She is ___ to start a new job in July.",
                        "correct": "going",
                        "explanation": (
                            "O plano usa be going to: She is going to start. Depois do to be, "
                            "sempre vem going to + verbo na forma base — 'is go to start' não "
                            "existe."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual frase expressa um plano já pensado (intenção)?",
                        "choices": [
                            "I'm going to buy a car next year.",
                            "I buy a car next year.",
                            "I buying a car next year.",
                            "I'm buy a car next year.",
                        ],
                        "correct_index": 0,
                        "explanation": (
                            "A única frase com a estrutura correta é 'I'm going to buy a car "
                            "next year' (am + going to + verbo base). As demais quebram a "
                            "formação: falta o to be, o going to ou a forma base."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: visit / we're going to / our grandparents / on Sunday",
                        "correct": "We're going to visit our grandparents on Sunday.",
                        "explanation": (
                            "A ordem é sujeito + to be + going to + verbo + complemento: We're "
                            "going to visit our grandparents on Sunday. O dia (on Sunday) fecha "
                            "a frase."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "They are going to move to Canada.",
                        "explanation": (
                            "They are going to move anuncia um plano já pensado: are + going to "
                            "+ move (verbo base). 'move to Canada' mostra o destino com a "
                            "preposição to."
                        ),
                    },
                ],
            },
            {
                "slug": "a2-will-decisions",
                "title": "Decided on the Spot",
                "skill": "Grammar",
                "summary": "Use will para decisões espontâneas, promessas e ofertas feitas na hora da conversa.",
                "theory": (
                    "Se 'going to' é para planos pensados antes, 'will' brilha quando a decisão "
                    "acontece na hora da fala: o telefone toca e você diz 'I'll get it!'. "
                    "Formamos o futuro com will + verbo na forma base — 'I'll help you' (I will "
                    "help you). Além de decisões espontâneas, will também marca promessas ('I "
                    "won't tell anyone') e ofertas ('I'll carry that bag for you'). O erro "
                    "típico do brasileiro é misturar as estruturas: 'I will going' e 'I will to "
                    "help' não existem — depois do will, o verbo vem puro, sem to e sem -ing. "
                    "Na negativa, will not vira won't. Uma dica prática: se você já tinha o "
                    "plano, use going to; se acabou de decidir ao falar, use will."
                ),
                "example": "The phone is ringing. I'll get it! Don't worry, I'll help you.",
                "key_points": [
                    "will + verbo base",
                    "Decisão na hora: I'll get it!",
                    "Promessa: I won't tell anyone.",
                    "won't = will not",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "O telefone está tocando e você decide atender na hora. O que você diz?",
                        "choices": ["I'll answer it!", "I answer it.", "I will answering it.", "I'm going answer it."],
                        "correct_index": 0,
                        "explanation": (
                            "A decisão é instantânea, então will: I'll answer it! As outras "
                            "opções quebram a formação: falta o will, ou o verbo depois dele "
                            "não está na forma base."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "It's cold in here. I ___ close the window. (decisão na hora)",
                        "correct": "will",
                        "explanation": (
                            "A janela está aberta agora e a decisão de fechá-la acontece no "
                            "momento da fala: I will close. will + verbo base, sem to — 'will "
                            "to close' não existe."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual é uma promessa correta com will?",
                        "choices": [
                            "I won't tell anyone.",
                            "I don't tell anyone.",
                            "I not will tell anyone.",
                            "I won't telling anyone.",
                        ],
                        "correct_index": 0,
                        "explanation": (
                            "Promessa em inglês usa will; na negativa, will not vira won't: I "
                            "won't tell anyone. As outras opções quebram a formação ('I not "
                            "will', 'won't + -ing')."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: tonight / you / I'll / call",
                        "correct": "I'll call you tonight.",
                        "explanation": (
                            "Promessa feita na hora: I'll call you tonight. A ordem é sujeito + "
                            "will (abreviado em I'll) + verbo + complemento, e tonight fecha a "
                            "frase."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "I will help you move tomorrow.",
                        "explanation": (
                            "I will help you move tomorrow é uma oferta: will + help (forma "
                            "base) + you + move. Note a forma completa will, comum quando "
                            "queremos enfatizar a promessa."
                        ),
                    },
                ],
            },
            {
                "slug": "a2-making-plans",
                "title": "Let's Make Plans",
                "skill": "Conversation",
                "summary": (
                    "Viva um diálogo combinando um encontro: dias com on, horas com at e frases "
                    "prontas para marcar."
                ),
                "theory": (
                    "Combinar um encontro em inglês segue um roteiro bem previsível, e nesta "
                    "lição você vai dominá-lo. Comece perguntando se a pessoa está livre: 'Are "
                    "you free on Friday?' ou 'Do you want to go?'. Combine os detalhes com "
                    "'What time does it start?' e 'Where should we meet?'. Note duas preposições "
                    "essenciais: on com dias (on Friday, on Sunday) e at com horas e lugares "
                    "específicos (at seven, at the coffee shop). O erro comum do brasileiro é "
                    "dizer 'in Friday' por influência do 'na sexta' — com dias da semana, "
                    "sempre on. Para fechar, confirme com 'See you on Friday!'. Observe no "
                    "diálogo como as perguntas curtas mantêm a conversa leve e natural."
                ),
                "example": "Are you free on Friday? Let's meet at seven at the coffee shop.",
                "key_points": [
                    "Are you free on Friday?",
                    "on + dias / at + horas e lugares",
                    "Where should we meet?",
                    "See you on Friday!",
                ],
                "dialogue": [
                    {"speaker": "Lucas", "line": "Hey Emma! Are you free on Friday night?"},
                    {"speaker": "Emma", "line": "Let me check... I think so. Why?"},
                    {"speaker": "Lucas", "line": "There's a new action movie at the Regal Cinema. Do you want to go?"},
                    {"speaker": "Emma", "line": "Sounds great! What time does it start?"},
                    {"speaker": "Lucas", "line": "At eight, but let's meet at seven at the coffee shop next door."},
                    {"speaker": "Emma", "line": "Perfect. Should I buy the tickets online?"},
                    {"speaker": "Lucas", "line": "Good idea. I'm going to get popcorn for us."},
                    {"speaker": "Emma", "line": "Deal! See you on Friday at seven."},
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Segundo o diálogo, a que horas o filme começa?",
                        "choices": ["Às oito", "Às sete", "Às nove", "Às dez"],
                        "correct_index": 0,
                        "explanation": (
                            "Lucas diz que o filme começa 'At eight'. O encontro é às sete (at "
                            "seven) na cafeteria — muitos respondem sete por lerem rápido, mas "
                            "o filme em si começa às oito."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Onde Lucas sugere se encontrarem antes do filme?",
                        "choices": [
                            "Na cafeteria ao lado do cinema",
                            "Em frente ao cinema",
                            "Na casa de Emma",
                            "No shopping do centro",
                        ],
                        "correct_index": 0,
                        "explanation": (
                            "Lucas sugere 'let's meet at seven at the coffee shop next door' — "
                            "ao lado do cinema. Note at para lugar específico: at the coffee "
                            "shop."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Do you want ___ go to the movies with us? (preposição)",
                        "correct": "to",
                        "explanation": (
                            "want sempre pede to + verbo: Do you want to go? 'Do you want go' é "
                            "o erro clássico de quem traduz 'quer ir' palavra por palavra."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: the coffee shop / let's meet / at / on Friday / at seven",
                        "correct": "Let's meet at the coffee shop on Friday at seven.",
                        "explanation": (
                            "Let's (vamos) abre a frase, seguida do verbo base meet. Note as "
                            "preposições: on + dia (on Friday) e at + hora/lugar (at seven, at "
                            "the coffee shop)."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "Are you free on Friday night?",
                        "explanation": (
                            "Are you free on Friday night? é a pergunta clássica para combinar "
                            "algo. Note on Friday: com dias da semana, a preposição é sempre "
                            "on, nunca in."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "title": "Comparing Everything",
        "position": 3,
        "description": (
            "Compare pessoas, lugares e coisas com comparativos e superlativos, use some, any, "
            "much e many e faça compras em inglês."
        ),
        "lessons": [
            {
                "slug": "a2-comparatives",
                "title": "Bigger, Better, Faster",
                "skill": "Grammar",
                "summary": "Compare duas coisas com -er + than, more + than e os irregulares better e worse.",
                "theory": (
                    "Para comparar duas coisas, o inglês tem duas receitas. Adjetivos curtos "
                    "ganham -er + than: 'Sao Paulo is bigger than Rio', 'My car is faster than "
                    "yours'. Adjetivos longos (três sílabas ou mais) ficam com more + adjetivo + "
                    "than: 'more expensive than', 'more interesting than'. Os irregulares mais "
                    "famosos são good → better e bad → worse. Dois erros clássicos de "
                    "brasileiro: dizer 'more big' (misturando as receitas) e esquecer o than no "
                    "final — 'bigger than mine', nunca 'bigger mine'. Também não use more com "
                    "adjetivo curto: cheaper, e não 'more cheap'. Compare coisas do seu dia a "
                    "dia — filmes, cidades, comidas — para fixar o padrão."
                ),
                "example": "This phone is cheaper than that one, but it's better.",
                "key_points": [
                    "curto: adj + er + than",
                    "longo: more + adj + than",
                    "good → better / bad → worse",
                    "than é obrigatório na comparação",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Complete: São Paulo is ___ Rio.",
                        "choices": ["bigger than", "more big than", "biggest than", "big than"],
                        "correct_index": 0,
                        "explanation": (
                            "big é adjetivo curto, então compara com -er + than: bigger than. "
                            "'more big' mistura as duas receitas — more é só para adjetivos "
                            "longos, como more expensive."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "My new car is ___ (fast) than my old one.",
                        "correct": "faster",
                        "explanation": (
                            "fast é curto e de uma sílaba: fast + er = faster. E a comparação "
                            "completa exige than depois: faster than my old one."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual é o comparativo de 'good'?",
                        "choices": ["better", "gooder", "more good", "best"],
                        "correct_index": 0,
                        "explanation": (
                            "good é irregular: good → better no comparativo. 'gooder' e 'more "
                            "good' não existem. 'best' é o superlativo (the best), assunto da "
                            "próxima lição."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: this book / more interesting / is / than / that one",
                        "correct": "This book is more interesting than that one.",
                        "explanation": (
                            "interesting é adjetivo longo, então usa more + interesting + than: "
                            "This book is more interesting than that one. O sujeito abre a "
                            "frase e o than conecta as duas coisas."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "My sister is taller than me.",
                        "explanation": (
                            "taller than é comparativo curto: tall + er + than. A frase "
                            "compara duas pessoas — minha irmã e eu — com a estrutura clássica "
                            "de comparação."
                        ),
                    },
                ],
            },
            {
                "slug": "a2-superlatives",
                "title": "The Best of All",
                "skill": "Grammar",
                "summary": "Coroa o campeão do grupo com superlativos: the -est, the most, the best e the worst.",
                "theory": (
                    "Quando algo é o campeão de um grupo — o maior, o melhor, o pior — entra o "
                    "superlativo. A estrutura é the + adjetivo com -est para adjetivos curtos: "
                    "'the biggest mall in the city', 'the tallest player on the team'. "
                    "Adjetivos longos usam the most: 'the most beautiful beach in Brazil'. Os "
                    "irregulares estrelas são good → the best e bad → the worst. Note que o the "
                    "é obrigatório em inglês, diferente do português, que usa apenas 'o/a "
                    "maior' — o erro típico é escrever 'She is youngest' sem the. Depois do "
                    "superlativo, costumamos dizer o grupo: 'in town', 'in the class', 'on the "
                    "team'. Lembre-se: comparativo compara dois; superlativo coroa um entre "
                    "todos."
                ),
                "example": "It's the best restaurant in town.",
                "key_points": [
                    "the + adj + est",
                    "the most + adjetivo longo",
                    "the best / the worst",
                    "in town, in the class, on the team",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Complete: That was ___ movie of the year!",
                        "choices": ["the best", "the better", "best", "the most good"],
                        "correct_index": 0,
                        "explanation": (
                            "good é irregular no superlativo: the best. E não esqueça do the: "
                            "superlativo em inglês sempre vem com the na frente. 'the better' é "
                            "comparativo, para duas coisas."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "This is ___ (big) mall in the city. (superlativo)",
                        "correct": "the biggest",
                        "explanation": (
                            "big é curto: the + big + est = the biggest mall in the city. O the "
                            "é obrigatório, e o 'in the city' mostra o grupo onde o shopping é "
                            "campeão."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual frase com superlativo está correta?",
                        "choices": [
                            "She is the youngest in the class.",
                            "She is the most young in the class.",
                            "She is youngest in the class.",
                            "She is the younger in the class.",
                        ],
                        "correct_index": 0,
                        "explanation": (
                            "A formação correta é the + adjetivo curto + est: the youngest. "
                            "'the most young' é errado (young é curto), 'youngest' sem the "
                            "está incompleto e 'the younger' é comparativo."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: the worst / in town / that pizza place / is",
                        "correct": "That pizza place is the worst in town.",
                        "explanation": (
                            "bad é irregular: bad → the worst. A frase coroa a pior pizzaria "
                            "entre todas da cidade: That pizza place is the worst in town."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "He is the tallest player on the team.",
                        "explanation": (
                            "the tallest player on the team usa the + tall + est. Note o grupo "
                            "depois: on the team — é entre os jogadores do time que ele é o "
                            "mais alto."
                        ),
                    },
                ],
            },
            {
                "slug": "a2-quantifiers",
                "title": "Some, Any, Much & Many",
                "skill": "Grammar",
                "summary": (
                    "Use some, any, much, many e a lot of com contáveis e incontáveis — sem "
                    "dizer 'informations'."
                ),
                "theory": (
                    "Em inglês, os substantivos se dividem em contáveis (apple, book) e "
                    "incontáveis (money, water, information) — e isso muda as palavras que "
                    "usamos. Use many + plural de contáveis ('many books') e much + incontáveis "
                    "('much time'). Some aparece em frases afirmativas ('I have some friends'), "
                    "e any em negativas e perguntas ('Do we have any milk?'). A lot of funciona "
                    "com os dois tipos e é a escolha segura do dia a dia. Aqui vai o erro mais "
                    "famoso dos brasileiros: palavras como information, advice e news são "
                    "incontáveis em inglês, então 'informations' e 'advices' não existem — "
                    "diga 'some information', 'a piece of advice'. No singular, use 'there "
                    "isn't any'; no plural, 'there aren't any'."
                ),
                "example": "I don't have any money, but I have some good friends.",
                "key_points": [
                    "many + contáveis no plural",
                    "much + incontáveis",
                    "some (afirmativas) / any (negativas e perguntas)",
                    "information e advice são incontáveis",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Complete: How ___ sugar do you want in your coffee?",
                        "choices": ["much", "many", "some", "any"],
                        "correct_index": 0,
                        "explanation": (
                            "sugar é incontável, então a pergunta usa much: How much sugar? "
                            "many é para contáveis no plural, como many apples."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "I'm hungry, but there isn't ___ food in the kitchen. (some ou any?)",
                        "correct": "any",
                        "explanation": (
                            "Negativa + substantivo → any: there isn't any food. Se a frase "
                            "fosse afirmativa, some seria a escolha: there is some food."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual frase está correta em inglês?",
                        "choices": [
                            "I need some information.",
                            "I need some informations.",
                            "I need many information.",
                            "I need a informations.",
                        ],
                        "correct_index": 0,
                        "explanation": (
                            "information é incontável em inglês: some information. "
                            "'informations' e 'advices' são erros clássicos de brasileiros — "
                            "essas palavras nunca vão para o plural."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "How ___ time do we have before the class? (much ou many?)",
                        "correct": "much",
                        "explanation": (
                            "time, no sentido de tempo, é incontável: How much time? Compare "
                            "com How many minutes? — minutes é contável, então leva many."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: how many / do / you / books / have",
                        "correct": "How many books do you have?",
                        "explanation": (
                            "A pergunta com contáveis usa many + plural: How many books do you "
                            "have? Note a ordem: How many + substantivo + do + sujeito + verbo."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "We don't have much time today.",
                        "explanation": (
                            "time é incontável, então a negativa usa much: don't have much "
                            "time. Compare: don't have many books (contável, no plural)."
                        ),
                    },
                ],
            },
            {
                "slug": "a2-shopping",
                "title": "Shopping Spree",
                "skill": "Conversation",
                "summary": (
                    "Compre com confiança: preços, tamanhos, provador e pagamento em um diálogo "
                    "real de loja."
                ),
                "theory": (
                    "Fazer compras em inglês tem frases prontas que fazem toda a diferença. "
                    "Para perguntar o preço: 'How much is this?' ou 'How much are these?'. Para "
                    "provar roupa: 'Can I try it on?' e para pedir tamanho: 'Do you have it in "
                    "a medium / a large?'. No caixa, ouça 'How would you like to pay?' e "
                    "responda 'By credit card' ou 'In cash'. O erro típico é traduzir 'vestir' "
                    "como 'dress' na hora de provar — em loja, a expressão certa é try on. Se "
                    "algo não serviu, 'It's too tight' (apertado) ou 'It's too loose' (largo) "
                    "resolvem rapidinho. Repare no diálogo como Laura negocia tamanho, preço e "
                    "pagamento com frases curtas e educadas — decorar esse roteiro deixa "
                    "qualquer compra tranquila."
                ),
                "example": "Excuse me, how much is this sweater? Do you have it in a medium?",
                "key_points": [
                    "How much is this? / How much are these?",
                    "Do you have it in a medium?",
                    "Can I try it on?",
                    "How would you like to pay?",
                ],
                "dialogue": [
                    {"speaker": "Laura", "line": "Excuse me, how much is this sweater?"},
                    {"speaker": "Ben", "line": "It's forty dollars. Would you like to try it on?"},
                    {"speaker": "Laura", "line": "Yes, please. Do you have it in a medium?"},
                    {"speaker": "Ben", "line": "Sure. Here you go. The fitting rooms are over there."},
                    {"speaker": "Laura", "line": "It's a little tight. Do you have a large?"},
                    {"speaker": "Ben", "line": "Of course. This large is very comfortable."},
                    {"speaker": "Laura", "line": "It fits perfectly! I'll take it."},
                    {"speaker": "Ben", "line": "Great choice! How would you like to pay?"},
                    {"speaker": "Laura", "line": "By credit card, please. Can I get a bag too?"},
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Segundo o diálogo, quanto custa o suéter?",
                        "choices": [
                            "Quarenta dólares",
                            "Quatorze dólares",
                            "Cinquenta dólares",
                            "Quatro dólares",
                        ],
                        "correct_index": 0,
                        "explanation": (
                            "Ben responde 'It's forty dollars'. Cuidado para não confundir "
                            "forty (40) com fourteen (14) na escuta — o 'r' mais forte e a "
                            "sílaba tônica diferente ajudam a distinguir."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Por que Laura pede um tamanho maior?",
                        "choices": [
                            "Porque o M ficou apertado",
                            "Porque o M ficou largo",
                            "Porque não gostou da cor",
                            "Porque o preço era alto",
                        ],
                        "correct_index": 0,
                        "explanation": (
                            "Laura diz 'It's a little tight' — ficou um pouco apertada — e "
                            "então pede um large. tight = apertado; loose = largo. São opostos "
                            "muito úteis em loja."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Can I try ___ this jacket, please? (preposição)",
                        "correct": "on",
                        "explanation": (
                            "try on = provar roupa. A preposição on completa a expressão: Can I "
                            "try this jacket on? Sem o on, try significa apenas 'tentar'."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: how much / are / these shoes",
                        "correct": "How much are these shoes?",
                        "explanation": (
                            "Com plural, o verbo vai para are: How much are these shoes? No "
                            "singular, seria How much is this sweater? — is com this, are com "
                            "these."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "I'll take the blue one.",
                        "explanation": (
                            "I'll take the blue one é a frase para fechar a compra: 'I'll take "
                            "it' = vou levar. O one substitui o substantivo para não repeti-lo."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "title": "Out & About",
        "position": 4,
        "description": (
            "Circule pela cidade em inglês: direções, pedidos educados com can e could, "
            "conselhos com should e um jantar no restaurante."
        ),
        "lessons": [
            {
                "slug": "a2-directions",
                "title": "Finding Your Way",
                "skill": "Vocabulary",
                "summary": "Aprenda imperativos e o vocabulário de direções para navegar a cidade em inglês.",
                "theory": (
                    "Pedir e dar direções é um vocabulário de sobrevivência. Para dar direções, "
                    "o inglês usa imperativos: 'Go straight for two blocks', 'Turn left at the "
                    "light', 'Turn right after the gas station'. Repare que o verbo vem sozinho "
                    "no início, sem 'you' — igual ao português 'vire à esquerda', que também usa "
                    "imperativo, então esse padrão costuma ser fácil para brasileiros. Para "
                    "localizar lugares, use next to (ao lado de), between (entre), across from "
                    "(em frente a) e behind (atrás de). O erro comum é confundir 'across from' "
                    "(do outro lado da rua, em frente) com 'across' sozinho (atravessar). Se "
                    "estiver perdido, pergunte: 'Excuse me, how do I get to the station?' — e "
                    "confirme com 'Is it far?'."
                ),
                "example": "Go straight for two blocks and turn left. The bank is next to the pharmacy.",
                "key_points": [
                    "Go straight for two blocks.",
                    "Turn left / Turn right",
                    "next to / between / across from",
                    "How do I get to...?",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "O banco está ___ da farmácia e do correio, exatamente entre os dois.",
                        "choices": ["between", "next to", "across from", "behind"],
                        "correct_index": 0,
                        "explanation": (
                            "between indica posição entre duas coisas: between the pharmacy and "
                            "the post office. next to é ao lado, across from é em frente e "
                            "behind é atrás — posições diferentes no espaço."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "___ left at the traffic light. (imperativo com o verbo turn)",
                        "correct": "Turn",
                        "explanation": (
                            "Direções usam imperativo: Turn left at the traffic light. O verbo "
                            "abre a frase, sem sujeito — igual ao português 'vire à esquerda'."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Como se diz 'siga em frente' em inglês?",
                        "choices": ["Go straight", "Go direct", "Follow front", "Go ahead straight"],
                        "correct_index": 0,
                        "explanation": (
                            "siga em frente = Go straight. 'Go direct' e 'Follow front' são "
                            "traduções literais que não existem; straight é a palavra certa "
                            "para 'reto, em linha reta'."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: next to / the pharmacy / the bank / is",
                        "correct": "The bank is next to the pharmacy.",
                        "explanation": (
                            "next to = ao lado de: The bank is next to the pharmacy. A ordem é "
                            "sujeito + is + localização — o padrão para dizer onde algo fica."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "Turn right after the gas station.",
                        "explanation": (
                            "Turn right after the gas station junta dois padrões: imperativo "
                            "(Turn) + after para sequência (depois do posto). 'After' conecta a "
                            "direção a um ponto de referência."
                        ),
                    },
                ],
            },
            {
                "slug": "a2-can-could",
                "title": "Polite Requests",
                "skill": "Grammar",
                "summary": (
                    "Peça coisas com educação com can e could, peça permissão e ofereça com "
                    "would you like."
                ),
                "theory": (
                    "Para pedir coisas com educação, o inglês tem uma escala: 'Can you help "
                    "me?' é direto e informal, enquanto 'Could you help me, please?' é mais "
                    "suave e formal — could é a escolha certa com estranhos e no trabalho. O "
                    "erro típico do brasileiro é fazer o pedido sem sujeito, como no português "
                    "'pode me ajudar?' — em inglês, o 'you' é obrigatório: 'Can/Could you help "
                    "me?'. Para pedir permissão, use 'Can I sit here?' ou, mais elegante, 'May "
                    "I sit here?'. E não confunda pedidos com ofertas: 'Would you like some "
                    "coffee?' é para oferecer algo agora, enquanto 'Do you like coffee?' "
                    "pergunta sobre gosto em geral. Na resposta a um pedido, 'Sure!' e 'Of "
                    "course!' mostram boa vontade na hora."
                ),
                "example": "Could you open the window, please? Would you like some coffee?",
                "key_points": [
                    "Could you...? = pedido educado",
                    "Can I...? = permissão",
                    "Would you like...? = oferta",
                    "Sure! / Of course!",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Qual pedido é o mais educado para pedir ajuda a um estranho?",
                        "choices": [
                            "Could you help me, please?",
                            "Can you help me?",
                            "Help me now.",
                            "You help me?",
                        ],
                        "correct_index": 0,
                        "explanation": (
                            "could deixa o pedido mais suave e educado que can — ideal com "
                            "pessoas que você não conhece bem. O please reforça a cortesia, e "
                            "o you é obrigatório em inglês."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "___ you pass me the salt, please? (mais educado que 'can')",
                        "correct": "Could",
                        "explanation": (
                            "Para pedir com elegância, could é melhor que can: Could you pass "
                            "me the salt? Aqui o could não é passado — é o can em versão "
                            "polida, mais suave e formal."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Complete: ___ you like some coffee? (para oferecer agora)",
                        "choices": ["Would", "Do", "Could", "Will"],
                        "correct_index": 0,
                        "explanation": (
                            "Would you like...? é a oferta clássica: 'gostaria de...?'. 'Do "
                            "you like coffee?' pergunta se você gosta de café em geral, não se "
                            "quer uma xícara agora."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: could you / open / please / the window",
                        "correct": "Could you please open the window?",
                        "explanation": (
                            "Could you please open the window? segue a ordem Could + sujeito + "
                            "(please) + verbo. O please pode vir depois do sujeito ou fechar a "
                            "frase."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "Can I sit here, please?",
                        "explanation": (
                            "Can I sit here? pede permissão. can é informal; em contextos "
                            "formais, 'May I sit here?' é a versão mais elegante — mesma "
                            "função, tom diferente."
                        ),
                    },
                ],
            },
            {
                "slug": "a2-should-advice",
                "title": "Friendly Advice",
                "skill": "Grammar",
                "summary": "Dê e peça conselhos com should/shouldn't + verbo base, sem cair no erro 'should to'.",
                "theory": (
                    "Quando um amigo pede conselho, o inglês usa should: 'You should see a "
                    "doctor', 'You should rest this weekend'. Should expressa recomendação — "
                    "'você deveria' — sem o tom forte de obrigação. A formação é simples: "
                    "should + verbo na forma base, e o mesmo vale para a negativa shouldn't: "
                    "'You shouldn't eat so much candy'. O erro clássico dos brasileiros é "
                    "colocar to depois do should, por analogia com want to — 'should to see' "
                    "não existe. Perguntas de conselho são ótimas para iniciar conversas: "
                    "'What should I do?' e 'Should I call her?'. Combine com conselhos reais do "
                    "dia a dia: drink more water, study a little every day, take a break."
                ),
                "example": "You look tired. You should rest this weekend.",
                "key_points": [
                    "should + verbo base",
                    "shouldn't + verbo base",
                    "'should to see' NÃO existe",
                    "What should I do?",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Seu amigo está com dor de garganta. Qual conselho está correto?",
                        "choices": [
                            "You should see a doctor.",
                            "You should to see a doctor.",
                            "You should seeing a doctor.",
                            "You should saw a doctor.",
                        ],
                        "correct_index": 0,
                        "explanation": (
                            "should + verbo base: You should see a doctor. 'should to see' não "
                            "existe — depois do should nunca vem to, -ing ou forma passada."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "You ___ drink more water every day. (conselho — 'deveria')",
                        "correct": "should",
                        "explanation": (
                            "Conselho afirmativo = should + verbo base: You should drink more "
                            "water. A ideia é recomendação ('você deveria'), não obrigação."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Complete: You ___ eat so much candy before dinner.",
                        "choices": ["shouldn't", "don't should", "should not to", "not should"],
                        "correct_index": 0,
                        "explanation": (
                            "A negativa de should é shouldn't: You shouldn't eat so much "
                            "candy. 'don't should' e 'not should' não existem — should já é o "
                            "próprio auxiliar da frase."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: this weekend / you / rest / should",
                        "correct": "You should rest this weekend.",
                        "explanation": (
                            "You should rest this weekend segue sujeito + should + verbo base. "
                            "Rest fica puro, sem to e sem -ing: 'should to rest' e 'should "
                            "resting' não existem."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "You shouldn't work on weekends.",
                        "explanation": (
                            "shouldn't = should not: You shouldn't work on weekends. É um "
                            "conselho negativo — a recomendação é NÃO fazer algo."
                        ),
                    },
                ],
            },
            {
                "slug": "a2-restaurant",
                "title": "At the Restaurant",
                "skill": "Conversation",
                "summary": "Peça comida com naturalidade: I'll have, I'd like e o pedido da conta no restaurante.",
                "theory": (
                    "No restaurante, um roteiro de frases prontas deixa tudo fácil. O garçom "
                    "abre com 'Are you ready to order?' e você responde com o verbo have: "
                    "'I'll have the chicken' — a forma mais natural de pedir, bem melhor que o "
                    "literal 'I want the chicken'. Para beber, 'I'll have a glass of water' ou "
                    "'I'd like a coffee' funcionam perfeitamente. O erro típico do brasileiro "
                    "é traduzir 'querer' com want, que soa bruto em restaurante; have e would "
                    "like são as escolhas elegantes. No fim, peça a conta com 'Could we have "
                    "the check, please?' — check nos EUA, bill no Reino Unido. Observe no "
                    "diálogo como Rafael pede bebida, prato e informações com educação e "
                    "naturalidade."
                ),
                "example": "I'll have the chicken with rice, please. Could we have the check?",
                "key_points": [
                    "Are you ready to order?",
                    "I'll have the chicken.",
                    "I'd like a coffee.",
                    "Could we have the check, please?",
                ],
                "dialogue": [
                    {"speaker": "Sofia", "line": "Good evening! Welcome to Bella Roma. Table for one?"},
                    {"speaker": "Rafael", "line": "Yes, please. Could I sit near the window?"},
                    {"speaker": "Sofia", "line": "Of course. Here's the menu. Can I get you something to drink?"},
                    {"speaker": "Rafael", "line": "I'll have a glass of orange juice, please."},
                    {"speaker": "Sofia", "line": "Perfect. Are you ready to order, or do you need a minute?"},
                    {"speaker": "Rafael", "line": "I'm ready. I'll have the chicken with rice, please."},
                    {"speaker": "Sofia", "line": "Excellent choice! It comes with a small salad."},
                    {"speaker": "Rafael", "line": "Great. How long does the chicken take?"},
                    {"speaker": "Sofia", "line": "About twenty minutes. I'll bring your juice right away."},
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "O que Rafael pede para beber?",
                        "choices": [
                            "Um copo de suco de laranja",
                            "Uma garrafa de água",
                            "Um refrigerante",
                            "Um chá gelado",
                        ],
                        "correct_index": 0,
                        "explanation": (
                            "Rafael pede 'I'll have a glass of orange juice, please'. I'll have "
                            "é a forma natural de pedir no restaurante — mais elegante que 'I "
                            "want'."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Como Sofia pergunta se Rafael já quer fazer o pedido?",
                        "choices": [
                            "Are you ready to order?",
                            "Do you ready to order?",
                            "Are you ready for order?",
                            "You want order?",
                        ],
                        "correct_index": 0,
                        "explanation": (
                            "'Are you ready to order?' usa to be + adjetivo + to + verbo — a "
                            "construção padrão com ready. 'Do you ready' é tradução literal de "
                            "'você está pronto' e não funciona."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "I'll ___ the chicken with rice, please. (verbo para pedir no restaurante)",
                        "correct": "have",
                        "accepted": ["have", "take"],
                        "explanation": (
                            "No restaurante, pede-se com have: I'll have the chicken. take "
                            "também é aceito ('I'll take the chicken'), mas want soa bruto em "
                            "inglês."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: the check / could we / have / please",
                        "correct": "Could we have the check, please?",
                        "explanation": (
                            "Could we have the check, please? pede a conta com educação: Could "
                            "+ sujeito + verbo. check é a conta nos EUA; no Reino Unido, use "
                            "bill."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "I'd like a glass of water.",
                        "explanation": (
                            "I'd like a glass of water = 'eu gostaria de'. I'd like é a versão "
                            "polida de I want e funciona para qualquer pedido educado em "
                            "restaurante ou café."
                        ),
                    },
                ],
            },
        ],
    },
    {
        "title": "Experiences & Review",
        "position": 5,
        "description": (
            "Conte suas experiências com present perfect, for e since, fale de viagens e revise "
            "tudo o que aprendeu no nível A2."
        ),
        "lessons": [
            {
                "slug": "a2-present-perfect-intro",
                "title": "Already & Yet",
                "skill": "Grammar",
                "summary": (
                    "Conheça o Present Perfect com already, yet e just para falar de "
                    "experiências até agora."
                ),
                "theory": (
                    "O Present Perfect conecta o passado ao presente: 'I have already eaten "
                    "lunch' significa que almocei em algum momento antes de agora — e o momento "
                    "exato não importa. Formamos com have/has + particípio: 'She has seen that "
                    "movie', 'They have finished the work'. Os marcadores-chave são already "
                    "(já, em afirmativas), yet (ainda/não, em negativas e perguntas, geralmente "
                    "no fim da frase) e just (acabou de acontecer). O erro mais comum dos "
                    "brasileiros é usar o Simple Past com already: 'I already ate lunch' soa "
                    "estranho quando a ideia é experiência presente — o certo é 'I have "
                    "already eaten lunch'. Compare: Simple Past conta quando aconteceu "
                    "(yesterday); Present Perfect foca no resultado até agora. Guarde os "
                    "particípios: eaten, seen, done, gone, finished."
                ),
                "example": "I have already finished my homework. She has just arrived.",
                "key_points": [
                    "have/has + particípio",
                    "already = já (afirmativas)",
                    "yet = ainda (negativas e perguntas)",
                    "just = acabou de",
                    "I have already eaten (não 'I already ate')",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Complete: She ___ already seen that movie.",
                        "choices": ["has", "have", "is", "was"],
                        "correct_index": 0,
                        "explanation": (
                            "Com she (3ª pessoa do singular), o Present Perfect usa has: She "
                            "has already seen that movie. have é para I, you, we e they."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "I have ___ (to finish) the report. (particípio)",
                        "correct": "finished",
                        "explanation": (
                            "O Present Perfect usa have + particípio: have finished. Como "
                            "finish é regular, o particípio coincide com o passado: finish → "
                            "finished."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual frase está correta para dizer 'eu já almocei' (até agora)?",
                        "choices": [
                            "I have already eaten lunch.",
                            "I already ate lunch.",
                            "I have already ate lunch.",
                            "I already eaten lunch.",
                        ],
                        "correct_index": 0,
                        "explanation": (
                            "Com already no sentido de 'até agora', use Present Perfect: have + "
                            "already + particípio (eaten). 'I already ate' é o erro clássico de "
                            "quem traduz 'eu já almocei' — e 'ate' é passado, não particípio."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: that book / I / read / haven't / yet",
                        "correct": "I haven't read that book yet.",
                        "explanation": (
                            "yet fecha a frase em negativas: I haven't read that book yet. A "
                            "ordem é sujeito + haven't + particípio + yet."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "He has just arrived at the airport.",
                        "explanation": (
                            "has just arrived = acabou de chegar: has + just + particípio. O "
                            "just entra entre have/has e o verbo, indicando algo que aconteceu "
                            "instantes atrás."
                        ),
                    },
                ],
            },
            {
                "slug": "a2-for-since",
                "title": "For & Since",
                "skill": "Grammar",
                "summary": "Diga há quanto tempo com for (duração) e since (ponto inicial) no Present Perfect.",
                "theory": (
                    "Para dizer há quanto tempo algo acontece, o Present Perfect ganha dois "
                    "companheiros: for e since. Use for + duração — 'for two years', 'for ten "
                    "days' — e since + ponto inicial — 'since 2020', 'since Monday', 'since I "
                    "was a kid'. A pergunta que abre tudo é 'How long have you lived here?'. O "
                    "erro clássico do brasileiro é trocar as preposições: 'since two years' e "
                    "'for 2020' não existem; pense 'for = durante quanto tempo' e 'since = "
                    "desde quando'. Outra armadilha é traduzir 'há dois anos' como 'have two "
                    "years' — em inglês, o have do Present Perfect é do verbo, não do tamanho "
                    "do tempo: 'I've lived here for two years'. Pratique com fatos da sua "
                    "vida: trabalho, casa, amizades."
                ),
                "example": "I've lived here for two years, since 2024.",
                "key_points": [
                    "for + duração (for two years)",
                    "since + ponto inicial (since 2020)",
                    "How long have you...?",
                    "I've lived here for two years.",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Complete: I've worked here ___ 2020.",
                        "choices": ["since", "for", "from", "at"],
                        "correct_index": 0,
                        "explanation": (
                            "2020 é um ponto inicial (ano específico), então since: since 2020. "
                            "for viria com duração medida: for six years."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "She has studied English ___ three years. (for ou since?)",
                        "correct": "for",
                        "explanation": (
                            "three years é uma duração, então for: for three years. A pergunta "
                            "mental: 'desde quando' → since; 'por quanto tempo' → for."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Complete: We've known each other ___ we were kids.",
                        "choices": ["since", "for", "from", "when"],
                        "correct_index": 0,
                        "explanation": (
                            "'we were kids' é um ponto de partida no tempo, então since: since "
                            "we were kids. for exige duração medida (for years), não um evento "
                            "inicial."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: for five years / I've / in this city / lived",
                        "correct": "I've lived in this city for five years.",
                        "explanation": (
                            "I've lived in this city for five years usa for + duração. A ordem "
                            "é sujeito + have/has + particípio + lugar + tempo."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "They have been friends since high school.",
                        "explanation": (
                            "since high school marca o início da amizade: since + ponto "
                            "inicial. Se fosse duração, diríamos for ten years."
                        ),
                    },
                ],
            },
            {
                "slug": "a2-travel-stories",
                "title": "Travel Stories",
                "skill": "Conversation",
                "summary": "Alterne passado, present perfect e going to em um diálogo real sobre viagens.",
                "theory": (
                    "Contar histórias de viagem é onde todo o A2 se junta: perguntas no "
                    "passado, respostas com verbos irregulares e planos com going to. Abra com "
                    "'Where did you go?' e 'How long did you stay?'. Nas respostas, os "
                    "irregulares brilham — went, took, saw, had — e para falar de experiências "
                    "ainda não vividas, o Present Perfect entra em cena: 'I haven't traveled "
                    "this year yet'. Para planos, 'I'm going to go to Chile in March'. O erro "
                    "típico é misturar tempos sem perceber: se a viagem já acabou, fique no "
                    "passado; se é plano, fique no futuro. No diálogo, observe como Hannah e "
                    "Bruno alternam passado, present perfect e going to sem esforço — essa "
                    "fluência de alternar tempos é a meta do nível."
                ),
                "example": "I went to Italy last month. It was amazing!",
                "key_points": [
                    "Where did you go?",
                    "How long did you stay?",
                    "I haven't traveled yet.",
                    "I'm going to go to Chile.",
                ],
                "dialogue": [
                    {"speaker": "Hannah", "line": "Hi, Bruno! I heard you traveled last month. Where did you go?"},
                    {"speaker": "Bruno", "line": "I went to Italy with my brother. It was amazing!"},
                    {"speaker": "Hannah", "line": "How nice! Which cities did you visit?"},
                    {"speaker": "Bruno", "line": "We visited Rome and Florence. We took a train between the two."},
                    {"speaker": "Hannah", "line": "How long did you stay there?"},
                    {"speaker": "Bruno", "line": "Ten days. It wasn't enough! What about you?"},
                    {"speaker": "Hannah", "line": "I haven't traveled this year yet, but I'm going to go to Chile in March."},
                    {"speaker": "Bruno", "line": "Cool! Are you going with friends?"},
                    {"speaker": "Hannah", "line": "Yes, with two friends from work. We already booked the tickets."},
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Segundo o diálogo, quais cidades Bruno visitou na Itália?",
                        "choices": [
                            "Roma e Florença",
                            "Roma e Veneza",
                            "Milão e Roma",
                            "Florença e Nápoles",
                        ],
                        "correct_index": 0,
                        "explanation": (
                            "Bruno diz 'We visited Rome and Florence'. Repare como a resposta "
                            "espelha a pergunta: 'Which cities did you visit?' → 'We "
                            "visited...' — padrão que se repete em toda conversa de viagem."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "O que Hannah vai fazer em março?",
                        "choices": [
                            "Viajar para o Chile com amigos",
                            "Viajar para a Itália com o irmão",
                            "Fazer um curso de inglês",
                            "Conhecer Roma e Florença",
                        ],
                        "correct_index": 0,
                        "explanation": (
                            "Hannah diz 'I'm going to go to Chile in March' com dois amigos do "
                            "trabalho. going to indica plano já pensado — ela até já comprou as "
                            "passagens (already booked)."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "I ___ (to go) to Italy with my brother. (Simple Past)",
                        "correct": "went",
                        "explanation": (
                            "go no passado é went, irregular: I went to Italy. 'goed' não "
                            "existe, e o contexto (last month) confirma o tempo passado."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: many photos / we / took / at the Colosseum",
                        "correct": "We took many photos at the Colosseum.",
                        "explanation": (
                            "took é o passado irregular de take: We took many photos at the "
                            "Colosseum. A ordem é sujeito + verbo + complemento + lugar."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "I visited Rome last summer.",
                        "explanation": (
                            "visited é passado regular (visit + ed): I visited Rome last "
                            "summer. A ação terminou, então o verbo marca o passado — e o "
                            "'last summer' confirma."
                        ),
                    },
                ],
            },
            {
                "slug": "a2-review-mission",
                "title": "Mission: A2 in Action",
                "skill": "Review",
                "summary": "Revisão geral do A2: passado, presente contínuo, futuro, comparações e present perfect.",
                "theory": (
                    "Missão final: hora de revisar tudo o que você construiu no A2. Passado "
                    "regular e irregular, perguntas com did, present continuous, going to, "
                    "will, comparativos, superlativos, quantifiers e present perfect com for e "
                    "since — o arsenal completo. A melhor forma de consolidar é alternar: uma "
                    "mesma história pode começar no passado ('I went to Rome'), trazer o "
                    "presente ('I'm telling you about it') e apontar o futuro ('I'm going to "
                    "go back'). Se errar alguma questão, volte à lição correspondente e releia "
                    "a teoria — revisar o erro é onde o aprendizado acontece. Depois desta "
                    "lição, você está pronto para se apresentar, contar histórias, planejar e "
                    "comparar em inglês. Parabéns por chegar até aqui!"
                ),
                "example": "I went to Rome last year, I'm saving money now, and I'm going to go back.",
                "key_points": [
                    "Passado: did + verbo base / verbos irregulares",
                    "Agora: am/is/are + -ing",
                    "Plano: going to / Decisão: will",
                    "Experiência: have + particípio",
                    "Compare: -er than / the -est",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Complete: She ___ her keys at home this morning.",
                        "choices": ["left", "leaved", "leaves", "was leaving"],
                        "correct_index": 0,
                        "explanation": (
                            "leave → left, irregular. 'this morning' é tempo terminado, então o "
                            "passado é obrigatório — e 'leaved' não existe em inglês."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "Listen! The neighbors ___ (to argue) again.",
                        "correct": "are arguing",
                        "explanation": (
                            "A ação está acontecendo agora (Listen!), então Present Continuous: "
                            "are arguing. E repare: argue perde o e antes do ing, como make → "
                            "making."
                        ),
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Complete: This bag is ___ than the one I bought last year.",
                        "choices": ["more expensive", "expensiver", "most expensive", "the most expensive"],
                        "correct_index": 0,
                        "explanation": (
                            "expensive é adjetivo longo, então more + expensive + than. "
                            "'expensiver' mistura as receitas; most expensive seria superlativo, "
                            "para coroar o campeão."
                        ),
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "I have ___ (to lose) my passport! (particípio)",
                        "correct": "lost",
                        "explanation": (
                            "lose → lost no particípio e no passado. Com have, use o particípio: "
                            "have lost. A experiência presente (perdi, agora não tenho) pede "
                            "Present Perfect."
                        ),
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: a new car / we're going to / buy / next month",
                        "correct": "We're going to buy a new car next month.",
                        "explanation": (
                            "Plano já pensado → going to: We're going to buy a new car next "
                            "month. A ordem é to be + going to + verbo base + complemento + "
                            "tempo."
                        ),
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "She has already called her mom.",
                        "explanation": (
                            "She has already called her mom usa Present Perfect com already: "
                            "has + already + particípio (called). A ação terminou, mas o foco é "
                            "o resultado até agora."
                        ),
                    },
                ],
            },
        ],
    },
]


from .advanced_extension import reclassify_skills  # noqa: E402

reclassify_skills(
    UNITS,
    {
        "a2-past-questions": "Speaking",
        "a2-going-to": "Speaking",
        "a2-will-decisions": "Speaking",
        "a2-should-advice": "Speaking",
    },
)
