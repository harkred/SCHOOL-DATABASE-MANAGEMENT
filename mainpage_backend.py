import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from mysql_commands import execute_cmd

class MainpageBackend():
    def clear_entries(self, entries):
        """For clearing entries"""
        for entry in entries:
            entry.delete(0, tk.END)
    
    def add_data(self):
        """For adding data to the database"""
        values = []
        
        for entry in self.add_entries: 
            if entry.get() == '': #Makes sure dat entries are not black
                msg.showerror('', 'Please fill the data appropriately')
                break
            else: values.append(entry.get()) #Entries are appended to values so dat it can be stored to the database
        
        else:
            try:
                execute_cmd("""
                    INSERT INTO student_data(Name, Class, Phone, DOB, DOA)
                    VALUES(%s, %s, %s, %s, %s)
            """, values, 'school') #Adds valid record
                msg.showinfo('', 'Record sucessfully added')
                self.clear_entries(self.add_entries)
                
            except Exception as e: msg.showerror('', 'Please fill the data appropriately')