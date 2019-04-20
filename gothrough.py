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
        for (dirpath, dirnames, filenames) in walk(mypath):
            files.extend(filenames)
            
            for file in filenames:
                text=''
                filename = str(file)
                x = re.findall("py$",filename)
                
                if(x):
                    n_files = n_files+1
                    python_files.append(file)
                    python_directory.append(dirpath)
                    try: 
                        f1=open(os.path.join(str(dirpath),str(file)), "r", encoding="utf8")

                        for lines in f1:
                            #lines = lines.encode('utf-8').strip()
                            lines = lines.lstrip()
                            y = re.findall("^#",str(lines))
                            
                            text = text+str(lines)
                            if(y):
                                f2.write(str(lines))
                                f2.write("\n")
                                #print(lines)
                        a=re.compile("\'\'\'.*?\'\'\'",re.DOTALL)
                        ans=a.findall(text)
                        for text in ans:
                            f2.write(text)
                            f2.write("\n")
                        #print(ans)
                        b=re.compile('\"\"\".*?\"\"\"',re.DOTALL)
                        ans1 = b.findall(text)
                        for text in ans1:
                            f2.write(text)
                            f2.write("\n")
                        #print(ans1)
                        f1.close()
                    except:
                        print("err")
            directory.append(dirpath)
        f8.write(str(n_files))
        f8.write("\n")    
        f2.close()
print(num)
f8.close()
