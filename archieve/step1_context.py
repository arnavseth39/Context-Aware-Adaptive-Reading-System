from transformers import pipeline

# Load zero-shot classification model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define your labels
labels = ["action", "dialogue", "suspense", "narrative"]

def detect_context(text):
    result = classifier(text, labels)
    return result["labels"][0]

# Sample test text (you can change this)
text = """
He ran as fast as he could, his heart pounding loudly. Suddenly, a loud noise echoed behind him.
"Stop right there!" someone shouted. He froze.
"""

# Split into chunks
chunk_size = 40
words = text.split()

for i in range(0, len(words), chunk_size):
    chunk = " ".join(words[i:i+chunk_size])
    context = detect_context(chunk)
    print(f"Text: {chunk}")
    print(f"Detected Context: {context}")
    print("-" * 50)