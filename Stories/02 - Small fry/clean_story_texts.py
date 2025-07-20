import os
import glob
import re

# Build the full pattern
cwd = os.getcwd()
full_pattern = os.path.join(cwd, "stories", "02 - Small fry", "story_text", "*")

# Get matching files
files = glob.glob(full_pattern)

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

        # Clean the text
        text_cleaned = re.sub(r'\s+', ' ', text)
        text_cleaned = re.sub(r'\d+', '', text_cleaned)

        # Prepare output path
        file_output = file.replace('story', 'story_cleaned')

        # Ensure output directory exists
        output_dir = os.path.dirname(file_output)
        os.makedirs(output_dir, exist_ok=True)

        # Write cleaned text
        with open(file_output, 'w', encoding='utf-8') as f_out:
            f_out.write(text_cleaned)

    # break  # Uncomment this if you want to test only the first file