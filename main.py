from mainpage import MainPage
from mysql_commands import execute_cmd

#Creating database and table
try:
    execute_cmd('CREATE DATABASE school')#Creates database
    execute_cmd(""" 
        CREATE TABLE student_data
        (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        Name VARCHAR(256),
        Class VARCHAR(10),
        Phone VARCHAR(15),
        DOB DATE,
        DOA DATE)
""", database='school') #Creates table

except Exception as e: pass


#__main__
win = MainPage()
win.add_notebooks()

win.mainpage.mainloop()