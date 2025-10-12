import multiprocessing as mp
import threading
import time


def start_ivy(q: mp.Queue):
    print("UI process is running")
    from main import start
    import eel
    from lib.main.command import all_commands

    # Start Eel (start() should call eel.start(..., block=False))
    start()

    # Consume hotword events and run commands in the UI process
    def consume():
        while True:
            msg = q.get()
            if msg == "hotword":
                eel.spawn(all_commands)  # safe call with UI connected

    threading.Thread(target=consume, daemon=True).start()

    # Keep UI process alive
    while True:
        time.sleep(1)


def listen_hotword(q: mp.Queue):
    print("Hotword process is running")
    from lib.main.features import hotword

    hotword(q)  # emit events instead of calling eel


if __name__ == "__main__":
    q = mp.Queue()
    p1 = mp.Process(target=start_ivy, args=(q,), daemon=True)
    p2 = mp.Process(target=listen_hotword, args=(q,), daemon=True)
    p1.start()
    p2.start()
    p1.join()
