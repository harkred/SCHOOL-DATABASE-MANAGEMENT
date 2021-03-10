import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import threading
import time

#Threading
class MainpageThread():
    def create_thread(self, function, _args):
        """For creating a thread"""
        t = threading.Thread(target=function, args=_args)
        t.setDaemon(True)
        t.start()

    def addprogress_thread(self):
        """Updating progress when a valid record is added"""
        for _ in range(0, 20):
            self.add_progress['value'] += 5
            self.mainpage.update_idletasks()
            time.sleep(0.5)
                        
        msg.showinfo('', 'Record sucessfully added')
        self.mainpage.update_idletasks()
        self.add_progress['value'] = 0
        
        for entry in self.add_entries:
            entry.config(state='normal')
            
    def searchprogress_thread(self, datas):
        """Updating progress when a record is searched"""
        for _ in range(0, 2):
            self.search_progress['value'] += 50
            self.mainpage.update_idletasks()
            time.sleep(1)
            
        msg.showinfo('', 'Student data found')
        self.mainpage.update_idletasks()
        self.search_progress['value'] = 0
        
        for data in datas:
            self.data_lst.insert(tk.END, f'Id: {str(data[0])}')
            self.data_lst.insert(tk.END, f'Name: {str(data[1])}')
            self.data_lst.insert(tk.END, f'Class: {str(data[2])}')
            self.data_lst.insert(tk.END, f'Phone: {str(data[3])}')
            self.data_lst.insert(tk.END, f'DOB: {str(data[4])}')
            self.data_lst.insert(tk.END, f'DOA: {str(data[5])}')
            self.data_lst.insert(tk.END, '')

    def editsrchprogress_thread1(self, datas):
        """Updating progress when a record is searched for editin"""
        for _ in range(0, 2):
            self.edit_search_progress['value'] += 50
            self.mainpage.update_idletasks()
            time.sleep(0.5)
        
        self.edit_srch.delete(0, tk.END)
        msg.showinfo('', 'Student data found')
        
        self.edit_search_progress['value'] = 0
        
        for data in datas:
            self.edit_entries[datas.index(data)].config(state='normal')
            self.edit_entries[datas.index(data)].insert(0, data)
            
        self.edit.config(state='enabled')
        
    def editsrchprogress_thread2(self, datas):
        """Updating progress when a record is searched for editin"""
        
        def choose_record(datas):
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
                    self.edit.config(state='enabled')
            
            #Choosing the record
            choose_rec = tk.Tk()
            choose_rec.resizable(0,0)
            choose_rec.title('Choose a record to edit by double clicking it')
            
            screen_width = choose_rec.winfo_screenwidth()
            screen_height = choose_rec.winfo_screenheight()
            
            choose_rec.geometry(f'+{screen_width//4}+{screen_height//4}')
            
            #Listbox 
            choose_lst = tk.Listbox(choose_rec, width=100)
            choose_lst.grid(row=0, column=0)
            choose_lst.bind('<Double 1>', data_selected)
                
            scrol = ttk.Scrollbar(choose_rec, command=choose_lst.yview)
            scrol.grid(row=0, column=1, sticky=tk.W)
                
            choose_lst.config(yscrollcommand=scrol.set)
            
            for data in datas:
                choose_lst.insert(tk.END, f'{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}, ')
            
            choose_rec.mainloop()
        
        for _ in range(0, 2):
            self.edit_search_progress['value'] += 50
            self.mainpage.update_idletasks()
            time.sleep(0.5)
        
        msg.showinfo('', 'More than 1 student reord found, choose on to edit')
        self.edit_search_progress['value'] = 0
        choose_record(datas)
        
    def editprogress_thread(self):
        """Updating progress when a record edited"""
        for entry in self.edit_entries:
            entry.config(state='readonly')
            
        self.edit.config(state='disabled')
        for _ in range(0, 5):
            self.edit_search_progress['value'] += 20
            self.mainpage.update_idletasks()
            time.sleep(0.5)
            
        msg.showinfo('', 'Data sucessfully edited')
        
        for entry in self.edit_entries:
            entry.config(state='normal')
        
        self.clear_entries(self.edit_entries)
        self.edit_search_progress['value'] = 0
        
        for entry in self.edit_entries:
            entry.config(state='readonly')