import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from mysql_commands import execute_cmd
from mainpage_thread import MainpageThread

#Backend
class MainpageBackend(MainpageThread):
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
            if values[2].isdigit():

                try:
                    execute_cmd("""
                        INSERT INTO student_data(Name, Class, Phone, DOB, DOA)
                        VALUES(%s, %s, %s, %s, %s)
                """, values, 'school') #Adds valid record
                    self.clear_entries(self.add_entries)
                    
                    for entry in self.add_entries:
                        entry.config(state='readonly')
                    
                    #Threading
                    self.create_thread(self.addprogress_thread, [])
                    
                except Exception as e: msg.showerror('', 'Please fill dates in the designated')
            else: msg.showerror('', 'Please fill the phone number properly')
            
    def search_record(self):
        """For searching from the database"""
        datas = execute_cmd("""
                SELECT * FROM student_data WHERE {} = %s
        """.format(self.bywat_combo.get()), values=(self.srch.get(),), database='school')
        
        self.srch.delete(0, tk.END)
        
        try: self.data_lst.delete(0, tk.END)
        except Exception as e: pass
        
        if len(datas) == 0: msg.showerror('', 'Student data not found')
        
        elif len(datas) > 0:
            #Threading
            self.create_thread(self.searchprogress_thread, [datas])
        
    def edit_search_record(self):
        """Searching from the database for editing"""
        
        try: self.clear_entries(self.edit_entries)
        except Exception as e: pass
        
        datas = execute_cmd("""
                SELECT * FROM student_data WHERE {} = %s
        """.format(self.edit_bywat_combo.get()), values=(self.edit_srch.get(),), database='school')
        
        
        if len(datas) == 0:
            self.edit_srch.delete(0, tk.END)
            msg.showerror('', 'Student data not found')
            self.clear_entries(self.edit_entries)
            self.edit.config(state='disabled')
        
        #Data editin when only 1 result is fetched
        elif len(datas) == 1:
            datas = list(datas[0])
            self.sid = datas.pop(0)
            self.create_thread(self.editsrchprogress_thread1, [datas])
        
        #Data editin when more than 1 data is fetched
        elif len(datas) > 1:
            self.edit_srch.delete(0, tk.END)
            self.create_thread(self.editsrchprogress_thread2, [datas])

    def edit_record(self):
        """For changing the records"""
        values = []
        
        for entry in self.edit_entries: 
            if entry.get() == '': #Makes sure dat entries are not black
                msg.showerror('', 'Please fill the data appropriately')
                break
            else: values.append(entry.get()) #Entries are appended to values so dat it can be stored to the database
        values.append(self.sid)
        values = tuple(values)
        
        values = tuple(map(lambda x:x.strip(), values))
        
        if values[2].isdigit():
            try:
                execute_cmd("""
                        UPDATE student_data
                        SET 
                            Name = %s,
                            Class = %s,
                            Phone = %s,
                            DOB = %s,
                            DOA = %s
                        WHERE id = %s
                """, values, database='school')
                
                self.create_thread(self.editprogress_thread, [])
                
            except Exception as e: msg.showerror('', 'Please fill dates in the designated')

        else: msg.showerror('', 'Please fill the phone number properly')
        
    def del_search_record(self):
        """For searching a record to  delete"""
        
        try: self.del_lst.delete(0, tk.END)
        except Exception as e: pass
        
        datas = execute_cmd("""
                SELECT * FROM student_data WHERE {} = %s
        """.format(self.del_bywat_combo.get()), values=(self.del_srch.get(),), database='school')
        
        self.del_srch.delete(0, tk.END)
        
        if len(datas) == 0: msg.showerror('', 'Student data not found')
        
        else:
            self.create_thread(self.delsrchprogress_thread, [datas])
    
    def del_record(self, event):
        """For deleting the selected record"""

        execute_cmd("""
                DELETE FROM student_data WHERE id = %s
        """, values=(self.del_lst.get(tk.ANCHOR)[0],), database='school')
        
        self.create_thread(self.delprogress_thread, [])