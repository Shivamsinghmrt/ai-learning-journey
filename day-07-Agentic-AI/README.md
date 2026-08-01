# Day 07 - Agentic AI Basics

## Overview

This day introduces the shift from a simple chatbot to an agent. An agent is not just a model that answers questions. It is a system that can plan, reason, and act toward a goal.

## What you will learn

- How a planning agent breaks a goal into smaller steps
- How reflection improves a draft plan
- How a tool-using agent can perform calculations reliably
- Why agentic behavior often involves several steps instead of one response

## Why this matters

An ordinary LLM response is often one shot. An agent can take an idea, break it into tasks, use tools, and adjust its approach. That makes it much more useful for real workflows.

## Main ideas

### 1. Planning agents
A planning agent turns a big goal into a short action list. This is useful for project planning, research, and task execution.

### 2. Self-critique
The self-critiquing planner drafts a plan and then reviews it for weaknesses. This improves the quality of the final result.

### 3. Tool use
The calculator example shows that an agent can request a tool call when the task requires exact computation.

## Files in this folder

- 1A-Task-PlannerAgent.py - simple planning agent
- 1B-Self-CritiquingSprintPlanner.py - reflection-based planning loop
- 2A-GiveAgentCalculator.py - tool-calling calculator agent
- notes.md - detailed explanation

## Takeaway

Agentic AI is about giving the model a goal and letting it decide how to proceed step by step.
