from gensim.models import Word2Vec
from nltk import word_tokenize, sent_tokenize
import numpy as np

with open("Moscow.txt") as f:
    text = f.read()
text = [ word_tokenize(i) for i in sent_tokenize(text) ]

for i in range(len(text)):
    a = [j.lower() for j in text[i] if len(j) > 3]
    text[i] = a

model = Word2Vec(sentences=text, vector_size=100, window=30, min_count=1)
sims = model.wv.most_similar('city', topn=10)
for i in range(10):
    print(sims[i][0])
