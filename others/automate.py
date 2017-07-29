import os

files = os.listdir()
pyfiles=[]
for file in files:
    if file[-2:] == 'py' and file != "automate.py":
        os.system("python3 {}".format(file))


