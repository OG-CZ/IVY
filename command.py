import pyttsx3

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
