# 🎥 Story to Video

This is a command-line Python tool that allows you to convert a PDF story into a video. The tool is modular and broken into six steps:

## 🚀 Steps:
- 📄 Extract pages from a PDF.
- 🧹 Clean the extracted text (remove whitespace, newlines, tabs).
- ✂️ Split story into logical segments based on tokens.
- 🔊 Generate audio from text using TTS.
- 🎵 Merge generated audios into one track.
- 🎥 Merge audio with an image to create an MP4 video.


##  How to Use
### 1. Launch the Tool
```bash
python main.py
```

You will be prompted to enter:

* PDF path of the book
* Page range
* Story name (folder)
### Example prompt:
```bash
python main.py

# Book: book.pdf
# Start page number: 5
# Stop page number: 15
# Story: my_story
```
### 2. Script List

| Step | Script Name                 | Description                                                                     |
| ---- | --------------------------- | ------------------------------------------------------------------------------- |
| 1    | `read_pdf.py`               | Reads specific pages from a PDF and saves them as a text file in a story folder |
| 2    | `clean_story.py`            | Cleans the story (removes whitespace, tabs, etc.)                               |
| 3    | `split_story_by_tokens.py`  | Splits the story text by logical chunks (tokens)                                |
| 4    | `generate_audios.py`        | Generates audio clips for each text chunk                                       |
| 5    | `merge_audio_folder.py`     | Merges audio clips into one audio file                                          |
| 6    | `merge_audio_with_image.py` | Merges final audio with an image into an MP4 video                              |
---

## 🛠 Folder Structure

```
.
├── main.py
├── src/
│   └── scripts/
│       ├── read_pdf.py
│       ├── clean_story.py
│       ├── split_story_by_tokens.py
│       ├── generate_audios.py
│       ├── merge_audio_folder.py
│       └── merge_audio_with_image.py
```

## 📦 Requirements 
Install dependencies:
```bash
pip install pedalboard soundfile numpy moviepy
```
