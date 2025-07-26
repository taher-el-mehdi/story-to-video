import pymupdf
import os

# === Configurable Page Range (1-based) ===
start_reading = 51
stop_reading = 60

# === File Paths ===
cwd = os.getcwd()
book_path = os.path.join(cwd, "stories", "book.pdf")
output_dir = os.path.join(cwd, "stories", "07 - EASTER NIGHT")
story_path = os.path.join(output_dir, "story_text.txt")

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Open the PDF document
doc = pymupdf.open(book_path)

# Convert to 0-based indexing
start_index = max(0, start_reading - 1)
stop_index = min(len(doc), stop_reading)

# Read pages and write text to output file
with open(story_path, "w", encoding="utf-8") as out:
    for page_index in range(start_index, stop_index):
        page = doc[page_index]
        text = page.get_text()
        out.write(text)
        print(f"✅ Page {page_index + 1} has been written to 'story_text.txt'")
print("🎉 Story extraction completed! You can now review 'story_text.txt'.")