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
