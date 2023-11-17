
""" The implementation of class and method for report Generation of TOWTA execution
    
    date Created : 16-Nov-2023
    @Author      : Ganesh Prasad, <gpc.puttur@gmail.com>
"""

import os, sys

from library import template


row_temp = template.test_case_row


class ReportGenerator():
    """ The method 'ReportGenerator' will implement the required methods for the generation of TOWTA execution report.
        The report will get refreshed at the end of every test execution to update the result of current test execution.
    """

    def __init__(self):

        reporter_path = os.path.join(os.path.dirname(os.getcwd()), "reports")
        self.reporter_path = os.path.join(reporter_path, "reports")
        self.si_num = 0
        self.all_test_data = ""
        

    def __get_test_si_num(self):
        self.si_num+=1
        return self.si_num


    def generate_report(self, test_details):
        """ The method 'generate_report()' adds the test execution results of each test execution when it is called.
            Args : test_details - Result of each test execution to be updated to the report.
            Returns : None
        """
        if test_details['status']==True:
            status_cell_color = "#52BE80"
            status_string = "PASS"
        else:
            status_cell_color = "#FF0000"
            status_string = "FAIL"
        self.all_test_data+=row_temp%(str(self.__get_test_si_num()), test_details['test_id'], test_details['suite_name'], test_details['test_name'], test_details['steps'],
                                test_details['expected_res'], test_details['actual_res'], status_cell_color, status_string, test_details['exe_time'],
                                test_details['screenshots'], test_details['screenshots'])

        rep_data = template.html_first_part+template.html_last_part+self.all_test_data+template.html_end
                
        f = open (os.path.join(self.reporter_path, "report.html"), 'w')
        f.write(rep_data)
        f.close()


if __name__=="__main__":
    rep = ReportGenerator()        
    


        

    








