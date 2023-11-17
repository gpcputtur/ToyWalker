""" Globals class for using certain variable globally with single instance
    date Created : 16-Nov-2023
    @Author      : Ganesh Prasad, <gpc.puttur@gmail.com>
"""


class Globals():
    """ The class to hold certain global variables and objects across the framework.
        Some of the configuration values at framework and test level would be set at run time and
        availabel to use throughtout the framework and test layers
    """

    log_level = True

    def __init__(self):
        None
