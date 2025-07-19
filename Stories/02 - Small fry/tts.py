import asyncio
import os
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer
from openai import OpenAIError, RateLimitError
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai = AsyncOpenAI(api_key=OPENAI_API_KEY)
import aiofiles
instructions = """Voice: Soft, introspective, with a hint of nervousness and empathy.
Tone: Gentle, thoughtful, subtly ironic when fitting; never mocking.
Pacing: Slow to moderate, with natural pauses for reflection and hesitation.
Emotion: Restrained but human — hint at shame, loneliness, and quiet struggle.
Pronunciation: Clear; lightly stress words like ashamed, forgotten, invisible.
Pauses: Use short pauses to show awkwardness, doubt, or emotional weight.
Overall: Like telling the story of a small life with quiet depth and dignity."""

input_text = "الحمد لله على كل حال"

async def main() -> None:
    try:
        # Create a streaming response for speech synthesis
        async with  openai.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="sage",
            input=input_text,
            response_format="wav",
        ) as response:
            output_path = "حمدلله.wav"
            # Save streamed audio to file
            async with aiofiles.open(output_path, "wb") as f:
                async for chunk in response.iter_bytes():
                    await f.write(chunk)

        print(f"✅ Audio saved to: {output_path}")

    except RateLimitError:
        print("❌ Quota exceeded. Please check your OpenAI account billing and limits.")
    except OpenAIError as e:
        print(f"❌ OpenAI API error: {e}")

if __name__ == "__main__":
    asyncio.run(main())