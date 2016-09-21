#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import tkFont

import subprocess

def myclick():
    word = entry.get()
    if not word:
        print("No word to translate")
        return
    try:
        result = subprocess.check_output(["./youdao.py", word])
    except subprocess.CalledProcessError, e:
        print "Ping stdout output:\n", e.output

    translate = result.split('\n')
    maxlength = max(translate, key=len)
    outtext.config(height=len(translate))
    outtext.config(width=len(maxlength))
    outtext.config(state=NORMAL)
    outtext.insert(CURRENT, result)
    outtext.config(state=DISABLED)

if __name__ == '__main__':
    root = Tk() 
    root.title("Youdao")

    textfont = tkFont.Font(family="Arial", size=20)
    entry = Entry(root, font=textfont, cursor="arrow")
    outtext = Text(root, height=10, width=40, font=textfont, cursor="arrow")

    button = Button(root, text="Translate", command=myclick)

    entry.focus_set()
    outtext.config(state=DISABLED)
    entry.grid(row=0, column=0)
    button.grid(row=0, column=1)
    outtext.grid(row=1,column=0,columnspan=2)
    root.mainloop()
