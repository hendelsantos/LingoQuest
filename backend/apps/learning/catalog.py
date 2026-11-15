COURSE = {
    "slug": "a1-foundations",
    "title": "A1 Foundations",
    "description": (
        "Uma base prática para se apresentar, falar da rotina e entender situações do dia a dia."
    ),
    "level": "A1",
}

UNITS = [
    {
        "title": "Welcome",
        "position": 1,
        "description": "Primeiros contatos e estruturas essenciais.",
        "lessons": [
            {
                "slug": "hello",
                "title": "Hello, World!",
                "skill": "Speaking",
                "summary": "Saudações e apresentações",
                "theory": (
                    "Em inglês, uma apresentação simples costuma seguir três passos: cumprimentar, "
                    "dizer seu nome e encerrar com uma expressão amigável. Use “Good "
                    "morning” até o "
                    "meio-dia, “Good afternoon” durante a tarde e “Good evening” ao chegar à noite."
                ),
                "example": "Hello! My name is Alex. Nice to meet you.",
                "key_points": [
                    "Hello e Hi servem para cumprimentar.",
                    "My name is... apresenta seu nome.",
                    "Nice to meet you significa “Prazer em conhecer você”.",
                ],
                "questions": [
                    (
                        "Como dizer bom dia?",
                        ["Good night", "Good morning", "Goodbye"],
                        1,
                        "Good morning é a saudação usada pela manhã.",
                    ),
                    (
                        "My name ___ Alex.",
                        ["am", "are", "is"],
                        2,
                        "Name está na terceira pessoa do singular, por isso usamos is.",
                    ),
                    (
                        "Prazer em conhecer você.",
                        ["Nice to meet you", "See you tomorrow", "How old are you?"],
                        0,
                        "Nice to meet you é a expressão usada ao conhecer alguém.",
                    ),
                ],
            },
            {
                "slug": "tobe",
                "title": "The Verb To Be",
                "skill": "Grammar",
                "summary": "Am, is e are sem mistério",
                "theory": (
                    "O verbo to be significa “ser” ou “estar”. A forma muda conforme a pessoa: use "
                    "am com I; is com he, she e it; e are com you, we e they. Para "
                    "negar, acrescente "
                    "not: I am not, she is not, they are not."
                ),
                "example": "I am a student. She is a teacher. We are friends.",
                "key_points": ["I am", "He / She / It is", "You / We / They are"],
                "questions": [
                    ("I ___ happy.", ["is", "am", "are"], 1, "O pronome I sempre usa am."),
                    ("They ___ at school.", ["am", "is", "are"], 2, "They é plural e usa are."),
                    (
                        "She ___ not tired.",
                        ["is", "are", "am"],
                        0,
                        "She usa is; a negativa completa é is not.",
                    ),
                ],
            },
            {
                "slug": "articles",
                "title": "A, An & The",
                "skill": "Grammar",
                "summary": "Artigos para falar com clareza",
                "theory": (
                    "Use a antes de um som consonantal e an antes de um som vocálico "
                    "quando algo ainda não é específico: a book, an apple. Use the "
                    "quando a pessoa já sabe de qual item "
                    "você está falando: the book on the table."
                ),
                "example": "I have an apple and a book. The book is blue.",
                "key_points": ["a + som consonantal", "an + som vocálico", "the + item específico"],
                "questions": [
                    (
                        "___ orange",
                        ["a", "an", "is"],
                        1,
                        "Orange começa com som vocálico, então usamos an.",
                    ),
                    (
                        "I have ___ dog.",
                        ["an", "a", "am"],
                        1,
                        "Dog começa com som consonantal, então usamos a.",
                    ),
                    (
                        "Já falamos sobre o livro. ___ book is blue.",
                        ["An", "A", "The"],
                        2,
                        "O livro já é conhecido na conversa, então usamos the.",
                    ),
                ],
            },
        ],
    },
    {
        "title": "Everyday English",
        "position": 2,
        "description": "Inglês para rotina, família, horários e perguntas.",
        "lessons": [
            {
                "slug": "routine",
                "title": "My Daily Routine",
                "skill": "Grammar",
                "summary": "Simple Present no dia a dia",
                "theory": (
                    "Use o Simple Present para hábitos e fatos. Com I, you, we e they, "
                    "use a forma base: I work. Com he, she e it, normalmente acrescente "
                    "-s: he works. Perguntas usam do "
                    "ou does; negativas usam do not ou does not."
                ),
                "example": "I work every day. He works in a factory.",
                "key_points": [
                    "I / You / We / They work",
                    "He / She / It works",
                    "Do / Does nas perguntas",
                ],
                "questions": [
                    (
                        "She ___ English.",
                        ["study", "studies", "studying"],
                        1,
                        "Com she, study troca o y por ies: studies.",
                    ),
                    (
                        "___ you work here?",
                        ["Does", "Do", "Is"],
                        1,
                        "Perguntas com you no Simple Present usam do.",
                    ),
                    (
                        "He ___ like coffee.",
                        ["do not", "does not", "are not"],
                        1,
                        "A negativa de he usa does not + verbo na forma base.",
                    ),
                ],
            },
            {
                "slug": "family",
                "title": "People & Family",
                "skill": "Vocabulary",
                "summary": "Pessoas e adjetivos possessivos",
                "theory": (
                    "Adjetivos possessivos mostram a quem algo pertence e vêm antes do "
                    "substantivo: "
                    "my, your, his, her, our e their. Eles não mudam no plural: my book, my books. "
                    "Escolha a forma pela pessoa que possui, não pelo objeto."
                ),
                "example": "This is my sister. Her name is Jane.",
                "key_points": ["I → my", "He / She → his / her", "We / They → our / their"],
                "questions": [
                    (
                        "Meu livro",
                        ["My book", "Your book", "His book"],
                        0,
                        "My significa meu ou minha.",
                    ),
                    (
                        "She loves ___ own family.",
                        ["his", "her", "their"],
                        1,
                        "Her se refere a quem possui: she.",
                    ),
                    (
                        "We live with ___ parents.",
                        ["our", "your", "my"],
                        0,
                        "Our significa nosso ou nossa e acompanha we.",
                    ),
                ],
            },
            {
                "slug": "time",
                "title": "What Time Is It?",
                "skill": "Listening",
                "summary": "Horas e compromissos",
                "theory": (
                    "Para dizer as horas de forma direta, fale a hora e os minutos: "
                    "7:30 é seven thirty. Use at antes de horários específicos: at six, "
                    "at eight thirty. Para perguntar, use "
                    "What time is it?"
                ),
                "example": "It is seven thirty. I start work at eight.",
                "key_points": ["7:30 → seven thirty", "at + horário", "What time is it?"],
                "questions": [
                    (
                        "7:30 em inglês",
                        ["Seven thirteen", "Seven thirty", "Seventy-three"],
                        1,
                        "Thirty significa trinta; 7:30 é seven thirty.",
                    ),
                    (
                        "I wake up ___ six.",
                        ["in", "on", "at"],
                        2,
                        "Usamos at antes de um horário específico.",
                    ),
                    (
                        "Como perguntar as horas?",
                        ["What time is it?", "How old are you?", "Where is it?"],
                        0,
                        "What time is it? é a pergunta padrão para saber as horas.",
                    ),
                ],
            },
            {
                "slug": "questions",
                "title": "Ask Me Anything",
                "skill": "Speaking",
                "summary": "Perguntas para conversar melhor",
                "theory": (
                    "As question words abrem perguntas específicas: what (o quê), where "
                    "(onde), when (quando), who (quem), why (por quê) e how (como). No "
                    "Simple Present, normalmente "
                    "seguimos com do ou does: Where do you live?"
                ),
                "example": "Where do you live? What do you do?",
                "key_points": ["Where = onde", "When = quando", "Why = por quê", "How = como"],
                "questions": [
                    (
                        "___ do you live?",
                        ["Where", "When", "Who"],
                        0,
                        "Where pergunta sobre lugar: onde você mora?",
                    ),
                    (
                        "___ is your birthday?",
                        ["What", "When", "Where"],
                        1,
                        "When pergunta quando algo acontece.",
                    ),
                    (
                        "___ are you?",
                        ["Who", "Why", "How"],
                        2,
                        "How are you? significa “Como você está?”.",
                    ),
                ],
            },
            {
                "slug": "review",
                "title": "Mission: Real Life",
                "skill": "Review",
                "summary": "Combine tudo em uma apresentação",
                "theory": (
                    "Agora combine as estruturas da unidade. Apresente-se com to be, "
                    "fale da sua rotina no Simple Present e faça perguntas com question "
                    "words. O objetivo não é decorar "
                    "frases, mas reconhecer padrões para criar as suas."
                ),
                "example": "Hello! I am Lucas. I live in Brazil and I work every day.",
                "key_points": [
                    "I am para se apresentar",
                    "Simple Present para rotina",
                    "Question words para continuar a conversa",
                ],
                "questions": [
                    ("I ___ from Brazil.", ["am", "are", "is"], 0, "I usa am: I am from Brazil."),
                    (
                        "He ___ at eight.",
                        ["work", "works", "working"],
                        1,
                        "Na terceira pessoa, work recebe s: he works.",
                    ),
                    (
                        "___ do you study English? Because I love it.",
                        ["What", "Why", "When"],
                        1,
                        "Why pergunta o motivo e combina com a resposta because.",
                    ),
                ],
            },
        ],
    },
]
