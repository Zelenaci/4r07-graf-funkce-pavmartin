# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:32:46 2019

@author: Martin
"""

import pylab as p
import tkinter as tk
from tkinter import Label, Radiobutton, IntVar, Entry, LabelFrame, Message, \
                    StringVar, Button, messagebox, filedialog

class Application(tk.Tk):
    name = 'Graf funkce'
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.config(borderwidth=5)
        
        self.grflblfr = LabelFrame(self,text="Udělat graf funkce", padx=20, pady=1)
        self.grflblfr.grid(row=1,column=1)
        
        self.fcelbl = Label(self.grflblfr)
        self.fcelbl.grid(row=1, column=1)
        
        self.v = IntVar()
        
        self.sinrdb = Radiobutton(self.fcelbl,text="sin",variable=self.v, value=1)
        self.sinrdb.grid(row=1, column=1)
        
        self.logrdb = Radiobutton(self.fcelbl,text="log",variable=self.v, value=2)
        self.logrdb.grid(row=2, column=1) 
        
        self.exprdb = Radiobutton(self.fcelbl,text="exp",variable=self.v, value=3)
        self.exprdb.grid(row=3, column=1)
        
        self.oddolbl = Label(self.grflblfr)
        self.oddolbl.grid(row=1, column=2)
        
        self.odmess = Message(self.oddolbl, text="Od:")
        self.odmess.grid(row=1, column=1)
        
        self.sod = StringVar()
        
        self.odentr = Entry(self.oddolbl, textvariable=self.sod,width=10)
        self.odentr.grid(row=1, column=2)
        
        self.domess = Message(self.oddolbl, text="Do:")
        self.domess.grid(row=2, column=1)
        
        self.sdo = StringVar()
        
        self.doentr = Entry(self.oddolbl, textvariable=self.sdo,width=10)
        self.doentr.grid(row=2, column=2)
        
        self.vg = Button(self,text="Udělat graf", width=9, height=2, command=self.udelejgraf)
        self.vg.grid(row=2, column=1)
        
        self.grftxtlblfr = LabelFrame(self,text="Udělat graf z textových dat", \
                                      padx=20, pady=18)
        self.grftxtlblfr.grid(row=1, column=2)
        
        self.a = StringVar()
        self.a.set("")
        
        self.csentr = Entry(self.grftxtlblfr, textvariable=self.a)
        self.csentr.grid(row=1, column=1)
        
        self.vgs = Button(self.grftxtlblfr,text="Vybrat soubor", \
                          command=self.vybersoubor)
        self.vgs.grid(row=2, column=1)
        
        self.vgb = Button(self,text="Udělat graf\n ze souboru", \
                          width=9, height=2, command=self.udelejgrafzesouboru)
        self.vgb.grid(row=2, column=2)
        
        self.osylblfr = LabelFrame(self,text="Názvy os:", padx=20)
        self.osylblfr.grid(row=3, column=1, columnspan=2)
        
        self.osxmess = Message(self.osylblfr, text="Osa x:")
        self.osxmess.grid(row=1, column=1)
        
        self.osx = StringVar()

        self.osxentr = Entry(self.osylblfr, textvariable=self.osx, width=10)
        self.osxentr.grid(row=1, column=2)

        self.osymess = Message(self.osylblfr, text="Osa y:")
        self.osymess.grid(row=2, column=1)

        self.osy = StringVar()

        self.osyentr = Entry(self.osylblfr, textvariable=self.osy, width=10)
        self.osyentr.grid(row=2, column=2)

    def udelejgraf(self):
        try:
            od = float(self.sod.get())
            do = float(self.sdo.get())
            x = p.linspace(od, do, 500)
            if self.v.get() == 1:
                y=p.sin(x)
            elif self.v.get() == 2:
                y=p.log10(x)
            elif self.v.get() == 3:
                y=p.exp(x)
            p.figure()
            p.plot(x,y)
            p.xlabel(self.osx.get())
            p.ylabel(self.osy.get())
            p.grid(True)
            p.show()
        except:
            messagebox.showerror(title='Chybné meze', \
                                 message='Zadejte meze osy X\n jako reálná čísla')        

    def vybersoubor(self):
        cesta= filedialog.askopenfilename(title='Vyberte soubor')    
        if cesta != '':
            self.a.set(cesta)

    def udelejgrafzesouboru(self):
        try:
            cesta = self.a.get()
            f = open(cesta,'r')
            x=[]
            y=[]
            while 1:
                radek=f.readline()
                if radek == '':
                    break
                cisla=radek.split()
                x.append(float(cisla[0]) )
                y.append(float(cisla[1]) )
            f.close()
            p.figure()
            p.plot(x,y)
            p.xlabel(self.osx.get())
            p.ylabel(self.osy.get())
            p.grid(True)
            p.show()
        except:
            messagebox.showerror(title='Chybný formát souboru', \
                                 message='Graf se nepodařilo vytvořit,\n zkontrolujte formát souboru!')

app = Application()
app.mainloop()
