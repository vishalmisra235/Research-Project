import matplotlib.pyplot as plt
f = open("results_rq2.txt", "r")
allvalues = f.readlines()
dictValues = {}
avgtime = []
relevantcomm = []
for i in range(0,len(allvalues)):
    allvalues[i] = allvalues[i].strip()
    a = allvalues[i].split(' ')
    a[0] = float(a[0])/86400
    avgtime.append(a[0])
    dictValues[a[0]] = a[-1]

print(avgtime)
avgtime.sort()
print(avgtime)
for i in range(0, len(avgtime)):
    relevantcomm.append(float(dictValues[avgtime[i]]))

print(relevantcomm)

plt.plot(avgtime,relevantcomm)
plt.xlabel("time")
plt.ylabel("% relev")
plt.show()
