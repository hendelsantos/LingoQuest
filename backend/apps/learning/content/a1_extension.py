"""Enriquecimento pedagógico e revisões cumulativas do A1."""


def _pedagogy(
    objective: str,
    activation: str,
    mistakes: list[str],
    mode: str,
    prompt: str,
    model: str,
    focus: str,
    reviews: list[str],
) -> dict:
    return {
        "objective": objective,
        "activation_prompt": activation,
        "common_mistakes": mistakes,
        "production_task": {
            "mode": mode,
            "prompt": prompt,
            "model": model,
            "checklist": [
                "Cumpri a situação proposta sem copiar o modelo inteiro.",
                focus,
                "Reli ou repeti minha resposta e corrigi o que percebi.",
            ],
        },
        "review_prompts": reviews,
    }


PEDAGOGY_BY_SLUG = {
    "routine": _pedagogy(
        "Descrever três ações da própria rotina usando o Simple Present.",
        "Diga, sem consultar: a que horas você acorda, trabalha ou estuda?",
        [
            "Com he, she e it, o verbo normalmente recebe -s.",
            "Depois de does, o verbo volta à forma base: Does she work?",
        ],
        "SPEAKING",
        "Descreva sua manhã em três ou quatro frases e inclua pelo menos um horário.",
        "I wake up at seven. I have breakfast and I start work at eight.",
        "Usei o presente simples e mantive a forma correta do verbo.",
        [
            "Conte sua manhã em três frases sem consultar o modelo.",
            "Transforme He works at eight em pergunta e negativa.",
        ],
    ),
    "family": _pedagogy(
        "Apresentar familiares e indicar relações de posse com my, his, her, our e their.",
        "Pense em duas pessoas da sua família. Como você diria o nome e a relação delas?",
        [
            "Escolha o possessivo pela pessoa que possui, não pelo objeto possuído.",
            "Não combine the com um possessivo: diga my sister, não the my sister.",
        ],
        "SPEAKING",
        "Apresente duas pessoas da sua família e diga uma informação sobre cada uma.",
        "This is my sister. Her name is Carla. She is a teacher.",
        "Usei pelo menos dois possessivos de forma coerente.",
        [
            "Apresente um familiar usando três frases.",
            "Complete de memória: we → ___; she → ___; they → ___.",
        ],
    ),
    "time": _pedagogy(
        "Perguntar e informar horários de compromissos cotidianos.",
        "Tente dizer em inglês o horário atual e a hora em que seu dia começa.",
        [
            "Use at antes de horários específicos: at seven thirty.",
            "Destaque o final de thirteen e a primeira sílaba de thirty.",
        ],
        "SPEAKING",
        "Diga o horário de três compromissos do seu dia e faça a pergunta What time…?",
        "What time is the class? It starts at nine. I have lunch at twelve thirty.",
        "Usei at antes dos horários e pronunciei os números com atenção.",
        [
            "Diga 7:15, 8:30 e 13:45 em inglês.",
            "Pergunte a hora da aula e responda com um horário completo.",
        ],
    ),
    "questions": _pedagogy(
        "Fazer perguntas sobre pessoa, lugar, tempo e motivo na ordem correta.",
        "Crie uma pergunta com where e outra com when antes de rever a estrutura.",
        [
            "A ordem é question word + do/does + sujeito + verbo.",
            "Não use do/does com o verbo to be: diga Where are you?, não Where do you are?",
        ],
        "SPEAKING",
        "Imagine que conheceu alguém. Faça quatro perguntas usando question words diferentes.",
        "Where do you live? What do you do? When is your birthday? How are you?",
        "Usei pelo menos três question words e mantive a ordem das perguntas.",
        [
            "Faça uma pergunta com what, where, when e how.",
            "Reordene mentalmente: you / where / do / work?",
        ],
    ),
    "review": _pedagogy(
        "Combinar apresentação, rotina, família, horários e perguntas em uma conversa curta.",
        "Apresente-se e faça uma pergunta a um colega sem olhar nenhuma anotação.",
        [
            "Não tente traduzir palavra por palavra; use os blocos praticados.",
            "Em pergunta com does, retire o -s do verbo principal.",
        ],
        "SPEAKING",
        "Faça uma apresentação de 45 segundos e termine com duas perguntas ao interlocutor.",
        "Hi, I'm Leo. I work at a store and I start at nine. Where do you work?",
        "Combinei informações pessoais e perguntas numa fala contínua.",
        [
            "Apresente sua rotina em quatro frases.",
            "Faça duas perguntas e responda como se fosse o interlocutor.",
        ],
    ),
    "numbers": _pedagogy(
        "Usar números para informar idade, telefone, preço e quantidade.",
        "Diga sua idade e leia um número de telefone fictício em inglês.",
        [
            "Telefone costuma ser lido dígito por dígito.",
            "Não confunda -teen com -ty: fourteen e forty têm acentos diferentes.",
        ],
        "SPEAKING",
        "Diga sua idade, um preço e um telefone fictício como se estivesse preenchendo um cadastro.",
        "I'm thirty-two. It costs fifteen dollars. My number is five five five, zero one two three.",
        "Diferenciei dezenas de números terminados em -teen.",
        [
            "Leia em voz alta 13, 30, 14, 40, 15 e 50.",
            "Crie uma frase com idade, preço e quantidade.",
        ],
    ),
    "there-is-are": _pedagogy(
        "Descrever o que existe em um lugar usando there is e there are.",
        "Olhe ao redor: tente dizer uma coisa que existe e duas coisas que existem no ambiente.",
        [
            "Use there is no singular e there are no plural.",
            "Para perguntar, inverta: Is there…? / Are there…?",
        ],
        "WRITING",
        "Descreva um cômodo em quatro frases, incluindo afirmação, negativa e pergunta.",
        "There is a desk. There are two chairs. There isn't a TV. Is there a window?",
        "Diferenciei singular e plural em todas as frases.",
        [
            "Descreva seu quarto com there is e there are.",
            "Transforme There are two cafés em negativa e pergunta.",
        ],
    ),
    "prepositions-place": _pedagogy(
        "Localizar objetos usando in, on, under, next to, between e behind.",
        "Escolha um objeto próximo e diga onde ele está em relação a outro.",
        [
            "On indica contato com uma superfície; over pode indicar apenas posição acima.",
            "Between costuma ligar um item a dois pontos de referência.",
        ],
        "SPEAKING",
        "Descreva a posição de quatro objetos no ambiente sem apontar para eles.",
        "The phone is on the table. The bag is under the chair.",
        "Usei pelo menos três preposições diferentes.",
        [
            "Explique onde estão três objetos sem usar gestos.",
            "Compare in, on e under com exemplos novos.",
        ],
    ),
    "food-and-drinks": _pedagogy(
        "Expressar preferências e fazer um pedido simples de comida ou bebida.",
        "Diga uma comida de que gosta e uma de que não gosta.",
        [
            "Depois de like, use substantivo ou verbo em -ing conforme a ideia.",
            "Em pedidos, I'd like é mais natural e cortês do que I want.",
        ],
        "SPEAKING",
        "Simule um pedido: escolha uma bebida, uma comida e faça uma pergunta sobre o cardápio.",
        "I'd like a coffee and a sandwich, please. Do you have orange juice?",
        "Usei I'd like e finalizei o pedido com please.",
        [
            "Faça um pedido completo sem olhar o modelo.",
            "Diga duas coisas de que gosta e uma de que não gosta.",
        ],
    ),
    "can-abilities": _pedagogy(
        "Falar sobre habilidades e pedir permissão com can e can't.",
        "Diga duas coisas que você sabe fazer e uma que ainda não sabe.",
        [
            "Depois de can, use o verbo na forma base: can swim, não can to swim.",
            "Can não recebe -s com he ou she.",
        ],
        "SPEAKING",
        "Apresente três habilidades e faça um pedido de permissão adequado ao trabalho ou estudo.",
        "I can drive and I can cook, but I can't swim. Can I use your computer?",
        "Usei can/can't + verbo base em todas as frases.",
        [
            "Fale sobre três habilidades sem consultar.",
            "Transforme She can drive em pergunta e negativa.",
        ],
    ),
    "was-were": _pedagogy(
        "Descrever estados e localizações no passado com was e were.",
        "Tente dizer onde você estava ontem à noite e como se sentia.",
        [
            "I, he, she e it usam was; you, we e they usam were.",
            "Em perguntas, was/were vem antes do sujeito.",
        ],
        "WRITING",
        "Escreva quatro frases sobre ontem: onde você estava, com quem e como estava se sentindo.",
        "I was at home. My friends were there. We were tired, but the evening was fun.",
        "Combinei was e were de acordo com o sujeito.",
        [
            "Conte onde três pessoas estavam ontem.",
            "Transforme They were busy em pergunta e negativa.",
        ],
    ),
    "likes-ing": _pedagogy(
        "Falar sobre atividades de que gosta ou não gosta usando verbo + -ing.",
        "Liste mentalmente três atividades que você gosta de fazer.",
        [
            "Depois de like/love/hate, use -ing para atividades: like reading.",
            "A grafia pode mudar: run → running; dance → dancing.",
        ],
        "SPEAKING",
        "Fale sobre dois hobbies de que gosta, um de que não gosta e explique um motivo.",
        "I love cooking because it's relaxing. I like reading, but I hate running.",
        "Usei corretamente as formas em -ing.",
        [
            "Fale sobre três hobbies e um motivo.",
            "Forme o -ing de swim, write, study e dance.",
        ],
    ),
    "adverbs-frequency": _pedagogy(
        "Descrever a frequência de hábitos com always, usually, sometimes e never.",
        "Responda: com que frequência você estuda inglês, cozinha e faz exercícios?",
        [
            "Advérbios de frequência vêm antes do verbo principal, mas depois de to be.",
            "Never já é negativo; não use don't never.",
        ],
        "WRITING",
        "Escreva quatro frases verdadeiras sobre sua semana usando frequências diferentes.",
        "I usually study at night. I am always busy on Monday. I never work on Sunday.",
        "Posicionei o advérbio corretamente com verbo comum e com to be.",
        [
            "Crie uma frase com always, usually, sometimes e never.",
            "Corrija: I go always to work early e I don't never cook.",
        ],
    ),
    "everyday-phrases": _pedagogy(
        "Usar expressões de sobrevivência para pedir ajuda, repetição e esclarecimento.",
        "Imagine que não entendeu alguém. Que frase em inglês você tentaria usar?",
        [
            "Sorry? sozinho pode funcionar, mas Could you repeat that? é mais claro.",
            "I don't understand é correto; evite I not understand.",
        ],
        "SPEAKING",
        "Simule três problemas: não entendeu, precisa de ajuda e procura um lugar.",
        "Could you repeat that, please? Can you help me? Where is the restroom?",
        "Usei expressões completas e tom cortês.",
        [
            "Peça repetição de duas formas diferentes.",
            "Peça ajuda e pergunte onde fica um local.",
        ],
    ),
    "small-talk": _pedagogy(
        "Iniciar, sustentar e encerrar uma conversa social curta.",
        "Pense em uma pergunta segura para iniciar conversa com alguém que acabou de conhecer.",
        [
            "Small talk pede perguntas abertas e respostas com algum detalhe.",
            "Evite responder apenas yes/no; acrescente uma frase e devolva uma pergunta.",
        ],
        "SPEAKING",
        "Faça uma conversa de um minuto sobre o dia, trabalho/estudo e planos próximos.",
        "How's your day going? Pretty well. I'm finishing work. What about you?",
        "Fiz perguntas, desenvolvi respostas e encerrei com naturalidade.",
        [
            "Inicie conversa, faça uma continuação e encerre com cortesia.",
            "Transforme três respostas curtas em respostas que mantêm a conversa.",
        ],
    ),
    "final-review": _pedagogy(
        "Realizar uma interação A1 completa sobre identidade, rotina, preferências e necessidades.",
        "Fale por um minuto sobre você usando apenas o que consegue recuperar agora.",
        [
            "Priorize clareza e continuidade; não pare a cada pequeno erro.",
            "Use frases conhecidas como blocos e combine-as para criar mensagens novas.",
        ],
        "SPEAKING",
        "Faça uma apresentação de 90 segundos e inclua duas perguntas ao interlocutor.",
        "Hi, I'm Camila. I live in Recife and I work at a hospital. I usually start at eight…",
        "Integrei pelo menos quatro temas do A1 numa fala compreensível.",
        [
            "Apresente-se por 60 segundos sem modelo.",
            "Responda: rotina, família, habilidade, preferência e plano de hoje.",
        ],
    ),
}


def _review_lesson(slug: str, title: str, summary: str, questions: list[dict], task: dict) -> dict:
    return {
        "slug": slug,
        "title": title,
        "skill": "Review",
        "summary": summary,
        "theory": (
            "Esta missão mistura conteúdos anteriores. Primeiro tente recuperar cada padrão sem "
            "voltar às aulas. Depois use o feedback para decidir o que revisar. O objetivo não é "
            "decorar respostas, mas escolher estruturas conhecidas dentro de uma situação nova."
        ),
        "example": task["production_task"]["model"],
        "key_points": [
            "Recupere antes de reler.",
            "Explique por que escolheu cada forma.",
            "Termine produzindo uma mensagem própria.",
        ],
        "pedagogy": task,
        "questions": questions,
    }


CUMULATIVE_REVIEWS = {
    "Welcome": _review_lesson(
        "welcome-checkpoint",
        "Checkpoint: Meet Someone",
        "Integre saudações, pronomes, to be e artigos numa primeira conversa.",
        [
            {"type": "MCQ", "prompt": "Hi! I ___ Bruno.", "choices": ["is", "am", "are"], "correct_index": 1, "explanation": "I combina com am: I am Bruno."},
            {"type": "FILL_IN", "prompt": "This is Ana. ___ is my teacher.", "correct": "she", "accepted": ["she"], "explanation": "Ana é uma pessoa feminina no singular, então usamos she."},
            {"type": "ORDERING", "prompt": "Reorganize: an / is / engineer / he", "correct": "He is an engineer.", "explanation": "Sujeito + to be + artigo + profissão: He is an engineer."},
            {"type": "LISTENING", "prompt": "Ouça e escreva a apresentação.", "correct": "Hello, I am Alex. Nice to meet you.", "explanation": "A fala combina saudação, I am + nome e encerramento cortês."},
        ],
        _pedagogy(
            "Apresentar-se e apresentar outra pessoa numa conversa inicial.",
            "Apresente-se em duas frases e escolha um pronome para falar de outra pessoa.",
            ["Mantenha o sujeito antes de am/is/are.", "Escolha a/an pelo som inicial da palavra seguinte."],
            "SPEAKING",
            "Simule o primeiro encontro entre você e um colega. Apresente-se e apresente uma terceira pessoa.",
            "Hi, I'm Bia. Nice to meet you. This is Paulo. He is a teacher.",
            "Combinei saudação, to be, pronome e artigo numa interação.",
            ["Apresente-se sem modelo.", "Apresente duas pessoas usando he e she."],
        ),
    ),
    "Numbers & The World Around You": _review_lesson(
        "world-checkpoint",
        "Checkpoint: Around Town",
        "Use números, localização, existência e comida numa situação cotidiana.",
        [
            {"type": "MCQ", "prompt": "___ two cafés next to the bank.", "choices": ["There is", "There are", "It is"], "correct_index": 1, "explanation": "Two cafés é plural, então usamos There are."},
            {"type": "FILL_IN", "prompt": "The menu is ___ the table.", "correct": "on", "accepted": ["on"], "explanation": "On indica contato com a superfície da mesa."},
            {"type": "ORDERING", "prompt": "Reorganize: like / I'd / coffee / a", "correct": "I'd like a coffee.", "explanation": "I'd like + item é a forma cortês de fazer o pedido."},
            {"type": "LISTENING", "prompt": "Ouça e escreva a frase.", "correct": "The restaurant is next to the hotel.", "explanation": "Next to localiza o restaurante ao lado do hotel."},
        ],
        _pedagogy(
            "Pedir comida e compreender orientações simples sobre um local.",
            "Explique onde há um café próximo e faça um pedido simples.",
            ["There are acompanha plural.", "Em pedido cortês, prefira I'd like a I want."],
            "SPEAKING",
            "Imagine que está numa cidade nova: pergunte onde há um café e faça um pedido ao chegar.",
            "Is there a café near here? Yes, it's next to the hotel. I'd like a sandwich, please.",
            "Usei localização, there is/are e um pedido cortês.",
            ["Descreva três lugares da sua rua.", "Faça um pedido com comida, bebida e please."],
        ),
    ),
    "Abilities & Fun": _review_lesson(
        "abilities-checkpoint",
        "Checkpoint: Then & Now",
        "Combine habilidades, passado, preferências e frequência.",
        [
            {"type": "MCQ", "prompt": "She ___ swim, but she can't drive.", "choices": ["can", "cans", "is can"], "correct_index": 0, "explanation": "Can não muda com she e vem antes do verbo base."},
            {"type": "FILL_IN", "prompt": "We ___ at the park yesterday.", "correct": "were", "accepted": ["were"], "explanation": "We combina com were no passado de to be."},
            {"type": "ORDERING", "prompt": "Reorganize: usually / I / weekends / cook / on", "correct": "I usually cook on weekends.", "explanation": "Usually vem antes do verbo principal cook."},
            {"type": "LISTENING", "prompt": "Ouça e escreva a frase.", "correct": "I love reading, but I never read at work.", "explanation": "Love reading usa -ing; never vem antes do verbo read."},
        ],
        _pedagogy(
            "Comparar hábitos e habilidades atuais com uma situação passada.",
            "Diga algo que sabe fazer, um hobby e onde estava ontem.",
            ["Can usa verbo base sem to.", "Advérbio vem antes do verbo comum e depois de to be."],
            "WRITING",
            "Escreva cinco frases sobre suas habilidades, hobbies, frequência e o que aconteceu ontem.",
            "I can cook. I usually cook on weekends. I love trying new recipes. Yesterday I was busy.",
            "Integrei can, frequência, -ing e was/were corretamente.",
            ["Fale sobre duas habilidades e dois hobbies.", "Compare sua rotina atual com ontem."],
        ),
    ),
}


def apply_a1_extension(units: list[dict]) -> None:
    for unit in units:
        review = CUMULATIVE_REVIEWS.get(unit["title"])
        if review and not any(lesson["slug"] == review["slug"] for lesson in unit["lessons"]):
            unit["lessons"].append(review)
        for lesson in unit["lessons"]:
            pedagogy = PEDAGOGY_BY_SLUG.get(lesson["slug"])
            if pedagogy:
                lesson["pedagogy"] = pedagogy
