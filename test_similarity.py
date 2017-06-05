from math import *

def jaccard_similarity(x,y):
	
	intersection_cardinality=len(set.intersection(*[set(x), set(y)]))
	union_cardinality=len(set.union(*[set(x), set(y)])) 
	
	return intersection_cardinality/float(union_cardinality)

def conversion(font_file):
	txt_file=open(font_file, 'r') 
	txt_list=txt_file.readlines()
 	
	return txt_list

batang='batang.txt'
conversion_batang=conversion(batang)

gungseo='gungseo.txt'
conversion_gungseo=conversion(gungseo)

batang2='batang2.txt'
conversion_batang2=conversion(batang2)

result=jaccard_similarity(conversion_batang, conversion_gungseo)
print(result)
result2=jaccard_similarity(conversion_batang, conversion_batang2)
print(result2)

