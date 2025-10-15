import re


def extract_yt_term(command):
    pattern = r"play\s+(.*?)\s+on\s+youtube"
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1).strip() if match else None


def clean_app_name(app_name):

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
    words = input_string.split()

    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    result_string = " ".join(filtered_words)

    return result_string


def extract_city_from_query(query: str) -> str | None:
    if not query:
        return None
    m = re.search(r"\b(?:in|at)\s+([a-zA-Z][\w\-\s\.'’]+)", query, flags=re.IGNORECASE)
    if not m:
        return None
    city = m.group(1).strip(" .,!?:;")
    return re.sub(r"\s{2,}", " ", city) or None


def is_weather_query(text: str) -> bool:
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
