
""" This library file implements various Parsers class for ini files, xml files and cvs/excel files.

    date Created : 16-Nov-2023
    @Author      : Ganesh Prasad, <gpc.puttur@gmail.com>
"""

import os
import configparser


class INIParser():

    def __init__(self):
        pass
    

    def parse_test_ini(self, ini_file):
        """ The method parse_test_ini() parses the test.ini file.
            Args    : ini_file     - Name of the config ini file which we would read through this method
            Returns : ini_data - Dictionary containing the confis items of an ini file.
        """
        ini_data = {}
        config = configparser.ConfigParser()
        config.read(os.path.join(os.getcwd(), "config", ini_file))
        all_sections = config.sections()
        for each_section in all_sections:
            ini_data[each_section] = {}
            for key in config[each_section]:
                ini_data[each_section][key] = config[each_section][key]
        return ini_data


