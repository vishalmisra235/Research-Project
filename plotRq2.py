import matplotlib.pyplot as plt
from scipy.interpolate import spline
import numpy as np
import os
from scipy.optimize import curve_fit

def func(x, a,d):
    return (a/(x))

f9 = open(os.path.join(r'C:\Users\Sai Krupa\Documents\Documents\CS-VI\Research_Project\GitHubRepos','pythonfiles.txt'), "r")
python_files= []
for num in f9:
    python_files.append(int(num))

f1 = open("avgissuetime.txt", "r")
f2 = open("percentrelevcomm.txt", "r")
avgTimeValues = f1.readlines()
print(len(avgTimeValues))
percentCommValues  = f2.readlines()
repoInfo = {}
repos = []
avgtime = []
relevcomm = []
for i in range(0,len(avgTimeValues)):
    avgTimeValues[i] = avgTimeValues[i].strip()
    percentCommValues[i] = percentCommValues[i].strip()
    timeName = avgTimeValues[i].split(' ')
    repoName = timeName[0]
    avgTime = timeName[1]
    relevCommInfo = percentCommValues[i].split()
    numberOfComm = relevCommInfo[1]
    relevCommpercent = relevCommInfo[2]
    if (int(numberOfComm)>500):
        repos.append(repoName)
        eachRepoInfo = []
        eachRepoInfo.append(float(avgTime)/86400)
        eachRepoInfo.append(int(numberOfComm))
        relevcomm.append(int(numberOfComm))
        eachRepoInfo.append(float(relevCommpercent))
        #relevcomm.append(float(relevCommpercent))
        repoInfo[repoName] = eachRepoInfo



plot1 = {}
for i in range(0,len(repos)):
    lis = repoInfo[repos[i]]
    plot1[lis[1]] = lis[0]

relevcomm.sort()
for i in range(0, len(relevcomm)):
    avgtime.append(plot1[relevcomm[i]])
print(len(avgtime))
print(repoInfo)
print(plot1)
x = np.array(relevcomm)
print(x)
y = np.array(avgtime)
param, param_cov = curve_fit(func, x,y)
print(param)
print(param_cov)
ans = (param[0]/(x))
'''xdata = np.array(relevcomm)
ydata = func(xdata,100000, 1)
plt.plot(xdata, ydata, 'b-',label='data')'''
plt.scatter(relevcomm, avgtime)
plt.plot(relevcomm, ans)
plt.ylabel("time")
plt.xlabel("% relev")
plt.show()
f9.close()
