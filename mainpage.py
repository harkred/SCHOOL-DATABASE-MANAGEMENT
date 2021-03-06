import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk, THEMES
from mainpage_views import MainpageView

#Main body
class MainPage(MainpageView):

    def __init__(self):
        """Window with main frame"""
        self.mainpage = ThemedTk()
        
        screen_width = self.mainpage.winfo_screenwidth()
        screen_height = self.mainpage.winfo_screenheight()
        
        self.mainpage.geometry(f'+{screen_width//4}+{screen_height//4}')
        
        self.mainpage.resizable(0,0)
        self.mainframe = ttk.LabelFrame(self.mainpage)
        self.mainframe.pack(fill=tk.BOTH, expand=1)
        
        #Notebook
        self.notebook = ttk.Notebook(self.mainframe)
        self.notebook.pack(side='left', anchor=tk.N)


    def add_notebooks(self):
        """For adding notebooks"""
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
        super().edit_Frame()
        
        #Deleting record frame
        self.frame_delete = ttk.Frame(self.mainframe)
        self.notebook.add(self.frame_delete, text='Delete record')
        super().delete_Frame()
        
        #Setting theme frame
        self.frame_theme = ttk.Frame(self.mainframe)
        self.notebook.add(self.frame_theme, text='Select theme')
        super().theme_Frame()