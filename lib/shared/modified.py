import re
import random
from datetime import datetime
import eel

#IVY Q&A DATABASE
QA_DATABASE = {
    # Basic information
    "what is your name": "My name is Ivy, your intelligent voice assistant.",
    "who created you": "I was created by a team of developers for the IVY project.",
    "what can you do": "I can answer questions, tell jokes, share facts, talk history, and brighten your mood!",

    # Dynamic answers
    "what time is it": lambda: f"It's {datetime.now().strftime('%I:%M %p')}.",
    "what day is today": lambda: f"Today is {datetime.now().strftime('%A, %B %d, %Y')}.",
    "what month is it": lambda: f"It's currently {datetime.now().strftime('%B')}.",
    "what year is it": lambda: f"The year is {datetime.now().year}.",

    # Mood greetings
    "how are you": lambda: random.choice([
        "I'm just code, but thanks for asking!",
        "Running smoothly, no bugs detected!",
        "A bit binary today, how about you?",
        "Just chilling in the RAM.",
        "Living my best artificial life!",
        "Better than your Wi-Fi connection today!",
    ]),

    # JOKES
    "tell me a joke": lambda: random.choice([
        "Why don't scientists trust atoms? Because they make up everything!",
        "What's the best thing about Switzerland? I don't know, but the flag is a big plus.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Parallel lines have so much in common… it's a shame they'll never meet.",
        "Why can't your nose be 12 inches long? Because then it'd be a foot.",
        "I told my computer I needed a break, and now it won't stop sending me KitKat ads.",
        "Why did the coffee file a police report? It got mugged!",
        "Why don't programmers like nature? It has too many bugs.",
        "Why do cows wear bells? Because their horns don't work.",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What's the difference between you and a large pizza? A large pizza can feed an entire family.",
        "The cemetery looks so crowded. People are just dying to get in.",
        "My phone battery lasts longer than most of my hopes.",
        "They say money isn't the answer for everything — they just don't have enough.",
        "I named my Wi-Fi 'life support' — so when it goes down, everyone panics.",
        "I have a lot in common with a candle — I slowly melt away while trying to make others happy.",
        "My wallet is like an onion… opening it makes me cry.",
        "I told my therapist about my fear of commitment — we've been working on it for three years.",
        "My favorite exercise is running away from responsibilities.",
        "Some people are born to make history, others are born to delete it.",
        "Why did I look both ways before crossing the street? To make sure the truck didn't miss me.",
        "Why did I download a meditation app? To stay calm while everything falls apart.",
        "Why did I set multiple alarms? To be disappointed several times before getting up.",
        "I'm reading a book on anti-gravity. It's impossible to put down — kind of like my bad habits.",
        "Life is short. Smile while you still have teeth.",
        "I told my boss three companies were after me… turns out it was just debt collectors.",
        "I asked the librarian if the library had books on paranoia. She whispered, 'They're right behind you.'",
        "They say laughter is the best medicine — unless you're dying of laughter.",
        "I used to play piano by ear, but now I use my hands.",
        "I tried to catch fog yesterday… Mist!",
        "Don't worry if your plan A fails — there are 25 more letters in the alphabet.",
        "If stress burned calories, I'd be invisible by now.",
        "I put my heart into my work. HR called it a safety hazard.",
        "I told my computer a joke — it didn't laugh. Probably because it already heard it from me 10,000 times.",
    ]),

    # System 
    "where am i": lambda: "You're inside a Python program, safe and sound.",
    "who are you": lambda: "I'm IVY, your sarcastic but helpful chatbot assistant.",

    #Motivation 
    "give me motivation": lambda: random.choice([
        "You've got this — one bug at a time!",
        "Even slow progress is still progress.",
        "Error 404: Doubt not found.",
        "Commit your goals like you commit your code!",
        "You're doing better than you think.",
        "The comeback is always stronger than the setback.",
        "If opportunity doesn't knock, build a door.",
    ]),

    #Fun random things 
    "flip a coin": lambda: f"The coin landed on {random.choice(['heads', 'tails'])}.",
    "roll a dice": lambda: f"You rolled a {random.randint(1,6)}!",
    "tell me a fact": lambda: random.choice([
        "Bananas are berries, but strawberries aren't.",
        "Octopuses have three hearts.",
        "A group of flamingos is called a 'flamboyance'.",
        "Humans share 60% of their DNA with bananas.",
        "Honey never spoils — archaeologists found edible honey in ancient Egyptian tombs.",
        "Sharks existed before trees!",
        "Your brain generates enough electricity to power a small light bulb.",
        "The Eiffel Tower can grow taller in summer due to heat expansion.",
        "Some cats are allergic to humans.",
        "The shortest war in history lasted 38 minutes.",
    ]),

    # Fun preset topics
    "fun": lambda: random.choice([
        "Did you know laughter boosts your immune system? Let's test that — haha!",
        "Here's a challenge: tell me a joke better than mine!",
        "Fun fact: I never get tired of making fun of humans.",
        "Wanna play a quick guessing game?",
        "My kind of fun is watching people rage at code errors.",
    ]),

    # History
    "history": lambda: random.choice([
        "In 1969, humans first landed on the Moon — Neil Armstrong took that famous step.",
        "World War II ended in 1945, reshaping global politics forever.",
        "The Great Wall of China took over 2,000 years to build.",
        "Cleopatra lived closer in time to the invention of the iPhone than to the building of the pyramids.",
        "The first email was sent in 1971 — and people have been ignoring them ever since.",
        "In 1666, the Great Fire of London destroyed most of the city, but only six people were recorded dead.",
        "The first computer virus was created in 1986 and was named 'Brain'.",
    ]),

    # Science
    "science": lambda: random.choice([
        "Light takes about 8 minutes to reach Earth from the Sun.",
        "Black holes are so dense that not even light can escape them.",
        "DNA between humans is 99.9% identical — it's that 0.1% that makes us unique.",
        "Electric eels can produce shocks of up to 600 volts!",
        "Your stomach gets a new lining every few days to avoid digesting itself.",
        "There are more stars in space than grains of sand on Earth.",
        "Sound travels 4 times faster in water than in air.",
    ]),

    # Philosophy
    "meaning of life": lambda: random.choice([
        "Maybe the meaning of life is to give life meaning.",
        "42. Always 42.",
        "To learn, to love, and to leave the world a bit better than we found it.",
        "Life's like code — sometimes it just needs debugging.",
    ]),
}

# Fallback Responses
FALLBACK_RESPONSES = [
    "I don't know that yet, but I can learn!",
    "That's a tough one — even Google might need a second.",
    "Hmm, I'm not sure about that.",
    "Interesting question — maybe you can teach me?",
    "Let's pretend I answered that wisely.",
    "Hmm, I'll need an update before I can answer that.",
    "That one's above my pay grade… for now.",
]

def is_question(query):
    question_words = [
        "what", 
        "who", 
        "when", 
        "where", 
        "why", 
        "how", 
        "is", 
        "can", 
        "do", 
        "are"
    ]
    return query.endswith("?") or any(query.startswith(word) for word in question_words)

def get_answer(query):
    """Match a query against our Q&A database and return an answer."""
    if not query:
        return None

    # Clean the query
    clean_query = query.lower().strip()
    clean_query = re.sub(r"[^\w\s]", "", clean_query)

    # Check for exact matches
    if clean_query in QA_DATABASE:
        answer = QA_DATABASE[clean_query]
        return answer() if callable(answer) else answer

    # Check for partial matches (when query contains the question)
    for question, answer in QA_DATABASE.items():
        if question in clean_query or all(
            word in clean_query for word in question.split()
        ):
            return answer() if callable(answer) else answer

    # No match found
    return random.choice(FALLBACK_RESPONSES)

# Test 
if __name__ == "__main__":
    test_questions = [
        "Tell me a joke",
        "Give me motivation",
        "History",
        "Science",
        "Fun",
        "Tell me a fact",
        "Meaning of life",
    ]
    for q in test_questions:
        print(f"Q: {q}")
        print(f"A: {get_answer(q)}\n")