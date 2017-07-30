import os

class Path():
    def __init__(self):
        pass

    def returnPath():
        path = os.getcwd()
        if os.name=='nt':
            path = path[:-8] + "\driver\chromedriver.exe"
        else:
            path = path[:-8] + "/driver/chromedriver"
        return path
