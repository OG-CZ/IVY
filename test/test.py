import struct
import time
import pvporcupine
import pyaudio
import pyautogui
import config

print(config.PORCUPINE_API_KEY)


def hotword():
    porcupine = None
    paud = None
    audio_stream = None

    try:
        print("Initializing Porcupine...")
        porcupine = pvporcupine.create(
            access_key=config.PORCUPINE_API_KEY,
            keyword_paths=["model/hot-word-detection/hey-ivy_en_windows_v3_0_0.ppn"],
        )

        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length,
        )

        print("Listening for hotword...")

        last_detected = 0
        cooldown = 3

        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:
                now = time.time()
                if now - last_detected > cooldown:
                    print("Hotword detected!")

                    pyautogui.keyDown("win")
                    pyautogui.press("j")
                    pyautogui.keyUp("win")

                    last_detected = now

    except Exception as e:
        print("Error:", e)

    finally:
        if porcupine:
            porcupine.delete()
        if audio_stream:
            audio_stream.close()
        if paud:
            paud.terminate()
        print("Program exited cleanly.")


if __name__ == "__main__":
    hotword()
