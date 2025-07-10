from transformers import pipeline
doc_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")
def summarize_text(text, max_length=130, min_length=30, do_sample=False):
    summary = doc_pipeline(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
    return summary[0]['summary_text'] if summary else ""

text = """Climate change is one of the most pressing challenges of the 21st century, affecting ecosystems, economies, and communities worldwide. Rising global temperatures have led to more frequent and severe weather events, such as hurricanes, floods, and droughts, displacing millions of people and threatening food and water security. Scientists agree that reducing greenhouse gas emissions is crucial to slowing down these impacts. Transitioning to renewable energy, improving energy efficiency, and protecting forests are among the key strategies proposed to mitigate climate change. While international agreements like the Paris Accord have set ambitious targets, their success depends on the collective efforts of governments, businesses, and individuals alike."""
summary = summarize_text(text)
print("Summary:")
print(summary)
