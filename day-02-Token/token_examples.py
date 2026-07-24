# Token example   
  
"""  
===========================================================  
Day 2 - Tokenization Examples  
Author : Shivam Singh  
Topic  : Understanding Tokenization using tiktoken  
===========================================================  
  
Objective:  
----------  
Understand how Large Language Models (LLMs) convert human  
language into Tokens before processing.  
  
LLMs DO NOT understand:  
    - Words  
    - Characters  
    - Sentences  
  
LLMs ONLY understand:  
    - Token IDs  
  
Pipeline:  
  
Text  
 ↓  
Tokenizer  
 ↓  
Tokens  
 ↓  
Token IDs  
 ↓  
Embeddings  
 ↓  
LLM  
  
"""  
  
import tiktoken  
  
# Load OpenAI tokenizer  
encoder = tiktoken.get_encoding("o200k_base")  
  
  
def analyze(text):  
    """  
    Prints detailed token information.  
    """  
  
    print("=" * 80)  
    print("Input Text")  
    print("-" * 80)  
    print(text)  
  
    token_ids = encoder.encode(text)  
  
    token_pieces = [encoder.decode([token]) for token in token_ids]  
  
    print("\nWord Count :", len(text.split()))  
    print("Token Count:", len(token_ids))  
  
    print("\nToken IDs")  
    print(token_ids)  
  
    print("\nToken Pieces")  
  
    for index, piece in enumerate(token_pieces, start=1):  
        print(f"{index:02d}. {repr(piece)}")  
  
    print()  
  
  
###########################################################################  
# Example 1  
###########################################################################  
  
analyze("Generative AI is transforming banking operations.")  
  
###########################################################################  
# Example 2  
###########################################################################  
  
analyze("Balance?")  
  
###########################################################################  
# Example 3  
###########################################################################  
  
analyze("Java Spring Boot")  
  
###########################################################################  
# Example 4  
###########################################################################  
  
analyze("I love Artificial Intelligence.")  
  
###########################################################################  
# Example 5  
###########################################################################  
  
analyze("₹100000")  
  
###########################################################################  
# Example 6  
###########################################################################  
  
analyze("987654321")  
  
###########################################################################  
# Example 7  
###########################################################################  
  
analyze("Hello 😊")  
  
###########################################################################  
# Example 8  
###########################################################################  
  
analyze("SELECT * FROM Employee WHERE salary > 100000")  
  
###########################################################################  
# Example 9  
###########################################################################  
  
analyze("""  
{  
    "name":"Shivam",  
    "technology":"Spring Boot"  
}  
""")  
  
###########################################################################  
# Example 10  
###########################################################################  
  
analyze("Internationalization")  
  
###########################################################################  
# Example 11  
###########################################################################  
  
analyze("OpenAI GPT models predict one token at a time.")  
  
###########################################################################  
# Example 12  
###########################################################################  
  
analyze("The quick brown fox jumps over the lazy dog.")  
  
###########################################################################  
# Example 13  
###########################################################################  
  
analyze("आज मौसम बहुत अच्छा है।")  
  
###########################################################################  
# Example 14  
###########################################################################  
  
analyze("AI + Java + Python + LangChain + RAG")  
  
###########################################################################  
# Example 15  
###########################################################################  
  
analyze("""  
public class Employee{  
  
    public static void main(String args[]){  
  
        System.out.println("Hello");  
  
    }  
  
}  
""")  
  
print("=" * 80)  
print("End of Tokenization Experiments")  
print("=" * 80)  
