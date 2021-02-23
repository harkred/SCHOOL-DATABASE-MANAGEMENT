import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from ttkthemes import ThemedTk, THEMES
import time

class MainpageView():
    
    #For adding data frame
    def add_Frame(self):
        
        #Frame
        self.add_frame = ttk.LabelFrame(self.frame_add, text="Add a student's record")
        self.add_frame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)
        
        #Labels
        labels = [
                'Name: ',
                'Class: ',
                'Phone: ',
                '       D.O.B: \n(yyyy-mm-dd)',
                '       D.O.A: \n(yyyy-mm-dd)'
        ]
        for row, label in enumerate(labels):
            ttk.Label(self.add_frame, text=label).grid(row=row, column=0, padx=10, pady=5)
        
        #Entries
        self.name = ttk.Entry(self.add_frame, width=35)
        self.clas = ttk.Entry(self.add_frame, width=35)
        self.phone = ttk.Entry(self.add_frame, width=35)
        self.dob = ttk.Entry(self.add_frame, width=35)
        self.doa = ttk.Entry(self.add_frame, width=35)
        entries = [
                self.name,
                self.clas,
                self.phone,
                self.dob,
                self.doa
        ]
        
        #Entry shoving
        for row, entry in enumerate(entries):
            entry.grid(row=row, column=1, columnspan=2, padx=10, pady=10)
            
        #Button for submiting
        self.submit = ttk.Button(self.add_frame, text='Submit')
        self.submit.grid(column=1, padx=10, pady=10)
        
        #Progressbar
        self.add_progress = ttk.Progressbar(self.add_frame, length=300)
        self.add_progress.grid(column=0, columnspan=3, padx=10, pady=10)
    
    #For searching data frame
    def search_Frame(self):
        
        #Search frame
        self.search_frame = ttk.LabelFrame(self.frame_search, text="Search a student's record")
        self.search_frame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)
        
        #Search By what combobox
        category = ['Id', 'Name', 'Phone']
        self.bywat_combo = ttk.Combobox(self.search_frame, values=category, width=7)
        self.bywat_combo.current(1)
        self.bywat_combo.grid(row=0, column=0, padx=5, pady=10)
        
        #Search entry
        self.srch = ttk.Entry(self.search_frame, width=35)
        self.srch.grid(row=0, column=1, padx=5, pady=10)
        
        #Search button
        self.srch_btn = ttk.Button(self.search_frame, text='Search')
        self.srch_btn.grid(row=0, column=2, padx=5, pady=10)
        
        #ScrolledText for showing data
        self.data = scrolledtext.ScrolledText(self.search_frame, width=35, height=12, wrap=tk.WORD)
        self.data.grid(row=1, column=0, columnspan=3, padx=5, pady=10)
        
        #Search progressbasr
        self.search_progress = ttk.Progressbar(self.search_frame, length=300)
        self.search_progress.grid(row=2, column=0, columnspan=3, padx=5, pady=10)
        
    #For setting theme frame
    def theme_Frame(self):
        
        #Theme frame 
        self.theme_frame = ttk.LabelFrame(self.frame_theme, text='Choose theme')
        self.theme_frame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)
        
        #Combobox to choose themes from
        self.theme_combo = ttk.Combobox(self.theme_frame, values=THEMES, width=35)
        self.theme_combo.pack(padx=10, pady=10)
        self.theme_combo.bind('<<ComboboxSelected>>', lambda event:self.mainpage.set_theme(self.theme_combo.get()))
        
        #Theme progressbar
        self.theme_progress = ttk.Progressbar(self.theme_frame, length=300)
        self.theme_progress.pack(padx=10, pady=10)


#Main
class MainPage(MainpageView):
    def __init__(self):
        #Window with main frame
        self.mainpage = ThemedTk()
        self.mainpage.resizable(0,0)
        self.mainframe = ttk.LabelFrame(self.mainpage)
        self.mainframe.pack(fill=tk.BOTH, expand=1)
        
        #Notebook
        self.notebook = ttk.Notebook(self.mainframe)
        self.notebook.pack(side='left', anchor=tk.N)

    #For adding notebooks
    def add_notebooks(self):
    
        #Adding record frame
        self.frame_add = ttk.Frame(self.mainframe)
        self.notebook.add(self.frame_add, text='Add record')
        super().add_Frame()
        
        #Searching record frame
        self.frame_search = ttk.Frame(self.mainframe)
        self.notebook.add(self.frame_search, text='Search record')
        super().search_Frame()
        
        #Editing record frame
        self.frame_edit = ttk.Frame(self.mainframe)
        self.notebook.add(self.frame_edit, text='Edit record')
        
        #Deleting record frame
        self.frame_delete = ttk.Frame(self.mainframe)
        self.notebook.add(self.frame_delete, text='Delete record')
        
        #Setting theme frame
        self.frame_theme = ttk.Frame(self.mainframe)
        self.notebook.add(self.frame_theme, text='Select theme')
        super().theme_Frame()