import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data 
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")

#Initialize lemmatizer
lemmatizer= WordNetLemmatizer()

def process_text_file(file_path):
    """ processes a text file and finds 'is' and lemmatize surrounding """
    try:
        with open(file_path, "r", encoding ="utf-8") as file:
            text = file.read()
            sentences = sent_tokenize(text)
            sentence_count =0

            for sentence in sentences:
                words = word_tokenize(sentence)
                print(f"\nTokenized words: {words}")

                indices = [i for i, word in enumerate(words) if word.lower()=="is"]

                if indices:
                    sentence_count +=1
                    print(f"Found 'is' in sentence :{sentence}") 

                for i in indices:
                    before_is= lemmatizer.lemmatize(words[i-1]) if i>0 else None
                    after_is = lemmatizer.lemmatize(words[i+1]) if i < len(words) -1 else None

                    print(f"Lemmatizer words before 'is': {before_is}") if before_is else "No word before is"
                    print(f"Lemmatizer words after 'is': {after_is}") if after_is else "No word after"

                print(f"\nTotal sentences containing 'is' : {sentence_count}")
    except FileNotFoundError:
            print("Error: File not found.")
    except Exception as e:
         print(f"An error occured: {e}")

file_path= "textforpreprocessing2updated.txt"
process_text_file(file_path)
