# Day 06 - Chunking and Retrieval Preparation

## Overview

This day explains a very practical problem in RAG systems: how do you split a long document into useful pieces? A document that is too large cannot be used as one giant block, so it must be broken into smaller chunks.

## What you will learn

- Why chunking is necessary
- How fixed chunking differs from recursive chunking
- Why chunk overlap is helpful
- How poor chunking hurts retrieval quality
- How vector databases store and retrieve these chunks

## Why this matters

If a chunk is too big, it may contain too much unrelated information. If it is too small, you may lose important context. The right chunk size helps the system retrieve the most useful passage.

## Main ideas

### 1. Fixed chunking
Fixed chunking cuts text into pieces of a set size. It is simple but may split ideas awkwardly.

### 2. Recursive chunking
Recursive chunking is smarter because it tries to split at natural boundaries such as paragraphs, sentences, or words.

### 3. Semantic chunking
Semantic chunking goes one step further by splitting where the meaning changes. This is often better for retrieval because it keeps related ideas together.

### 4. ChromaDB
ChromaDB is a vector database that can store documents and query them by meaning. This turns the chunking work into a usable retrieval pipeline.

## Files in this folder

- 2-A-FixedvsRecursivechunking.py - compares simple and recursive splitting
- 2-B-SemanticChunkingVsFixedChunkingOnRetrievalQuality.py - shows how chunking quality affects retrieval
- 3-A-StoreAndQueryWithChromaDB.py - introduces a real vector database workflow
- notes.md - detailed explanation

## Takeaway

Chunking is not just a technical detail. It directly affects whether the retrieval system finds the right context and whether the model provides a good answer.
