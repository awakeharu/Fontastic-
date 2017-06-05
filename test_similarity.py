from math import *

def jaccard_similarity(x,y):

	intersection_cardinality=len(set.intersection(*[set(x), set(y)]))
	union_cardinality=len(set.union(*[set(x), set(y)]))
	return intersection_cardinality/float(union_cardinality)

def conversion(font_file):

	txt_file=(font_file, 'r')
	txt_list=txt_file.readlines()

	return txt_list
