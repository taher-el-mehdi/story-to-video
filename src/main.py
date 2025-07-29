import subprocess
import os

def list_scripts():
    return {
        "1": {
            "name": "Read pages from PDF and write into story_text for folder of story.",
            "script": "./src/scripts/read_pdf.py",
            "args": [
                {"flag": "--pdf", "prompt": "Path to PDF file"},
                {"flag": "--start", "prompt": "Start page number"},
                {"flag": "--stop", "prompt": "Stop page number"},
                {"flag": "--folder", "prompt": "Output folder name"},
            ]
        },
        "2": {
            "name": "Clean the story from (Extra whitespace, Newlines and tabs) save it under story_cleaned.txt",
            "script": "./src/scripts/clean_story.py",
            "args": [
                {"flag": "--story", "prompt": "Path to story file text"},
            ]
        },
        "3": {
            "name": "split story by tokens",
            "script": "./src/scripts/split_story_by_tokens.py",
            "args": [
                {"flag": "--story", "prompt": "Path to story file text"},
            ]
        },
        "4": {
            "name": "Generate audios",
            "script": "./src/scripts/generate_audios.py",
            "args": [
                {"flag": "--story", "prompt": "Path to story file text"},
            ]
        }
    }

def main():
    scripts = list_scripts()

    print("Steps to make a short story:")
    for key, val in scripts.items():
        print(f"{key}. {val['name']}")

    choice = input("Enter the number: ").strip()

    if choice not in scripts:
        print("❌ Invalid choice.")
        return

    selected = scripts[choice]
    cmd = ["python", selected["script"]]

    for arg in selected["args"]:
        default = f" (default: {arg['default']})" if "default" in arg else ""
        value = input(f"{arg['prompt']}{default}: ").strip()
        if not value and "default" in arg:
            value = arg["default"]
        if value:
            cmd.extend([arg["flag"], value])

    print("\n🔧 Running:", " ".join(cmd), "\n")
    subprocess.run(cmd)

if __name__ == "__main__":
    main()