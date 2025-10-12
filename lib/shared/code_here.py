"""_INSTRUCTIONS_

How to Add Q&A Functionality to Ivy:

1. Create a dictionary of question-answer pairs
   - Keys: Simplified questions (lowercase, no punctuation)
   - Values: Either answer strings or functions that return answers

2. Add a function to match user input against your Q&A database
   - Clean user input (lowercase, remove punctuation)
   - Check for exact or partial matches
   - Return appropriate answers

3. Add your Q&A functionality to the main command flow:
   - Import your module in command.py
   - Call your answer function before other command processing
   - Return immediately if a question is answered

4. Test your functionality:
   - Try variations of your questions
   - Ensure answers are returned correctly
   - Check that other commands still work

Example implementation below - customize with your own Q&A pairs!
"""

import re
import random
from datetime import datetime
import eel

# Sample Q&A pairs - add your own!
QA_DATABASE = {
    # Basic information
    "what is your name": "My name is Ivy, your intelligent voice assistant.",
    "who created you": "I was created by a team of developers for the IVY project.",
    "what can you do": "I can answer questions, open applications, play music, and more.",
    # Dynamic answers (use functions)
    "what time is it": lambda: f"It's {datetime.now().strftime('%I:%M %p')}.",
    "what day is today": lambda: f"Today is {datetime.now().strftime('%A, %B %d')}.",
    # Fun responses
    "tell me a joke": lambda: random.choice(
        [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What's the best thing about Switzerland? I don't know, but the flag is a big plus.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
        ]
    ),
}

# Fallback responses when no answer is found
FALLBACK_RESPONSES = [
    "I don't know the answer to that yet.",
    "I'm not sure how to answer that.",
    "I don't have that information.",
]


def is_question(query):
    """Check if the input is likely a question."""
    # Questions usually end with ? or start with question words
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
        "are",
    ]
    return query.endswith("?") or any(query.startswith(word) for word in question_words)


def get_answer(query):
    """Match a query against our Q&A database and return an answer."""
    if not query or not is_question(query):
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


# To integrate with command.py, add this code to all_commands():
"""
# Add near the beginning of all_commands():
query = take_command()
if query:
    answer = get_answer(query)
    if answer:
        speak(answer)
        return answer
        
    # Continue with other command processing...
"""

# Test your Q&A functionality
if __name__ == "__main__":
    test_questions = [
        "What is your name?",
        "Who created you?",
        "Tell me a joke",
        "What time is it now?",
        "How do you work?",  # Not in database
    ]

    for question in test_questions:
        print(f"Q: {question}")
        print(f"A: {get_answer(question)}")
        print()
