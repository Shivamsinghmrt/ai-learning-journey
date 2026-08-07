import ast
import operator as op
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def calculate(expression: str) -> str:
    ops = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv, ast.Pow: op.pow, ast.USub: op.neg}

    def ev(node):
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.BinOp):
            return ops[type(node.op)](ev(node.left), ev(node.right))
        if isinstance(node, ast.UnaryOp):
            return ops[type(node.op)](ev(node.operand))
        raise ValueError("unsupported expression")

    return str(ev(ast.parse(expression, mode="eval").body))


def tool_call_for_debt_ratio(income: float, debt: float, loan: float) -> str:
    expression = f"({debt}+{loan})/{income}"
    return calculate(expression)


def ask_with_tool(question: str) -> str:
    tools = [{
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Evaluate an arithmetic expression and return the result.",
            "parameters": {
                "type": "object",
                "properties": {"expression": {"type": "string", "description": "A math expression, e.g. '2*(3+4)'"}},
                "required": ["expression"],
            },
        },
    }]

    messages = [{"role": "user", "content": question}]
    first = client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=tools, tool_choice="auto")
    msg = first.choices[0].message

    if not msg.tool_calls:
        return msg.content or "No tool call requested."

    messages.append(msg)
    for call in msg.tool_calls:
        args = json.loads(call.function.arguments)
        result = calculate(args["expression"])
        messages.append({"role": "tool", "tool_call_id": call.id, "content": result})

    second = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return second.choices[0].message.content
