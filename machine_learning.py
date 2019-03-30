import sklearn
import os
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split

categories = ['Copyright','Header','Useless']

docs_to_train = sklearn.datasets.load_files(r'F:\Research Project\model', description=None, categories=categories, load_content=True, encoding='utf-8', shuffle=True,decode_error='ignore', random_state=42)
print(docs_to_train.target_names)
#print(docs_to_train.data)

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(docs_to_train.data)

tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
print(X_train_tf.shape)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf.shape)

clf = MultinomialNB().fit(X_train_tfidf, docs_to_train.target)
print(clf)

docs_new = ['Author: Vishal Misra', 'This method does nothing']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)
for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc, docs_to_train.target_names[category]))

#X_train, X_test, y_train, y_test = train_test_split(docs_to_train.data, docs_to_train.target, test_size=0.33, random_state=42)
text_clf = Pipeline([('count_vect', CountVectorizer()),
                     ('tfidf_transformer', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42,
                       max_iter=5, tol=None)),])
text_clf.fit(docs_to_train.data, docs_to_train.target)
predicted = text_clf.predict(docs_to_train.data)
print(np.mean(predicted == docs_to_train.target))

print(metrics.classification_report(docs_to_train.target, predicted,target_names=docs_to_train.target_names))
