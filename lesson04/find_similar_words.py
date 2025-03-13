
# Choose words related to "sun" indirectly.
# Use semantic relationships (e.g., "day" and "light" for "sun", "vehicle" and "road" for "car").
# Balance positive and negative words to guide the similarity search.
# import gensim.downloader as api
#load the data word2vec 
# model = api.load("word2vec-google-news-300")
# model = api.load("word2vec-google-news-300")


# positive_words = ["Day","Light",["Drive"] ,["Road"] ]
# Negative_words = ["Night", "Walk"]
# #Get most similar words 
# sims = model.most_similar(positive=positive_words, negative= Negative_words, topn=10)

# for word, score in sims:
#     print(word)

import gensim.downloader as api
 
try:
    model = api.load("word2vec-google-news-300")
except Exception as e:
    print("Error loading model:", e)
    exit()
 
positive_words = ["Day", "Light", "Drive", "Road"]   
negative_words = ["Night", "Walk"]
 
for word in positive_words + negative_words:
    if word not in model.key_to_index:
        print(f"Warning: '{word}' not in vocabulary.")
 
try:
    sims = model.most_similar(positive=positive_words, negative=negative_words, topn=10)
    
    if not sims:
        print("No similar words found.")
    else:
        for word, score in sims:
            print(f"{word}: {score}")

except IndexError as e:
    print("An IndexError occurred:", e)
except Exception as e:
    print("An error occurred:", e)

