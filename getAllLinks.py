import os
f3 = open("filenames.txt", "r")
alldir = f3.readlines()
print(len(alldir))
for i in range(0, len(alldir)):
    alldir[i] = alldir[i].replace("\n", '')

f1=open(os.path.join(r'C:\Users\Sai Krupa\Documents\Documents\CS-VI\Research_Project\GitHubRepos','repolinks.txt'), "r")
links = f1.readlines()
print(len(links))
f2 = open("allrepolinks.txt", "w")

for link in links:
    link = link.strip()
    #print(link)
    repo = ''
    pos = link.rfind('/')
    repo = link[pos+1:] + '-master'
    #print(repo)
    if repo in alldir:
        f2.write(link)
        f2.write("\n")

f2.close()

f4 = open("allrepolinks.txt", "r")
alllinks = f4.readlines()
print(len(alllinks))
