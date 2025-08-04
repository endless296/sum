from fastapi import FastAPI, Request
from pydantic import BaseModel
import re
from transformers import pipeline

# Load summarizer once
summarizer = pipeline("summarization", model="Falconsai/text_summarization")
app = FastAPI()

class TextInput(BaseModel):
    text: str

# -- (All your helper functions here: chunk_text, scale_summary_length, etc.) --
# Paste `chunk_text`, `truncate_to_words`, `scale_summary_length`, `summarize_text`, `improve_summary` here

@app.post("/summarize")
def summarize(input_data: TextInput):
    raw_summary = summarize_text(input_data.text)
    max_words = min(50, max(20, len(input_data.text.split()) // 10))
    final_summary = improve_summary(raw_summary, max_words=max_words)
    return {"summary": final_summary}
