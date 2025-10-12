import re
import webbrowser
from playsound import playsound
import eel
from lib.main.command import *
import os
import lib.main.response as response
import pywhatkit as kit
import sqlite3

con = sqlite3.connect("./database/ivy.db")
cursor = con.cursor()


# play assistant sound function
@eel.expose
def play_assistant_sound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)


# for opening apps
def open_command(query):
    query = query.replace(config.ASSISTANT_NAME, "")
    query = query.lower().strip()

    query = re.sub(r"\bopen\b", "", query)
    query = re.sub(r"[?!.,]", "", query)
    query = query.strip()

    words = query.split()
    if len(words) > 0:
        app_name = words[-1]
    else:
        app_name = ""

    if app_name != "":
        app_name = clean_app_name(app_name)
        try:
            cursor.execute("SELECT path FROM sys_command WHERE name = ?", (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening " + app_name)
                os.startfile(results[0][0])
            else:
                cursor.execute(
                    "SELECT url FROM web_command WHERE name = ?", (app_name,)
                )
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening " + app_name)
                    webbrowser.open(results[0][0])
                else:
                    speak("Opening " + app_name)
                    os.system("start " + app_name)

        except Exception as e:
            import traceback

            print("Error in open_command:", e)
            traceback.print_exc()
            speak(random.choice(response.cannot_understand_user))


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
    }

    return replacements.get(app_name, app_name)


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
