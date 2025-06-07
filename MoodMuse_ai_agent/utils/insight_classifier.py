# utils/insight_classifier.py
import re

def classify_topic(text):
    patterns = {
        "Relationship": ["breakup", "dating", "partner", "love", "boyfriend", "girlfriend"],
        "School": ["exam", "school", "professor", "class", "grades"],
        "Work": ["job", "career", "boss", "burnout", "promotion"],
        "Self": ["identity", "confidence", "purpose", "lost", "self-worth"]
    }
    for topic, keywords in patterns.items():
        if any(re.search(rf"\\b{kw}\\b", text, re.IGNORECASE) for kw in keywords):
            return topic
    return "General"