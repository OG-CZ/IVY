import pyaudio
import numpy as np
from faster_whisper import WhisperModel

# Load model
model = WhisperModel("small.en", device="cpu")

# Mic config
RATE = 16000
CHUNK = 1024
CHANNELS = 1
FORMAT = pyaudio.paInt16

p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
)

print("🎙️ Listening... (Ctrl+C to stop)")

buffer = np.array([], dtype=np.int16)

try:
    while True:
        # Read mic audio
        data = stream.read(CHUNK)
        audio_chunk = np.frombuffer(data, dtype=np.int16)
        buffer = np.append(buffer, audio_chunk)

        # Keep ~2 seconds of audio in buffer
        if len(buffer) > RATE * 2:
            # Normalize and convert to float32 for model
            audio_float32 = (buffer / 32768.0).astype(np.float32)

            # Transcribe current buffer
            segments, _ = model.transcribe(audio_float32, beam_size=1)

            text = " ".join([seg.text for seg in segments])
            if text.strip():
                print("You said:", text)

            # Clear buffer for next cycle
            buffer = np.array([], dtype=np.int16)

except KeyboardInterrupt:
    print("\n🛑 Stopped by user")
    stream.stop_stream()
    stream.close()
    p.terminate()
