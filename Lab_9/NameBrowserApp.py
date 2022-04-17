#******************************************************************************
# Author:           Khanh Vu
# Lab:              Lab_9: UI & Database use in Python
# Date:             03.04.2022, 03.07.2022, 03.10.2022, 03.11.2022
# Description:      The main (main.py) contains the main code of the program. This code includes the UI where user
#                   can select gender and enter a name.
#                   This code imports the Name class from the Name module. The user inputs are used as the search
#                   parameter and use the readNames() method from Name module to fetch the matching Name objects.
# Inputs:           A List of Name objects whose properties are str name, str gender, int year, int count
#                   int year, str gender (user inputs)
# Outputs:          str name, str gender, int year, int count
# Sources:          Prof. Marc Goodman's Youtube Channel - 133Y IMDB browser Program
#                   Murach's Python Programming - Beginner... Chapter 14_ How to define and use your own classes
#                   Murach's Python Programming - Beginner... Chapter 16_ Database
#                   CIS-133Y- Python Programming I Lecture Notes - Module 6: OOP
#                   CIS-133Y- Python Programming I Lecture Notes - Module 7: Database Development
#                   Lab 9 specification

#******************************************************************************

import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
from Name import *


class NamebrowserappApp:

    PROJECT_PATH = pathlib.Path(__file__).parent
    PROJECT_UI = PROJECT_PATH / "nameBrowserApp.ui"

    __builder = None
    __tree = None
    __mainWindow = None
    __genderCombo = None
    __nameEntry = None

    def __init__(self, parent):
        self.initUi(parent)
        self.setupGenderCombo()
        self.setupTree()

    #Show the UI
    def initUi(self, parent):
        self.__builder = builder = pygubu.Builder()
        builder.add_resource_path(NamebrowserappApp.PROJECT_PATH)
        builder.add_from_file(NamebrowserappApp.PROJECT_UI)
        self.__mainWindow = builder.get_object('topFrame', parent)
        builder.connect_callbacks(self)

        # Create properties
        self.__builder = builder
        self.__genderCombo = builder.get_object('genderCombo', parent)
        self.__nameEntry = builder.get_object('nameEntry', parent)
        self.__nameTree = builder.get_object('nameTree', parent)

    # Set up the Name data tree view
    def setupTree(self):
        nameTree = self.__nameTree

        nameTree.configure(columns=(0, 1, 2, 3, 4))  # Create columns for Name data to be populated

        #Add headings for all columns
        nameTree.heading(0, text="Year")
        nameTree.heading(1, text="Name")
        nameTree.heading(2, text="Gender")
        nameTree.heading(3, text="Count")
        nameTree.heading(4, text="Total")

        nameTree.column(0, width=50, anchor=tk.CENTER)
        nameTree.column(1, width=100, anchor=tk.CENTER)
        nameTree.column(2, width=50, anchor=tk.CENTER)
        nameTree.column(3, width=100, anchor=tk.CENTER)
        nameTree.column(4, width=100, anchor=tk.CENTER)

    #Populate the gender list from the Database to the Gender Combo Box
    def setupGenderCombo(self):
        genders = Gender.readGender() # Fetch genders from the Database by calling Gender.readGender() method

        self.__genderCombo['value'] = [i.gender for i in genders] # Set the values for combo box

    # Gender input by user to be selected
    def genderSelected(self, event):
        #print("Gender Changed:", self.__genderCombo.get())   #TEST
        self.fetchNameData()

    # Name input by user to be selected
    def nameEntered(self, event):
        #print("Name Entered: ", self.__nameEntry.get())   #TEST
        self.fetchNameData()

    # Create a tuple that store Name data fetched from the Database
    # Fetch name data from the Database by calling Name.readNames() method. This will be more convenient later
    # when Name data are populated in the tree view.
    def nameDataToTuple(nameData):
        return (nameData.year
                , nameData.name
                , nameData.gender
                , nameData.count
                , nameData.total
                )       #Return a tuple that contains Name data

    def fetchNameData(self):
        # Fetch name Data from the Database. the readNames() method from the Name object return a list of Name objects
        nameData = Name.readNames(self.__nameEntry.get(), self.__genderCombo.get())

        # This code below will clear the old results on the treeview. It helps to display only the most recent results
        # when the inputs change.
        for i in self.__nameTree.get_children():
            self.__nameTree.delete(i)

        #Populate fetched data to the tree view
        for i in nameData:
            self.__nameTree.insert('', 'end', values=NamebrowserappApp.nameDataToTuple(i))

    def run(self):
        self.__mainWindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Name Browser App")
    app = NamebrowserappApp(root)
    app.run()


