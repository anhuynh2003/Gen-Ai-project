# utils/crisis_detector.py

def is_crisis(text):
    crisis_keywords = [
        # Direct and severe
        "suicidal", "kill myself", "end it all", "want to die",
        "no reason to live", "give up", "can't go on", "i'm done",
        "ending everything", "wish i were dead", "tired of living",
        "nothing matters", "life is meaningless", "no way out",
        "don't want to be here", "i want it to stop",

        # Emotional despair
        "i hate my life", "everything hurts", "i feel numb",
        "my heart is heavy", "i feel empty", "broken inside",
        "overwhelmed", "i'm drowning", "lost all hope",
        "i cry every night", "can't stop crying",

        # Loneliness & isolation
        "nobody cares", "no one would notice", "i feel invisible",
        "everyone would be better off", "i’m all alone",
        "i feel unwanted", "no one loves me", "abandoned",
        "i have no one", "i feel disconnected",

        # Burnout & mental exhaustion
        "i'm exhausted mentally", "i can't do this anymore",
        "i can't keep pretending", "so tired of everything",
        "everything is falling apart", "i can’t take this",
        "i can’t breathe emotionally", "my mind won’t stop",

        # Self-harm and despair language
        "hurt myself", "cutting again", "i bled last night",
        "relapsed", "pain makes me feel alive", "i deserve this pain",
        "it's the only way", "this is my last message"
    ]

    return any(kw in text.lower() for kw in crisis_keywords)
