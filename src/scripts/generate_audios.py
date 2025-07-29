import asyncio
import os
import glob
import logging
from openai import AsyncOpenAI, OpenAIError, RateLimitError
from dotenv import load_dotenv
import aiofiles
import argparse

parser = argparse.ArgumentParser(description="Generate audios")
parser.add_argument("--story", required=True, help="story folder name.")
args = parser.parse_args()

# === CONFIG ===
INPUT_TEXTS = os.path.join("stories", args.story, "chunks")
VOICE_MODEL = "gpt-4o-mini-tts"
VOICE_NAME = "sage"

INSTRUCTIONS_STORYTELLING = """
Voice: Soft, introspective, with a hint of nervousness and empathy.
Tone: Gentle, thoughtful, subtly ironic when fitting; never mocking.
Pacing: Slow to moderate, with natural pauses for reflection and hesitation.
Emotion: Restrained but human — hint at shame, loneliness, and quiet struggle.
Pronunciation: Clear; lightly stress words like ashamed, forgotten, invisible.
Pauses: Use short pauses to show awkwardness, doubt, or emotional weight.
Overall: Like telling the story of a small life with quiet depth and dignity.
"""

# === INITIALIZATION ===
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai = AsyncOpenAI(api_key=OPENAI_API_KEY)

# === SETUP LOGGING ===
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# === FUNCTION TO GENERATE AUDIO ===
async def generate_audio(file_path: str) -> None:
    try:
        async with aiofiles.open(file_path, mode="r", encoding="utf-8") as f:
            input_text = await f.read()

        logging.info(f"📖 Processing: {os.path.basename(file_path)}")

        async with openai.audio.speech.with_streaming_response.create(
            model=VOICE_MODEL,
            voice=VOICE_NAME,
            input=input_text,
            instructions=INSTRUCTIONS_STORYTELLING,
            response_format="wav",
        ) as response:
            output_path = file_path.replace("chunks", "audios").replace(".txt", ".wav")
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            async with aiofiles.open(output_path, mode="wb") as out_f:
                async for chunk in response.iter_bytes():
                    await out_f.write(chunk)

        logging.info(f"✅ Audio saved to: {output_path}")

    except RateLimitError:
        logging.error("❌ Quota exceeded. Please check your OpenAI account billing and limits.")
    except OpenAIError as e:
        logging.error(f"❌ OpenAI API error while processing {file_path}: {e}")
    except Exception as e:
        logging.error(f"❌ Unexpected error with {file_path}: {e}")

# === MAIN FUNCTION ===
async def main() -> None:
    cwd = os.getcwd()
    full_pattern = os.path.join(cwd, INPUT_TEXTS, "*.txt")
    files = glob.glob(full_pattern)

    if not files:
        logging.warning("⚠️ No input files found.")
        return

    tasks = [generate_audio(file) for file in files]
    await asyncio.gather(*tasks)

# === ENTRY POINT ===
if __name__ == "__main__":
    asyncio.run(main())