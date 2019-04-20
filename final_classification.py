import sklearn
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


column_names=['CopyrightComments','RelevantComments','TaskComments','CodeComments','IrrelevantComments']
df = pd.read_csv("ResearchData.csv",names=column_names)

copyright_com = df.CopyrightComments.tolist()

copyright_comments =  [x for x in copyright_com if str(x) != 'nan']

relevant_comments = [x for x in df.RelevantComments.tolist() if str(x) != 'nan']

task_comments = [x for x in df.TaskComments.tolist() if str(x) != 'nan']

code_comments = [x for x in df.CodeComments.tolist() if str(x) != 'nan']

irrelevant_comments = [x for x in df.IrrelevantComments.tolist() if str(x) != 'nan']

X=[]
Y=[]
for s in copyright_comments:
    X.append(s)
    Y.append('CopyrightComments')

for s in relevant_comments:
    X.append(s)
    Y.append('RelevantComments')

for s in task_comments:
    X.append(s)
    Y.append('TaskComments')

for s in code_comments:
    X.append(s)
    Y.append('CodeComments')

for s in irrelevant_comments:
    X.append(s)
    Y.append('IrrelevantComments')

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X)

tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
print(X_train_tf.shape)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf.shape)

clf = MultinomialNB().fit(X_train_tfidf, Y)
print(clf)

docs_new = ['Copyright: Vishal Misra', 'This method does nothing']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)
print(predicted)

print('SVM classifier')
print()
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.23, shuffle=True, random_state=42)
text_clf = Pipeline([('count_vect', CountVectorizer()),
                     ('tfidf_transformer', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42,
                       max_iter=5, tol=None)),])
text_clf.fit(X_train, y_train)
predicted = text_clf.predict(X_test)
print(np.mean(predicted == y_test))

print(metrics.classification_report(y_test, predicted,target_names=column_names))

print('Decision Tree Classifier')
print()
text_clf = Pipeline([('count_vect', CountVectorizer()),
                     ('tfidf_transformer', TfidfTransformer()),
                     ('clf',DecisionTreeClassifier(max_depth=5, random_state=42),)])
text_clf.fit(X_train, y_train)
predicted = text_clf.predict(X_test)
print(np.mean(predicted == y_test))

print(metrics.classification_report(y_test, predicted,target_names=column_names))

print('Logistic Regresion')
text_clf = Pipeline([('count_vect', CountVectorizer()),
                     ('tfidf_transformer', TfidfTransformer()),
                     ('clf',LogisticRegression(solver="lbfgs", random_state=42),)])
text_clf.fit(X_train, y_train)
predicted = text_clf.predict(X_test)
print(np.mean(predicted == y_test))

print(metrics.classification_report(y_test, predicted,target_names=column_names))

 
