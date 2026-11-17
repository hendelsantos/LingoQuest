"""Nível A1 — Foundations.

Primeiros contatos com o inglês: verbo to be, artigos, pronomes, rotina,
números, existência (there is/are), preposições, can, passado do to be e
conversação básica de sobrevivência.
"""

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
                    "morning” até o meio-dia, “Good afternoon” durante a tarde e “Good evening” ao chegar à noite. "
                    "Para responder a “How are you?”, o padrão é “I'm fine, thank you. And you?”."
                ),
                "example": "Hello! My name is Alex. Nice to meet you.",
                "key_points": [
                    "Hello e Hi servem para cumprimentar.",
                    "My name is... apresenta seu nome.",
                    "Nice to meet you significa “Prazer em conhecer você”.",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Como dizer bom dia?",
                        "choices": ["Good night", "Good morning", "Goodbye"],
                        "correct_index": 1,
                        "explanation": "Good morning é a saudação usada pela manhã; good night é para despedida à noite.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "My name ___ Alex.",
                        "correct": "is",
                        "accepted": ["is"],
                        "explanation": "Name está na terceira pessoa do singular, por isso usamos is.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras para se apresentar: meet / nice / you / to",
                        "correct": "Nice to meet you.",
                        "explanation": "A ordem natural é Nice to meet you — o “to” liga o adjetivo à ação.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "Hello! How are you?",
                        "explanation": "Hello! How are you? é a forma mais comum de cumprimentar e perguntar como a pessoa está.",
                    },
                ],
            },
            {
                "slug": "tobe",
                "title": "The Verb To Be",
                "skill": "Grammar",
                "summary": "Am, is e are sem mistério",
                "theory": (
                    "O verbo to be significa “ser” ou “estar”. A forma muda conforme a pessoa: use "
                    "am com I; is com he, she e it; e are com you, we e they. Para negar, acrescente "
                    "not: I am not, she is not, they are not. Em perguntas, inverta a ordem: Are you a student? "
                    "Atenção: em inglês o sujeito quase nunca é omitido, diferente do português."
                ),
                "example": "I am a student. She is a teacher. We are friends.",
                "key_points": ["I am", "He / She / It is", "You / We / They are"],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "I ___ happy.",
                        "choices": ["is", "am", "are"],
                        "correct_index": 1,
                        "explanation": "O pronome I sempre usa am.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "They ___ at school.",
                        "choices": ["am", "is", "are"],
                        "correct_index": 2,
                        "explanation": "They é plural e usa are.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "She ___ not tired.",
                        "correct": "is",
                        "accepted": ["is"],
                        "explanation": "She usa is; a negativa completa é is not (ou isn't).",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: are / we / friends",
                        "correct": "We are friends.",
                        "explanation": "A ordem é sujeito (we) + verbo (are) + complemento (friends).",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "I am a student.",
                        "explanation": "I am a student. — apresentação clássica com o verbo to be.",
                    },
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
                    "quando a pessoa já sabe de qual item você está falando: the book on the table. "
                    "O som é o que importa, não a letra: an hour (h mudo), a university (som de “iu”). "
                    "Cuidado: substantivos em inglês quase sempre pedem algum artigo ou plural."
                ),
                "example": "I have an apple and a book. The book is blue.",
                "key_points": ["a + som consonantal", "an + som vocálico", "the + item específico"],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "___ orange",
                        "choices": ["a", "an", "is"],
                        "correct_index": 1,
                        "explanation": "Orange começa com som vocálico, então usamos an.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "I have ___ dog.",
                        "correct": "a",
                        "accepted": ["a"],
                        "explanation": "Dog começa com som consonantal, então usamos a.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Já falamos sobre o livro. ___ book is blue.",
                        "choices": ["An", "A", "The"],
                        "correct_index": 2,
                        "explanation": "O livro já é conhecido na conversa, então usamos the.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "The book is on the table.",
                        "explanation": "The book is on the table. — usa the porque o livro é específico e conhecido.",
                    },
                ],
            },
            {
                "slug": "pronouns",
                "title": "I, You & Friends",
                "skill": "Grammar",
                "summary": "Pronomes pessoais e o verbo certo",
                "theory": (
                    "Os pronomes pessoais são I (eu), you (você ou vocês), he (ele), "
                    "she (ela), it (coisas, animais e situações), we (nós) e they (eles/elas). "
                    "Duas armadilhas para brasileiros: you serve para singular e plural — o "
                    "inglês não usa “you is”, sempre you are; e it é obrigatório para objetos, "
                    "enquanto no português costumamos omitir o sujeito."
                ),
                "example": "He is my brother. It is my phone. They are my friends.",
                "key_points": [
                    "you = você e também vocês",
                    "it = coisas e animais",
                    "ele/ela = he / she (só para pessoas)",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Maria is my sister. ___ is a doctor.",
                        "choices": ["He", "She", "It"],
                        "correct_index": 1,
                        "explanation": "Maria é uma mulher, então usamos she.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "___ is my brother. (ele)",
                        "correct": "he",
                        "accepted": ["he"],
                        "explanation": "He é o pronome para “ele”, pessoa do singular masculina.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Você e seu amigo chegaram. They say ___ are late.",
                        "choices": ["they", "you", "we"],
                        "correct_index": 1,
                        "explanation": "You serve tanto para um “você” quanto para “vocês”, sem mudar a forma.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: is / it / phone / my",
                        "correct": "It is my phone.",
                        "explanation": "Para objetos usamos it como sujeito: It is my phone.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "She is my teacher.",
                        "explanation": "She is my teacher. — she para uma professora.",
                    },
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
                    "-s: he works. Perguntas usam do ou does; negativas usam do not ou does not. "
                    "Erro clássico de brasileiro: usar does e o -s juntos (“does she works?”) — "
                    "quando aparece does, o verbo volta à forma base."
                ),
                "example": "I work every day. He works in a factory.",
                "key_points": [
                    "I / You / We / They work",
                    "He / She / It works",
                    "Do / Does nas perguntas",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "She ___ English.",
                        "choices": ["study", "studies", "studying"],
                        "correct_index": 1,
                        "explanation": "Com she, study troca o y por ies: studies.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "___ you work here?",
                        "correct": "do",
                        "accepted": ["do"],
                        "explanation": "Perguntas com you no Simple Present usam do + verbo na forma base.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "He ___ like coffee.",
                        "choices": ["do not", "does not", "are not"],
                        "correct_index": 1,
                        "explanation": "A negativa de he usa does not + verbo na forma base.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: every day / he / works",
                        "correct": "He works every day.",
                        "explanation": "A ordem é sujeito + verbo + complemento; every day fecha a frase.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "I work in a bank.",
                        "explanation": "I work in a bank. — rota com Simple Present na forma base.",
                    },
                ],
            },
            {
                "slug": "family",
                "title": "People & Family",
                "skill": "Vocabulary",
                "summary": "Pessoas e adjetivos possessivos",
                "theory": (
                    "Adjetivos possessivos mostram a quem algo pertence e vêm antes do "
                    "substantivo: my, your, his, her, our e their. Eles não mudam no plural: my book, my books. "
                    "Escolha a forma pela pessoa que possui, não pelo objeto: brother é homem, "
                    "mas se a irmã possui algo, é her brother's car... na verdade: “This is her car” "
                    "porque quem possui é ela. Erro comum: usar “the” possessivo do português "
                    "(“the Maria's car”) — em inglês, escolha my/his/her ou the, nunca os dois."
                ),
                "example": "This is my sister. Her name is Jane.",
                "key_points": ["I → my", "He / She → his / her", "We / They → our / their"],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Meu livro",
                        "choices": ["My book", "Your book", "His book"],
                        "correct_index": 0,
                        "explanation": "My significa meu ou minha.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "We live with ___ parents. (nossos)",
                        "correct": "our",
                        "accepted": ["our"],
                        "explanation": "Our significa nosso ou nossa e acompanha we.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "She loves ___ own family.",
                        "choices": ["his", "her", "their"],
                        "correct_index": 1,
                        "explanation": "Her se refere a quem possui: she.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "This is my sister.",
                        "explanation": "This is my sister. — apresentação clássica de um membro da família.",
                    },
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
                    "at eight thirty. Para perguntar, use What time is it? "
                    "Atenção à pronúncia dos números parecidos: thirteen (13) e thirty (30) "
                    "se distinguem pela sílaba forte final (-teen)."
                ),
                "example": "It is seven thirty. I start work at eight.",
                "key_points": ["7:30 → seven thirty", "at + horário", "What time is it?"],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "7:30 em inglês",
                        "choices": ["Seven thirteen", "Seven thirty", "Seventy-three"],
                        "correct_index": 1,
                        "explanation": "Thirty significa trinta; 7:30 é seven thirty.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "I wake up ___ six.",
                        "correct": "at",
                        "accepted": ["at"],
                        "explanation": "Usamos at antes de um horário específico.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Como perguntar as horas?",
                        "choices": ["What time is it?", "How old are you?", "Where is it?"],
                        "correct_index": 0,
                        "explanation": "What time is it? é a pergunta padrão para saber as horas.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "The class starts at nine.",
                        "explanation": "The class starts at nine. — at + horário específico.",
                    },
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
                    "Simple Present, normalmente seguimos com do ou does: Where do you live? "
                    "Lembre-se da ordem fixa: question word + do/does + sujeito + verbo. "
                    "Errar essa ordem é o erro mais comum de quem está começando."
                ),
                "example": "Where do you live? What do you do?",
                "key_points": ["Where = onde", "When = quando", "Why = por quê", "How = como"],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "___ do you live?",
                        "choices": ["Where", "When", "Who"],
                        "correct_index": 0,
                        "explanation": "Where pergunta sobre lugar: onde você mora?",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "___ is your birthday?",
                        "correct": "when",
                        "accepted": ["when"],
                        "explanation": "When pergunta quando algo acontece.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "___ are you?",
                        "choices": ["Who", "Why", "How"],
                        "correct_index": 2,
                        "explanation": "How are you? significa “Como você está?”.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: do / where / you / live",
                        "correct": "Where do you live?",
                        "explanation": "A ordem correta é question word + do + sujeito + verbo.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a pergunta que você ouviu.",
                        "correct": "What do you do?",
                        "explanation": "What do you do? é a pergunta padrão sobre a profissão de alguém.",
                    },
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
                    "words. O objetivo não é decorar frases, mas reconhecer padrões para criar as suas. "
                    "Dica de estudo: monte três frases sobre você mesmo antes de avançar — "
                    "produzir cedo acelera a fixação."
                ),
                "example": "Hello! I am Lucas. I live in Brazil and I work every day.",
                "key_points": [
                    "I am para se apresentar",
                    "Simple Present para rotina",
                    "Question words para continuar a conversa",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "I ___ from Brazil.",
                        "choices": ["am", "are", "is"],
                        "correct_index": 0,
                        "explanation": "I usa am: I am from Brazil.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "He ___ at eight.",
                        "choices": ["work", "works", "working"],
                        "correct_index": 1,
                        "explanation": "Na terceira pessoa, work recebe s: he works.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "___ do you study English? Because I love it.",
                        "correct": "why",
                        "accepted": ["why"],
                        "explanation": "Why pergunta o motivo e combina com a resposta because.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: in Brazil / I / live",
                        "correct": "I live in Brazil.",
                        "explanation": "Sujeito + verbo + lugar: I live in Brazil.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "She works at a school.",
                        "explanation": "She works at a school. — terceira pessoa com -s e at para o lugar de trabalho.",
                    },
                ],
            },
        ],
    },
    {
        "title": "Numbers & The World Around You",
        "position": 3,
        "description": "Números, plurais, existência e preposições de lugar.",
        "lessons": [
            {
                "slug": "numbers",
                "title": "Counting Life",
                "skill": "Vocabulary",
                "summary": "Números e substantivos no plural",
                "theory": (
                    "Aprenda os números de 0 a 20 e as dezenas (twenty, thirty, forty...). "
                    "Para plurais, a regra básica é acrescentar -s: book → books. Palavras "
                    "terminadas em -ch, -sh, -s ou -x ganham -es: watch → watches. Terminadas "
                    "em consoante + y trocam para -ies: baby → babies. E há os irregulares que "
                    "precisam de memorização: man → men, woman → women, child → children, "
                    "person → people. Cuidado com o erro clássico: “peoples” e “childs” não existem."
                ),
                "example": "I have two children and three dogs.",
                "key_points": [
                    "book → books (regra geral)",
                    "watch → watches (-ch, -sh, -s, -x)",
                    "child → children (irregular)",
                    "13 = thirteen · 30 = thirty",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Qual é o plural de “child”?",
                        "choices": ["childs", "children", "childes"],
                        "correct_index": 1,
                        "explanation": "Child é irregular: o plural é children.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "I have three ___ (brother).",
                        "correct": "brothers",
                        "accepted": ["brothers"],
                        "explanation": "Brother é regular: basta acrescentar -s.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual número é “fifteen”?",
                        "choices": ["50", "15", "5"],
                        "correct_index": 1,
                        "explanation": "Fifteen é 15; fifty seria 50. Ouça a sílaba forte: fif-TEEN.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: children / the family / seven / has",
                        "correct": "The family has seven children.",
                        "explanation": "Sujeito + verbo + quantidade + plural: The family has seven children.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "She has two children.",
                        "explanation": "She has two children. — children é o plural irregular de child.",
                    },
                ],
            },
            {
                "slug": "there-is-are",
                "title": "There Is & There Are",
                "skill": "Grammar",
                "summary": "Existência sem confundir com “have”",
                "theory": (
                    "Para dizer que algo existe em um lugar, use there is + singular e "
                    "there are + plural: There is a bank here. There are two parks here. "
                    "A negativa usa there isn't / there aren't e a pergunta inverte: Is there...? / Are there...? "
                    "Armadilha para brasileiros: onde o português usa “tem” para tudo, o inglês "
                    "separa posse (I have a car) de existência (There is a car outside)."
                ),
                "example": "There is a bank near here. There are two banks on this street.",
                "key_points": [
                    "There is + singular",
                    "There are + plural",
                    "Is there...? / Are there...?",
                    "Posse = have · Existência = there is/are",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "___ a book on the table.",
                        "choices": ["There are", "There is", "They are"],
                        "correct_index": 1,
                        "explanation": "Book é singular: There is a book on the table.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "___ there any milk in the fridge?",
                        "correct": "is",
                        "accepted": ["is"],
                        "explanation": "Milk é incontável (singular): Is there any milk...?",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "There ___ two parks in this city.",
                        "choices": ["is", "be", "are"],
                        "correct_index": 2,
                        "explanation": "Two parks é plural: there are.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: in the bag / there / two apples / are",
                        "correct": "There are two apples in the bag.",
                        "explanation": "There are + quantidade + plural + lugar.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "There is a big park near my house.",
                        "explanation": "There is a big park near my house. — existência no singular.",
                    },
                ],
            },
            {
                "slug": "prepositions-place",
                "title": "Where Is It?",
                "skill": "Grammar",
                "summary": "Preposições de lugar com precisão",
                "theory": (
                    "As preposições de lugar mais úteis são: in (dentro), on (sobre/em "
                    "contato com a superfície), under (embaixo), next to / beside (ao lado), "
                    "between (entre dois), behind (atrás) e in front of (na frente). "
                    "Erro típico de brasileiro: dizer “in the table” para “na mesa” — em inglês "
                    "é on the table, porque o objeto está sobre a superfície. Também usamos "
                    "at para pontos de referência: at the bus stop, at the door."
                ),
                "example": "The keys are on the table. The cat is in the box.",
                "key_points": [
                    "on = sobre a superfície (on the table)",
                    "in = dentro (in the box)",
                    "under = embaixo",
                    "next to = ao lado",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "The keys are ___ the table.",
                        "choices": ["in", "on", "at"],
                        "correct_index": 1,
                        "explanation": "As chaves estão sobre a superfície da mesa: on the table.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "The cat is ___ the box. (dentro)",
                        "correct": "in",
                        "accepted": ["in"],
                        "explanation": "In indica que o gato está dentro da caixa.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "The bakery is ___ the bank and the school.",
                        "choices": ["between", "behind", "under"],
                        "correct_index": 0,
                        "explanation": "Between indica algo localizado entre dois outros pontos.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: the table / is / the dog / under",
                        "correct": "The dog is under the table.",
                        "explanation": "Sujeito + is + preposição + lugar: The dog is under the table.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "My phone is on the bed.",
                        "explanation": "My phone is on the bed. — on para superfícies.",
                    },
                ],
            },
            {
                "slug": "food-and-drinks",
                "title": "Food & Drinks",
                "skill": "Vocabulary",
                "summary": "Comidas e como pedir com educação",
                "theory": (
                    "Vocabulário essencial de comida: bread (pão), rice (arroz), cheese "
                    "(queijo), chicken (frango), coffee (café), water (água), juice (suco). "
                    "Para gostos, use I like / I don't like + comida. Para pedir com educação, "
                    "use I'd like (= I would like): I'd like a coffee, please. "
                    "Erro clássico de brasileiro no restaurante: “I like a coffee” para pedir — "
                    "I like significa “eu gosto de”; o pedido correto é I'd like."
                ),
                "example": "I like pizza, but I don't like onions. I'd like a cheese sandwich, please.",
                "key_points": [
                    "I like = eu gosto de",
                    "I'd like = eu gostaria de (pedido)",
                    "..., please = por favor",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Como pedir um café com educação?",
                        "choices": ["I like a coffee.", "I'd like a coffee, please.", "I am a coffee."],
                        "correct_index": 1,
                        "explanation": "I'd like é o pedido educado; I like expressa preferência geral.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "I ___ like fish. (não gosto)",
                        "correct": "don't",
                        "accepted": ["don't", "do not"],
                        "explanation": "A negativa do Simple Present com I é don't like.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "O que significa “bread”?",
                        "choices": ["Pão", "Leite", "Manteiga"],
                        "correct_index": 0,
                        "explanation": "Bread é pão; milk é leite e butter é manteiga.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: like / I / chocolate cake",
                        "correct": "I like chocolate cake.",
                        "explanation": "Sujeito + like + objeto: I like chocolate cake.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "She likes Italian food.",
                        "explanation": "She likes Italian food. — terceira pessoa: like + s.",
                    },
                ],
            },
        ],
    },
    {
        "title": "Abilities & Fun",
        "position": 4,
        "description": "Habilidades com can, passado do to be e gostos com -ing.",
        "lessons": [
            {
                "slug": "can-abilities",
                "title": "I Can Do It",
                "skill": "Grammar",
                "summary": "Habilidades e pedidos com can",
                "theory": (
                    "Can expressa habilidade ou permissão e é seguido do verbo na forma "
                    "base: I can swim. A negativa é can't (cannot). Para perguntas, inverta: "
                    "Can you swim? A resposta curta é Yes, I can / No, I can't. "
                    "Atenção: can nunca muda — não existe “she cans”. Isso acontece porque "
                    "can é um verbo modal, que já carrega a noção de pessoa."
                ),
                "example": "She can swim very well. I can't drive.",
                "key_points": [
                    "can + verbo na forma base",
                    "can't = cannot",
                    "Can you...? Yes, I can.",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "She ___ swim.",
                        "choices": ["cans", "can to", "can"],
                        "correct_index": 2,
                        "explanation": "Can é um modal: nunca recebe -s. She can swim.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "They ___ dance. (não sabem)",
                        "correct": "can't",
                        "accepted": ["can't", "cannot", "can not"],
                        "explanation": "A negativa de can é can't (ou cannot), + verbo base.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Como responder a “Can you play the guitar?”",
                        "choices": ["Yes, I can.", "Yes, I do.", "Yes, I am."],
                        "correct_index": 0,
                        "explanation": "Perguntas com can são respondidas com can: Yes, I can.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: very well / she / sing / can",
                        "correct": "She can sing very well.",
                        "explanation": "Ordem com modal: sujeito + can + verbo + complemento.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "I can speak a little English.",
                        "explanation": "I can speak a little English. — can + verbo na forma base.",
                    },
                ],
            },
            {
                "slug": "was-were",
                "title": "Yesterday with To Be",
                "skill": "Grammar",
                "summary": "Was e were no passado",
                "theory": (
                    "O passado do verbo to be é was (I, he, she, it) e were (you, we, they). "
                    "A negativa é wasn't / weren't e a pergunta inverte: Were you at home? "
                    "Use-o para estados e situações no passado: I was tired yesterday. "
                    "Dica para memorizar: as mesmas pessoas que usam is/was e are/were no presente "
                    "se mantêm no passado."
                ),
                "example": "I was at home. They were at the party.",
                "key_points": ["I / He / She / It → was", "You / We / They → were", "wasn't / weren't"],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "I ___ at home yesterday.",
                        "choices": ["were", "was", "am"],
                        "correct_index": 1,
                        "explanation": "I usa was no passado do to be.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "They ___ happy at the party.",
                        "correct": "were",
                        "accepted": ["were"],
                        "explanation": "They usa were no passado.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "___ you at the concert last night?",
                        "choices": ["Was", "Is", "Were"],
                        "correct_index": 2,
                        "explanation": "You usa were; na pergunta, o verbo vem primeiro.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: the movie / was / great",
                        "correct": "The movie was great.",
                        "explanation": "Sujeito + was + adjetivo: The movie was great.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "We were tired last night.",
                        "explanation": "We were tired last night. — were com we.",
                    },
                ],
            },
            {
                "slug": "likes-ing",
                "title": "Love + -ing",
                "skill": "Grammar",
                "summary": "Gostos com like, love e hate",
                "theory": (
                    "Para falar do que você gosta de fazer, use like, love, hate ou enjoy "
                    "seguidos do verbo com -ing: I love cooking. She hates waking up early. "
                    "Erro clássico de brasileiro: “I like dance” — falta o -ing (ou like + to + "
                    "verbo, também correto: I like to dance). Com enjoy, só vale -ing: I enjoy reading. "
                    "A formação é simples: verbo + -ing (cook → cooking, get → getting)."
                ),
                "example": "I love cooking. She hates getting up early.",
                "key_points": [
                    "like / love / hate + -ing",
                    "enjoy + -ing (sempre)",
                    "I like dance ✗ → I like dancing ✓",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "I enjoy ___ books.",
                        "choices": ["read", "reading", "to read"],
                        "correct_index": 1,
                        "explanation": "Enjoy é sempre seguido de -ing: enjoy reading.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "She hates ___ up early. (wake)",
                        "correct": "waking",
                        "accepted": ["waking"],
                        "explanation": "Hate + verbo com -ing: hates waking up early.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "They love ___ pizza.",
                        "choices": ["eats", "eating", "eat"],
                        "correct_index": 1,
                        "explanation": "Love + -ing: They love eating pizza.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: hates / he / up / getting / early",
                        "correct": "He hates getting up early.",
                        "explanation": "Sujeito + hates + verbo-ing: He hates getting up early.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "I love cooking on weekends.",
                        "explanation": "I love cooking on weekends. — love + -ing.",
                    },
                ],
            },
            {
                "slug": "adverbs-frequency",
                "title": "Always & Never",
                "skill": "Grammar",
                "summary": "Advérbios de frequência e sua posição",
                "theory": (
                    "Os advérbios de frequência dizem com que frequência algo acontece: "
                    "always (100%), usually, often, sometimes, rarely e never (0%). "
                    "A posição importa: antes do verbo principal (I always wake up early) e "
                    "depois do verbo to be (She is always busy). Erro típico de brasileiro: "
                    "colocar o advérbio no fim da frase como no português (“I wake up always early”) — "
                    "em inglês, ele vem antes do verbo."
                ),
                "example": "I always drink coffee. She is never late.",
                "key_points": [
                    "always → nunca muda de forma",
                    "antes do verbo principal",
                    "depois do verbo to be",
                    "never já é negativo",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Ela sempre chega cedo. Qual a frase correta?",
                        "choices": ["She arrives always early.", "She always arrives early.", "Always she arrives early."],
                        "correct_index": 1,
                        "explanation": "O advérbio vem antes do verbo principal: She always arrives early.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "He is ___ late. (sempre)",
                        "correct": "always",
                        "accepted": ["always"],
                        "explanation": "Com o verbo to be, o advérbio vem depois: He is always late.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Qual expressa frequência zero?",
                        "choices": ["Sometimes", "Usually", "Never"],
                        "correct_index": 2,
                        "explanation": "Never significa “nunca” (0%). Como já é negativo, não se usa not.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: never / coffee / she / drinks / at night",
                        "correct": "She never drinks coffee at night.",
                        "explanation": "Sujeito + never + verbo + restante: She never drinks coffee at night.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "I usually get up at seven.",
                        "explanation": "I usually get up at seven. — usually antes do verbo principal.",
                    },
                ],
            },
        ],
    },
    {
        "title": "Wrap-Up A1",
        "position": 5,
        "description": "Frases de sobrevivência, small talk e a missão final do A1.",
        "lessons": [
            {
                "slug": "everyday-phrases",
                "title": "Survival Phrases",
                "skill": "Vocabulary",
                "summary": "Frases prontas para o dia a dia",
                "theory": (
                    "Guarde estas frases de sobrevivência: Excuse me (com licença, para "
                    "chamar atenção ou passar), I'm sorry (desculpa), Thank you / You're welcome "
                    "(obrigado / de nada), How much is it? (quanto custa?), Where is the bathroom? "
                    "e Can you repeat that, please? (pode repetir, por favor?). "
                    "Diferença importante: excuse me vem antes de incomodar; sorry vem depois. "
                    "Elas funcionam em qualquer situação e abrem portas em viagens."
                ),
                "example": "Excuse me, how much is it? — It's ten dollars. Thank you!",
                "key_points": [
                    "Excuse me = com licença (antes)",
                    "I'm sorry = desculpa (depois)",
                    "How much is it? = quanto custa?",
                    "Can you repeat that, please?",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Como perguntar o preço de algo?",
                        "choices": ["How much is it?", "How many is it?", "What price it?"],
                        "correct_index": 0,
                        "explanation": "How much is it? é a pergunta padrão para preço.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "___ me, where is the bathroom? (com licença)",
                        "correct": "excuse",
                        "accepted": ["excuse"],
                        "explanation": "Excuse me é usado antes de incomodar alguém ou pedir atenção.",
                    },
                    {
                        "type": "MCQ",
                        "prompt": "Você pisou no pé de alguém. O que dizer?",
                        "choices": ["Excuse me", "I'm sorry", "You're welcome"],
                        "correct_index": 1,
                        "explanation": "Sorry (I'm sorry) é o pedido de desculpa; excuse me é preventivo.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "Can you repeat that, please?",
                        "explanation": "Can you repeat that, please? — frase essencial para pedir repetição.",
                    },
                ],
            },
            {
                "slug": "small-talk",
                "title": "Small Talk, Big Help",
                "skill": "Conversation",
                "summary": "Conversa casual como os nativos",
                "theory": (
                    "Small talk é a conversa casual que abre relacionamentos em países de "
                    "língua inglesa. Os tópicos seguros são: clima (Beautiful day, isn't it?), "
                    "trabalho (What do you do?), fim de semana (How was your weekend?) e a "
                    "viagem (How was your flight?). Responda curto e devolva a pergunta: "
                    "I'm good, thanks. And you? Evite perguntas muito pessoais logo no início, "
                    "como salário e religião — comum no Brasil, evitado por nativos."
                ),
                "example": "How's it going? — Pretty good, thanks. And you?",
                "key_points": [
                    "How's it going? = tudo bem?",
                    "What do you do? = qual seu trabalho?",
                    "Beautiful day, isn't it? = clima seguro",
                    "Responda e devolva: And you?",
                ],
                "dialogue": [
                    {"speaker": "Anna", "line": "Hi! I don't think we've met. I'm Anna."},
                    {"speaker": "Bruno", "line": "Nice to meet you, Anna. I'm Bruno."},
                    {"speaker": "Anna", "line": "Nice to meet you too. How's it going?"},
                    {"speaker": "Bruno", "line": "Pretty good, thanks. It's my first day here."},
                    {"speaker": "Anna", "line": "Welcome! What do you do, Bruno?"},
                    {"speaker": "Bruno", "line": "I'm a designer. And you?"},
                    {"speaker": "Anna", "line": "I work in marketing. Beautiful office, isn't it?"},
                    {"speaker": "Bruno", "line": "It really is. Well, see you at lunch!"},
                    {"speaker": "Anna", "line": "See you! Have a great first day."},
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "Como responder a “How are you?” de forma natural?",
                        "choices": ["I'm good, thanks. And you?", "Yes, I am.", "I have 25 years."],
                        "correct_index": 0,
                        "explanation": "Responda como está e devolva a pergunta com And you? — assim a conversa flui.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "What do you ___? (pergunta sobre a profissão)",
                        "correct": "do",
                        "accepted": ["do"],
                        "explanation": "What do you do? é a pergunta padrão sobre a profissão de alguém.",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: it / how / going / is",
                        "correct": "How is it going?",
                        "explanation": "How is it going? (ou How's it going?) — cumprimento casual comum.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "Beautiful day, isn't it?",
                        "explanation": "Beautiful day, isn't it? — comentário clássico sobre o clima para iniciar conversa.",
                    },
                ],
            },
            {
                "slug": "final-review",
                "title": "Mission: A1 Complete",
                "skill": "Review",
                "summary": "Revisão geral de todo o nível A1",
                "theory": (
                    "Missão final do A1! Você revisará to be, Simple Present, there is/are, "
                    "can, passado do to be e as estruturas de conversação. Se alguma pergunta "
                    "travar, volte à lição correspondente — no LingoQuest, revisar não é recomeçar: "
                    "é consolidar. Ao concluir, você está pronto para o A2, onde o passado "
                    "com verbos de ação e o futuro entram em cena."
                ),
                "example": "I am ready! There are many things I can say in English now.",
                "key_points": [
                    "To be: am / is / are / was / were",
                    "Simple Present: hábitos e rotina",
                    "There is / There are: existência",
                    "Can: habilidade",
                ],
                "questions": [
                    {
                        "type": "MCQ",
                        "prompt": "I ___ from Brazil.",
                        "choices": ["am", "is", "are"],
                        "correct_index": 0,
                        "explanation": "I sempre usa am no presente do to be.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "___ you like pizza?",
                        "correct": "do",
                        "accepted": ["do"],
                        "explanation": "Pergunta no Simple Present com you: Do you like pizza?",
                    },
                    {
                        "type": "ORDERING",
                        "prompt": "Reorganize as palavras: on the table / there / two books / are",
                        "correct": "There are two books on the table.",
                        "explanation": "There are + plural + lugar: There are two books on the table.",
                    },
                    {
                        "type": "LISTENING",
                        "prompt": "Ouça o áudio e escreva a frase que você ouviu.",
                        "correct": "She can play the piano.",
                        "explanation": "She can play the piano. — modal can + verbo na forma base.",
                    },
                    {
                        "type": "FILL_IN",
                        "prompt": "He ___ (work) in a hospital.",
                        "correct": "works",
                        "accepted": ["works"],
                        "explanation": "Terceira pessoa do singular no Simple Present: works.",
                    },
                ],
            },
        ],
    },
]
