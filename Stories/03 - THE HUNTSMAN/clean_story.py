import os
import glob
import re

cwd = os.getcwd()
file = os.path.join(cwd,"stories", "03 - THE HUNTSMAN", "story_text.txt")

with open(file, "r", encoding="utf-8") as f:
    text = f.read()

    # Clean the text
    text_cleaned = re.sub(r'\s+', ' ', text)
    text_cleaned = re.sub(r'\d+', '', text_cleaned)

    # Prepare output path
    file_output = file.replace('story_text.txt', 'story_cleaned.txt')

    # Write cleaned text
    with open(file_output, 'w', encoding='utf-8') as f_out:
        f_out.write(text_cleaned)