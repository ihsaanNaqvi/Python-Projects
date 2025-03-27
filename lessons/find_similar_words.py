
# Choose words related to "sun" indirectly.
# Use semantic relationships (e.g., "day" and "light" for "sun", "vehicle" and "road" for "car").
# Balance positive and negative words to guide the similarity search.
# import gensim.downloader as api
#load the data word2vec 
# model = api.load("word2vec-google-news-300")
# model = api.load("word2vec-google-news-300")


import gensim.downloader as api


model = api.load("glove-twitter-200")

positive = [
    "bright", "road", "drive", "summer", "sunshine", "sunny", "beach", "roadtrip",
    "driving", "highway", "convertible", "vehicle", "speed", "warm", "heat", "daylight",
    "sky", "transport", "travel", "automobile", "energy", "wheels"
]   

negative = [
    "night", "walk", "rain", "cloud", "cold", "dark", "slow", "storm", "shadow"
]   

 
sims = model.most_similar(positive=positive, negative=negative, topn=10)

 
print("Top similar words:")
for word, similarity in sims:
    print(word, similarity)

 
found_words = [word for word, _ in sims if word in ["sun", "car"]]

if found_words:
    print("\nSuccessfully found:", ", ".join(found_words))
else:
    print("\nDidn't get 'sun' or 'car'. Try adjusting the word lists!")


