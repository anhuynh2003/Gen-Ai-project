# utils/journaling_prompts.py
def get_prompt_by_emotion(emotion):
    prompts = {
        "😊 Positive": "What has been bringing you joy recently?",
        "😢 Negative": "What's weighing on you the most right now?",
        "😐 Neutral": "What are you curious about exploring emotionally today?"
    }
    return prompts.get(emotion, "How are you feeling today, really?")
