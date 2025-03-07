
# The task is to calculate tF-IDF for three documents 
# (this require fixing the calculation procedure, since at the moment 
# it can process only two documents). After that please get cosine products
#  for the third and the first document, and for the third and the second document. 
# Having these two values of consine products please compare is the third document is closer 
#  to the first one or to the second one.

from math import log, sqrt
from sklearn.feature_extraction.text import CountVectorizer

def show(scores, words):
    s = sorted(zip(scores, [i for i in range(len(scores))]), reverse=True)
    for i in range(min(30, len(s))):   
        print(words[s[i][1]], s[i][0])

def read(name):
    res = ""
    with open(name) as f:
        for i in f.readlines():
            res += " " + i.strip()  
    return res
 
documents = [
    read("textforpreprocessing2updated.txt"),
    read("textforpreprocessing.txt"),
    read("textforpreprocessing3.txt")  
]
 
vect = CountVectorizer()
matrix = vect.fit_transform(documents)
 
city_vectors = matrix.toarray()
words = vect.get_feature_names_out()
count = len(words)
 
tfidf_results = []
 
for doc_index in range(len(documents)):
    doc_vector = city_vectors[doc_index]
    doc_sum = sum(doc_vector)
    doc_tfidf = [0.0 for _ in range(count)]
    
    for i in range(count):
        idf = sum(1 for j in range(len(documents)) if city_vectors[j][i] > 0)  
        if idf > 0:
            idf = log(float(len(documents)) / idf)
            doc_tfidf[i] = (float(doc_vector[i]) / doc_sum) * idf
    
    tfidf_results.append(doc_tfidf)
 
def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = sqrt(sum(a * a for a in vec1))
    magnitude2 = sqrt(sum(b * b for b in vec2))
    
    return dot_product / (magnitude1 * magnitude2) if magnitude1 and magnitude2 else 0.0
 
similarity_1_3 = cosine_similarity(tfidf_results[0], tfidf_results[2])  
similarity_2_3 = cosine_similarity(tfidf_results[1], tfidf_results[2])   

print(f"Cosine Similarity between Document 1 and Document 3: {similarity_1_3:.4f}")
print(f"Cosine Similarity between Document 2 and Document 3: {similarity_2_3:.4f}")
 
if similarity_1_3 > similarity_2_3:
    print("Document 3 is closer to Document 1.")
elif similarity_1_3 < similarity_2_3:
    print("Document 3 is closer to Document 2.")
else:
    print("Document 3 is equally close to Document 1 and Document 2.")
 
show(tfidf_results[2], words)