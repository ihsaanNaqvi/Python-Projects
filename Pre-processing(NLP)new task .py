import os
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Set NLTK data path to a writable directory
nltk.data.path.append(os.getcwd())

# Download required NLTK data
nltk.download('punkt', download_dir=os.getcwd())
nltk.download('wordnet', download_dir=os.getcwd())
nltk.download('omw-1.4', download_dir=os.getcwd())  # Open Multilingual WordNet

 
text = open("textforpreprocessing2updated.txt", "rt").read()

sentence_count = 0
 
sentences = sent_tokenize(text)
print("\nSentence tokens:")
for sentence in sentences:
    print(f"- {sentence}")
    # Check if "is" is in the current sentence
    if " is " in sentence:  # Check for " is " to avoid partial matches
      sentence_count += 1
 
print(f"\nTotal sentences containing 'is': {sentence_count}")
 