from playsound import playsound
import eel
from lib.vocal.command import *
import config
import os


# play assistant sound function
@eel.expose
def play_assistant_sound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)


# opening
def open_command(query):
    query = query.replace(config.ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query != "":
        speak("opening " + query)
        os.system("start " + query)
    else:
        speak("not found")
