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


# whatsapp country code
COUNTRY_CODES = {
    "PH": "+63",  # Philippines
    "IN": "+91",  # India
    "US": "+1",  # United States
    "UK": "+44",  # United Kingdom
    "CA": "+1",  # Canada
    "AU": "+61",  # Australia
    "SG": "+65",  # Singapore
    "MY": "+60",  # Malaysia
    "DE": "+49",  # Germany
    "FR": "+33",  # France
    # Add more as needed
}

# WEATHER API USING OPEN METEO
GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

# IP Api
IP_API = "http://ip-api.com/json/?fields=status,message,city,regionName,country,lat,lon,timezone,query"

DEFAULT_CITY = "singapore"

WEATHER_ANIM = {
    "sunny": "assets/animations/weather/sunny.json",
    "rain": "assets/animations/weather/rain1.json",
    "cloudy": "assets/animations/weather/cloudy.json",  # fixed typo
    "storm": "assets/animations/weather/storm.json",
    "snow": "assets/animations/weather/snow.json",
    "fog": "assets/animations/weather/fog.json",
    "default": "assets/animations/weather/sunny.json",
}
