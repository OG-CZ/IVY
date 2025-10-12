import re
import struct
import webbrowser
from playsound import playsound
import eel
import pvporcupine
from lib.main.command import *
import lib.main.response as response
from lib.main.helper import *
import os
import pywhatkit as kit
import sqlite3
import pyautogui as autogui

import time
import pyaudio
import traceback
import random

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


#  running in background
def hotword(q=None):
    porcupine = None
    paud = None
    audio_stream = None

    try:
        print("Initializing Porcupine...")
        porcupine = pvporcupine.create(
            access_key=config.PORCUPINE_API_KEY,
            keyword_paths=[config.PORCUPINE_IVY_HOTKEY_MODEL],
        )

        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length,
        )

        print("Listening for hotword...")

        last_detected = 0
        cooldown = 3  # seconds to wait before re-triggering

        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:
                now = time.time()
                if now - last_detected > cooldown:
                    print("Hotword detected!")

                    if q is not None:
                        q.put("hotword")
                    else:
                        import eel
                        from lib.main.command import all_commands

                        eel.spawn(all_commands)

                    last_detected = now

                    # simulate a shortcut key (example: Win + J)
                    autogui.keyDown("ctrl")
                    autogui.press("i")
                    autogui.keyUp("ctrl")
    except Exception as e:
        print("Error:", repr(e))
        traceback.print_exc()
    finally:
        if porcupine:
            porcupine.delete()
        if audio_stream:
            audio_stream.close()
        if paud:
            paud.terminate()
        print("Program exited cleanly.")
