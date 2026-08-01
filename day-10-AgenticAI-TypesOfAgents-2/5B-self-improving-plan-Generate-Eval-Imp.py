# Exercise 5B  Self-Improving Plan (Generate → Evaluate → Improve)    DEEP DIVE

 

# Problem Statement:  A Planner drafts a plan; a Critic scores it 1–10 and gives feedback; the Planner revises. Loop until the score reaches 8 or you hit the iteration limit.

# Goal of the Problem:  Implement a reinforcement-style planning loop where an evaluator acts as the reward signal.

 

# Step 1 —  Install the library and set your API key

# Run this once per session. Paste the OpenAI API key you were given.

# Python

# pip install openai --quiet

 

# Python

import os
from dotenv import load_dotenv
load_dotenv()
 

# Expected output

# (No output. The key is now available to the OpenAI client.)

 

# Step 2 —  Define the Planner and the Critic (reward signal)

# Python

from openai import OpenAI

import json

client = OpenAI()

 

def plan_step(goal, feedback=None):

  user = f"Goal: {goal}"

  if feedback:

       user += f"\nImprove the plan using this feedback: {feedback}"

  r = client.chat.completions.create(model="gpt-4o-mini",

       messages=[{"role": "system", "content": "Produce a concise 4-step plan."},

                 {"role": "user", "content": user}])

  return r.choices[0].message.content

 

def critic(goal, plan):

  r = client.chat.completions.create(model="gpt-4o-mini",

       response_format={"type": "json_object"},

       messages=[{"role": "system", "content":

                    'Score the plan 1-10 for feasibility and completeness. '

                    'Return JSON {"score": int, "feedback": "one improvement"}'},

                 {"role": "user", "content": f"Goal: {goal}\nPlan: {plan}"}])

  return json.loads(r.choices[0].message.content)

 

# Expected output

# (No output - a Planner and a Critic. The Critic is the "reward signal".)

 

# Step 3 —  Run the improvement loop

# Python

goal = "Reduce our monthly cloud bill by 30% within one quarter"

plan = plan_step(goal)

 

for i in range(1, 4):                       # up to 3 improvement iterations

  review = critic(goal, plan)

  print(f"Iteration {i}: score={review['score']} | {review['feedback'][:70]}")

  if review["score"] >= 8:

       print("Goal met - stopping."); break

  plan = plan_step(goal, review["feedback"])   # revise using feedback

 

print("\n===== FINAL PLAN =====\n")

print(plan)

 

# Expected output

# Iteration 1: score=6 | Add specific cost-monitoring and set measurable targets

# Iteration 2: score=8 | Looks feasible and measurable

# Goal met - stopping.

 

# ===== FINAL PLAN =====

# 1. Audit current usage with a cost dashboard ...

# 2. Right-size or shut down idle instances ...

# 3. Move suitable workloads to reserved/spot pricing ...

# 4. Set alerts and review weekly against the 30% target ...

# # Scores rise as the plan improves - a generate/evaluate/improve (reinforcement) loop