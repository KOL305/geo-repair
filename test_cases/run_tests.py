import unittest
import HtmlTestRunner
from test_suite import HomeTest
import sys
import os
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')  # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, './test_cases')


# get all tests from SearchText and HomePageTest class
home_test = unittest.TestLoader().loadTestsFromTestCase(HomeTest)
test_suite = unittest.TestSuite(
    [
        home_test,
    ]
)


# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(report_title='Test Report', combine_reports=True, open_in_browser=True,output='test_cases/reports')

# run the suite using HTMLTestRunner
runner.run(test_suite)