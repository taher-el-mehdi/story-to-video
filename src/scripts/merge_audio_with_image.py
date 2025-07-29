from moviepy import *
import os.path
import argparse

parser = argparse.ArgumentParser(description="Generate audios")
parser.add_argument("--story", required=True, help="story folder name.")
args = parser.parse_args()
story = args.story
# Paths to your files
audio_path = os.path.join("Stories",story, "story.wav")
image_path =  os.path.join("Stories",story, "story.png")
output_path = os.path.join("Stories",story, "story.mp4")

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