# Day 09 - Types of Agents

## Overview

This day compares different styles of agents. The main point is that not all agents are the same. Some respond immediately, while others reason, use tools, and adjust their actions over time.

## What you will learn

- What a reactive agent is
- What a deliberative agent is
- How a ReAct loop works
- Why some tasks need deeper reasoning than others

## Why this matters

Some problems are simple and can be solved with rules. Others need context, planning, or tool use. The right agent type depends on the problem.

## Main ideas

### 1. Reactive agents
These agents make an immediate decision based on the current input. They are fast and simple but limited.

### 2. Deliberative agents
These agents think through a problem before acting. They may use tools and follow a reasoning loop.

### 3. ReAct pattern
The ReAct pattern alternates between reasoning and action. The agent decides what to do next, acts, observes the result, and then continues.

## Files in this folder

- 1A-ReactiveSupport-TriageAgent.py - simple rules-based triage agent
- 1B-DeliberativeReActAgentWithTools.py - tool-using deliberative agent
- 2A-Writer-Editr-MultAgenf.py - multi-agent collaboration example
- notes.md - detailed explanation

## Takeaway

The architecture of an agent should match the complexity of the task.
