from transformers import pipeline

# Load model (keep accurate one)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

labels = ["action", "dialogue", "suspense", "narrative"]

def preprocess_text(text, chunk_size=30):
    words = text.split()
    chunks = []

    # Split into chunks
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)

    results = []

    print("Processing chunks...\n")

    for idx, chunk in enumerate(chunks):
        result = classifier(chunk, labels)
        context = result["labels"][0]

        results.append({
            "chunk": chunk,
            "context": context
        })

        print(f"Chunk {idx+1}: {context}")

    return results


# Sample text (replace later with book)
text = """
He walked slowly into the dark room. The silence was unsettling. 
A sudden noise echoed behind him and he turned quickly.

"Who's there?" he shouted.

No response came. His heart pounded as he moved forward cautiously.
Suddenly, footsteps approached rapidly and he began to run.

He pushed the door open and escaped into the night, breathing heavily.
"""

processed_data = preprocess_text(text)

print("\nFinal Stored Data:\n")
for item in processed_data:
    print(item)
    print("-" * 40)