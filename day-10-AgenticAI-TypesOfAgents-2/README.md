# Day 10 - Advanced Agentic AI Patterns

## Overview

This day brings together many of the concepts learned earlier: planning, memory, retrieval, and structured execution. The goal is to show how agents become more capable when they combine several mechanisms at once.

## What you will learn

- How planning pipelines work
- How agents can re-plan when priorities change
- How memory can be stored and retrieved
- How vector databases support knowledge-based agents
- How constraints help keep outputs aligned with a goal

## Why this matters

Real-world agents are rarely single-purpose. They may plan a task, check memory, retrieve facts, and adjust if the goal changes. This day shows how those pieces fit together.

## Main ideas

### 1. Planning and execution
A workflow can be split into planning, executing, and synthesizing result steps.

### 2. Replanning
When the goal shifts, the agent should update its plan instead of blindly following the old one.

### 3. Memory and retrieval
The RAG memory example stores knowledge in Chroma and retrieves relevant facts when answering a question.

### 4. Constraints
The itinerary and budgeting examples show that agents can be guided by business rules and limits.

## Files in this folder

- 7B-RAG-Memory-Agent-with-a-Chroma-Vector-Store.py - memory-based retrieval agent
- notes.md - detailed explanation

## Takeaway

Advanced agents are not just “smart chatbots.” They are systems that plan, retrieve context, and follow constraints.
