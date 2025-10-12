import time
import api

# assistant info
ASSISTANT_NAME = "Ivy"
MODEL_DIR = "machine-learning/faster-whisper-small.en"
MODEL_BACKUP = "model/"

# setup
HOST = "localhost"
PORT = 5500
VERSION = int(time.time())

# hot word detection api -> https://console.picovoice.ai/ - sign up to get key
PORCUPINE_API_KEY = api.PORCUPINE_API_KEY  # paste here
PORCUPINE_IVY_HOTKEY_MODEL = "model/hot-word-detection/hey-ivy_en_windows_v3_0_0.ppn"
