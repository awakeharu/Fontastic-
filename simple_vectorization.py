from sklearn.feature_extraction.text import TfidfVectorizer

fdir='batang.txt'
documents=open(fdir, 'r')
tfidf=TfidfVectorizer().fit_transform(documents)

print(tfidf)