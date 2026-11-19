"""Correções de equilíbrio comunicativo nos níveis A2 a C2."""


B2_REVIEW = {
    "slug": "b2-integration-review",
    "title": "B2 Integration Lab",
    "skill": "Review",
    "summary": "Integre narrativa, hipótese, estruturas avançadas e fluência natural.",
    "theory": (
        "No B2, a decisão importante não é apenas formar uma estrutura, mas escolhê-la para "
        "organizar significado. Narre distinguindo cenário, evento e passado anterior; trate "
        "hipóteses pelo grau de realidade; use passiva e causativa quando o foco não está no "
        "agente; e conecte ideias com colocações e marcadores naturais. Nesta revisão, identifique "
        "primeiro a intenção comunicativa e só depois escolha a forma."
    ),
    "example": (
        "If I'd checked the forecast, I wouldn't have got soaked; by the time I arrived, "
        "the meeting had already been moved online."
    ),
    "key_points": [
        "Escolha tempos narrativos pela função na história.",
        "Diferencie hipótese passada, presente e mista.",
        "Use estruturas avançadas para mudar foco, não para ornamentar.",
        "Conecte e qualifique argumentos com naturalidade.",
    ],
    "pedagogy": {
        "objective": "Sustentar uma narrativa e um argumento B2 usando escolhas gramaticais coerentes.",
        "activation_prompt": "Conte um contratempo e explique o que teria mudado o resultado.",
        "common_mistakes": [
            "Não misture referências temporais sem definir o ponto de vista da narrativa.",
            "Em condicionais, escolha a combinação pelo sentido, não por uma fórmula isolada.",
        ],
        "production_task": {
            "mode": "SPEAKING",
            "prompt": "Conte um problema real, explique suas causas e proponha uma alternativa usando pelo menos uma hipótese.",
            "model": "I had been working against the clock when the system crashed. If we'd kept a backup, we wouldn't have lost the draft.",
            "checklist": [
                "Organizei claramente contexto, evento e consequência.",
                "Usei uma condicional coerente com a referência temporal.",
                "Conectei as ideias sem listar frases soltas.",
            ],
        },
        "review_prompts": [
            "Reconstrua uma história usando simple, continuous e perfect.",
            "Explique a diferença entre uma terceira condicional e uma condicional mista.",
        ],
    },
    "questions": [
        {"type": "MCQ", "prompt": "By the time help arrived, we ___ for over two hours.", "choices": ["had been waiting", "were waiting", "have waited", "waited"], "correct_index": 0, "explanation": "A duração começou antes de outro ponto passado: past perfect continuous."},
        {"type": "FILL_IN", "prompt": "If I had read the contract, I ___ (not/sign) it.", "correct": "wouldn't have signed", "accepted": ["wouldn't have signed", "would not have signed"], "explanation": "Consequência passada irreal: would have + particípio."},
        {"type": "MCQ", "prompt": "I need a professional to repair the roof. I need to ___.", "choices": ["have the roof repaired", "repair the roof myself", "have repaired the roof", "get the roof repair"], "correct_index": 0, "explanation": "Have + objeto + particípio indica serviço realizado por outra pessoa."},
        {"type": "ORDERING", "prompt": "Reorganize: point / having / said / that / I / see / your", "correct": "Having said that, I see your point.", "explanation": "Having said that introduz contraste; I see your point reconhece o argumento."},
        {"type": "LISTENING", "prompt": "Ouça e escreva a frase.", "correct": "If I were you, I'd look into it before making a decision.", "explanation": "A frase combina conselho hipotético, phrasal verb e before + -ing."},
    ],
}


C2_CONVERSATIONS = [
    {
        "unit": "The Architecture of English",
        "lesson": {
            "slug": "c2-diplomatic-disagreement",
            "title": "Disagree Without Derailing",
            "skill": "Conversation",
            "summary": "Discorde com precisão, preserve a relação e negocie pressupostos.",
            "theory": (
                "Discordância C2 raramente é um simples yes ou no. Falantes experientes separam "
                "a pessoa da premissa, concedem o ponto válido e delimitam exatamente onde a "
                "inferência deixa de funcionar: 'I take your point about cost; where I part "
                "company with you is on timing.' Hedging não significa fraqueza: 'I'm not "
                "entirely persuaded that...' reduz atrito enquanto mantém a posição. O objetivo "
                "é tornar o desacordo discutível, não torná-lo invisível."
            ),
            "example": "I take your point; I'm not convinced, though, that the evidence warrants that conclusion.",
            "key_points": [
                "Conceda o ponto válido antes de delimitar a divergência.",
                "Ataque a premissa ou inferência, não a pessoa.",
                "Use hedging para calibrar força, não para esconder a posição.",
            ],
            "dialogue": [
                {"speaker": "Maya", "line": "Given the figures, postponing the launch seems unavoidable."},
                {"speaker": "Jon", "line": "I take your point about the figures. I'm not convinced postponement is the only inference, though."},
                {"speaker": "Maya", "line": "What alternative do you see?"},
                {"speaker": "Jon", "line": "A limited release would address the risk without sacrificing the entire window."},
                {"speaker": "Maya", "line": "That's fair, although it assumes support can absorb the extra load."},
                {"speaker": "Jon", "line": "Agreed. That's the assumption we need to test before deciding."},
            ],
            "questions": [
                {"type": "MCQ", "prompt": "Qual resposta discorda sem atacar o interlocutor?", "choices": ["That's nonsense.", "I take your point; where I differ is on the likely outcome.", "You clearly haven't understood.", "No, you're wrong."], "correct_index": 1, "explanation": "A resposta concede parte do argumento e delimita a divergência."},
                {"type": "FILL_IN", "prompt": "I'm not entirely ___ that the data supports that claim.", "correct": "convinced", "accepted": ["convinced", "persuaded"], "explanation": "Not entirely convinced/persuaded calibra discordância firme e diplomática."},
                {"type": "ORDERING", "prompt": "Reorganize: company / where / part / I / you / with / is / timing / on", "correct": "Where I part company with you is on timing.", "explanation": "A cleft delimita com precisão o ponto de desacordo."},
                {"type": "MCQ", "prompt": "Em 'That's fair, although...', qual é a função de That's fair?", "choices": ["Conceder validade parcial", "Encerrar o assunto", "Ironizar o interlocutor", "Concordar integralmente"], "correct_index": 0, "explanation": "A expressão reconhece um ponto válido antes de introduzir a reserva."},
                {"type": "LISTENING", "prompt": "Ouça e escreva a frase.", "correct": "I see the logic, but I question the assumption behind it.", "explanation": "A fala reconhece a lógica e desloca a crítica para o pressuposto."},
            ],
        },
    },
    {
        "unit": "Style & Rhetoric",
        "lesson": {
            "slug": "c2-humor-implication",
            "title": "Read the Room",
            "skill": "Conversation",
            "summary": "Interprete ironia, subtexto e humor sem perder o contexto social.",
            "theory": (
                "No C2, muito do significado conversacional está no que o falante escolhe não "
                "dizer diretamente. 'Well, that went brilliantly' depois de um desastre depende "
                "da incompatibilidade entre palavras e contexto. Understatement como 'not ideal' "
                "pode comunicar crítica intensa; humor seco depende de entrega neutra. Antes de "
                "interpretar literalmente, verifique situação, entonação, relação entre falantes "
                "e conhecimento compartilhado. Ironia sem contexto é ambígua por definição."
            ),
            "example": "The server crashed five minutes before launch. So, impeccable timing as always.",
            "key_points": [
                "Compare palavras ao contexto para detectar ironia.",
                "Understatement pode intensificar uma crítica.",
                "Entonação e relação social alteram a leitura.",
            ],
            "dialogue": [
                {"speaker": "Leah", "line": "The projector died halfway through my presentation."},
                {"speaker": "Sam", "line": "Excellent. Exactly the kind of support one hopes for."},
                {"speaker": "Leah", "line": "I know. The timing was almost artistic."},
                {"speaker": "Sam", "line": "Did the audience take it well?"},
                {"speaker": "Leah", "line": "Let's just say their enthusiasm was understated."},
                {"speaker": "Sam", "line": "That bad, then?"},
            ],
            "questions": [
                {"type": "MCQ", "prompt": "O que Sam realmente comunica com 'Excellent' após a falha?", "choices": ["Aprovação genuína", "Crítica irônica à situação", "Dúvida técnica", "Surpresa positiva"], "correct_index": 1, "explanation": "O elogio entra em conflito com o contexto negativo e funciona como ironia."},
                {"type": "FILL_IN", "prompt": "Descrever um desastre como 'not ___' é um understatement comum.", "correct": "ideal", "accepted": ["ideal", "great"], "explanation": "Not ideal/not great minimiza na forma e intensifica pelo contraste contextual."},
                {"type": "ORDERING", "prompt": "Reorganize: timing / impeccable / as / always", "correct": "Impeccable timing, as always.", "explanation": "O elogio exagerado ganha leitura irônica no contexto de uma falha recorrente."},
                {"type": "MCQ", "prompt": "Qual pista é insuficiente sozinha para confirmar ironia?", "choices": ["A frase isolada sem contexto", "Contraste com a situação", "Entonação do falante", "Conhecimento compartilhado"], "correct_index": 0, "explanation": "Sem contexto, a frase isolada pode admitir leitura literal ou irônica."},
                {"type": "LISTENING", "prompt": "Ouça e escreva a frase.", "correct": "Well, that could hardly have gone better.", "explanation": "Dependendo do contexto e entonação, o elogio extremo comunica o oposto."},
            ],
        },
    },
    {
        "unit": "Translation Traps & Final Mastery",
        "lesson": {
            "slug": "c2-high-stakes-conversation",
            "title": "When Every Word Counts",
            "skill": "Conversation",
            "summary": "Gerencie conversas sensíveis, esclareça compromissos e encerre com precisão.",
            "theory": (
                "Conversas de alto risco exigem precisão pragmática: nomear o problema sem "
                "inflamá-lo, testar entendimento e transformar acordo abstrato em compromisso "
                "verificável. 'Let me make sure I've understood...' previne falsa concordância; "
                "'What I'm hearing is...' explicita a interpretação; 'Can we agree that X will "
                "happen by Friday?' fecha responsabilidade e prazo. Linguagem sofisticada não é "
                "o objetivo — clareza, face e consequência são."
            ),
            "example": "Let me make sure I've understood: you'll revise the proposal, and we'll reconvene on Thursday.",
            "key_points": [
                "Parafraseie para testar entendimento.",
                "Separe observação, impacto e pedido.",
                "Feche acordos com responsável, ação e prazo.",
            ],
            "dialogue": [
                {"speaker": "Nora", "line": "We're now two weeks behind, and the client hasn't been informed."},
                {"speaker": "Eli", "line": "I understand the concern. What I'm hearing is that the communication gap is now the immediate risk."},
                {"speaker": "Nora", "line": "Exactly. I need clarity on who contacts them and when."},
                {"speaker": "Eli", "line": "I'll draft the update today and send it to you by four for approval."},
                {"speaker": "Nora", "line": "Good. Can we agree it goes to the client no later than ten tomorrow?"},
                {"speaker": "Eli", "line": "Agreed. I'll own the send and confirm once it's done."},
            ],
            "questions": [
                {"type": "MCQ", "prompt": "Qual fechamento produz um compromisso verificável?", "choices": ["Let's stay in touch.", "We'll try our best.", "I'll send the update by ten tomorrow and confirm delivery.", "Something should happen soon."], "correct_index": 2, "explanation": "A frase define responsável, ação, prazo e confirmação."},
                {"type": "FILL_IN", "prompt": "Let me make sure I've ___ you correctly.", "correct": "understood", "accepted": ["understood", "heard"], "explanation": "A fórmula abre uma paráfrase para confirmar entendimento."},
                {"type": "ORDERING", "prompt": "Reorganize: hearing / what / is / I'm / communication / that / risk / the / is", "correct": "What I'm hearing is that communication is the risk.", "explanation": "What I'm hearing is... explicita a interpretação antes de agir."},
                {"type": "MCQ", "prompt": "Em uma conversa sensível, qual sequência reduz defensividade?", "choices": ["Acusação → ultimato → silêncio", "Observação → impacto → pedido específico", "Opinião → julgamento → ameaça", "Elogio → evasão → assunto novo"], "correct_index": 1, "explanation": "A sequência mantém foco em fatos, consequências e ação futura."},
                {"type": "LISTENING", "prompt": "Ouça e escreva a frase.", "correct": "Can we agree on who will do what by Friday?", "explanation": "A pergunta converte concordância abstrata em responsabilidade e prazo."},
            ],
        },
    },
]


def add_b2_review(units: list[dict]) -> None:
    final_unit = units[-1]
    if not any(lesson["slug"] == B2_REVIEW["slug"] for lesson in final_unit["lessons"]):
        final_unit["lessons"].append(B2_REVIEW)


def add_c2_conversations(units: list[dict]) -> None:
    units_by_title = {unit["title"]: unit for unit in units}
    for addition in C2_CONVERSATIONS:
        lessons = units_by_title[addition["unit"]]["lessons"]
        if not any(lesson["slug"] == addition["lesson"]["slug"] for lesson in lessons):
            lessons.append(addition["lesson"])


def reclassify_skills(units: list[dict], mapping: dict[str, str]) -> None:
    for unit in units:
        for lesson in unit["lessons"]:
            if lesson["slug"] in mapping:
                lesson["skill"] = mapping[lesson["slug"]]
