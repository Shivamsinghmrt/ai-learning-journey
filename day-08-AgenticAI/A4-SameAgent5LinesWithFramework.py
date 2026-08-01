# Quick Win 4A: The Same Agent, 5 Lines with a Framework

 

# Problem Statement: Rebuild the calculator agent — but let a framework handle the whole tool loop for you.

 

# Goal of the Problem: See how much boilerplate a framework removes. create_react_agent runs the reason → act → observe loop automatically.

 

# Step 1.  Install the framework packages.

# !pip install -U langgraph langchain-openai (Google Collab)

# pip install -U langgraph langchain-openai (VS Code)

 

# Expected output

# Successfully installed langgraph-... langchain-openai-... (and deps)

 

# Step 2.  Define a tool with the @tool decorator and create the agent.

import os

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

load_dotenv()


@tool
def calculate(expression: str) -> str:
    """Evaluate a basic arithmetic expression like '2*(3+4)'."""

    import ast
    import operator as o

    ops = {
        ast.Add: o.add,
        ast.Sub: o.sub,
        ast.Mult: o.mul,
        ast.Div: o.truediv,
        ast.Pow: o.pow,
        ast.Mod: o.mod,
        ast.FloorDiv: o.floordiv,
        ast.USub: o.neg,
        ast.UAdd: o.pos,
    }

    def ev(n):
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return n.value

        if isinstance(n, ast.BinOp):
            if type(n.op) not in ops:
                raise ValueError(f"unsupported operator: {type(n.op).__name__}")
            return ops[type(n.op)](ev(n.left), ev(n.right))

        if isinstance(n, ast.UnaryOp):
            if type(n.op) not in ops:
                raise ValueError(f"unsupported operator: {type(n.op).__name__}")
            return ops[type(n.op)](ev(n.operand))

        raise ValueError("bad expression")

    return str(ev(ast.parse(expression, mode="eval").body))


model = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

agent = create_react_agent(model, tools=[calculate])

 

# Expected output

# (no output — agent ready)

 

# Step 3.  Invoke the agent. The tool loop runs for you.

result = agent.invoke({"messages": [("user",

   "What is 4567 times 12, minus 89? Then tell me if the result is even or odd.")]})

print(result["messages"][-1].content)

 

# Expected output

# 4567 x 12 - 89 = 54715, which is an odd number.

 

# Step 4.  Peek inside the loop to see the reasoning + tool call the framework ran.

for m in result["messages"]:

   m.pretty_print()

 

# Expected output

# ================ Human Message =================

# What is 4567 times 12, minus 89? ...

# ================= Ai Message ===================

# Tool Calls: calculate  ({'expression': '4567*12-89'})

# ================= Tool Message =================

# 54715

# ================= Ai Message ===================

# 54715, which is an odd number.