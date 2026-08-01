# Day 05 - Retrieval-Augmented Generation (RAG)

## Overview

Day 05 introduces one of the most important AI application patterns: Retrieval-Augmented Generation. Instead of relying only on what the model already “knows,” you give it relevant information from a knowledge base before it answers.

## What you will learn

- How embeddings represent meaning
- How semantic search finds related content even when words are different
- How cosine similarity is used to rank results
- How a small retrieval system can power a question-answering experience
- Why RAG helps reduce hallucinations

## Why this matters

An LLM is powerful, but it does not know everything and it can make things up. RAG solves this by letting the model answer using retrieved facts from a trusted source.

## Main ideas

### 1. Meaning over keywords
Traditional search finds words. Semantic search finds meaning. That is why a question like “I forgot my password” can retrieve a document about “reset your login credentials.”

### 2. Embeddings
Embeddings are numeric vectors that represent meaning. Similar meanings end up close to each other in vector space.

### 3. Retrieval
The system searches through a set of documents and finds the most relevant ones for the question.

### 4. Grounded answers
The retrieved text is added to the prompt, and the model answers using that context. This makes the answer more grounded and less speculative.

## Files in this folder

- 1-A-FindTheClosestSentenceByMeaning.py - shows semantic similarity with embeddings
- 1-B-SemanticSearchEngine.py - turns the idea into a reusable retriever
- notes.md - detailed explanation

## Takeaway

RAG is one of the simplest and most effective ways to make AI systems more reliable and useful in real-world settings.
