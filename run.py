import multiprocessing as mp


def start_ivy():
    print("UI process is running.")
    from main import start

    start()


def listen_hotword():
    print("Hotword process is running.")
    from lib.main.features import hotword

    hotword()


if __name__ == "__main__":
    mp.set_start_method("spawn", force=True)
    p1 = mp.Process(target=start_ivy, daemon=False)
    p2 = mp.Process(target=listen_hotword, daemon=True)
    p1.start()
    p2.start()
    p1.join()
    if p2.is_alive():
        p2.terminate()
        p2.join()
