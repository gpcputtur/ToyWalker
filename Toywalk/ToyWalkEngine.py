
""" Implementation of TOWTA (Toy Walker Test Automation Framework) engine.
    This will be an entry point to the Test Execution.

    date Created : 16-Nov-2023
    @Author      : Ganesh Prasad, <gpc.puttur@gmail.com>
"""
import sys, os
sys.path.append(os.path.dirname(os.getcwd()))

import unittest
from tests import number_validator

from Globals.globals import Globals
from library import parsers


class ATEngineDriver():
    """ The class 'ATEngineDriver' implements the TOWTA Engine.
    The instance method 'execute' is the entry point to the individual test suite execution.
    """

    def __init__(self):

        config_ini_parser_obj = parsers.INIParser()

        # Load the execution profile
        Globals.sett_configs = config_ini_parser_obj.parse_test_ini("config.ini")

        # Load the test profile
        Globals.test_configs = config_ini_parser_obj.parse_test_ini("tests.ini")


    def execute(self):
        """ The method 'execute' will start the test execution by loading the tests writter using Python-Unittest module.
        """
        suite = unittest.TestLoader().loadTestsFromModule(number_validator)
        unittest.TextTestRunner(verbosity=2).run(suite)


if __name__=="__main__":
    at = ATEngineDriver()
    at.execute()


        
