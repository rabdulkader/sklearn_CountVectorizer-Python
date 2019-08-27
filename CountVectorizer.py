#Read Explanation.txt to understand how this work

from sklearn.feature_extraction.text import CountVectorizer

text = ['Hello my name is Reayn','Hola Meyamo Reyan']

vectorizer = CountVectorizer()
x= vectorizer.fit_transform(text)
z= vectorizer.get_feature_names()
print(z)
print('\n',x.toarray())
