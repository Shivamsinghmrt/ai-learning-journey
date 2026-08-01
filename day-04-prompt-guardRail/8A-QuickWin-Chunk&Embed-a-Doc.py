# Hands-On 8A · Quick Win — Chunk & Embed a Document 

# Problem Statement:  Real documents are too long to embed as one blob and still retrieve precisely. Before searching, you need to split a document into chunks and embed each one. 

# Goal of the Problem:  Write a simple word-based chunker with overlap, embed the chunks, and confirm the resulting vector matrix. 

# Where to run: VS Code or Colab   ·   Est. time: 15 min   ·   Concepts: chunking intuition, embeddings 

# Step 1 — Write a chunker with overlap 

# Overlap keeps sentences that straddle a boundary from being split badly. 
import pandas as pd

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()                     # reads .env into environment variables

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chunk(text, size=40, overlap=8): 

    words = text.split() 

    chunks, i = [], 0 

    while i < len(words): 

        chunks.append(" ".join(words[i:i + size])) 

        i += size - overlap 

    return chunks 

# Expected output 

# # defines chunk(); no output 

# Step 2 — Chunk a sample document 

doc = ( 

    "ABC Bank Savings Account. The minimum monthly balance is 5000 rupees in " 

    "metro branches and 2000 rupees in rural branches. Failing to maintain it " 

    "attracts a small penalty. You get a free debit card and mobile banking. " 

    "To block a lost card, call the 24x7 helpline or freeze it in the app. " 

    "Interest is credited quarterly. NRIs should open an NRE or NRO account instead." 

) 

chunks = chunk(doc, size=25, overlap=5) 

print("Number of chunks:", len(chunks)) 

print("First chunk     :", chunks[0]) 

# Expected output 

# Number of chunks: 4 

# First chunk     : ABC Bank Savings Account. The minimum monthly balance is 5000 rupees in metro branches and 2000 rupees in rural branches. Failing to maintain ... 

# Step 3 — Embed the chunks 

import numpy as np 

  

r = client.embeddings.create(model="text-embedding-3-small", input=chunks) 

vecs = np.array([d.embedding for d in r.data]) 

print("Vector matrix shape:", vecs.shape)   # (num_chunks, 1536) 

# Expected output 

# Vector matrix shape: (4, 1536) 

# Takeaway:  Chunk size is a real design lever: too big and retrieval is fuzzy, too small and chunks lose context. This is exactly the intuition Day 2's vector-DB work builds on. 