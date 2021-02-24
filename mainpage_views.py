import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from ttkthemes import ThemedTk, THEMES
from mainpage_backend import MainpageBackend

#Views
class MainpageView(MainpageBackend):
    
    def add_Frame(self):
        """For adding data frame"""
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
        self.add_name = ttk.Entry(self.add_frame, width=35)
        self.add_clas = ttk.Entry(self.add_frame, width=35)
        self.add_phone = ttk.Entry(self.add_frame, width=35)
        self.add_dob = ttk.Entry(self.add_frame, width=35)
        self.add_doa = ttk.Entry(self.add_frame, width=35)
        self.add_entries = [
                self.add_name,
                self.add_clas,
                self.add_phone,
                self.add_dob,
                self.add_doa
        ]
        
        #Entry shoving
        for row, entry in enumerate(self.add_entries):
            entry.grid(row=row, column=1, columnspan=2, padx=10, pady=10)
            
        #Button for submiting
        self.submit = ttk.Button(self.add_frame, text='Submit', command=self.add_data)
        self.submit.grid(column=1, padx=10, pady=10)
        
        #Progressbar
        self.add_progress = ttk.Progressbar(self.add_frame, length=400)
        self.add_progress.grid(column=0, columnspan=3, padx=20, pady=20)
    
    def search_Frame(self):
        """For searching data frame"""
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
        self.srch.focus()
        
        #Search button
        self.srch_btn = ttk.Button(self.search_frame, text='Search')
        self.srch_btn.grid(row=0, column=2, padx=5, pady=10)
        
        #ScrolledText for showing data
        self.data = scrolledtext.ScrolledText(self.search_frame, width=50, height=15, wrap=tk.WORD)
        self.data.grid(row=1, column=0, columnspan=3, padx=5, pady=10)
        self.data.config(state='disabled')
        
        #Search progressbasr
        self.search_progress = ttk.Progressbar(self.search_frame, length=400)
        self.search_progress.grid(row=2, column=0, columnspan=3, padx=5, pady=10)
        
    
    def edit_Frame(self):
        """For editing record frame"""
        #Editing frame
        self.edit_frame = ttk.LabelFrame(self.frame_edit, text="Search a student's data to edit")
        self.edit_frame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)
        
        #Search By what combobox
        category = ['Id', 'Name', 'Phone']
        self.edit_bywat_combo = ttk.Combobox(self.edit_frame, values=category, width=7)
        self.edit_bywat_combo.current(1)
        self.edit_bywat_combo.grid(row=0, column=0, padx=5, pady=10)
        
        #Search entry
        self.edit_srch = ttk.Entry(self.edit_frame, width=35)
        self.edit_srch.grid(row=0, column=1, padx=5, pady=10)
        self.edit_srch.focus()
        
        #Search button
        self.edit_srch_btn = ttk.Button(self.edit_frame, text='Search')
        self.edit_srch_btn.grid(row=0, column=2, padx=5, pady=10)
        
        #Labels
        labels = [
                'Name: ',
                'Class: ',
                'Phone: ',
                '       D.O.B: \n(yyyy-mm-dd)',
                '       D.O.A: \n(yyyy-mm-dd)'
        ]
        for row, label in enumerate(labels):
            ttk.Label(self.edit_frame, text=label).grid(row=row+1, column=0, padx=10, pady=5)
        
        #Entries
        self.name = ttk.Entry(self.edit_frame, width=35)
        self.clas = ttk.Entry(self.edit_frame, width=35)
        self.phone = ttk.Entry(self.edit_frame, width=35)
        self.dob = ttk.Entry(self.edit_frame, width=35)
        self.doa = ttk.Entry(self.edit_frame, width=35)
        entries = [
                self.name,
                self.clas,
                self.phone,
                self.dob,
                self.doa
        ]
        
        #Entry shoving
        for row, entry in enumerate(entries):
            entry.grid(row=row+1, column=1, columnspan=2, padx=10, pady=10)
            entry.config(state='readonly')
            
        #Button for editing
        self.submit = ttk.Button(self.edit_frame, text='Edit')
        self.submit.grid(column=1, padx=10, pady=10)
        
        #Search/Edit progressbasr
        self.edit_search_progress = ttk.Progressbar(self.edit_frame, length=400)
        self.edit_search_progress.grid(column=0, columnspan=3, padx=5, pady=10)
    
    def delete_Frame(self):
        """For deleting record frame"""
        #Delete frame
        self.delete_frame = ttk.LabelFrame(self.frame_delete, text='Delete a record')
        self.delete_frame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)

        #Search By what combobox
        category = ['Id', 'Name', 'Phone']
        self.del_bywat_combo = ttk.Combobox(self.delete_frame, values=category, width=8)
        self.del_bywat_combo.current(1)
        self.del_bywat_combo.grid(row=0, column=0, padx=10, pady=10)
        
        #Search entry
        self.del_srch = ttk.Entry(self.delete_frame, width=35)
        self.del_srch.grid(row=0, column=1, padx=10, pady=10)
        self.del_srch.focus()
        
        #Delte item lstbox
        self.del_lst = tk.Listbox(self.delete_frame, width=70, height=15)
        self.del_lst.grid(row=1, column=0, columnspan=3, sticky=tk.E)
        
        self.del_lst_scroll = ttk.Scrollbar(self.delete_frame, command=self.del_lst.yview)
        self.del_lst_scroll.grid(row=1, column=3, sticky=tk.W, ipady=95)
        
        self.del_lst.config(yscrollcommand=self.del_lst_scroll.set)
        
        #Search button
        self.del_srch_btn = ttk.Button(self.delete_frame, text='Search')
        self.del_srch_btn.grid(row=0, column=2, padx=10, pady=10)
        
        #Delete progressbasr
        self.delete_progress = ttk.Progressbar(self.delete_frame, length=400)
        self.delete_progress.grid(row=2, column=0, columnspan=3, padx=5, pady=10)
        
    def theme_Frame(self):
        """For setting theme frame"""
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