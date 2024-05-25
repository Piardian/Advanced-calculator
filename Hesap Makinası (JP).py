import tkinter as tk
from tkinter import *

# Küresel değişkenler
hesap = ''
s1 = 0
yuzde = False

def yaz(x):
    s = len(giris.get())
    giris.insert(s, str(x))

def islemler(x):
    global hesap
    global s1
    global yuzde
    if x in "+-*/":
        hesap = x
        try:
            s1 = float(giris.get())
        except ValueError:
            giris.delete(0, 'end')
            giris.insert(0, "Hata")
            return
        giris.delete(0, 'end')
    elif x == "%":
        yuzde = True
        try:
            s1 = float(giris.get())
        except ValueError:
            giris.delete(0, 'end')
            giris.insert(0, "Hata")
            return
        giris.delete(0, 'end')
    else:
        giris.insert(END, x)

def hesapla():
    global s1
    global yuzde
    try:
        if yuzde:
            yuzde_degeri = float(giris.get())
            sonuc = (yuzde_degeri / 100) * s1
            yuzde = False
        else:
            s2 = float(giris.get())
            if hesap == '+':
                sonuc = s1 + s2
            elif hesap == '-':
                sonuc = s1 - s2
            elif hesap == '/':
                if s2 != 0:
                    sonuc = s1 / s2
                else:
                    giris.delete(0, 'end')
                    giris.insert(0, "Hata: Sıfıra bölme")
                    return
            elif hesap == '*':
                sonuc = s1 * s2

        sonuc_str = str(sonuc)
        if sonuc % 1 == 0:
            sonuc_str = str(int(sonuc))

        giris.delete(0, 'end')
        giris.insert(0, sonuc_str)
    except ValueError:
        giris.delete(0, 'end')
        giris.insert(0, "Hata")

def sil():
    giris.delete(len(giris.get()) - 1)

def temizle():
    giris.delete(0, 'end')

window = Tk()
window.title('Hesap Makinası')
window.geometry("300x400")
window.configure(background='black')
window.resizable(width=False, height=False)

giris = tk.Entry(window, width=29, bd=4, justify=RIGHT, font=("Helvetica", 16))
giris.place(height=60, width=275, x=13, y=20)

Button(window, width=4, text="x", fg="black", font=("Helvetica", 16), background='white', command=lambda: islemler("*")).place(x=160, y=100)
Button(window, width=4, text="/", fg="black", font=("Helvetica", 16), background='white', command=lambda: islemler("/")).place(x=90, y=100)
Button(window, width=4, text="C", fg="black", font=("Helvetica", 16), background='white', command=temizle).place(x=230, y=100)
Button(window, width=4, text="%", fg="black", font=("Helvetica", 16), background='white', command=lambda: islemler("%")).place(x=20, y=100)
Button(window, width=4, text="1", fg="black", font=("Helvetica", 16), background='white', command=lambda: yaz(1)).place(x=20, y=160)
Button(window, width=4, text="2", fg="black", font=("Helvetica", 16), background='white', command=lambda: yaz(2)).place(x=90, y=160)
Button(window, width=4, text="3", fg="black", font=("Helvetica", 16), background='white', command=lambda: yaz(3)).place(x=160, y=160)
Button(window, width=4, text="4", fg="black", font=("Helvetica", 16), background='white', command=lambda: yaz(4)).place(x=20, y=220)
Button(window, width=4, text="5", fg="black", font=("Helvetica", 16), background='white', command=lambda: yaz(5)).place(x=90, y=220)
Button(window, width=4, text="6", fg="black", font=("Helvetica", 16), background='white', command=lambda: yaz(6)).place(x=160, y=220)
Button(window, width=4, text="7", fg="black", font=("Helvetica", 16), background='white', command=lambda: yaz(7)).place(x=20, y=280)
Button(window, width=4, text="8", fg="black", font=("Helvetica", 16), background='white', command=lambda: yaz(8)).place(x=90, y=280)
Button(window, width=4, text="9", fg="black", font=("Helvetica", 16), background='white', command=lambda: yaz(9)).place(x=160, y=280)
Button(window, width=4, text=".", fg="black", font=("Helvetica", 16), background='white', command=lambda: yaz(".")).place(x=160, y=340)
Button(window, width=4, text="=", fg="black", font=("Helvetica", 16), background='white', command=hesapla).place(x=230, y=340)
Button(window, width=10, text="0", fg="black", font=("Helvetica", 16), background='white', command=lambda: yaz(0)).place(height=40, x=20, y=340)
Button(window, width=4, text="+", fg="black", font=("Helvetica", 16), background='white', command=lambda: islemler("+")).place(x=230, y=280)
Button(window, width=4, text="-", fg="black", font=("Helvetica", 16), background='white', command=lambda: islemler("-")).place(x=230, y=220)
Button(window, width=4, text="⌫", fg="black", font=("Helvetica", 16), background='white', command=sil).place(x=230, y=160)

# Klavye bağlamaları
window.bind("<Return>", lambda event: hesapla())
window.bind("<KP_Divide>", lambda event: islemler("/"))
window.bind("<KP_Multiply>", lambda event: islemler("*"))
window.bind("<KP_Subtract>", lambda event: islemler("-"))
window.bind("<KP_Add>", lambda event: islemler("+"))
window.bind("<percent>", lambda event: islemler("%"))
window.bind("<KP_Enter>", lambda event: hesapla())
window.bind("<Key>", lambda event: klavye_islemleri(event))

def klavye_islemleri(event):
    if event.char in '0123456789':
        yaz(event.char)
    elif event.char in '+-*/%':
        islemler(event.char)
    elif event.char == '\r':
        hesapla()
    elif event.char == '.':
        yaz('.')

window.mainloop()
