import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import threading
import time

#Threading
class MainpageThread():
    def create_thread(self, function):
        """For creating a thread"""
        t = threading.Thread(target=function)
        t.setDaemon(True)
        t.start()
        
    def addprogress(self):
        """Updating progress when a valid record is added"""
        for i in range(0, 20):
            self.add_progress['value'] += 5
            self.mainpage.update_idletasks()
            time.sleep(0.5)
                        
        msg.showinfo('', 'Record sucessfully added')
        self.mainpage.update_idletasks()
        self.add_progress['value'] = 0
        for entry in self.add_entries:
            entry.config(state='normal')
