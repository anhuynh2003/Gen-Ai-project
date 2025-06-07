# utils/quote_handler.py
import random

def get_comforting_quote():
    quotes = [
        "This too shall pass.",
        "Even the darkest night will end and the sun will rise. – Victor Hugo",
        "You are not alone in this.",
        "Feelings are just visitors. Let them come and go. – Mooji",
        "You’ve survived 100% of your worst days."
    ]
    return random.choice(quotes)