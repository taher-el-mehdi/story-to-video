import subprocess
import os

def list_scripts():
    return {
        "1": {
            "name": "Read pages from PDF and write into story_text for folder of story.",
            "script": "./src/scripts/read_pdf.py",
            "args": [
                {"flag": "--pdf", "prompt": "Book"},
                {"flag": "--start", "prompt": "Start page number"},
                {"flag": "--stop", "prompt": "Stop page number"},
                {"flag": "--story", "prompt": "Story"},
            ]
        },
        "2": {
            "name": "Clean the story from (Extra whitespace, Newlines and tabs) save it under story_cleaned.txt",
            "script": "./src/scripts/clean_story.py",
        },
        "3": {
            "name": "split story by tokens",
            "script": "./src/scripts/split_story_by_tokens.py",
        },
        "4": {
            "name": "Generate audios",
            "script": "./src/scripts/generate_audios.py",
        },
        "5": {
            "name": "Merge audios",
            "script": "./src/scripts/merge_audio_folder.py",
        },
        "6": {
            "name": "Merge audio with image to produce a video",
            "script": "./src/scripts/merge_audio_with_image.py",
        }
    }

def main():
    scripts = list_scripts()

    
    story = ''
    for key, val in scripts.items():
        name = val["name"]
        script = val["script"]
        cmd = ["python", script]
        print(key, name)
        if 'args' in val:
            for arg in val["args"]:
                default = f" (default: {arg['default']})" if "default" in arg else ""
                value = input(f"{arg['prompt']}{default}: ").strip()
                cmd.extend([arg["flag"], value])
                if arg["flag"]=='--story':
                    story = value
        else:
            cmd = ["python", script, "--story", story]

        subprocess.run(cmd)

if __name__ == "__main__":
    main()