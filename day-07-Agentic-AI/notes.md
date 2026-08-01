# Day 07 - Agentic AI Basics

## Goal

This day introduces the core idea behind agentic AI: using a model not just to answer a question but to carry out a task.

## 1. What is an agent?

An agent is a system that can take a goal, reason through it, and choose actions. It is more than a chatbot because it can plan and use tools.

## 2. Planning a task

The task-planner example shows how a high-level goal becomes a list of concrete steps. For example, “organize a team session” becomes a practical plan with agenda, audience, demo, and follow-up tasks.

## 3. Reflection and revision

The self-critiquing planner takes the idea one step further. It writes a plan, reviews it, and improves it. This is a fundamental agent pattern: draft, critique, revise.

## 4. Tool calling

The calculator example shows another important pattern. Instead of asking the model to do arithmetic directly, the system gives it a real tool. The model requests the tool when needed, and the tool returns the result. This is much more reliable.

## 5. Why this matters

Real-world tasks often require more than one step. You might need to search, calculate, classify, or retrieve information before you can respond. Agents are built for exactly that kind of work.

## Learning takeaway

The agent pattern is a shift from single-turn response generation to multi-step execution.
