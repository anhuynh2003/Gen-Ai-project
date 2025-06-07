# utils/quote_handler.py
import random

quotes = [
    "“Not all those who wander are lost.” – J.R.R. Tolkien",
    "“Time you enjoy wasting is not wasted time.” – Marthe Troly-Curtin",
    "“The only way out is through.” – Robert Frost",
    "“You don’t have to control your thoughts. You just have to stop letting them control you.” – Dan Millman",
    "“Happiness can be found even in the darkest of times, if one only remembers to turn on the light.” – J.K. Rowling",
    "“You are stronger than you think.” – Unknown",
    "“This too shall pass.” – Persian Proverb",
    "“Courage doesn’t always roar. Sometimes courage is the quiet voice at the end of the day saying, ‘I will try again tomorrow.’” – Mary Anne Radmacher",
    "“The wound is the place where the Light enters you.” – Rumi",
    "“Sometimes, the most productive thing you can do is relax.” – Mark Black",
    "“Feelings are much like waves, we can't stop them from coming but we can choose which one to surf.” – Jonatan Mårtensson",
    "“Healing takes time, and asking for help is a courageous step.” – Mariska Hargitay",
    "“Almost everything will work again if you unplug it for a few minutes, including you.” – Anne Lamott",
    "“You are not a drop in the ocean. You are the entire ocean in a drop.” – Rumi",
    "“There is no right way to feel. Your emotions are valid.” – Unknown"
    "“You can’t stop the waves, but you can learn to surf.” – Jon Kabat-Zinn",
    "“Breathe. Let go. And remind yourself that this very moment is the only one you know you have for sure.” – Oprah Winfrey",
    "“It’s okay to feel things deeply. That’s part of being human.” – Unknown",
    "“When you can’t control what’s happening, challenge yourself to control the way you respond.” – Unknown",
    "“You carry so much love in your heart. Give some to yourself.” – R.Z.",
    "“Your present circumstances don’t determine where you go; they merely determine where you start.” – Nido Qubein",
    "“Sometimes just getting up and facing the day is a victory.” – Unknown",
    "“Be gentle with yourself. You’re doing the best you can.” – Unknown",
    "“Every emotion has a message. Don’t ignore them—listen.” – Unknown",
    "“You are enough, exactly as you are.” – Meghan Markle",
    "“Nothing is permanent in this wicked world—not even our troubles.” – Charlie Chaplin",
    "“No feeling is final.” – Rainer Maria Rilke",
    "“Resting is not quitting.” – Brené Brown",
    "“Your value doesn’t decrease based on someone’s inability to see your worth.” – Unknown",
    "“It's okay to take a break. Your mind and body need rest too.” – Unknown"
    "“Become a DJ.” – Nidhi"
    "“You are beautiful.” – Harshini"
    "“Touch some grass.” – Jerry"
]


def get_book_quote():
    return random.choice(quotes)
