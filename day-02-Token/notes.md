# Notes  
  
# Day 2 – Tokenization  
  
---  
  
# Objective  
  
Understand how Large Language Models convert human-readable text into machine-understandable tokens.  
  
---  
  
# What is Tokenization?  
  
Tokenization is the process of breaking text into smaller units called Tokens.  
  
Example  
  
Input  
  
Generative AI is transforming banking operations.  
  
↓  
  
Tokens  
  
Gener  
ative  
AI  
is  
transforming  
banking  
operations  
.  
  
Notice that  
  
Generative  
  
became  
  
Gener  
ative  
  
A token is NOT necessarily a word.  
  
---  
  
# Why Tokenization?  
  
Computers cannot understand English.  
  
LLMs also cannot understand English.  
  
They understand only numbers.  
  
Therefore,  
  
Text  
  
↓  
  
Tokens  
  
↓  
  
Token IDs  
  
↓  
  
Embeddings  
  
↓  
  
Neural Network  
  
---  
  
# Token IDs  
  
Every token has a unique integer.  
  
Example  
  
Token  
  
AI  
  
↓  
  
ID  
  
20837  
  
The actual number has no meaning.  
  
It simply acts as an identifier.  
  
Similar to  
  
Employee ID  
  
Customer ID  
  
Product ID  
  
---  
  
# Why not Character by Character?  
  
Imagine this word  
  
Internationalization  
  
If every character becomes a token  
  
I  
n  
t  
e  
r  
...  
  
The sentence becomes very long.  
  
Instead,  
  
Tokenizer finds common pieces  
  
Inter  
national  
ization  
  
This reduces token count.  
  
---  
  
# Vocabulary  
  
Tokenizer contains a predefined vocabulary.  
  
Example  
  
bank  
  
banking  
  
AI  
  
Java  
  
Spring  
  
Boot  
  
?  
  
Whenever possible,  
  
Tokenizer selects the longest matching token.  
  
---  
  
# Why does Generative become  
  
Gener  
  
ative  
  
Because  
  
Generative  
  
was not present as one token.  
  
But  
  
Gener  
  
and  
  
ative  
  
were available.  
  
---  
  
# Word Count vs Token Count  
  
Words  
  
I love AI  
  
Words = 3  
  
Tokens  
  
I  
love  
AI  
  
Tokens = 3  
  
But  
  
Internationalization  
  
Words = 1  
  
Tokens may become  
  
Inter  
national  
ization  
  
Tokens = 3  
  
Therefore  
  
Words != Tokens  
  
---  
  
# Why Token Count Matters  
  
OpenAI charges by tokens.  
  
Context Window is measured in tokens.  
  
Speed depends on tokens.  
  
Memory depends on tokens.  
  
Cost depends on tokens.  
  
---  
  
# Java Analogy  
  
Java Source Code  
  
↓  
  
Lexical Analysis  
  
↓  
  
Tokens  
  
↓  
  
Parser  
  
↓  
  
Compiler  
  
LLM  
  
Text  
  
↓  
  
Tokenizer  
  
↓  
  
Token IDs  
  
↓  
  
Embeddings  
  
↓  
  
Transformer  
  
---  
  
# Today's Python APIs  
  
encode()  
  
Converts text into token IDs.  
  
Example  
  
encoder.encode(text)  
  
decode()  
  
Converts token ID back to text.  
  
Example  
  
encoder.decode([token])  
  
---  
  
# Key Learnings  
  
✓ LLMs never understand English directly.  
  
✓ LLMs process Token IDs.  
  
✓ One word can become many tokens.  
  
✓ One token can represent multiple characters.  
  
✓ Token count is different from word count.  
  
✓ Billing is based on tokens.  
  
✓ Context Window is measured in tokens.  
  
---  
  
# Interview Questions  
  
Q. What is Tokenization?  
  
Breaking text into smaller machine-processable units called tokens.  
  
---  
  
Q. Are Tokens equal to Words?  
  
No.  
  
One word may become multiple tokens.  
  
---  
  
Q. Why do LLMs use Tokens?  
  
Because neural networks work with numbers.  
  
---  
  
Q. Why not Characters?  
  
Character-level processing is inefficient and increases sequence length.  
  
---  
  
Q. What library did we use?  
  
tiktoken  
  
---  
  
# Summary  
  
Text  
  
↓  
  
Tokenizer  
  
↓  
  
Token IDs  
  
↓  
  
Embeddings  
  
↓  
  
Transformer  
  
↓  
  
Predicted Token  
  
↓  
  
Tokenizer  
  
↓  
  
English Output  
  
This is the first step in every LLM.  
