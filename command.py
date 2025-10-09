import pyttsx3
import speech_recognition as sr
from vosk import Model, KaldiRecognizer
import json
import os

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"


def speak(text):
    engine = pyttsx3.init()

    # speed of talk
    engine.setProperty("rate", 136.5)

    # voice choose
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)

    engine.say(text)
    engine.runAndWait()


import os
import speech_recognition as sr


def take_command():
    model_dir = "machine-learning/vosk-model-small-en-us-0.15"
    if not os.path.isdir(model_dir):
        print(f"Model folder missing: {model_dir}")
        return ""
    os.environ["VOSK_MODEL_PATH"] = model_dir  # let recognize_vosk find it

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, timeout=10, phrase_time_limit=6)
    try:
        print("recognizing")
        result = r.recognize_vosk(audio, language="en-US")
        if result.startswith("{"):
            import json

            try:
                txt = json.loads(result).get("text", "")
            except json.JSONDecodeError:
                txt = ""
        else:
            txt = result
        return txt.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.WaitTimeoutError:
        print("Timeout waiting for speech.")
    except Exception as e:
        print("Recognition error:", e)
    return ""


def check_mic_to_use():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(
            'Microphone with name "{1}" found for `Microphone(device_index={0})`'.format(
                index, name
            )
        )


text = take_command()
speak(text)


def take_command_force(device_index=None):
    """
    Brute-force listen-and-recognize loop using Vosk/Kaldi.

    under the hood version for speech recognition sr.recognize_vosk() -> str
    if it that function is not available we can use this

    Args:
        device_index (int|None): optional microphone device index for sr.Microphone

    Returns:
        str: recognized text in lowercase, or "" if the model folder is missing.
    """

    model_dir = "machine-learning/vosk-model-small-en-us-0.15"
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
            print("Calibrating (0.5s)...")
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
        print("Recognizing (KaldiRecognizer)...")
        rec = KaldiRecognizer(model, 16000)
        raw = audio.get_raw_data(convert_rate=16000, convert_width=2)
        if rec.AcceptWaveform(raw):
            data = json.loads(rec.Result())
        else:
            data = json.loads(rec.FinalResult())
        text = data.get("text", "").strip()
        print("You said:", text or "<empty>")
        return text.lower()
    except json.JSONDecodeError:
        print("JSON parse error.")
    except Exception as e:
        print(f"Recognition error: {e}")
    return ""
