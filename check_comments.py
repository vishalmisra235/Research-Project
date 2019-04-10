'''This code walks through the given repository and prints all the code comments
wether be single line or multiline'''

from os import walk
import os
import re

files=[]
python_files = []
directory = []
python_directory=[]

#need to provide path to repository
mypath='F:\Research Project\Python-master'
f2 = open(os.path.join('F:\Research Project','comments.txt'), "w", encoding="utf8")

for (dirpath, dirnames, filenames) in walk(mypath):
    files.extend(filenames)
    
    for file in filenames:
        text=''
        filename = str(file)
        x = re.findall("py$",filename)
        if(x):
            python_files.append(file)
            python_directory.append(dirpath)
            f1=open(os.path.join(str(dirpath),str(file)), "r", encoding="utf8")

            for lines in f1:
                y = re.findall("^#",str(lines))
                
                text = text+str(lines)
                if(y):
                    f2.write(str(lines))
                    f2.write("\n")
                    print(lines)
            a=re.compile("\'\'\'.*?\'\'\'",re.DOTALL)
            ans=a.findall(text)
            b=re.compile("\"\"\".*?\"\"\"",re.DOTALL)
            ans1 = b.findall(text)
            for text in ans1:
                f2.write(text)
                f2.write("\n")
            print(ans)
            f1.close()
    directory.append(dirpath)

f2.close()
print(len(directory))
print(python_files)
print(python_directory)

