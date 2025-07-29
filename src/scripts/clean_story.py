import os
import glob
import re
import argparse

def main():
    parser = argparse.ArgumentParser(description="Clean the story from (Extra whitespace, Newlines and tabs)")
    parser.add_argument("--story", required=True, help="story folder name.")
    args = parser.parse_args()

    cwd = os.getcwd()
    file = os.path.join(cwd,"Stories", args.story, "story_text.txt")
    print(file)
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


if __name__ == "__main__":
    main()