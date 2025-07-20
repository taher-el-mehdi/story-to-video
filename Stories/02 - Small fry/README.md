# Small Fry — Text Cleaning & Audio Generation

This project is based on Anton Chekhov’s short story **“Small Fry”**, a quietly tragic and darkly humorous tale of a minor government clerk who, after drinking at a celebration, reflects on his life’s emptiness while wandering alone at night — even obsessing over a cockroach he notices on his coat. The story is a subtle exploration of insignificance, loneliness, and the desperate search for meaning.


## ⚙️ Scripts Overview
### 1. `clean_texts.py`  
This script processes the raw text files of the story by:

- Reading all `.txt` files from the `stories/02 - Small fry/story/` directory.
- Removing:
  - Extra whitespace
  - Newlines and tabs
  - All numeric digits
- Saving the cleaned versions into a parallel directory: `story_cleaned/`, preserving the original filenames.

### 2. `generate_audios.py`  
This script generates audio files from the cleaned text:

- Takes cleaned `.txt` files from `story_cleaned/`
- Converts each file into a `.wav` file using text-to-speech
- Saves the `.wav` files into the `story_audios/` directory
- Each output audio file matches the name of the cleaned input file.

## 🧪 What’s Next?

- I built a script that splits the text and generates all `.wav` files automatically — but next time, I want to improve it to **generate only one complete audio file**, instead of many small ones.