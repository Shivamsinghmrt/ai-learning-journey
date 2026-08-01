# Day 05 - Retrieval-Augmented Generation (RAG)

## Goal

This day teaches you how to make an LLM answer questions using relevant external information instead of relying only on memory.

## Why this is useful

A language model can sound confident even when it is guessing. RAG fixes that by letting the model first look up facts from a knowledge base and then answer using those facts.

## 1. The basic idea

You start with a question. Then you search a set of documents to find the most relevant text. That text is inserted into the prompt, and the model answers using the retrieved context.

## 2. Semantic meaning instead of exact words

In earlier exercises, you saw that two sentences can be very similar in meaning even if they use different words. Semantic search captures this by embedding text into vectors.

## 3. Similarity scoring

A score is computed between the question embedding and the document embeddings. The most similar documents are selected and ranked.

## 4. Why this reduces hallucinations

If the model is only given the relevant retrieved passages, it is less likely to invent facts. This makes it much better for support bots, Q&A systems, and domain-specific knowledge assistants.

## 5. The practical workflow

A common RAG workflow is:

1. Receive a question
2. Convert the question into an embedding
3. Search the available documents
4. Retrieve the most relevant passages
5. Add them to the prompt
6. Ask the model to answer using only that context

## Learning takeaway

RAG is one of the clearest ways to make AI systems more trustworthy because they can answer from evidence rather than guesswork.
