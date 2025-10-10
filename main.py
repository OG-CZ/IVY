import os
import time
import eel
from lib.vocal.features import *
from lib.vocal.command import *

eel.init("www")

HOST = "localhost"
PORT = 5500
VERSION = int(time.time())


def main():
    start_page = f"index.html?v={VERSION}"
    os.system(f'start msedge.exe --app="http://{HOST}:{PORT}/{start_page}"')

    eel.start(
        start_page,
        options={"mode": None, "host": HOST, "port": PORT, "chromeFlags": []},
        block=True,
    )


if __name__ == "__main__":
    main()
