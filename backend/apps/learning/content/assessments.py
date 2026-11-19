"""Avaliações A1 paralelas para estimar evolução, sem finalidade de certificação."""


ASSESSMENTS = {
    "initial": {
        "title": "Ponto de partida A1",
        "description": (
            "Uma fotografia inicial de estruturas, vocabulário, escuta e organização de frases. "
            "O resultado orienta o estudo e não é certificado de nível."
        ),
        "questions": [
            {"id": "i1", "type": "MCQ", "prompt": "She ___ a nurse.", "choices": ["am", "is", "are"], "correct_index": 1, "explanation": "She combina com is.", "category": "GRAMMAR"},
            {"id": "i2", "type": "FILL_IN", "prompt": "I wake up ___ seven.", "correct": "at", "accepted": ["at"], "explanation": "Horários específicos usam at.", "category": "GRAMMAR"},
            {"id": "i3", "type": "ORDERING", "prompt": "Organize a pergunta: live / where / you / do", "correct": "Where do you live?", "explanation": "Question word + do + sujeito + verbo.", "category": "WORD_ORDER"},
            {"id": "i4", "type": "LISTENING", "prompt": "Ouça e escreva a frase.", "correct": "There are two chairs in the room.", "explanation": "There are apresenta elementos no plural.", "category": "LISTENING"},
            {"id": "i5", "type": "MCQ", "prompt": "Qual pedido é mais cortês?", "choices": ["I want coffee.", "Give me coffee.", "I'd like a coffee, please."], "correct_index": 2, "explanation": "I'd like… please é a forma cortês esperada.", "category": "COMPREHENSION"},
            {"id": "i6", "type": "FILL_IN", "prompt": "My parents are here. ___ are tired.", "correct": "they", "accepted": ["they"], "explanation": "Parents é plural e pode ser retomado por they.", "category": "VOCABULARY"},
        ],
        "speakingTask": "Apresente-se por até 60 segundos: nome, cidade, trabalho/estudo, rotina e uma preferência.",
        "writingTask": "Escreva de quatro a seis frases sobre você e faça uma pergunta ao leitor.",
    },
    "final": {
        "title": "Checkpoint final A1",
        "description": (
            "Uma avaliação paralela ao ponto de partida, com situações novas e a mesma matriz de "
            "habilidades. Compare os resultados como evidência de progresso, não certificação."
        ),
        "questions": [
            {"id": "f1", "type": "MCQ", "prompt": "They ___ my classmates.", "choices": ["am", "is", "are"], "correct_index": 2, "explanation": "They combina com are.", "category": "GRAMMAR"},
            {"id": "f2", "type": "FILL_IN", "prompt": "The class starts ___ nine thirty.", "correct": "at", "accepted": ["at"], "explanation": "Use at antes de um horário específico.", "category": "GRAMMAR"},
            {"id": "f3", "type": "ORDERING", "prompt": "Organize a pergunta: work / what time / start / do / you", "correct": "What time do you start work?", "explanation": "What time + do + you + verbo + complemento.", "category": "WORD_ORDER"},
            {"id": "f4", "type": "LISTENING", "prompt": "Ouça e escreva a frase.", "correct": "There is a small café next to the bank.", "explanation": "There is apresenta um café no singular; next to indica posição.", "category": "LISTENING"},
            {"id": "f5", "type": "MCQ", "prompt": "Você não entendeu. Qual resposta mantém a conversa?", "choices": ["Could you repeat that, please?", "I no understand.", "Repeat."], "correct_index": 0, "explanation": "A pergunta completa com please é clara e cortês.", "category": "COMPREHENSION"},
            {"id": "f6", "type": "FILL_IN", "prompt": "This is my sister. ___ name is Paula.", "correct": "her", "accepted": ["her"], "explanation": "Her é o possessivo correspondente a she.", "category": "VOCABULARY"},
        ],
        "speakingTask": "Fale por até 60 segundos sobre você, sua rotina e um lugar próximo; termine fazendo uma pergunta.",
        "writingTask": "Escreva de quatro a seis frases sobre sua semana, uma habilidade e uma preferência.",
    },
}
