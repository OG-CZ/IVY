import os
import time
import socket
import subprocess
import shutil
from pathlib import Path
import eel
import config
from lib.main.features import *
from lib.main.command import *
from lib.auth import recognize
import lib.main.response as response


def _wait_port(host, port, timeout=10):
    print(f"Waiting for server on {host}:{port}...")
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            s = socket.create_connection((host, port), timeout=0.5)
            s.close()
            print(f"Server is ready on {host}:{port}")
            return True
        except OSError as e:
            print(f"Port not ready yet: {e}")
            time.sleep(0.5)
    print(f"Timeout waiting for {host}:{port}")
    return False


def start():
    eel.init("ui")

    root = Path(__file__).resolve().parent
    bat = root / "device.bat"
    if bat.exists():
        try:
            print(f"Running {bat} ...")
            subprocess.run(str(bat), shell=True, check=False)
        except Exception as e:
            print(f"device.bat error: {e}")
    else:
        print(f"{bat} not found, skipping.")

    @eel.expose
    def init():

        # print("Initializing... please wait")
        # time.sleep(3)

        eel.hideLoader()
        print("now ready for face authentication")
        speak("Ready for Face Authentication")
        flag = recognize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication was Successful")
            eel.hideFaceAuthSuccess()
            speak(random.choice(response.welcome_back_user))
            eel.hideStart()
        else:
            speak("Face Authentication has Failed")

    start_page = f"index.html?v={config.VERSION}"
    url = f"http://{config.HOST}:{config.PORT}/{start_page}"

    try:
        print(f"Starting Eel server on {config.HOST}:{config.PORT}...")
        eel.start(
            start_page,
            options={"mode": None, "host": config.HOST, "port": config.PORT},
            block=False,
        )
        print("Eel server started successfully")
    except Exception as e:
        print(f"Error starting Eel: {e}")
        try:
            print("Trying fallback port 5500...")
            eel.start("index.html", mode="default", port=5500, block=False)
        except Exception as e2:
            print(f"Fallback also failed: {e2}")

    # Give the server time to start
    time.sleep(3)

    def _open_app_window(u: str) -> bool:
        edge = shutil.which("msedge") or shutil.which("msedge.exe")
        chrome = shutil.which("chrome") or shutil.which("chrome.exe")
        candidates = [
            edge,
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            chrome,
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ]
        for exe in filter(None, candidates):
            if os.path.exists(exe):
                try:
                    subprocess.Popen([exe, "--new-window", f"--app={u}"])
                    print(f"Launched app window with: {exe}")
                    return True
                except Exception as e:
                    print(f"Failed launching {exe}: {e}")
        try:
            os.startfile(u)
            print("Opened in default browser:", u)
            return True
        except Exception as e:
            print("Failed to open browser:", e)
            return False

    if _wait_port(config.HOST, config.PORT, timeout=15):
        _open_app_window(url)
    else:
        print("Eel server did not start in time:", url)
        print("Trying to open browser anyway...")
        _open_app_window(url)

    while True:
        eel.sleep(1.0)
