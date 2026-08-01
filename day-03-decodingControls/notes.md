# Day 03 - Decoding Controls

## Goal

This lesson helps you understand how an LLM produces text and how you can guide that generation process. In other words, you are learning the knobs that control the model’s behavior.

## Why this lesson is important

A language model does not think like a human. It predicts the next token based on patterns it has learned. Because of that, the same prompt can produce slightly different output every time unless you control the generation settings.

## The core idea

Imagine you ask a model to write a slogan. If you want a safe and repetitive result, you use a low temperature. If you want a more imaginative response, you raise the temperature. The model is still generating text, but you are deciding how much freedom it should have.

## 1. Temperature

Temperature is the main dial for creativity.

- Low temperature means the model is more confident and chooses the most likely next word.
- High temperature means the model explores more alternatives and becomes more varied.

A simple example is writing a tagline for a bank account. With temperature 0, the model tends to produce the same wording each time. With higher temperature, it may sound more creative but also less predictable.

## 2. Top-p

Top-p is another sampling control. Instead of letting the model choose from all possible tokens, it only considers the most likely options until a probability threshold is reached.

This is useful when you want some flexibility without letting the model go completely off-track.

## 3. Max tokens

Max tokens controls response length. If you ask for 20 tokens and the model would normally produce 80, it will stop early. If you set it too low, the output may be incomplete. If you set it too high, the response may become unnecessarily long.

## 4. Reproducibility

At temperature 0, the model becomes much more repeatable. That makes it excellent for testing, product features, or workflows that need stable behavior. In this lesson, you compare repeated runs and see that the output becomes almost the same.

## 5. Cost estimation

This lesson also introduces the idea that model usage has cost. The longer the prompt and the longer the answer, the more tokens are used. The cost grows with token count.

A simple mental model is:

- shorter prompt = less cost
- shorter completion = less cost
- stronger model = more cost

## 6. Why this matters in real applications

Companies care about three things at the same time:

- quality of response
- consistency of output
- cost of each request

That is why decoding controls are not just academic. They are part of real-world AI product design.

## Learning takeaway

When you use an LLM in production, you are not only choosing the prompt. You are also choosing the behavior of the generation process itself.
