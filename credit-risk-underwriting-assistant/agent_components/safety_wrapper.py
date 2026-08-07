import os
import re

from dotenv import load_dotenv

load_dotenv()

try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) if os.getenv("OPENAI_API_KEY") else None
except Exception:
    client = None

EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE = re.compile(r"\b(?:\+?\d{1,3}[- ]?)?\d{10}\b")


def is_flagged(text: str) -> bool:
    if client is None:
        return False
    response = client.moderations.create(model="omni-moderation-latest", input=text)
    return response.results[0].flagged


def redact(text: str) -> str:
    text = EMAIL.sub("[EMAIL]", text)
    text = PHONE.sub("[PHONE]", text)
    return text


def safe_input(text: str) -> dict:
    if is_flagged(text):
        return {"allowed": False, "text": None, "reason": "blocked by moderation"}
    return {"allowed": True, "text": redact(text), "reason": "ok"}
