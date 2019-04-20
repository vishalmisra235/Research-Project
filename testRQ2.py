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

f9 = open(os.path.join(r'C:\Users\Sai Krupa\Documents\Documents\CS-VI\Research_Project\GitHubRepos','pythonfiles.txt'), "r")
alldir = []
repos = []
f8 = open("filenames.txt", "r")
alldir = f8.readlines()
for i in range(0, len(alldir)):
    alldir[i] = alldir[i].replace("\n", '')
f7=open(os.path.join(r'C:\Users\Sai Krupa\Documents\Documents\CS-VI\Research_Project\GitHubRepos','allLinks.txt'), "r")
links = f7.readlines()
for i in range(0,151):
    link = links[i].strip()
    repo = ''
    pos = link.rfind('/')
    repo = link[pos+1:] + '-master'
    if repo in alldir:
        repos.append(repo)

print(len(repos))
frelevcomm = open("percentrelevcomm.txt", "w")
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

for repo in repos:
    f = open(r'C:\Users\Sai Krupa\Documents\Documents\CS-VI\Research_Project\GitHubRepos' + '\\' + repo + '\\' + 'comments.txt','r',encoding = "utf8")
    all_lines = ""
    x=[]
    for line in f:
        all_lines = all_lines+line
        y = re.findall("^#",str(line))
        if(y):
           x.append(str(line))
    slc=re.compile("\'\'\'.*?\'\'\'",re.DOTALL)
    ans = slc.findall(all_lines)
    b=re.compile("\"\"\".*?\"\"\"",re.DOTALL)
    ans1 = b.findall(all_lines)

    for lines in ans:
        x.append(lines)
    for lines in ans1:
        x.append(lines)
        
    c=0
    a=0
    d=0
    e=0
    f=0
    try:
        predict = text_clf.predict(x)
        frelevcomm.write(repo)
        frelevcomm.write(" ")
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
        frelevcomm.write(str(c))
        frelevcomm.write(" ")
        print(c/a)
        frelevcomm.write(str(c/a))
        frelevcomm.write("\n")
        print(d/a)
        print(e/a)
        print(f/a)
        #print(predict)
    except:
        frelevcomm.write(repo)
        frelevcomm.write(" ")
        frelevcomm.write("0")
        frelevcomm.write(" ")
        frelevcomm.write("0")
        frelevcomm.write("\n")
frelevcomm.close()
