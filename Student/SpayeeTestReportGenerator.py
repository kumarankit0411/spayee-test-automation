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

# Get all tests
AccessCode_test = unittest.TestLoader().loadTestsFromTestCase(AccessCode)
MainPages_test = unittest.TestLoader().loadTestsFromTestCase(MainPages)
AppsLink_test = unittest.TestLoader().loadTestsFromTestCase(AppsLink)
AuthLogin_test = unittest.TestLoader().loadTestsFromTestCase(AuthLogin)
DownloadBook_test = unittest.TestLoader().loadTestsFromTestCase(DownloadBook)
Cart_test = unittest.TestLoader().loadTestsFromTestCase(Cart)
ChangePassword_test = unittest.TestLoader().loadTestsFromTestCase(ChangePassword)
CheckTabs_test = unittest.TestLoader().loadTestsFromTestCase(CheckTabs)
DiscussionCreation_test = unittest.TestLoader().loadTestsFromTestCase(DiscussionCreation)
Enquiry_test = unittest.TestLoader().loadTestsFromTestCase(Enquiry)
Footer_test = unittest.TestLoader().loadTestsFromTestCase(Footer)
ForgotPassword_test = unittest.TestLoader().loadTestsFromTestCase(ForgotPassword)
FullScreenReader_test = unittest.TestLoader().loadTestsFromTestCase(FullScreenReader)
Filter_test = unittest.TestLoader().loadTestsFromTestCase(Filter)
LeftClick_test = unittest.TestLoader().loadTestsFromTestCase(LeftClick)
FormalLogin_test = unittest.TestLoader().loadTestsFromTestCase(FormalLogin)
MockTest_test = unittest.TestLoader().loadTestsFromTestCase(MockTest)
PreviewBook_test = unittest.TestLoader().loadTestsFromTestCase(PreviewBook)
PriceVerify_test = unittest.TestLoader().loadTestsFromTestCase(PriceVerify)
Profile_test = unittest.TestLoader().loadTestsFromTestCase(Profile)
Query_test = unittest.TestLoader().loadTestsFromTestCase(Query)
ReaderSetting_test = unittest.TestLoader().loadTestsFromTestCase(ReaderSetting)
AuthSignUp_test = unittest.TestLoader().loadTestsFromTestCase(AuthSignUp)
FormalSignUp_test = unittest.TestLoader().loadTestsFromTestCase(FormalSignUp)
BookSuggestion_test = unittest.TestLoader().loadTestsFromTestCase(BookSuggestion)
UserExist_test = unittest.TestLoader().loadTestsFromTestCase(UserExist)
SortBy_test = unittest.TestLoader().loadTestsFromTestCase(SortBy)

#code to get all test files name into a list 'pyfiles'
support_files = ['HTMLTestRunner.py', 'LoginPage.py', 'SpayeeTestReportGenerator.py']
files = os.listdir(dir)
pyfiles = []
for file in files:
    if file[-2:] == 'py' and file not in support_files:
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

# open report
os.chdir('..')
os.chdir('Report')
os.system('open {}'.format(filename))
