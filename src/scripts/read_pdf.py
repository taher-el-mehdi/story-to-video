# read_pdf.py
import pymupdf
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Extract pages from PDF and write to a text file.")
    parser.add_argument("--pdf", required=True, help="Path to the input PDF file.")
    parser.add_argument("--start", type=int, required=True, help="Start page (1-based).")
    parser.add_argument("--stop", type=int, required=True, help="Stop page (1-based).")
    parser.add_argument("--story", required=True, help="Output story name.")

    args = parser.parse_args()

    # === File Paths ===
    cwd = os.getcwd()
    output_dir = os.path.join(cwd, "Stories", args.story)
    story_path = os.path.join(output_dir, "story_text.txt")
    
    book_path = os.path.join(cwd, "Stories", args.pdf)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Open PDF
    doc = pymupdf.open(book_path)

    # Adjust indices
    start_index = max(0, args.start - 1)
    stop_index = min(len(doc), args.stop)

    # Read and write
    with open(story_path, "w", encoding="utf-8") as out:
        for page_index in range(start_index, stop_index):
            page = doc[page_index]
            text = page.get_text()
            out.write(text)
            print(f"✅ Page {page_index + 1} written to 'story_text.txt'")

    print(f"🎉 Done! Story saved at: {story_path}")

if __name__ == "__main__":
    main()
