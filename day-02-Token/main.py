import tiktoken

#Step 1 — Encode text into tokens
#tiktoken is OpenAI's tokenizer. The GPT-4.1 / GPT-4o family uses the o200k_base encoding. Run:

enc = tiktoken.get_encoding("o200k_base")
text = "Generative AI is transforming banking operations."
tokens = enc.encode(text)
print("Text          :", text)
print("Token count   :", len(tokens))
print("Token IDs     :", tokens)

#Step 2 — See the actual sub-word pieces
#Decode each token individually to reveal how words are broken up:

pieces = [enc.decode([t]) for t in tokens]
print("Pieces        :", pieces)

#Expected output
#Pieces        : ['Gener', 'ative', ' AI', ' is', ' transforming', ' banking', ' operations', '.']
#Notice 'Generative' became two tokens (Gener + ative) while common words are a single token. This is why token count is not the same as word count.

#Step 3 — Compare short vs long text

short = "Balance?"

long  = "Please summarise the last twelve months of transactions for this account."

for label, s in [("short", short), ("long", long)]:

  print(f"{label:6s} words={len(s.split()):2d}  tokens={len(enc.encode(s)):2d}")

#Expected output
#short  words= 1 tokens= 3
#long   words=11 tokens=13

tokens = enc.encode(long)

for i, token in enumerate(tokens):
 print(f"Token {i+1}")
 print("ID :", token)
 print("Piece :", repr(enc.decode([token])))
 print("-" * 30)