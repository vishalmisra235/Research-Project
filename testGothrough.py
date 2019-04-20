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
import statistics

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
#frelevcomm = open("percentrelevcomm.txt", "w")
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


'''This code walks through the given repository and prints all the code comments
wether be single line or multiline'''

from os import walk
import os
import re

alldir = []
f8 = open("filenames.txt", "r")
alldir = f8.readlines()
for i in range(0, len(alldir)):
    alldir[i] = alldir[i].replace("\n", '')

f8= open(os.path.join(r'C:\Users\Sai Krupa\Documents\Documents\CS-VI\Research_Project\GitHubRepos','pythonfiles.txt'), "w")
f7=open(os.path.join(r'C:\Users\Sai Krupa\Documents\Documents\CS-VI\Research_Project\GitHubRepos','allLinks.txt'), "r")
links = f7.readlines()
num=0
avgcommlist = []
for i in range(0,151):
    print(i)
    link = links[i].strip()
    print(link)
    repo = ''
    pos = link.rfind('/')
    repo = link[pos+1:] + '-master'
    print(repo)
    if repo in alldir:
        num = num + 1
        print("ok")
        files=[]
        python_files = []
        directory = []
        python_directory=[]

        #need to provide path to repository
        mypath=r'C:\Users\Sai Krupa\Documents\Documents\CS-VI\Research_Project\GitHubRepos' + '\\' + repo
        f2 = open(os.path.join(r'C:\Users\Sai Krupa\Documents\Documents\CS-VI\Research_Project\GitHubRepos' + '\\' + repo,'comments.txt'), "w", encoding="utf8")
        n_files=0
        commlist = []
        for (dirpath, dirnames, filenames) in walk(mypath):
            files.extend(filenames)
            
            for file in filenames:
                testlist = []
                text=''
                filename = str(file)
                x = re.findall("py$",filename)
                
                if(x):
                    n_files = n_files+1
                    python_files.append(file)
                    python_directory.append(dirpath)
                    try: 
                        f1=open(os.path.join(str(dirpath),str(file)), "r", encoding="utf8")
                        nlines = 0
                        ncomm = 0
                        for lines in f1:
                            nlines = nlines + 1
                            #lines = lines.encode('utf-8').strip()
                            lines = lines.lstrip()
                            y = re.findall("^#",str(lines))
                            
                            text = text+str(lines)
                            if(y):
                                testlist.append(str(lines))
                                ncomm = ncomm + 1
                                f2.write(str(lines))
                                f2.write("\n")
                                #print(lines)
                        a=re.compile("\'\'\'.*?\'\'\'",re.DOTALL)
                        ans=a.findall(text)
                        for text in ans:
                            testlist.append(str(text))
                            ncomm = ncomm + 1 
                            f2.write(text)
                            f2.write("\n")
                        #print(ans)
                        b=re.compile('\"\"\".*?\"\"\"',re.DOTALL)
                        ans1 = b.findall(text)
                        for text in ans1:
                            testlist.append(str(text))
                            ncomm = ncomm + 1
                            f2.write(text)
                            f2.write("\n")
                        #print(ans1)
                        f1.close()
                        sc=0
                        sa=0
                        sd=0
                        se=0
                        sf=0
                        try:
                            predict = text_clf.predict(x)
                            for text in predict:
                                if text == 'RelevantComments' or text == 'TaskComments':
                                    sc=sc+1
                                sa=sa+1

                                if text == 'CopyrightComments':
                                    sd=sd+1
                                if text == 'IrrelevantComments':
                                    se=se+1
                                if text == 'CodeComments':
                                    sf=sf+1
                            commlist.append(float(sc/nlines))
                        except:
                            commlist.append(float(0))
                    except:
                        print("err")
            directory.append(dirpath)
        f8.write(str(n_files))
        f8.write("\n")    
        f2.close()
        try:
            avgcommlist.append(statistics.mean(commlist))
        except:
            avgcommlist.append(0)
print(num)
print(avgcommlist)
print(len(avgcommlist))
f8.close()
