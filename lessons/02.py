
import gensim.downloader as api

#model = api.load("glove-twitter-200")
model = api.load("word2vec-google-news-300")
#model = api.load("fasttext-wiki-news-subwords-300")

#sims = model.most_similar(positive=["king", "woman"], negative=["man"])
#sims = model.most_similar(positive=["student"], negative=["university"])
sims = model.most_similar(positive=["winter"], negative=["snow"])

for i in range(10):
    print(sims[i][0])

