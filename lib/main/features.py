import re
from shlex import quote
import struct
import subprocess
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
from rapidfuzz import process
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
    from lib.main.helper import clean_app_name

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
            # Check system commands first
            cursor.execute("SELECT path FROM sys_command WHERE name = ?", (app_name,))
            sys_results = cursor.fetchall()

            # Check web commands
            cursor.execute("SELECT url FROM web_command WHERE name = ?", (app_name,))
            web_results = cursor.fetchall()

            if len(sys_results) != 0:
                speak("Opening " + app_name)
                os.startfile(sys_results[0][0])
                return
            elif len(web_results) != 0:
                speak("Opening " + app_name)
                webbrowser.open(web_results[0][0])
                return
            else:
                speak(
                    random.choice(
                        [r.format(app=app_name) for r in response.cannot_find_app]
                    )
                )
                print(f"App '{app_name}' not found in database")
                return

        except Exception as e:
            print("Error in open_command:", e)
            traceback.print_exc()
            speak(random.choice(response.cannot_understand_user))
    else:
        speak(random.choice(response.cannot_understand_app_name))
        print("No application name provided")


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


# find contacts in whatsapp
def findContact(query):
    words_to_remove = [
        config.ASSISTANT_NAME,
        "make",
        "a",
        "to",
        "phone",
        "call",
        "send",
        "message",
        "whatsapp",
        "video",
        "please",
        "can",
        "you",
        "me",
        "for",
        "the",
        "contact",
        ".",
        ",",
        "on",
        "with",
        "",
    ]
    query = remove_words(query, words_to_remove)
    query = query.strip().lower()

    cursor.execute("SELECT name, mobile_no FROM contacts")
    contacts = cursor.fetchall()
    contact_names = [name.lower() for name, _ in contacts]

    match, score, idx = process.extractOne(query, contact_names)
    if score > 70:
        mobile_number_str = str(contacts[idx][1])
        print(f"Selected contact: {match}, Number: {mobile_number_str}")
        if not mobile_number_str.startswith(
            config.COUNTRY_CODES["PH"]
        ):  # change this number according to your country
            mobile_number_str = config.COUNTRY_CODES["PH"] + mobile_number_str
        return mobile_number_str, match
    else:
        speak(random.choice(response.cannot_find_whatsapp_contact))
        return 0, 0


def whatsApp(mobile_no, message, flag, name):

    if flag == "message":
        target_tab = 12
        ivy_message = f"Message sent successfully to {name}"
    elif flag == "call":
        target_tab = 7
        message = ""
        ivy_message = f"Calling {name}"
    else:
        target_tab = 6
        message = ""
        ivy_message = f"Starting video call with {name}"

    import re

    message = re.sub(r"'{2,}", "'", message)
    message = message.replace(".", "")
    message = message.strip()

    encoded_message = quote(message)

    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"
    full_command = f'start "" "{whatsapp_url}"'

    try:
        subprocess.run(full_command, shell=True)
        time.sleep(5)

        autogui.hotkey("ctrl", "f")
        for _ in range(1, target_tab):
            autogui.hotkey("tab")
        autogui.hotkey("enter")
        speak(ivy_message)
    except Exception as e:
        print("Error sending WhatsApp message:", e)
        speak(random.choice(response.cannot_send_whatsapp_message))
