
# Natural Language Processing (NLP) Preprocessing Steps
# 1. Setup and Configuration
# - Import required library
# - Configure NLTK data path
# - Download necessary NLTK resources (punkt for tokenization, wordnet for lemmatization)
import os
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Set NLTK data path to a writable directory
nltk.data.path.append(os.getcwd())

# Download required NLTK data
nltk.download('punkt', download_dir=os.getcwd())
nltk.download('wordnet', download_dir=os.getcwd())
nltk.download('omw-1.4', download_dir=os.getcwd())  # Open Multilingual WordNet

# Example text
#text = """Natural Language Processing is fascinating! It helps computers understand human language. 
#Is  that not amazing? We can analyze text, sentiment, and much more."""
#read the file 
text = open("textforpreprocessing.txt", "rt").read()
# Count occurrences of "is"
count = 0
for i in word_tokenize(text):
    if i == "is":  # Note: using == for comparison, not =
        count = count + 1
        print("Found 'is', count:", count)

                       
# 2. Word Tokenization
# - Splits text into individual words/tokens
# - Handles punctuation and special characters
# - Preserves important tokens like numbers and symbols
words = word_tokenize(text)
print("Word tokens:", words[:10])  # First 10 tokens

# Sentence tokenization
sentences = sent_tokenize(text)
print("\nSentence tokens:")
for sentence in sentences:
    print(f"- {sentence}")

# segmentation 
from nltk.tokenize import sent_tokenize, word_tokenize
for i in sent_tokenize(text):
  print("new segment")
  for j in word_tokenize(i):
    print(j)

# 3. Stemming
# - Reduces words to their root/base form
# - Faster but less accurate than lemmatization
# - Uses Porter Stemming algorithm for English
from nltk.stem import PorterStemmer
p= PorterStemmer()
print(p.stem("running"))
print(p.stem("walking"))
print(p.stem("walked"))
print(p.stem("Apple"))

# 4. Lemmatization
# - Reduces words to their dictionary base form
# - More accurate than stemming as it considers word context
# - Uses WordNet lexical database for accurate word forms
from nltk.stem import WordNetLemmatizer
i= WordNetLemmatizer()
print(i.lemmatize("indices"))
print(i.lemmatize("walking"))
p= PorterStemmer()
print(p.stem("indices"))
  