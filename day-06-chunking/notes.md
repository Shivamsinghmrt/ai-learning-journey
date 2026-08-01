# Day 06 - Chunking and Retrieval Preparation

## Goal

This day teaches you how to break documents into smaller, meaningful pieces so that a retrieval system can find the right information efficiently.

## Why chunking matters

If you store an entire long document as one unit, retrieval becomes less precise. A query may match the document generally but not the specific part that matters. Chunking helps the system retrieve the right section of the document.

## 1. What is a chunk?

A chunk is a small piece of text taken from a larger document. It can be a paragraph, a sentence, or a fixed-size block of characters.

## 2. Fixed chunking

Fixed chunking splits text into pieces of a certain size. It is easy to implement, but it may cut through sentences or ideas in unnatural places.

## 3. Recursive chunking

Recursive chunking tries to respect natural boundaries such as paragraph breaks, sentence endings, and words. This usually produces more meaningful chunks.

## 4. Overlap

A small overlap between chunks means that one chunk can carry some context from the previous one. This helps when a sentence is split across boundaries.

## 5. Semantic chunking

Semantic chunking is more advanced. It identifies where the meaning changes and splits at those points. This often leads to better retrieval because related ideas stay together.

## 6. Vector stores

Once chunks are created, they can be embedded and stored in a vector store such as ChromaDB. Later, user questions are embedded and matched against the stored chunk embeddings.

## Learning takeaway

Chunking is one of the hidden reasons why retrieval systems succeed or fail. Good chunking makes the answers more relevant.
