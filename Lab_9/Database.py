#******************************************************************************
# Author:           Khanh Vu
# Lab:              Lab_9: GUI & Database use in Python
# Date:             03.04.2022, 03.07.2022, 03.10.2022, 03.11.2022
# Description:      The Database class is stored in a module named Database (Database.py). This code defines two class
#                   methods called readNames() and connect().
#                   - The method connect() makes a connection to the NAMES database.
#                   - The readNames() fetch name data from the Database based on filtered criteria. This method calls
#                   cls.connect() and takes two parameters: gender, and year which are used to filter the results.
#                   It contains the SQL query where the  two parameters are passed to the WHERE clause(use parameter
#                   binding. When called, the method return a list  of Name objects that match the criteria.
# Sources:          Prof. Marc Goodman's Youtube Channel - 133Y IMDB browser Program
#                   Murach's Python Programming - Beginner... Chapter 14_ How to define and use your own classes
#                   Murach's Python Programming - Beginner... Chapter 16_ Database
#                   CIS-133Y- Python Programming I Lecture Notes - Module 6: OOP
#                   CIS-133Y- Python Programming I Lecture Notes - Module 7: Database Development
#                   Lab 9 specification

#******************************************************************************

import pyodbc

class Database:
    __connection = None    # Class note: a property associated with the class and shared across all Database methods

    # Create a class method to make a connection the NAMES Database
    @classmethod
    def connect(cls):
        if cls.__connection is None:
            server = 'xxx'
            database = 'NAMES'
            username = 'xxx'
            password = 'xxx'
            cls.__connection = pyodbc.connect(                'DRIVER={SQL Server};SERVER=' + server
                + ';DATABASE=' + database
                + ';UID=' + username + ';PWD=' + password
            )

    # Create a class method to fetch data from a database
    @classmethod
    def readNames(cls, name, gender):
        # Call the connect(cls)
        cls.connect()

        # Open a cursor
        myCursor = cls.__connection.cursor()

        # sql query to fetch data
        sql = """
        SELECT N.Name
        ,YGT.Year
        , YGT.Gender               
        , NC.NameCount
        , YGT.Total
        
        FROM    names N LEFT JOIN name_counts NC
                ON N.NameID = NC.FK_NameID
                LEFT JOIN year_gender_totals YGT
                ON NC.FK_YearGenderTotalID = YGT.YearGenderTotalID
                    
        WHERE   LOWER(N.Name) = LOWER(?) AND
                LOWER(YGT.Gender) = LOWER(?)
                
        ORDER BY YGT.Year;

        """
        # Execute the query
        myCursor.execute(sql, name, gender)
        rows = myCursor.fetchall()

        #Create a list that contains name dictionary objects
        nameData = []
        for row in rows:
            nameDict = {"name": row[0], "year": row[1], "gender": row[2], "count": row[3], "total": row[4]}
            nameData.append(nameDict)

        return nameData

    # Create a class method to fetch Genders from a database
    @classmethod
    def readGender(cls):
        from Name import Gender

        # Call the connect(cls)
        cls.connect()

        # Open a cursor
        myCursor = cls.__connection.cursor()

        # sql query to fetch data
        sql = """
            SELECT DISTINCT Gender 
            FROM year_gender_totals
            """
        # Execute the query
        myCursor.execute(sql)
        rows = myCursor.fetchall()

        genders = []

        # Create a list that contains genders
        for row in rows:
            genders.append(Gender(row[0]))
        return genders

