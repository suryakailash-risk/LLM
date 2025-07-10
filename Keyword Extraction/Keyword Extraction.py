from transformers import pipeline
keyword_pipeline = pipeline("ner", model="ml6team/keyphrase-extraction-distilbert-inspec")
def extract_keywords(text):
    keywords = keyword_pipeline(text)
    # Filter out non-keyword entities
    keywords = [kw['word'] for kw in keywords ]
    return keywords  # Return top K keywords
text = """Climate change is one of the most pressing challenges of the 21st century."""
keywords = extract_keywords(text)
print("Extracted Keywords:")
for keyword in keywords:
    print(f"- {keyword}")
