#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import threading
from win10toast import ToastNotifier
from time import sleep
import random
import win32gui
import win32console
START = 1
STOP  = 0
EXIT  = -1

with open(r"bilgi.txt","r+") as f:
    oku = f.readlines()


def islem():
    global looping
    while True:
        if looping == START:
            toast = ToastNotifier()
            toast.show_toast("Bilgi",oku[random.randint(0,len(oku))],duration=int(txt.get()),icon_path=r"pics/meb.ico")
            sleep(7)
        if looping == EXIT:
            break
            
def basla():
    global looping

    looping = START

def dur():
    global looping

    looping = STOP

# --- main ---

looping = STOP

root = Tk()
root.title("AKS/2020-Sayısal İfadeler")
root.geometry("450x200+500+190")

root.iconphoto(False, ImageTk.PhotoImage(Image.open(r"pics/meb.png").resize((86, 30), Image.ANTIALIAS)))
frm = Frame()
lbl = Label(frm,text="AKS-Sayısal İfadeler Uyarı Programı")
lbl.grid(pady=2)
lbl2 = Label(frm,text="Uyarı aralığını giriniz(Saniye)")
lbl2.grid(pady=2)
v = StringVar()
v.set("60")
txt = Entry(frm,width=5,textvariable=v)
txt.grid(pady=2)
btn = Button(frm,text="BAŞLAT",command=basla)
btn.grid(pady=2)
btn2 = Button(frm,text="DURDUR",command=dur)
btn2.grid(pady=2)
btn3 = Button(frm,text="PROGRAMI GİZLE",command=lambda:root.withdraw())
btn3.grid(pady=2)
frm.pack()
statusbar = Label(root,text="#Dikkat! Programı gizlerseniz uyarılar bilgisayar tekrar başlatılıncaya kadar gelecektir.",bd=1,relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)
thread = threading.Thread(target=islem)
thread.daemon = True
thread.start()

root.mainloop()

looping = EXIT