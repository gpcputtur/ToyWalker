""" GUI Implementation for Toy Walker Test Automation Framework (TOWTA).
    This will be the UI available to end users to trigger the tests using TOWTA

    date Created : 16-Nov-2023
    @Author      : Ganesh Prasad, <gpc.puttur@gmail.com>
"""


import wx
import os, sys

from Toywalk import ToyWalkEngine


class TOWTA(wx.Panel):
    """ Class 'TOWTA' implements the Panel for the main GUI for triggering the tests of TOWTA Framework.
    This class is derived from wx.Panel class available in wx module of Python.
    """
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        toy_walk_header = wx.StaticText(self, -1, "TOY WALK Executer", (200, 15))
        toy_walk_header.SetFont(wx.Font(16, wx.DECORATIVE, wx.BOLD, wx.NORMAL))

        framework_base_fold = wx.StaticText(self, -1, "Select the Framework Base Folder", (50, 75))
        framework_base_fold_button = wx.Button(self, wx.ID_ANY, "Browse", (300, 73))
        framework_base_fold_button.Bind(wx.EVT_BUTTON, self.on_framework_base_fold)

        exe_settings_config_lab = wx.StaticText(self, -1, "Select the Execution Settings Config File", (50, 115))
        exe_settings_config_button = wx.Button(self, wx.ID_ANY, "Browse", (300, 113))
        exe_settings_config_button.Bind(wx.EVT_BUTTON, self.on_exe_sett_config)

        test_prof_config_lab = wx.StaticText(self, -1, "Select the Execution Settings Config File", (50, 155))
        test_prof_config_lab_button = wx.Button(self, wx.ID_ANY, "Browse", (300, 153))
        test_prof_config_lab_button.Bind(wx.EVT_BUTTON, self.on_test_prof_config)        

        self.Start_exe = wx.Button(self, wx.ID_ANY, "Trigger", (300, 210))
        self.Start_exe.Bind(wx.EVT_BUTTON, self.start_execution)

        self.download_message = wx.StaticText(self, -1, "Click on 'Trigger' button to Start the Test Execution...", (50, 270))



    def start_execution(self, event):
        """ The method 'start_execution' implements the sequence of actions to be triggered on clicking the 'Trigger' button in TOWTA GUI.
        Args    : event - event from wx triggered on clicking the button
        Returns : None
        """
            
        at = ToyWalkEngine.ATEngineDriver()
        at.execute()


    def on_framework_base_fold(self, event):
        """ The method 'on_framework_base_fold' implements the sequence of actions to be triggered on clicking the 'Browse' button in TOWTA GUI.
            This 'Browse' button will enable the user to select the framework main directory.
            Args    : event - event from wx triggered on clicking the button
            Returns : None
        """

        dialog = wx.DirDialog(None, "Choose a directory:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.base_fold = (dialog.GetPath())
        dialog.Destroy()


    def on_test_prof_config(self, event):
        """ The method 'on_test_prof_config' implements the sequence of actions to be triggered on clicking the 'Browse' button in TOWTA GUI.
            This 'Browse' button will enable the user to select the 'test config' file profile for the current test execution.
            Args    : event - event from wx triggered on clicking the button
            Returns : None
        """

        wildcard = "*.*"
        dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "")
        if dialog.ShowModal() == wx.ID_OK:
            self.test_prof_path = (dialog.GetPath())
        dialog.Destroy()


    """ The method 'on_exe_sett_config' implements the sequence of actions to be triggered on clicking the 'Browse' button in TOWTA GUI.
        This 'Browse' button will enable the user to select the 'execution config' file profile for the current test execution.
        Args    : event - event from wx triggered on clicking the button
        Returns : None
    """
    def on_exe_sett_config(self, event):
        wildcard = "*.*"
        dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "")
        if dialog.ShowModal() == wx.ID_OK:
            self.sett_prof_path = (dialog.GetPath() )
        dialog.Destroy()



class MainFrame(wx.Frame):
    """Class 'MainFrame' implements the GUI of TOTA Framework.
       This class is derived from 'wx.Frame' of wx module.
    """

    def __init__(self):
        wx.Frame.__init__(self, None, size=(600, 400))

        p = wx.Panel(self)

        nb = wx.Notebook(p)

        tab1 = TOWTA(nb)

        nb.AddPage(tab1, "TOY WALK Executer")

        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)



if __name__=="__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()
