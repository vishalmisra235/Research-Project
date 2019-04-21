import matplotlib.pyplot as plt
from scipy.interpolate import spline
import numpy as np
import os
#from testGothrough import avgcommlist
from scipy.optimize import curve_fit
from collections import defaultdict as dd



avgcommlist = [0.0125, 0.008399816752110097, 0.054903088389828596,
               0.04213466834768425, 0.041442242109001215,
               0.016196591394598323, 0.019113247597042173, 0.011344550636742124, 0.028825728209739384, 0.024769298062048115, 0.06283598027504116, 0.03844429415325683, 0.06037969466519524, 0.08415164982429116, 0.05829535933700241, 0.01952500499970614, 0.01899023388665886, 0.017309875696538843, 0.02124435932995749, 0.03700819583742612, 0.020976245755589776, 0.01692787213391176, 0.07487383407620829, 0.008767892274084392, 0.024769298062048115, 0.02309664803340986, 0.03650298341242153, 0.04790929782958917, 0.02335056926044287, 0.06072976340443199, 0.0026336583392306176, 0.01025599895062655, 0.1, 0.04050959604649368, 0.03925802897441262, 0.0648204317065585, 0.016426134369979042, 0.008771907558067692, 0.013459698497927188, 0.03206264824205508, 0.03882222536923697, 0.021064587403289446, 0.013970110460354204, 0.010519028812732938, 0.055085588128977264, 0.04723060449434276, 0.15284186193899138, 0.023806566601019884, 0.04419056137765793, 0.03431844613109483, 0.021117175712649733, 0.020059465086025064, 0.054752415215226787, 0.09663306186848898, 0.026430809589623835, 0.1530032026844409, 0.021215161975446564, 0.025729904964811222, 0.023113494367896188, 0.11191481116101991, 0.02442685768645781, 0.04975324929843882, 0.08545228958662288, 0.05064922604972397, 0.048487116737721395, 0.0186916575320209, 0.017684759130414163, 0.031056109900049773, 0.013683470843840296, 0.047087872927101496, 0.03655839097841353, 0, 0.018993746415602628, 0.024662105533413078, 0.06555749988824527, 0.06451917860585213, 0.03561160774160559, 0.0414042429086083, 0.2183555312740335, 0.04897750309647797, 0.03788165681812799, 0.018123437463892583, 0.024851302265776448, 0.014788972723945302, 0.02240001761360782, 0.030380726931065166, 0.08510268897768898, 0.023481351533287405, 0.09663608137197788, 0.006749844819351176, 0.026172504497729725, 0.090611762113944, 0.037003489277060125, 0.15301241197980328, 0.016455547837758565, 0.012801731590765988, 0.01750453578409774, 0.012655102483398099, 0.009227131000325513, 0.018019688151452253, 0.02382257867100047, 0.07770432434289654, 0.0052131181331205425, 0.02330458093418306, 0.03152412175456262, 0.009492620154156976, 0.010916613424598934]
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
    #if (int(numberOfComm)>1000):
    repos.append(repoName)
    eachRepoInfo = []
    eachRepoInfo.append(float(avgTime)/86400)
    eachRepoInfo.append(int(numberOfComm))
    relevcomm.append(int(numberOfComm))
    eachRepoInfo.append(float(relevCommpercent))
    #relevcomm.append(float(relevCommpercent))
    repoInfo[repoName] = eachRepoInfo



plot1 = {}
plot1 = dd(list)
print(len(repos))
print(len(avgcommlist))
for i in range(0,len(repos)):
    lis = repoInfo[repos[i]]
    if avgcommlist[i] != 0:
        plot1[avgcommlist[i]].append(lis[0])

plot1 = dict(plot1)
print(plot1)
avgcommlist.sort()
avgcommlist.remove(0)
print(avgcommlist)

for i in list(set(avgcommlist)):
    for j in range(avgcommlist.count(i)):
        avgtime.append(plot1[i][j])

print(len(avgtime))
print(repoInfo)

x = np.array(avgcommlist)
print(x)
y = np.array(avgtime)
param, param_cov = curve_fit(func, x,y)
print(param)
print(param_cov)
ans = (param[0]/(x))

#plt.xlim(0,20000)
plt.scatter(avgcommlist, avgtime)
#x,y = zip(*sorted((xVal, np.mean([yVal for a, yVal in zip(avgcommlist, avgtime) if xVal==a]))for xVal in set(relevcomm)))
plt.ylabel("time")
plt.xlabel("avg comm")
plt.plot(avgcommlist,ans)
#plt.show()
#plt.scatter(x,y)
#plt.savefig("SGDtestfig.png", dpi=200)
plt.show()
f9.close()
