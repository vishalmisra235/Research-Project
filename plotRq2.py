import matplotlib.pyplot as plt

f1 = open("avgissuetime.txt", "r")
f2 = open("percentrelevcomm.txt", "r")
avgTimeValues = f1.readlines()
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
    if int(numberOfComm) >= 100:
        repos.append(repoName)
        eachRepoInfo = []
        eachRepoInfo.append(float(avgTime)/86400)
        avgtime.append(float(avgTime)/86400)
        eachRepoInfo.append(int(numberOfComm))
        eachRepoInfo.append(float(relevCommpercent))
        repoInfo[repoName] = eachRepoInfo

plot1 = {}
for i in range(0,len(repos)):
    lis = repoInfo[repos[i]]
    plot1[lis[0]] = lis[2]

avgtime.sort()
for i in range(0, len(avgtime)):
    relevcomm.append(plot1[avgtime[i]])

print(repoInfo)
print(plot1)
plt.plot(avgtime,relevcomm)
plt.xlabel("time")
plt.ylabel("% relev")
plt.show()

