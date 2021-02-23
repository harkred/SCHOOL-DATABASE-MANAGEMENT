import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk, THEMES

class MainPage():
    def __init__(self):
        #Window with main frame
        self.mainpage = ThemedTk()
        self.mainpage.resizable(0,0)
        self.mainframe = ttk.LabelFrame(self.mainpage)
        self.mainframe.pack(fill=tk.BOTH, expand=1)
        
        #Notebook
        self.notebook = ttk.Notebook(self.mainframe)
        self.notebook.pack(side='left', anchor=tk.N)

    def add_notebooks(self):
        #Adding record frame
        self.frame_add = ttk.Frame(self.mainframe)
        self.notebook.add(self.frame_add, text='Add record')
        
        #Searching record frame
        self.frame_search = ttk.Frame(self.mainframe)
        self.notebook.add(self.frame_search, text='Search record')
        
        #Editing record frame
        self.frame_edit = ttk.Frame(self.mainframe)
        self.notebook.add(self.frame_edit, text='Edit record')
        
        #Deleting record frame
        self.frame_delete = ttk.Frame(self.mainframe)
        self.notebook.add(self.frame_delete, text='Delete record')
        
        #Setting theme frame
        self.frame_theme = ttk.Frame(self.mainframe)
        self.notebook.add(self.frame_theme, text='Select theme')
        self.theme_frame()
    
    #For setting theme frame
    def theme_frame(self):
        #Setting theme
        def choosetheme(event):
            self.mainpage.set_theme(self.theme_combo.get())
        
        #Frames and combobox to choose theme
        self.theme_frame = ttk.LabelFrame(self.frame_theme, text='Choose theme')
        self.theme_combo = ttk.Combobox(self.frame_theme, values=THEMES, width=35)
        self.theme_combo.pack(padx=10, pady=10)
        self.theme_combo.bind('<<ComboboxSelected>>', choosetheme)    