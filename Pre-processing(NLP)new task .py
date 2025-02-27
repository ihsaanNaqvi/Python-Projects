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
sentences = sent_tokenize(text)
sentence_count = 0
for sentence in sentences:
    words = word_tokenize(sentence)
    print(f"Tokenized words in sentence: {words}")
    if "is" in words:  # Check for "is" in the list of words
        sentence_count += 1
        print(f"Found 'is' in sentence: {sentence}") 
print(f"\nTotal sentences containing 'is': {sentence_count}")
 