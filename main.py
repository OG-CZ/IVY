import os
import eel
from features import *
from command import *

eel.init("www")

host = "localhost"
port = 8000

os.system(f'start msedge.exe --app="http://{host}:{port}/index.html"')

eel.start(
    "index.html",
    options={"mode": None, "host": host, "port": port, "chromeFlags": []},
    block=True,
)
