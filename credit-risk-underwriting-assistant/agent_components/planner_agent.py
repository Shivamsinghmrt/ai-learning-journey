import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def make_plan(goal: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a planning agent for loan underwriting. "
                    "Break the user's goal into a short ordered list of concrete steps."
                ),
            },
            {"role": "user", "content": goal},
        ],
    )
    return response.choices[0].message.content
