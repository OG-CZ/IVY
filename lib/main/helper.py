"""
helper.py - Enhanced with intelligent YouTube extraction
"""

import re


def extract_yt_term(command):
    """
    Intelligently extract YouTube search term from various command formats.

    Supports all natural variations:
    - play [title] on youtube
    - search [title] on youtube
    - search youtube for [title]
    - play the song [title] on youtube
    - look up [title] video on youtube
    - i want to watch [title] on youtube
    - etc.
    """
    if not command:
        return None

    query = command.lower().strip()
    query = re.sub(r"[?.!,;]+$", "", query)

    action_words = [
        "play",
        "search",
        "show",
        "find",
        "open",
        "look up",
        "lookup",
        "put on",
        "stream",
        "watch",
        "view",
    ]

    # Pattern 1: "[action] [title] on/in youtube"
    # Examples: "play how to be the dude on youtube", "search maroon5 what lovers do on youtube"
    pattern1 = r"(?:play|search|show|find|open|look\s+up|lookup|put\s+on|stream|watch|view)\s+(?:the\s+)?(?:song\s+)?(?:video\s+)?(?:clip\s+)?(?:music\s+)?(.+?)\s+(?:on|in)\s+(?:youtube|yt)"
    match = re.search(pattern1, query, re.IGNORECASE)
    if match:
        title = match.group(1).strip()
        return clean_youtube_title(title)

    # Pattern 2: "search/look up youtube for [title]"
    # Examples: "search youtube for maroon5 what lovers do"
    pattern2 = r"(?:search|look\s+up|lookup|find)\s+(?:youtube|yt)\s+for\s+(.+)"
    match = re.search(pattern2, query, re.IGNORECASE)
    if match:
        title = match.group(1).strip()
        return clean_youtube_title(title)

    # Pattern 3: "[action] [title] [content-type] on/in youtube"
    # Examples: "play how to code video on youtube"
    pattern3 = r"(?:play|search|show|find|open|watch|view)\s+(.+?)\s+(?:video|clip|music|song|track)\s+(?:on|in)\s+(?:youtube|yt)"
    match = re.search(pattern3, query, re.IGNORECASE)
    if match:
        title = match.group(1).strip()
        return clean_youtube_title(title)

    # Pattern 4: "i want to watch [title] on youtube"
    # Examples: "i want to watch the office on youtube"
    pattern4 = r"(?:i\s+want\s+to|id\s+like\s+to|i\'d\s+like\s+to)\s+(?:watch|see|view)\s+(.+?)\s+(?:on|in)\s+(?:youtube|yt)"
    match = re.search(pattern4, query, re.IGNORECASE)
    if match:
        title = match.group(1).strip()
        return clean_youtube_title(title)

    # Pattern 5: "can you/please [action] [title] on youtube"
    # Examples: "can you play despacito on youtube", "please search cats on youtube"
    pattern5 = r"(?:can\s+you|could\s+you|please|would\s+you)\s+(?:play|search|show|find|open)\s+(.+?)\s+(?:on|in)\s+(?:youtube|yt)"
    match = re.search(pattern5, query, re.IGNORECASE)
    if match:
        title = match.group(1).strip()
        return clean_youtube_title(title)

    for action in action_words:
        pattern = rf"\b{action}\b\s+(.+?)\s+(?:on|in)?\s*\b(?:youtube|yt)\b"
        match = re.search(pattern, query, re.IGNORECASE)
        if match:
            title = match.group(1).strip()
            cleaned = clean_youtube_title(title)
            if cleaned:
                return cleaned

    if "youtube" in query or "yt" in query:
        title = re.sub(r"\b(?:youtube|yt)\b", "", query, flags=re.IGNORECASE)
        title = re.sub(r"\b(?:on|in|at)\s*$", "", title, flags=re.IGNORECASE)

        for action in action_words:
            title = re.sub(rf"^\s*{action}\s+", "", title, flags=re.IGNORECASE)

        cleaned = clean_youtube_title(title)
        if cleaned:
            return cleaned

    return None


def clean_youtube_title(title):
    """
    Clean up extracted title while preserving the full search term.
    Only removes filler words from beginning/end, never from the middle.
    """
    if not title:
        return None

    # Remove extra whitespace
    title = re.sub(r"\s+", " ", title).strip()

    # Remove common filler words ONLY from the beginning
    title = re.sub(r"^\s*(?:the|a|an|for|me)\s+", "", title, flags=re.IGNORECASE)

    # Remove "song", "video", "clip", "music" ONLY from the end
    title = re.sub(
        r"\s+(?:song|video|clip|music|track)s?\s*$", "", title, flags=re.IGNORECASE
    )

    title = re.sub(r"\s+(?:for\s+me)\s*$", "", title, flags=re.IGNORECASE)

    title = title.strip()

    if len(title) < 2:
        return None

    return title


def is_youtube_query(query):
    """
    Check if query is asking to play/search something on YouTube.
    This is used to detect YouTube commands before trying to extract the title.
    """
    if not query:
        return False

    q = query.lower()

    has_youtube = any(word in q for word in ["youtube", "yt"])
    if not has_youtube:
        return False

    action_patterns = [
        "play",
        "search",
        "show",
        "find",
        "open",
        "look up",
        "lookup",
        "put on",
        "stream",
        "watch",
        "view",
        "can you",
        "please",
        "i want",
    ]

    has_action = any(action in q for action in action_patterns)

    return has_action


def clean_app_name(app_name):
    """Clean and normalize application names"""
    app_name = app_name.strip().lower()

    replacements = {
        "sigma": "figma",
        "you tube": "youtube",
        "you-tube": "youtube",
        "photo shop": "photoshop",
        "clod": "claude",
        "clad": "claude",
        "cloud": "claude",
        "clode": "claude",
        "clade": "claude",
        "claw": "claude",
        "clud": "claude",
        "glud": "claude",
        "gethub": "github",
        "get hub": "github",
        "danva": "canva",
    }

    return replacements.get(app_name, app_name)


def remove_words(input_string, words_to_remove):
    """Remove specified words from a string"""
    words = input_string.split()
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
    result_string = " ".join(filtered_words)
    return result_string


def extract_city_from_query(query: str) -> str | None:
    """Extract city name from weather queries"""
    if not query:
        return None
    m = re.search(r"\b(?:in|at)\s+([a-zA-Z][\w\-\s\.'']+)", query, flags=re.IGNORECASE)
    if not m:
        return None
    city = m.group(1).strip(" .,!?:;")
    return re.sub(r"\s{2,}", " ", city) or None


def is_weather_query(text: str) -> bool:
    """Check if query is asking about weather"""
    q = (text or "").lower()
    weather_words = (
        "weather",
        "temperature",
        "temp",
        "forecast",
        "rain",
        "raining",
        "rainy",
        "sunny",
        "cloudy",
        "overcast",
        "windy",
        "storm",
        "stormy",
        "snow",
        "snowy",
        "hail",
    )
    if any(w in q for w in weather_words):
        return True
    return bool(
        re.search(
            r"\b(?:is|will|does)\s+it\s+(?:rain|snow|hail|be\s+sunny|be\s+cloudy|be\s+windy)\b",
            q,
        )
    )


def extract_condition_from_query(text: str) -> str | None:
    """Extract weather condition from query"""
    q = (text or "").lower()
    if re.search(r"\b(rain|rainy|raining)\b", q):
        return "rain"
    if "sunny" in q:
        return "sunny"
    if re.search(r"\b(cloudy|overcast)\b", q):
        return "cloudy"
    if "windy" in q:
        return "windy"
    if re.search(r"\b(snow|snowy)\b", q):
        return "snow"
    if re.search(r"\b(storm|stormy|thunder)\b", q):
        return "storm"
    return None


def normalize_units(text: str) -> str:
    import re

    unit_map = {
        "B": " bytes",
        "KB": " kilobytes",
        "MB": " megabytes",
        "GB": " gigs",
        "TB": " terabytes",
        "PB": " petabytes",
    }

    text = re.sub(
        r"(?i)(\d+(?:\.\d+)?)\s*(b|kb|mb|gb|tb|pb)\b",
        lambda m: f"{m.group(1)}{unit_map[m.group(2).upper()]}",
        text,
    )

    text = re.sub(
        r"(?i)\b(b|kb|mb|gb|tb|pb)\b",
        lambda m: unit_map[m.group(1).upper()],
        text,
    )

    return text
