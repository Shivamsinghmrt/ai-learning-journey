# Hands-On 8B · Stretch — A Reusable Semantic Search Engine 

# Problem Statement:  You want one small, reusable component that indexes a set of banking documents and, given any natural-language question, returns the most relevant passages with scores — the retrieval core of a RAG system. 

# Goal of the Problem:  Build a SemanticSearch class that chunks and embeds documents, then ranks passages against a query using cosine similarity. This is your Module 1.4 deliverable. 

# Where to run: VS Code (recommended)   ·   Est. time: 35 min   ·   Concepts: chunking, embeddings, cosine ranking, retrieval 

# Step 1 — Build the engine class 

# Normalising vectors once lets us rank with a single fast matrix multiply instead of a loop. 

import numpy as np 
import pandas as pd

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()                     # reads .env into environment variables

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

  

class SemanticSearch: 

    def __init__(self, model="text-embedding-3-small"): 

        self.model = model 

        self.chunks = [] 

        self.vecs = None 

  

    def _embed(self, texts): 

        r = client.embeddings.create(model=self.model, input=texts) 

        return np.array([d.embedding for d in r.data]) 

  

    def index(self, docs, size=40, overlap=8): 

        for d in docs: 

            words = d.split() 

            i = 0 

            while i < len(words): 

                self.chunks.append(" ".join(words[i:i + size])) 

                i += size - overlap 

        v = self._embed(self.chunks) 

        self.vecs = v / np.linalg.norm(v, axis=1, keepdims=True)   # normalise rows 

  

    def search(self, query, k=3): 

        q = self._embed([query])[0] 

        q = q / np.linalg.norm(q) 

        scores = self.vecs @ q                      # cosine sim for every chunk 

        top = np.argsort(scores)[::-1][:k] 

        return [(round(float(scores[i]), 3), self.chunks[i]) for i in top] 

# Expected output 

# # defines the SemanticSearch class; no output 

# Step 2 — Index a small banking document set 

docs = [ 

    ("ABC Bank savings accounts require a minimum monthly balance of 5000 rupees " 

     "in metro branches. Interest is credited quarterly and you receive a free debit card."), 

    ("If your debit card is lost or stolen, block it immediately by calling the 24x7 " 

     "helpline or by freezing the card in the ABC Bank mobile app, then request a replacement."), 

    ("Home loan foreclosure carries no prepayment penalty for floating-rate loans. " 

     "Fixed-rate loans may attract a charge; check your sanction letter for details."), 

    ("To update your registered mobile number, visit any branch with a valid ID, " 

     "or use the profile section of net banking if your email is verified."), 

] 

  

engine = SemanticSearch() 

engine.index(docs) 

print("Indexed chunks:", len(engine.chunks)) 

# Expected output 

# Indexed chunks: 6 

# (exact count depends on chunk size/overlap) 

# Step 3 — Ask natural-language questions 

for q in ["how do I block my card if I lose it?", 

          "is there a penalty for repaying my home loan early?"]: 

    print("Q:", q) 

    for score, passage in engine.search(q, k=1): 

        print(f"   {score}  ->  {passage[:90]}...") 

    print() 

# Expected output 

# Q: how do I block my card if I lose it? 

#    0.63  ->  If your debit card is lost or stolen, block it immediately by calling the 24x7 helpline... 

  

# Q: is there a penalty for repaying my home loan early? 

#    0.58  ->  Home loan foreclosure carries no prepayment penalty for floating-rate loans... 

# Note:  Neither question reuses the document's exact words ('block'/'lose' vs 'lost or stolen'; 'repaying early' vs 'foreclosure'), yet the right passage is retrieved. That is semantic retrieval doing its job. 

# Deliverable:  This SemanticSearch class is your mini semantic-search prototype. On Day 2 you will swap the in-memory NumPy store for a real vector database — the interface (index / search) stays the same. 