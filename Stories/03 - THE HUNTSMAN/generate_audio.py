import asyncio
import os
import glob
import logging
from openai import AsyncOpenAI, OpenAIError, RateLimitError
from dotenv import load_dotenv
import aiofiles

# === CONFIG ===
OUTPUT_FILE = os.path.join("stories", "03 - THE HUNTSMAN", "story_cleaned_rest_of_2000_chars.txt")
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
            output_path = file_path.replace("story_cleaned", "story_audio").replace(".txt", ".wav")
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
    await asyncio.gather(generate_audio(OUTPUT_FILE))

# === ENTRY POINT ===
if __name__ == "__main__":
    asyncio.run(main())