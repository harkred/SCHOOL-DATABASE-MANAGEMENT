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
            if values[2].isdigit():
                try:
                    execute_cmd("""
                        INSERT INTO student_data(Name, Class, Phone, DOB, DOA)
                        VALUES(%s, %s, %s, %s, %s)
                """, values, 'school') #Adds valid record
                    msg.showinfo('', 'Record sucessfully added')
                    self.clear_entries(self.add_entries)
                    
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
    
    def edit_search_record(self):
        """Searching from the database for editing"""
        
        try: self.clear_entries(self.edit_entries)
        except Exception as e: pass
        
        def choose_record():
            """If more than one data is fetched, user is prompted to choose which one to edit"""
            
            def data_selected(event):
                """For fetching selected data"""
                #Cleansing the data
                raw_data = choose_lst.get(tk.ANCHOR)
                
                datas = []
                word = ''
                
                for i in range(len(raw_data)):
                    if raw_data[i:i+2] != ', ':
                        word += raw_data[i]
                    
                    elif raw_data[i:i+2] == ', ':
                        datas.append(word)
                        word = ''
                
                #For destroying the window
                choose_rec.destroy()
                
                #For inserting the record
                self.sid = datas.pop(0)
                for data in datas:
                    self.edit_entries[datas.index(data)].config(state='normal')
                    self.edit_entries[datas.index(data)].insert(0, data)
            
            #Choosing the record
            choose_rec = tk.Tk()
            choose_rec.resizable(0,0)
            
            #Listbox 
            choose_lst = tk.Listbox(choose_rec, width=100)
            choose_lst.grid(row=0, column=0)
            choose_lst.bind('<Double 1>', data_selected)
            
            scrol = ttk.Scrollbar(choose_rec, command=choose_lst.yview)
            scrol.grid(row=0, column=1, sticky=tk.W)
            
            choose_lst.config(yscrollcommand=scrol.set)
            
            for data in datas:
                choose_lst.insert(tk.END, f'{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}, ')
        
        datas = execute_cmd("""
                SELECT * FROM student_data WHERE {} = %s
        """.format(self.edit_bywat_combo.get()), values=(self.edit_srch.get(),), database='school')
        
        
        if len(datas) == 0:
            self.edit_srch.delete(0, tk.END)
            msg.showerror('', 'Student data not found')
            self.clear_entries(self.edit_entries)
        
        #Data editin when only 1 result is fetched
        elif len(datas) == 1:
            self.edit_srch.delete(0, tk.END)
            msg.showinfo('', 'Student data found')
            
            datas = list(datas[0])
            self.sid = datas.pop(0)
            
            for data in datas:
                self.edit_entries[datas.index(data)].config(state='normal')
                self.edit_entries[datas.index(data)].insert(0, data)
        
        #Data editin when more than 1 data is fetched
        elif len(datas) > 1:
            self.edit_srch.delete(0, tk.END)
            choose_record()
            
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
                
                msg.showinfo('', 'Data sucessfully edited')
                self.clear_entries(self.edit_entries)
                
                for entry in self.edit_entries:
                    entry.config(state='readonly')
                    
            except Exception as e: msg.showerror('', 'Please fill dates in the designated')
        
        else: msg.showerror('', 'Please fill the phone number properly')