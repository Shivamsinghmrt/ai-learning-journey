#  
import json
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI

client = OpenAI()

# Expected output

# (no output)

# Step 2 — The item to grade

question = "Why is agent evaluation harder than evaluating a normal function?"

reference = ("Because outputs are open-ended and non-deterministic, there is "

           "often no single correct answer, and errors compound across steps.")

candidate = ("Agent evaluation is harder because the same input can give "

           "different outputs and small mistakes pile up over many steps.")

# Expected output

# (no output)

# Step 3 — Ask the judge for a rubric score in JSON

judge_prompt = f"""You are a strict grader. Score the CANDIDATE answer against

the REFERENCE on two axes from 1 (poor) to 5 (excellent):

- coherence: is it clear and well structured?

- correctness: is it factually aligned with the reference?

 

Reply ONLY as JSON:

{{"coherence": <1-5>, "correctness": <1-5>, "reason": "<one short line>"}}

 

QUESTION: {question}

REFERENCE: {reference}

CANDIDATE: {candidate}"""

 

resp = client.chat.completions.create(

  model="gpt-4o-mini",

  messages=[{"role": "user", "content": judge_prompt}],

  temperature=0,

  response_format={"type": "json_object"},

)

score = json.loads(resp.choices[0].message.content)

print(json.dumps(score, indent=2))

# Expected output

# {

# "coherence": 5,

# "correctness": 5,

# "reason": "Clear and matches the reference on non-determinism and compounding errors."

# }

 

# (Scores may vary by a point; reason wording will differ.)

# Step 4 — Turn the scores into a simple verdict

avg = (score["coherence"] + score["correctness"]) / 2

print(f"Average score: {avg:.1f}/5 ->",

    "PASS" if avg >= 4 else "NEEDS WORK")

# Expected output

# Average score: 5.0/5 -> PASS

# Always ask the judge for a short reason. The justification is what lets you trust - or challenge - an automated score.