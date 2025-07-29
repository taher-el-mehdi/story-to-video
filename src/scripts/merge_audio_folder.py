import os
import soundfile as sf
import numpy as np
from pedalboard import Pedalboard, Gain

cwd = os.getcwd()
# === Configuration ===
AUDIO_FOLDER =  os.path.join(cwd, "Stories","08 - VANKA", "audios")
OUTPUT_FILE = os.path.join(cwd, "Stories","08 - VANKA", 'story.wav')

# === Load and sort audio files ===
audio_files = sorted([
    os.path.join(AUDIO_FOLDER, f)
    for f in os.listdir(AUDIO_FOLDER)
    if f.lower().endswith('.wav')
])

if not audio_files:
    raise Exception("No .wav files found in 'audios' folder!")

sample_rate = None
all_audio = []

for file in audio_files:
    audio, sr = sf.read(file)
    duration_sec = len(audio) / sr
    duration_str = f"{duration_sec:.2f} sec" if duration_sec < 60 else f"{duration_sec / 60:.2f} min"
    print(f"🗣️  Loaded: {file} | Duration: {duration_str}")


    # Ensure consistent sample rate
    if sample_rate is None:
        sample_rate = sr
    elif sr != sample_rate:
        raise ValueError(f"Sample rate mismatch: {file} has {sr}, expected {sample_rate}")

    # Convert mono to stereo if needed
    if audio.ndim == 1:
        audio = np.stack([audio, audio], axis=-1)

    all_audio.append(audio)

# === Concatenate all audio chunks ===
combined_audio = np.concatenate(all_audio)

# === Optional: Apply effects with Pedalboard ===
board = Pedalboard([
    Gain(gain_db=2.0),  # You can chain effects here
])
processed_audio = board(combined_audio, sample_rate)

# === Save output ===
sf.write(OUTPUT_FILE, processed_audio, sample_rate)
total_duration_sec = sum(len(a) for a in all_audio) / sample_rate
total_str = f"{total_duration_sec:.2f} sec" if total_duration_sec < 60 else f"{total_duration_sec / 60:.2f} min"
print(f"🎧 Total duration of all audio files: {total_str}")
