import os
import tiktoken
import argparse

def main():
    parser = argparse.ArgumentParser(description="split story by tokens")
    parser.add_argument("--story", required=True, help="story folder name.")
    args = parser.parse_args()
    
    # === CONFIGURATION ===
    INPUT_FILE = os.path.join("stories", args.story, 'story_cleaned.txt')        # Your input file
    OUTPUT_DIR = os.path.join("stories", args.story, 'chunks') 
    MAX_TOKENS = 1000                   # Tokens per chunk
    ENCODING_NAME = "cl100k_base"       # Tokenizer used by ChatGPT (GPT-4/3.5)

    # === SETUP ===
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    enc = tiktoken.get_encoding(ENCODING_NAME)

    # === LOAD TEXT ===
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        full_text = f.read()

    # === TOKENIZE INTO SENTENCES ===
    import re
    sentences = re.split(r'(?<=[.!?])\s+', full_text)

    chunks = []
    current_chunk = ""
    current_tokens = 0

    for sentence in sentences:
        sentence_tokens = len(enc.encode(sentence))

        if current_tokens + sentence_tokens > MAX_TOKENS:
            # Save current chunk
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
            current_tokens = sentence_tokens
        else:
            current_chunk += sentence + " "
            current_tokens += sentence_tokens

    # Add the last chunk
    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    # === SAVE CHUNKS TO FILES ===
    for i, chunk in enumerate(chunks, 1):
        file_name = os.path.join(OUTPUT_DIR, f'chunk_{i:03}.txt')
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(chunk)
    print(f"✅ Done. Split into {len(chunks)} chunks in '{OUTPUT_DIR}/'")

if __name__ == "__main__":
    main()