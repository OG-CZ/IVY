import webbrowser
import pyttsx3
import re


def speak(text: str):
    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 180)
    engine.setProperty("volume", 0.9)
    engine.say(text)
    engine.runAndWait()


def extract_search_query(command: str):
    """
    Extracts a Google search query from a natural language command.
    Returns the extracted query string, or None if no match.
    """
    command = command.lower().strip()

    # Predefined regex patterns (specific to Google)
    patterns = [
        r"search\s+(?:for\s+)?(.+?)\s+on\s+google",
        r"search\s+google\s+for\s+(.+)",
        r"look\s+up\s+(.+?)\s+(?:on|using)\s+google",
        r"find\s+(?:out\s+)?(.+?)\s+on\s+google",
        r"show\s+me\s+(.+?)\s+on\s+google",
        r"check\s+on\s+google\s+for\s+(.+)",
        r"get\s+info\s+on\s+google\s+about\s+(.+)",
        r"see\s+what\s+google\s+says\s+about\s+(.+)",
        r"(?:can\s+you\s+|could\s+you\s+|please\s+|just\s+|let'?s\s+|hey,?\s+)?google\s+(.+?)(?:\s+for\s+me)?$",
        r"open\s+google\s+and\s+search\s+(?:for\s+)?(.+)",
        r"type\s+(.+?)\s+on\s+google",
        r"i\s+want\s+to\s+google\s+(.+)",
        r"do\s+a\s+(?:quick\s+)?google\s+search\s+for\s+(.+)",
        r"google\s+search\s+(.+)",
        # Conversational forms like "what is AI on google"
        r"(?:what|who|where|when|why|how)\s+(?:is|are|to|does|did|can|do)?\s*(.+?)\s+on\s+google",
    ]

    for pattern in patterns:
        match = re.search(pattern, command)
        if match:
            query = match.group(1).strip()
            query = re.sub(r"\s+(for\s+me|please)$", "", query)
            return query

    if "google" in command:
        after_google = command.split("google", 1)[1].strip()
        query = re.sub(r"^(for|that|this|it|about|the)\s+", "", after_google)
        query = re.sub(r"\s+(for\s+me|please)$", "", query)
        if query:
            return query

    return None


def google_search(command: str):
    query = extract_search_query(command)

    if query:
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    else:
        speak("I couldn’t understand your Google search. Try saying it again.")


if __name__ == "__main__":
    test_commands = [
        "search something on google",
        "google Taylor Swift albums",
        "look up AI on google",
        "find the latest iPhone on google",
        "show me dogs on google",
        "check on google for elon musk",
        "get info on google about neuralink",
        "see what google says about python programming",
        "can you google what is quantum computing",
        "open google and search top games 2025",
        "type recipe for pancakes on google",
        "i want to google tesla stock price",
        "do a quick google search for climate change",
        "google search best laptops",
        "what is ivy on google",
        "who is taylor swift on google",
        "how to code in python on google",
    ]

    for cmd in test_commands:
        google_search(cmd)
