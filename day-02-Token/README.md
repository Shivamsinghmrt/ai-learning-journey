# Readme  
  
# Day 02 – Tokenization using tiktoken  
  
---  
  
## Overview  
  
This project demonstrates how Large Language Models (LLMs) convert human-readable text into Tokens before processing.  
  
The examples use OpenAI's `tiktoken` library to explore tokenization across different kinds of input such as English sentences, programming code, SQL queries, JSON, emojis, numbers, and multilingual text.  
  
---  
  
## Learning Objectives  
  
After completing this module, you should understand:  
  
- What a Token is  
- Difference between Words and Tokens  
- Token IDs  
- Encoding  
- Decoding  
- Token Count  
- Why tokenization is necessary  
- Why OpenAI pricing is based on Tokens  
- How tokenization fits into the LLM pipeline  
  
---  
  
## Project Structure  
  
```  
day-02-tokenization/  
  
│── main.py  
│── token_examples.py  
│── notes.md  
└── README.md  
```  
  
---  
  
## Installation  
  
Create Virtual Environment  
  
```bash  
python -m venv .venv  
```  
  
Activate Environment  
  
Windows  
  
```bash  
.venv\Scripts\activate  
```  
  
Install Dependency  
  
```bash  
pip install tiktoken  
```  
  
---  
  
## Run  
  
```bash  
python token_examples.py  
```  
  
---  
  
## Sample Output  
  
```  
Input  
  
Generative AI is transforming banking operations.  
  
Word Count : 6  
  
Token Count : 8  
  
Token IDs  
  
[...]  
  
Token Pieces  
  
Gener  
ative  
AI  
is  
transforming  
banking  
operations  
.  
```  
  
---  
  
## Key Concepts Covered  
  
- Tokenization  
- Vocabulary  
- Token IDs  
- Encoding  
- Decoding  
- Word Count  
- Token Count  
- Byte Pair Encoding (BPE) – High-level overview  
- LLM Input Pipeline  
  
---  
  
## LLM Pipeline  
  
```  
User Input  
  
↓  
  
Tokenizer  
  
↓  
  
Token IDs  
  
↓  
  
Embeddings  
  
↓  
  
Transformer  
  
↓  
  
Next Token Prediction  
  
↓  
  
Decoded Text  
  
↓  
  
Response  
```  
  
---  
  
## Real-world Importance  
  
Understanding tokenization helps with:  
  
- Prompt Engineering  
- RAG  
- Embeddings  
- Vector Databases  
- Context Window Management  
- API Cost Optimization  
- AI Agent Development  
  
---  
  
## Technologies Used  
  
- Python  
- tiktoken  
- VS Code  
  
---  
  
## References  
  
- OpenAI Tokenizer  
- tiktoken Library  
  
---  
  
## Author  
  
Shivam Singh  
  
Learning Journey: AI Engineering from Java Full Stack Developer  
