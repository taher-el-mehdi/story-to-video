# main.py
import argparse
import subprocess
import os

def main():
    parser = argparse.ArgumentParser(description="CLI to extract story from PDF.")
    parser.add_argument("--pdf", required=False, help="Path to the PDF file.")
    parser.add_argument("--start", type=int, required=True, help="Start page number.")
    parser.add_argument("--stop", type=int, required=True, help="Stop page number.")
    parser.add_argument("--folder", required=True, help="Folder name for output.")

    args = parser.parse_args()

    # Call the PDF reader script with args
    subprocess.run([
        "python", "./src/scripts/read_pdf.py",
        "--pdf", args.pdf,
        "--start", str(args.start),
        "--stop", str(args.stop),
        "--folder", args.folder
    ])

if __name__ == "__main__":
    main()