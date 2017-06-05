from sklearn.feature_extraction.text import TfidfVectorizer

def vectorization(font_pixel):
	documents=open(font_pixel, 'r')
	tfidf=TfidfVectorizer().fit_transform(documents)

	return tfidf

font='batang.txt'
vectored_font=vectorization(font)

print(vectored_font)