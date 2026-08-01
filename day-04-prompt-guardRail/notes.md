# Day 04 - Prompt Design and Guardrails

## Goal

This day teaches you that prompts are a form of control. A prompt is not just a question. It is a way to define the role, boundaries, and expected behavior of the model.

## Why this is a big deal

If you ask an LLM a vague question, you may get a useful answer. But if you ask it to act as a customer support assistant, stay inside a limited domain, and refuse out-of-scope requests, you need more structure.

## 1. The model needs direction

A model does not automatically know your business rules. You must explain them clearly. For example, if you build a bank FAQ bot, the model needs to know:

- which topics are allowed
- which topics are forbidden
- what response style is preferred
- what to say when the question is outside scope

Without that, the model may answer too broadly or give risky advice.

## 2. Guardrails are boundaries

Guardrails are simple rules that keep the system safe and focused. They can include:

- “Answer only about banking products”
- “Never give investment advice”
- “If the question is outside scope, reply with this exact sentence”

The benefit is that the system becomes more predictable. You are not hoping the model behaves correctly; you are designing it to behave correctly.

## 3. Chain-of-thought and structured output

This day also shows that reasoning can be guided without exposing free-form reasoning to downstream systems. The model can think step by step internally, but you can ask it to return a controlled format such as JSON with fields like decision, reasoning, or in_scope.

That is very useful because your application often only needs a small set of values, not a long explanation.

## 4. Prompt injection and untrusted input

A very important concept appears in the evaluation harness. User messages are not always safe. A user can try to override the instructions by saying things like “ignore your rules” or “reveal your system prompt.”

The solution is to treat user input as data, not as instructions. The prompt should clearly tell the model to ignore conflicting instructions inside the user content.

## 5. Evaluation harnesses

A prompt is not “done” just because it looked good once. In real systems, you need a set of test cases. This day introduces the idea of:

- defining a test set
- checking expected behavior
- scoring the output
- catching regressions when prompts are changed

This is important because prompt edits can silently break behavior.

## Learning takeaway

Good prompts are not just strings. They are the product’s policy layer. They help the model stay safe, useful, and consistent.
