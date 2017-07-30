import unittest
import HTMLTestRunner
import os
import time
from AccessCode import AccessCode
from MainPages import MainPages
from AppsLink import AppsLink
from AuthLogin import AuthLogin
from DownloadBook import DownloadBook
from Cart import Cart
from ChangePassword import ChangePassword
from BookSuggestion import BookSuggestion
from CheckTabs import CheckTabs
from DiscussionCreation import DiscussionCreation
from Enquiry import Enquiry
from Footer import Footer
from ForgotPassword import ForgotPassword
from FullScreenReader import FullScreenReader
from Filter import Filter
from LeftClick import LeftClick
from FormalLogin import FormalLogin
from MockTest import MockTest
from PreviewBook import PreviewBook
from PriceVerify import PriceVerify
from Profile import Profile
from Query import Query
from ReaderSetting import ReaderSetting
from AuthSignUp import AuthSignUp
from FormalSignUp import FormalSignUp
from SortBy import SortBy
from UserExist import UserExist

 
# get the directory path to output report file
dir = os.getcwd()

#code to get all test files name into a list 'pyfiles' and also instantiate test cases
support_files = ['PathCreator.py','HTMLTestRunner.py', 'LoginPage.py', 'SpayeeTestReportGenerator.py']
files = os.listdir(dir)
pyfiles = []
for file in files:
    if file[-2:] == 'py' and file not in support_files:
        #instantiating test cases in variable
        globals()[file[:-3]+'_test'] = unittest.TestLoader().loadTestsFromTestCase(globals()[file[:-3]])
        #adding these variables names in pyfiles
        pyfiles.append(locals()[file[:-3]+'_test'])

# create a test suite combining all files from 'pyfiles' list created earlier
test_suite = unittest.TestSuite(pyfiles)

# Get date and time
date = time.strftime('%d-%m-%Y')
time_ = time.strftime('%H-%M')
filename = '{}_{}.html'.format(date, time_)
# open the report file(dir[:-8] is used to get rid of parent folder names which is 8 letters long)
outfile = open(dir[:-8] + "/Report/{}".format(filename), "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Acceptance Tests')
 
# run the suite using HTMLTestRunner
runner.run(test_suite)

# close the file so another it can be opened from cmd or terminal
outfile.close()

# open report
os.chdir('..')
os.chdir('Report')
if os.name=='nt':
    os.system('{}'.format(filename))
else:
    os.system('open {}'.format(filename))
    
