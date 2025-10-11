import re
from playsound import playsound
import eel
from lib.main.command import *
import os
import lib.main.response as response
import pywhatkit as kit


# play assistant sound function
@eel.expose
def play_assistant_sound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)


# for opening apps
def open_command(query):
    try:
        query = query.lower()
        words = query.split()
        index = words.index("open")

        app = words[index + 1]
        speak("opening " + app)
        eel.DisplayMessage("opening " + app)
        os.system("start " + app)
    except ValueError:
        speak(random.choice(response.cannot_understand_user))

    eel.ShowHood()


def play_youtube(query):
    search_term = extract_yt_term(query)

    if not search_term:
        response_youtube = random.choice(response.cannot_understand_youtube)
        eel.DisplayMessage(response_youtube)
        speak(response_youtube)
        return

    speak(f"playing {search_term} on youtube")
    kit.playonyt(search_term)


def extract_yt_term(command):
    pattern = r"play\s+(.*?)\s+on\s+youtube"
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1).strip() if match else None
