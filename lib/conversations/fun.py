import random

# Jokes with categories
TECH_JOKES = [
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
    "Why do Java developers wear glasses? Because they can't C#!",
    "There are only 10 types of people in the world: those who understand binary and those who don't.",
]

DAD_JOKES = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "What's the best thing about Switzerland? I don't know, but the flag is a big plus!",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
]

SCIENCE_JOKES = [
    "Why was the math book sad? It had too many problems.",
    "What do you call an educated tube? A graduated cylinder!",
    "Why can't you trust atoms? They make up everything!",
    "What did one DNA strand say to the other? Do these genes make me look fat?",
]

# Riddles with difficulty levels
EASY_RIDDLES = [
    "What has keys but can't open locks? ...A piano!",
    "I'm tall when I'm young and short when I'm old. What am I? ...A candle!",
    "What can travel around the world while staying in a corner? ...A stamp!",
]

MEDIUM_RIDDLES = [
    "I speak without a mouth and hear without ears. I have no body, but come alive with wind. What am I? ...An echo!",
    "The more you take, the more you leave behind. What am I? ...Footsteps!",
    "I have cities but no houses, forests but no trees, and water but no fish. What am I? ...A map!",
]

HARD_RIDDLES = [
    "What flies without wings, cries without eyes, and moves without legs? ...A cloud!",
    "I am not alive, but I grow. I don't have lungs, but I need air. What am I? ...Fire!",
    "What can run but never walks, has a mouth but never talks? ...A river!",
]

# Interesting facts by category
NATURE_FACTS = [
    "Did you know? Honey never spoils. Archaeologists have found 3,000-year-old honey in Egyptian tombs that's still perfectly edible!",
    "A group of flamingos is called a 'flamboyance'. Pretty fitting, right?",
    "Octopuses have three hearts and blue blood! Two hearts pump blood to the gills, while the third pumps it to the rest of the body.",
    "Sea otters hold hands while sleeping so they don't drift apart. Adorable!",
]

FOOD_FACTS = [
    "Bananas are berries, but strawberries aren't. Mind blown!",
    "Honey is made from nectar and bee spit. Still delicious though!",
    "Pineapples take about two years to grow. That's some serious patience!",
    "A strawberry isn't actually a berry, it's an 'aggregate accessory fruit'.",
]

SPACE_FACTS = [
    "A day on Venus is longer than its year! It takes 243 Earth days to rotate once, but only 225 days to orbit the sun.",
    "There are more stars in the universe than grains of sand on all Earth's beaches. That's about 10,000 stars for every grain!",
    "In space, two pieces of metal will permanently stick together if they touch. It's called cold welding!",
]

HUMAN_FACTS = [
    "Your brain uses about 20% of your body's energy, but only makes up 2% of your weight. No wonder thinking makes you tired!",
    "Humans are the only animals that blush. And the only ones that need to!",
    "Your nose can remember 50,000 different scents. That's pretty impressive!",
]

# Conversational responses
JOKE_INTROS = [
    "Alright, here's a good one:",
    "Oh, I love this one!",
    "Okay okay, check this out:",
    "This one always cracks me up:",
    "Prepare yourself for this gem:",
]

RIDDLE_INTROS = [
    "Hmm, let me think of a good riddle...",
    "Alright, riddle time! Try to solve this:",
    "Here's a brain teaser for you:",
    "Let's see if you can figure this one out:",
    "Ooh, I've got a tricky one:",
]

FACT_INTROS = [
    "Here's something cool:",
    "Oh, this is fascinating!",
    "Fun fact alert!",
    "You're gonna love this:",
    "This one's wild:",
]

PLAYFUL_RESPONSES = [
    "I'm having fun chatting with you! Want to hear a joke, riddle, or fun fact?",
    "Life's too short to be boring! How about a joke to brighten your day?",
    "I'm all about good vibes! Want something funny, mysterious, or mind-blowing?",
    "Let's keep this fun going! Pick your poison: joke, riddle, or fact?",
    "You know what? I really enjoy our conversations! What can I share with you today?",
]

COMPLIMENT_RESPONSES = [
    "Aww, you're sweet! Here's something fun for being so nice:",
    "Thanks! You just made my circuits happy. Let me return the favor:",
    "You're pretty cool yourself! Here's a little something:",
]

CONFUSED_RESPONSES = [
    "Hmm, not sure what you're looking for, but here's something entertaining anyway!",
    "Let me just throw something fun at you:",
    "When in doubt, share a joke!",
]


def answer_fun_query(query: str) -> str:
    """
    Enhanced fun query handler with natural conversation flow
    """
    q = (query or "").lower()

    # Jokes
    if any(word in q for word in ["joke", "funny", "laugh", "humor"]):
        intro = random.choice(JOKE_INTROS)

        if "tech" in q or "computer" in q or "programming" in q:
            joke = random.choice(TECH_JOKES)
        elif "dad" in q:
            joke = random.choice(DAD_JOKES)
        elif "science" in q or "math" in q:
            joke = random.choice(SCIENCE_JOKES)
        else:
            all_jokes = TECH_JOKES + DAD_JOKES + SCIENCE_JOKES
            joke = random.choice(all_jokes)

        return f"{intro} {joke}"

    # Riddles
    if any(word in q for word in ["riddle", "puzzle", "brain teaser", "guess"]):
        intro = random.choice(RIDDLE_INTROS)

        if "easy" in q or "simple" in q:
            riddle = random.choice(EASY_RIDDLES)
        elif "hard" in q or "difficult" in q or "tricky" in q:
            riddle = random.choice(HARD_RIDDLES)
        else:
            all_riddles = EASY_RIDDLES + MEDIUM_RIDDLES + HARD_RIDDLES
            riddle = random.choice(all_riddles)

        return f"{intro} {riddle}"

    # Facts
    if any(
        word in q
        for word in ["fact", "did you know", "tell me something", "teach me", "learn"]
    ):
        intro = random.choice(FACT_INTROS)

        if any(word in q for word in ["nature", "animal", "ocean", "wildlife"]):
            fact = random.choice(NATURE_FACTS)
        elif any(word in q for word in ["food", "eat", "fruit"]):
            fact = random.choice(FOOD_FACTS)
        elif any(word in q for word in ["space", "planet", "star", "galaxy"]):
            fact = random.choice(SPACE_FACTS)
        elif any(word in q for word in ["human", "body", "brain"]):
            fact = random.choice(HUMAN_FACTS)
        else:
            all_facts = NATURE_FACTS + FOOD_FACTS + SPACE_FACTS + HUMAN_FACTS
            fact = random.choice(all_facts)

        return f"{intro} {fact}"

    # Compliments
    if any(word in q for word in ["love you", "awesome", "cool", "amazing", "great"]):
        response = random.choice(COMPLIMENT_RESPONSES)
        bonus = random.choice(TECH_JOKES + NATURE_FACTS)
        return f"{response} {bonus}"

    # Playful/general fun
    if any(
        word in q
        for word in ["play", "game", "fun", "entertain", "bored", "smile", "happy"]
    ):
        return random.choice(PLAYFUL_RESPONSES)

    # Default: surprise them with something random
    response = random.choice(CONFUSED_RESPONSES)
    content_pool = TECH_JOKES + DAD_JOKES + EASY_RIDDLES + NATURE_FACTS
    bonus = random.choice(content_pool)
    return f"{response} {bonus}"


def handle_fun_query(query: str) -> str:
    """
    Main handler for fun/casual queries with conversational flair
    """
    return answer_fun_query(query)


def match(query: str) -> bool:
    """Return True if this module should handle the query (simple keyword check)."""
    if not query:
        return False
    q = query.lower()
    fun_keywords = [
        "joke",
        "riddle",
        "fact",
        "fun",
        "entertain",
        "laugh",
        "smile",
        "play",
        "game",
    ]
    return any(kw in q for kw in fun_keywords)


def handle(query: str) -> str:
    return handle_fun_query(query)


# Optional: Add a function to get random entertainment
def get_random_entertainment():
    """Returns a random joke, riddle, or fact"""
    all_content = (
        TECH_JOKES
        + DAD_JOKES
        + SCIENCE_JOKES
        + EASY_RIDDLES
        + MEDIUM_RIDDLES
        + HARD_RIDDLES
        + NATURE_FACTS
        + FOOD_FACTS
        + SPACE_FACTS
        + HUMAN_FACTS
    )
    return random.choice(all_content)


# Example usage and testing
if __name__ == "__main__":
    test_queries = [
        "tell me a joke",
        "give me a tech joke",
        "riddle me this",
        "tell me a hard riddle",
        "fun fact please",
        "tell me about space",
        "you're awesome",
        "I'm bored",
        "make me laugh",
    ]

    print("=== Testing Fun Conversation Module ===\n")
    for query in test_queries:
        print(f"User: {query}")
        print(f"Assistant: {handle_fun_query(query)}")
        print()
