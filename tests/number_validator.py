
""" This is a sample Unittest Test suites, containing a bunch of test cases
    
    date Created : 16-Nov-2023
    @Author      : Ganesh Prasad, <gpc.puttur@gmail.com>
"""

import os, sys
sys.path.append(os.path.dirname(os.getcwd()))

from library import report_generator
from Globals.globals import Globals


sys.path.append(os.getcwd())

 

import unittest

class NumberValidator(unittest.TestCase):

    
    @classmethod
    def setUpClass(cls):
        NumberValidator.test_case_id = 1
        NumberValidator.reporter = report_generator.ReportGenerator()

    def setUp(self):
        print ("called first")
        print (Globals.sett_configs)
        
    def test_1(self):
        """
        1) Enter a number in the Device Keyboard.\
        2) Check if the number is entered properly.\
        3) verify if the number is shownup in the text box.\
        4) Check if the enter number is numeric - 1\
        """
        self.expected_res = "The value displayed in the screen should be 1"
        self.status = True

        if self.status:
            self.act_res = "The value displayed in the screen is 1 as expected"
        else:
            self.act_res = "The value displayed in the screen is not 1."

    def test_2(self):
        """
        1) Enter a number in the Device Keyboard.\
        2) Check if the number is entered properly.\
        3) verify if the number is shownup in the text box.\
        4) Check if the enter number is numeric - 1\
        """
        self.expected_res = "The value displayed in the screen should be 2"
        self.status = False
        if self.status:
            self.act_res = "The value displayed in the screen is 2 as expected"
        else:
            self.act_res = "The value displayed in the screen is not 2."

    def tearDown(self):

        suite_name = unittest.TestCase.id(self).split(".")[-2]        
        test_id = (suite_name+"_"+str(NumberValidator.test_case_id))
        test_name = unittest.TestCase.id(self).split(".")[-1]
        steps = unittest.TestCase.shortDescription(self)

        steps = steps.split(".")
        steps = "<br>".join(steps)

        d = {"test_id" : test_id, "suite_name" : suite_name,
         "test_name" : test_name, "steps" : steps,
         "expected_res" : self.expected_res, "actual_res" : self.act_res, "status" : self.status,
         "exe_time" : "'2 min, 15 sec'", "screenshots" : "fail.png"}

        NumberValidator.reporter.generate_report(d)
        

        NumberValidator.test_case_id+=2


        


if __name__=="__main__":
    unittest.main()
