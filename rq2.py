import sklearn
import os
import numpy as np
import pandas as pd
from sklearn import svm
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier

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

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.23, shuffle=True, random_state=42)

text_clf = Pipeline([('count_vect', CountVectorizer()),
                     ('tfidf_transformer', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42,
                       max_iter=5, tol=None)),])
text_clf.fit(X_train,y_train)
predict = text_clf.predict(X_test)
print(np.mean(predict == y_test))
print(metrics.classification_report(y_test, predict,target_names=column_names))
print()

f = open(r'F:\Research Project\fail2ban-0.11\comments.txt','r',encoding = "utf8")
all_lines = ""
x=[]
for line in f:
    all_lines = all_lines+line
    y = re.findall("^#",str(line))
    if(y):
       x.append(str(line)) 
b=re.compile("\"\"\".*?\"\"\"",re.DOTALL)
ans1 = b.findall(all_lines)

for lines in ans1:
    x.append(lines)
    
c=0
a=0
d=0
e=0
f=0
predict = text_clf.predict(x)
for text in predict:
    if text == 'RelevantComments' or text == 'TaskComments':
        c=c+1
    a=a+1

    if text == 'CopyrightComments':
        d=d+1
    if text == 'IrrelevantComments':
        e=e+1
    if text == 'CodeComments':
        f=f+1

print(a)
print(c/a)
print(d/a)
print(e/a)
print(f/a)
#print(predict)
