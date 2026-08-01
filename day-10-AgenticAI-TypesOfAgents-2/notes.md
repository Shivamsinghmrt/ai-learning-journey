# Day 10 - Advanced Agentic AI Patterns

## Goal

This day brings together many of the topics from earlier lessons and shows how they work together in a real agent system.

## 1. Planning pipelines

A complex task is often broken into stages such as planning, execution, and synthesis. This makes the workflow more manageable and easier to debug.

## 2. Replanning

Sometimes the goal changes while the agent is working. In that case, the agent should not keep following the old plan. It should re-evaluate and update its next steps.

## 3. Memory and retrieval

The RAG memory example shows a powerful pattern: the agent stores useful facts and later retrieves them when needed. This makes the system more grounded and less dependent on the model’s short-term memory.

## 4. Chroma vector store

Chroma is used as a vector database to store document embeddings and retrieve similar chunks for a query. This connects the earlier lessons on embeddings and retrieval with the agentic workflow.

## 5. Constraints and business rules

Many agent systems must obey rules. For example, a travel planner may need to stay within a budget or ensure a trip fits certain constraints. This is where structured generation and explicit rules become important.

## Learning takeaway

Advanced agents are not just about one smart prompt. They are systems built from planning, memory, retrieval, and control logic.
