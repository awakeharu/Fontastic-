from sklearn.feature_extraction.text import TfidfVectorizer
# This library is needed for converging pixel information formatted as txt file to vector
from scipy.sparse import csr_matrix
# This library is needed for normalize csr_matrix to general matrix
# from scipy.spatial import distance
from math import *
# This library is needed for calculating intersection and union of two fonts' list
import numpy as np
from numpy import matrix
# These two libraries are needed for transforming vectored pixel to single-dimensional list


def stand(font):
	docu=open(font, 'r')
	tfidf=TfidfVectorizer().fit_transform(docu)

	return tfidf.todense()
# This function is 1. converging txt file to vector(csr_matrix format) 2. converging csr_matrix vector to general matrix

def flatten(nlist):
	result=[val for sublist in nlist for val in sublist]
	# result=[]
	# for sublist in nlist:
		# for val in sublist:
			# result.append(val)

	return result
# This function is for flattening nested list(in exact, two-dimensional list) to single-dimensional list

def conversion(font):
	sfont=stand(font)
	cfont=np.squeeze(np.asarray(sfont))
	ffont=flatten(cfont)

	return ffont
# This function is for executing conversion process that can make txt file transformed as single dimensional list
# And this function is a set of above functions

def jacsim(ufont, dbfont):
	inter_card=len(set.intersection(*[set(ufont), set(dbfont)]))
	union_card=len(set.union(*[set(ufont), set(dbfont)]))
	sim=inter_card/float(union_card)

	return sim*100
# This function is for calculating similarity between two lists, so this can be used for comparing two fonts.

# def square_rooted(x):
	# return round(sqrt(sum([a*a for a in x])), 3)

# def cossim(list1, list2):
	# numerator=sum(a*b for a,b in zip(list1, list2))
	# denominator=square_rooted(list1)*square_rooted(list2)

	# return round(numerator/float(denominator), 3)
	
fontb='batang.txt'
fontg='gungseo.txt'
fontm='malgeungodic.txt'
fonthl='headline.txt'

batang=conversion(fontb)
gungseo=conversion(fontg)
mg=conversion(fontm)
headline=conversion(fonthl)

sim1=jacsim(batang, gungseo)
sim2=jacsim(batang, mg)
sim3=jacsim(gungseo, mg)
sim4=jacsim(batang, headline)
sim5=jacsim(mg, headline)
sim6=jacsim(gungseo, headline)

print(sim1)
print(sim2)
print(sim3)
print(sim4)
print(sim5)
print(sim6)
# print(batang)
# print(gungseo)



