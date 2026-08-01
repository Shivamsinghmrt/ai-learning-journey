# Day 08 - Agentic AI with Tools and Research Patterns

## Overview

This day builds on the agent idea by making the agent use tools and gather information from the outside world.

## What you will learn

- How a research agent gathers facts across multiple tool calls
- How a support agent can use domain tools to answer a ticket
- How agents can synthesize the information they gathered into a useful response

## Why this matters

A model by itself is limited to its training data and the current prompt. Tools expand its capabilities. With tools, an agent can look up facts, calculate values, or inspect structured data.

## Main ideas

### 1. Research scout
The research scout pattern runs several searches and then writes a concise brief from the results. It is useful for research assistants and executive summaries.

### 2. Customer support triage
A support agent can look up an order, check refund eligibility, and then write a response based on the retrieved facts.

### 3. Tool orchestration
The key idea is that the agent decides when to use a tool and what data to pass to it.

## Files in this folder

- B3-TheResearchScout.py - multi-step research agent pattern
- B4-ACustomerSupportTriageAgent.py - support agent with business tools
- notes.md - detailed explanation

## Takeaway

Tools make agents more useful because they can move from “talking” to “doing.”
