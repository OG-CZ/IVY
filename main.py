import os
import eel
from lib.main.features import *
from lib.main.command import *

eel.init("ui")


def main():
    start_page = f"index.html?v={config.VERSION}"
    os.system(
        f'start msedge.exe --app="http://{config.HOST}:{config.PORT}/{start_page}"'
    )

    eel.start(
        start_page,
        options={
            "mode": None,
            "host": config.HOST,
            "port": config.PORT,
            "chromeFlags": [],
        },
        block=True,
    )


if __name__ == "__main__":
    main()
