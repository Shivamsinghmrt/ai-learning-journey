# Day 03 - Decoding Controls

## Overview

This day teaches one of the most practical parts of working with LLMs: how to control the way the model generates text. In simple terms, even when the same prompt is given, the model can answer very differently depending on settings such as temperature, top-p, and max tokens.

## What you will learn

- Why the same prompt can produce different answers
- How temperature changes creativity and consistency
- How top-p influences the range of possible next words
- Why max tokens matters for length and cost
- How to estimate prompt cost before deploying a feature

## Why this matters

A model without controls is like a person who speaks freely without limits. Sometimes that is useful, but in real products you usually want predictable output. For example:

- A support bot should be consistent and safe.
- A creative writing tool should be more expressive.
- A customer-facing assistant should not ramble too long.

## Main ideas

### 1. Temperature
Temperature controls how random the response feels. A lower value makes the model choose more predictable words. A higher value makes it explore more possibilities and sound more varied.

### 2. Top-p
Top-p is another sampling control. It limits the pool of likely next tokens so the model does not drift into very unlikely choices.

### 3. Max tokens
Max tokens limits how long the reply can be. If it is too small, the response may be cut off. If it is too large, you may pay more and wait longer.

### 4. Cost and budget awareness
Every prompt and every output token costs money. This lesson shows how to estimate the cost of a request before using it in a real product.

## Files in this folder

- main.py - cost estimation exercise
- 2A-The-Temperature-Dial.py - temperature comparison
- 2B-Parameter-Comparison.py - parameter comparison harness
- examples.py - practice file
- notes.md - detailed explanation

## Takeaway

The model is not just “thinking” in a human way. It is generating one token at a time. Decoding controls let you steer that generation process so the output fits your goal.
