from sklearn.feature_extraction.text import TfidfVectorizer
from math import *

def jaccard_similarity(x, y):
	intersection_cardinality=len(set.intersection(*[set(x), set(y)]))
	union_cardinality=len(set.union(*[set(x), set(y)]))
	return intersection_cardinality/float(union_cardinality)

fdir_batang='batang.txt'
batang=open(fdir_batang, 'r')
fdir_gungseo='gungseo.txt'
gungseo=open(fdir_gungseo, 'r')

tfidf_batang=TfidfVectorizer().fit_transform(batang)
tfidf_gungseo=TfidfVectorizer().fit_transform(gungseo)

similarity=jaccard_similarity(tfidf_batang, tfidf_gungseo)
print(similarity)



