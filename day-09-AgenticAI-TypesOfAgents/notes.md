# Day 09 - Types of Agents

## Goal

This day helps you see that “agent” is not one single pattern. Different tasks require different agent designs.

## 1. Reactive agents

A reactive agent follows simple rules such as “if the message mentions refund, route to billing.” It is fast and easy, but it cannot understand context deeply.

## 2. Deliberative agents

A deliberative agent is more thoughtful. It can reason over a problem, decide whether a tool is needed, and then act. That makes it more suitable for multi-step tasks.

## 3. ReAct loop

In the ReAct pattern, the agent alternates between internal reasoning and actions. It may think, call a tool, inspect the result, and then think again.

## 4. Why the reactive approach breaks down

The support example shows that a simple rule-based system can mis-handle ambiguous cases. A more deliberative agent is better when context matters.

## Learning takeaway

Complex problems often need agents that can think and act, not just respond with a simple rule.
