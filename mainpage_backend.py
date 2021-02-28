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
            
    def search_record(self):
        """For searching from the database"""
        datas = execute_cmd("""
                SELECT * FROM student_data WHERE {} = %s
        """.format(self.bywat_combo.get()), values=(self.srch.get(),), database='school')
        
        self.srch.delete(0, tk.END)
        
        try: self.data_lst.delete(0, tk.END)
        except Exception as e: pass
        
        if len(datas) == 0: msg.showerror('', 'Student data not found')
        
        else:
            msg.showinfo('', 'Student data found')
            
            for data in datas:
                self.data_lst.insert(tk.END, f'Id: {str(data[0])}')
                self.data_lst.insert(tk.END, f'Name: {str(data[1])}')
                self.data_lst.insert(tk.END, f'Class: {str(data[2])}')
                self.data_lst.insert(tk.END, f'Phone: {str(data[3])}')
                self.data_lst.insert(tk.END, f'DOB: {str(data[4])}')
                self.data_lst.insert(tk.END, f'DOA: {str(data[5])}')
                self.data_lst.insert(tk.END, '')