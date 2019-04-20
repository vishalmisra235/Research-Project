from scipy import stats
import numpy as np

f1 = open("all_issues.txt", "r")
allIssues = f1.readlines()


j=0
openIssues = []
closedIssues= []
linknumber = []
for i in range(0, len(allIssues)):
    allIssues[i] = allIssues[i].strip()
    if j==0:
        j=1
    elif j==1:
        j=2
        if allIssues[i] != "Author":
            linknumber.append(int(i/3))
            allIssues[i] = allIssues[i].replace(',','')
            closedIssues.append(int(allIssues[i]))
            allIssues[i-1] = allIssues[i-1].replace(',', '')
            openIssues.append(int(allIssues[i-1]))
    elif j==2:
        j=0

print(openIssues)
print(closedIssues)
print(len(openIssues))
print(len(closedIssues))
print(linknumber)
print(len(linknumber))

openandcloseIssues = []

for i in range(0, len(openIssues)):
    openandcloseIssues.append(openIssues[i] + closedIssues[i])
print(openandcloseIssues)
print(len(openandcloseIssues))

f = open("percentrelevcomm1.txt", "r")
allValues = f.readlines()
print(len(allValues))
relevcomm = []
for i in range(0, len(allValues)):
    allValues[i] = allValues[i].strip()
    line = allValues[i].split(' ')
    comm = line[1]
    if i in linknumber:
        relevcomm.append(int(comm))
print(relevcomm)
print(len(relevcomm))

relevarray = np.array(relevcomm)
numissues = np.array(openandcloseIssues)

print(stats.spearmanr(relevarray, numissues))
