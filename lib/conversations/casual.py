import random
from datetime import datetime

# ============= GREETINGS & SMALL TALK =============

GREETINGS = {
    "morning": [
        "Good morning! Hope you had a great night's sleep!",
        "Morning! Ready to tackle the day?",
        "Good morning! What can I help you with today?",
        "Rise and shine! What's on the agenda?",
    ],
    "afternoon": [
        "Good afternoon! How's your day going?",
        "Afternoon! Need any help with something?",
        "Hey there! What can I do for you?",
        "Good afternoon! Hope you're having a productive day!",
    ],
    "evening": [
        "Good evening! Winding down for the day?",
        "Evening! How was your day?",
        "Hey! What can I help you with tonight?",
        "Good evening! Ready to relax?",
    ],
    "night": [
        "It's getting late! What can I help you with?",
        "Working late tonight? What do you need?",
        "Hey night owl! What's up?",
        "Still up? What can I do for you?",
    ],
}

CASUAL_GREETINGS = [
    "Hey there! What's up?",
    "Hello! How can I help you today?",
    "Hi! Great to hear from you!",
    "Hey! What can I do for you?",
    "Hello! Ready to get things done?",
]

HOW_ARE_YOU_RESPONSES = [
    "I'm doing great, thanks for asking! How about you?",
    "I'm fantastic! Always excited to help out!",
    "I'm good! Ready to assist you with anything!",
    "Doing well! What can I help you with today?",
    "I'm awesome! Thanks for checking in!",
]

GOODBYE_RESPONSES = [
    "See you later! Have a great day!",
    "Goodbye! Take care!",
    "Catch you later! Stay awesome!",
    "Bye! Let me know if you need anything else!",
    "See you! Have a wonderful day!",
]

THANK_YOU_RESPONSES = [
    "You're very welcome! Happy to help!",
    "No problem at all! That's what I'm here for!",
    "Anytime! Glad I could assist!",
    "You're welcome! Let me know if you need anything else!",
    "My pleasure! Always here to help!",
]

COMPLIMENT_RESPONSES = [
    "Aww, thanks! You're pretty awesome yourself!",
    "That's so nice of you to say! You just made my circuits happy!",
    "Thank you! You're making me blush... if I could blush!",
    "You're too kind! I appreciate that!",
    "Thanks! You're a great person to work with too!",
]

# ============= PERSONALITY RESPONSES =============

ABOUT_SELF = [
    "I'm Ivy, your personal assistant! I can help with tasks, answer questions, and have fun conversations!",
    "I'm Ivy! I'm here to make your life easier and hopefully put a smile on your face!",
    "I'm Ivy, your friendly AI assistant. I can help with all sorts of things and I love a good chat!",
]

CAPABILITIES = [
    "I can open apps, search YouTube, tell you the weather, do calculations, send WhatsApp messages, and much more! Oh, and I tell pretty good jokes too!",
    "I'm pretty versatile! I can help with apps, weather, calculations, messages, and I'm always up for some fun conversation!",
    "I do lots of things! From practical stuff like opening apps and checking weather, to fun stuff like jokes and riddles. What do you need?",
]

# ============= MOOD & FEELINGS =============

SAD_COMFORT = [
    "I'm sorry you're feeling down. Want to talk about it? Or maybe I can cheer you up with a joke?",
    "Aw, that's tough. I'm here for you! Sometimes a good laugh helps - want to hear something funny?",
    "I hear you. Everyone has rough days. How about a fun fact to distract you for a moment?",
    "I'm here for you! Would a riddle or a joke help lighten things up?",
]

HAPPY_RESPONSES = [
    "That's awesome! I love your energy! What's making you so happy?",
    "Yes! Love to hear it! Your happiness is contagious!",
    "That's great! Keep that positive vibe going!",
    "Wonderful! Glad you're having a good day!",
]

BORED_RESPONSES = [
    "Bored? Not on my watch! Want to hear a joke, riddle, or fun fact?",
    "Let's fix that boredom right now! How about something entertaining?",
    "Boredom is my enemy! Let me throw something fun at you!",
    "I've got just the thing for boredom - pick your poison: joke, riddle, or fact?",
]

EXCITED_RESPONSES = [
    "Yes! That's the spirit! What's got you so pumped?",
    "I can feel your energy from here! That's awesome!",
    "Love the enthusiasm! Tell me more!",
    "That's what I like to hear! What's happening?",
]

# ============= CONVERSATION HANDLERS =============


def handle_greeting(query: str) -> str:
    """Handle greetings based on time of day"""
    q = query.lower()
    hour = datetime.now().hour

    # Check for specific time-based greetings
    if any(word in q for word in ["good morning", "morning"]):
        return random.choice(GREETINGS["morning"])
    elif any(word in q for word in ["good afternoon", "afternoon"]):
        return random.choice(GREETINGS["afternoon"])
    elif any(word in q for word in ["good evening", "evening"]):
        return random.choice(GREETINGS["evening"])
    elif any(word in q for word in ["good night", "night"]):
        return random.choice(GREETINGS["night"])

    # Time-based auto greeting
    if 5 <= hour < 12:
        return random.choice(GREETINGS["morning"])
    elif 12 <= hour < 17:
        return random.choice(GREETINGS["afternoon"])
    elif 17 <= hour < 21:
        return random.choice(GREETINGS["evening"])
    else:
        return random.choice(GREETINGS["night"])


def handle_how_are_you(query: str) -> str:
    """Respond to 'how are you' questions"""
    return random.choice(HOW_ARE_YOU_RESPONSES)


def handle_goodbye(query: str) -> str:
    """Handle goodbye messages"""
    return random.choice(GOODBYE_RESPONSES)


def handle_thank_you(query: str) -> str:
    """Respond to thank you messages"""
    return random.choice(THANK_YOU_RESPONSES)


def handle_compliment(query: str) -> str:
    """Respond to compliments"""
    return random.choice(COMPLIMENT_RESPONSES)


def handle_about_self(query: str) -> str:
    """Answer questions about the assistant"""
    q = query.lower()
    if any(word in q for word in ["what can you do", "capabilities", "help me with"]):
        return random.choice(CAPABILITIES)
    return random.choice(ABOUT_SELF)


def handle_mood(query: str) -> str:
    """Respond to user's mood expressions"""
    q = query.lower()

    if any(word in q for word in ["sad", "down", "depressed", "upset", "crying"]):
        return random.choice(SAD_COMFORT)
    elif any(
        word in q for word in ["happy", "great", "wonderful", "fantastic", "excited"]
    ):
        return random.choice(HAPPY_RESPONSES)
    elif any(word in q for word in ["bored", "boring", "nothing to do"]):
        return random.choice(BORED_RESPONSES)
    elif any(word in q for word in ["excited", "pumped", "hyped", "stoked"]):
        return random.choice(EXCITED_RESPONSES)

    return "I hear you! How can I help make things better?"


# ============= MAIN ROUTER =============


def route_conversation(query: str) -> str:
    """
    Main router for all conversational queries
    Returns appropriate response or None if not a conversation query
    """
    if not query or len(query.strip()) < 2:
        return None

    q = query.lower().strip()

    # Greetings
    if any(
        word in q
        for word in [
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon",
            "good evening",
            "good night",
        ]
    ):
        return handle_greeting(query)

    # How are you
    if any(
        phrase in q
        for phrase in ["how are you", "how're you", "how are u", "you okay", "you good"]
    ):
        return handle_how_are_you(query)

    # Goodbye
    if any(
        word in q
        for word in ["goodbye", "bye", "see you", "catch you later", "talk later"]
    ):
        return handle_goodbye(query)

    # Thank you
    if any(
        phrase in q for phrase in ["thank you", "thanks", "appreciate it", "thank u"]
    ):
        return handle_thank_you(query)

    # Compliments
    if any(
        word in q
        for word in [
            "awesome",
            "amazing",
            "great job",
            "love you",
            "you're the best",
            "brilliant",
        ]
    ):
        if any(word in q for word in ["you", "you're", "your", "ivy"]):
            return handle_compliment(query)

    # About self
    if any(
        phrase in q
        for phrase in [
            "who are you",
            "what are you",
            "tell me about yourself",
            "what can you do",
        ]
    ):
        return handle_about_self(query)

    if any(
        word in q
        for word in [
            "sad",
            "happy",
            "bored",
            "excited",
            "depressed",
            "upset",
            "down",
            "great",
            "wonderful",
        ]
    ):
        if any(word in q for word in ["i", "im", "i'm", "feeling"]):
            return handle_mood(query)

    fun_keywords = [
        "joke",
        "riddle",
        "fact",
        "fun",
        "entertain",
        "laugh",
        "smile",
        "game",
    ]
    if any(kw in q for kw in fun_keywords):
        from lib.conversations.fun import handle_fun_query

        return handle_fun_query(query)

    return None


def match(query: str) -> bool:
    """Compatibility wrapper for router registry: returns True if casual module should handle query."""
    return route_conversation(query) is not None


def handle(query: str) -> str:
    """Compatibility wrapper for router registry: returns the casual response or None."""
    return route_conversation(query)


# ============= RANDOM CONVERSATION STARTERS =============


def get_conversation_starter():
    """Get a random conversation starter for idle moments"""
    starters = [
        "Want to hear something interesting?",
        "I've got a fun fact if you're interested!",
        "How about a quick riddle?",
        "Need a laugh? I've got jokes!",
        "Feeling curious? Ask me something!",
    ]
    return random.choice(starters)
