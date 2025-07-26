import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import base64


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai = AsyncOpenAI(api_key=OPENAI_API_KEY)

PROMPT = """A small, dimly lit 19th-century Russian student room with frosted windows and mismatched furniture. A pale young woman in simple clothes sits quietly by the window on a wooden stool, focused on embroidery. In the background, a young man in a vest paces the room reading from a medical book. The room is slightly cluttered — books, old dishes, thread, and paper scattered around. The mood is quiet and melancholic, with cold winter light filtering in through the icy glass. The colors are muted: browns, grays, and soft blues. Include the title “Anyuta” and the author’s name “Anton Chekhov” in a classic serif font."""

async def generate_image():
    response = await openai.images.generate(
        model="dall-e-2",
        prompt=PROMPT,
        n=1,
        size="1024x1024",
        response_format="b64_json",
    )
    image_data = response.data[0].b64_json
    with open("story.png", "wb") as f:
        f.write(base64.b64decode(image_data))

asyncio.run(generate_image())