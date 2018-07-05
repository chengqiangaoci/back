from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=1)
print(vectorizer)
content = ["How to format my hard disk","Hard disk format problems"]
x = vectorizer.fit_transform(content)
test = vectorizer.get_feature_names()
print(x)
print(vectorizer.vocabulary_)
print(test)
print(x.todense())