# Day 04 - Prompt Design and Guardrails

## Overview

This day moves from “making the model answer” to “making the model answer well.” The main idea is that prompts are not just text. They are instructions, rules, boundaries, and sometimes even contracts for how the model should behave.

## What you will learn

- How to write prompts that guide the model clearly
- How to limit the model’s scope so it stays on topic
- How to make the model refuse unsafe or out-of-scope requests
- How to force the output into a structured format
- How to test a prompt system so changes can be evaluated safely

## Why this matters

A model can be very helpful and still be wrong in ways that are dangerous for a product. For example, a customer support bot should not answer investment questions or give legal advice. That is why prompt design is a major part of building trustworthy AI assistants.

## Main ideas

### 1. Prompt structure
A strong prompt gives the model a role, a task, a scope, and rules. That is much better than writing a vague question.

### 2. Guardrails
Guardrails are limits you place around the model. They tell it what it can answer, what it should refuse, and how to respond when a request is outside scope.

### 3. Structured output
Sometimes you want more than free-form text. You want the model to return JSON or a fixed schema so another system can use it.

### 4. Prompt evaluation
When you change a prompt, the output may change too. Evaluation harnesses let you test many example questions and make sure the change improves or preserves behavior.

## Files in this folder

- 5B-Chain-of-Thought.py - shows how reasoning can be guided while keeping output structured
- 6A-Guardrailed-Responder.py - demonstrates scope-limiting and refusal behavior
- 6B-Versioned-FAQ-Responder-EvaluationHarness.py - shows how to version prompts and test them systematically
- 7A-QuickWin-MeaningAsGeometry.py - connects prompt concepts to semantic meaning
- 7B-Semantic-vs-KeywordSearch.py - contrasts meaning-based and keyword-based retrieval
- 8A-QuickWin-Chunk&Embed-a-Doc.py - links chunking to retrieval context
- 8B-ReusableSemanticSearchEngine.py - shows a reusable semantic search flow

## Takeaway

Prompt engineering is not just about getting a clever answer. It is about building dependable behavior in real systems.
