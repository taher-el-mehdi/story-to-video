from moviepy import *
import os.path

# Paths to your files
audio_path = os.path.join("Stories","08 - VANKA", "story.wav")
image_path =  os.path.join("Stories","08 - VANKA", "story.png")
output_path = os.path.join("Stories","08 - VANKA", "story.mp4")

# Load the audio
audio = AudioFileClip(audio_path)

# Load the image and set duration to match the audio
image = ImageClip(image_path).with_duration(audio.duration)

# Resize image if needed (optional)
image = image.resized(height=720)  # adjust as needed

# Set audio to image
video = image.with_audio(audio)

# Export video
video.write_videofile(output_path, fps=24)