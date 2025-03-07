# TF -IDF algorithm 
# term frequency - inversed document frequency d1, d2,d3, so on 
# T is a set of all terms in  the document

# t1 can be included in d1 n1 times 
# t1 can be included in d2  n2 times

# len(d1) is how many words are present in d1
# term frequency for a t1 in d1 is n1/len(d1
# p1 is how many documents contain t at least once 
# p is a total number of documents
# idf (t1) log (p/p1)
# tfudf(t1) = tf(t1) * idf(t1)

#several documents with cosine product 


from math import log, sqrt
from sklearn.feature_extraction.text import  CountVectorizer

def show(scores, words):
    s = sorted(zip(scores, [i for i in range(len(scores))]), reverse=True)
    for i in range(30):
        print(words[s[i][1]], s[i][0])

def read(name):
    res = ""
    with open(name) as f:
        for i in f.readlines():
            res = res + " " + i
    return res

documents = [
    read("textforpreprocessing2updated.txt"),
    read("textforpreprocessing.txt")
]

vect = CountVectorizer()
matrix = vect.fit_transform(documents)
city1 = matrix.toarray()[0]
city2 = matrix.toarray()[1]
words = vect.get_feature_names_out()
count = len(words)
city1_sum = sum(city1)
city1_res = [0.0 for i in range(count)]
city2_sum = sum(city2)
city2_res = [0.0 for i in range(count)]
countdoc = len(documents)
for i in range(count):
    idf = 0.0
    if city1[i] > 0:
        idf = idf + 1
    if city2[i] > 0:
        idf = idf + 1
        

    
    idf = log(float(countdoc) / idf)
    city1_res[i] = (float(city1[i]) / city1_sum) * idf
    city2_res[i] = (float(city2[i]) / city2_sum) * idf

# Compute Cosine Similarity
def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = sqrt(sum(a * a for a in vec1))
    magnitude2 = sqrt(sum(b * b for b in vec2))
    
    return dot_product / (magnitude1 * magnitude2) if magnitude1 and magnitude2 else 0.0

similarity_score = cosine_similarity(city1_res, city2_res)
print(f"Cosine Similarity between documents: {similarity_score:.4f}")

show(city2_res, words)