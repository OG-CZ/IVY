import random
import time
import traceback
import audioop
import pyttsx3
import speech_recognition as sr
import pyaudio
import wave
from faster_whisper import WhisperModel
import os
import eel
import config
import lib.main.response as response

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"


# load model
if os.path.exists(config.MODEL_DIR):
    model = WhisperModel("machine-learning/faster-whisper-small.en/", device="cpu")
    print(f"Model folder loaded: {config.MODEL_DIR}")
elif os.path.exists(config.MODEL_BACKUP):
    model = WhisperModel("model/", device="cpu")
    print("Model loaded successfully!")
else:
    model = WhisperModel("small.en", device="cpu")
    print("Model loaded successfully!")


def speak(text):

    engine = pyttsx3.init()

    # speed of talk
    engine.setProperty("rate", 174)

    # voice choose
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)

    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()


def record_audio(
    filename="input.wav",
    ambient_sample_seconds=0.5,
    silence_factor=3.0,
    min_silence_threshold=300,
    silence_duration=2.0,
):

    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    rate = 16000

    p = pyaudio.PyAudio()
    stream = p.open(
        format=sample_format,
        channels=channels,
        rate=rate,
        input=True,
        frames_per_buffer=chunk,
    )

    # --- calibrate ambient RMS ---
    frames_cal = []
    calibr_chunks = int(rate / chunk * ambient_sample_seconds)
    for _ in range(max(1, calibr_chunks)):
        data = stream.read(chunk, exception_on_overflow=False)
        frames_cal.append(data)
    ambient_rms = audioop.rms(b"".join(frames_cal), 2)
    # compute threshold from ambient rms but enforce a sensible minimum
    silence_threshold = max(int(ambient_rms * silence_factor), min_silence_threshold)

    eel.DisplayMessage(f"Listening...")
    print(f"threshold={silence_threshold}")

    frames = []
    silence_start = None

    try:
        while True:
            data = stream.read(chunk, exception_on_overflow=False)
            frames.append(data)

            # compute instantaneous rms
            rms = audioop.rms(data, 2)

            # --- debug line (uncomment during tuning) ---
            # print(f"rms={rms}, threshold={silence_threshold}")

            if rms < silence_threshold:
                if silence_start is None:
                    silence_start = time.time()
                elif time.time() - silence_start > silence_duration:
                    eel.DisplayMessage("Recognizing....")
                    break
            else:
                # voice detected; reset silence timer
                silence_start = None
    except Exception as e:
        print("Recording error:", e)
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(rate)
        wf.writeframes(b"".join(frames))

    return filename


def transcribe_audio(filename="input.wav"):
    segments, _ = model.transcribe(filename)
    text = " ".join([segment.text for segment in segments])
    if os.path.exists(filename):
        os.remove(filename)
    return text


# THE CORE CONNECTION OF ALL COMMANDS
@eel.expose
def take_command():
    # eel.DisplayMessage("Hello, I am Ivy")
    # eel.sleep(1.0)
    file = record_audio()
    query = transcribe_audio(file)
    eel.DisplayMessage(query)

    sleep_time = min(max(2, 0.4 * len(query.split())), 6)
    time.sleep(sleep_time)

    return query


# core logic for all commands
@eel.expose
def all_commands(message=1) -> str:

    if message == 1:
        query = take_command()
        query = query.rstrip()
        print("query is :", query)
    else:
        query = message

    call_keywords = [
        "call",
        "phone call",
        "make a call",
        "dial",
        "ring",
        "place a call",
        "video call",
    ]
    message_keywords = ["send message", "send a message", "message", "text"]

    try:
        # if no voice
        if len(query) < 2:
            speak(random.choice(response.cannot_understand_user))

        # opening app or website
        if "open" in query.lower():
            from lib.main.features import open_command

            open_command(query)

        # play video in youtube
        elif "on youtube" in query.lower() or "in youtube" in query.lower():
            from lib.main.features import play_youtube

            play_youtube(query)

            # send message,phone call, video call to whatsapp
        elif any(kw in query.lower() for kw in message_keywords + call_keywords):
            from lib.main.features import findContact, whatsApp
            import re

            # Clean the query to extract contact name
            cleaned_query = re.sub(r"[^\w\s]", "", query)
            cleaned_query = re.sub(
                r"\b("
                + "|".join(message_keywords + call_keywords)
                + r"|to|and|a|please)\b",
                "",
                cleaned_query,
                flags=re.IGNORECASE,
            )
            cleaned_query = cleaned_query.strip()

            contact_no, name = findContact(cleaned_query.lower())
            if contact_no != 0:
                flag = ""
                message = ""
                if any(kw in query.lower() for kw in message_keywords):
                    flag = "message"
                    speak("what message to send")
                    print("what message to send?")
                    message = take_command()
                elif any(kw in query.lower() for kw in call_keywords):
                    if "video call" in query.lower():
                        flag = "video call"
                    else:
                        flag = "call"
                    print(flag)
                else:
                    flag = "message"

                whatsApp(contact_no, message if flag == "message" else "", flag, name)
            else:
                print("something went wrong in whatsapp command.py")
        else:
            print(f"No command match found for: '{query}'")
        # speak(f"I heard '{query}' but I don't know how to handle that command yet.")

    except Exception as e:
        print("Error in all_commands:", e)
        traceback.print_exc()
    finally:
        print("=== calling ShowHood ===")
        try:
            eel.ShowHood()
        except Exception as e:
            print("ShowHood error:", e)


def check_mic_to_use():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(
            'Microphone with name "{1}" found for `Microphone(device_index={0})`'.format(
                index, name
            )
        )


""" _disabled_

def take_command_vosk():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening...")
        eel.DisplayMessage("listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=10)
        except sr.WaitTimeoutError:
            print("Timeout waiting for speech.")
            return ""

    try:
        print("recognizing")
        eel.DisplayMessage("recognizing....")

        # reuse the same model
        rec = KaldiRecognizer(model, 16000)
        rec.AcceptWaveform(audio.get_raw_data(convert_rate=16000, convert_width=2))
        result = json.loads(rec.Result())

        query = result.get("text", "").strip()
        if not query:
            eel.DisplayMessage("Could not understand, please try again.")
            eel.sleep(3.5)
            eel.ShowHood()
            return ""

        eel.DisplayMessage(query)
        eel.sleep(3.5)
        eel.ShowHood()
        return query.lower()

    except Exception as e:
        print("Recognition error:", e)
        eel.DisplayMessage(f"Error: {e}")
        eel.sleep(3.5)
        eel.ShowHood()
        return ""


# backup a bruteforce way if sr.recognize function is not working
def take_command_force(device_index=None):
       
        Brute-force listen-and-recognize loop using Vosk/Kaldi.

        under the hood version for speech recognition sr.recognize_vosk() -> str
        if it that function is not available we can use this

        Args:
            device_index (int|None): optional microphone device index for sr.Microphone

        Returns:
            str: recognized text in lowercase, or "" if the model folder is missing.
 
    model_dir = "machine-learning/vosk-model-en-us-0.22-lgraph"
    if not os.path.isdir(model_dir):
        print(f"Model folder not found: {model_dir}")
        print("Download a Vosk model and extract it there.")
        return ""
    model = Model(model_dir)

    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.dynamic_energy_threshold = True

    try:
        with sr.Microphone(device_index=device_index) as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
    except sr.WaitTimeoutError:
        print("No speech detected (timeout).")
        return ""
    except OSError as e:
        print(f"Microphone error: {e}")
        return ""

    try:
        print("Recognizing...")
        rec = KaldiRecognizer(model, 16000)
        raw = audio.get_raw_data(convert_rate=16000, convert_width=2)
        if rec.AcceptWaveform(raw):
            data = json.loads(rec.Result())
        else:
            data = json.loads(rec.FinalResult())
        text = data.get("text", "").strip()
        return text.lower()
    except json.JSONDecodeError:
        print("JSON parse error.")
    except Exception as e:
        print(f"Recognition error: {e}")
    return ""

"""
