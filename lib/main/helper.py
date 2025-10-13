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
