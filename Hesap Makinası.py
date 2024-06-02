import tkinter as tk
from tkinter import *
from tkinter import ttk

# Küresel değişkenler
hesap = []
s1 = []
yeni_islem = True
yuzde = False

def yaz(x):
    global yeni_islem
    if yeni_islem:
        giris.delete(0, 'end')
        yeni_islem = False
    s = len(giris.get())
    giris.insert(s, str(x))

def islemler(x):
    global hesap
    global s1
    global yuzde
    global yeni_islem

    if yeni_islem and x not in "+-*/%":
        giris.delete(0, 'end')
        yeni_islem = False

    if x in "+-*/":
        try:
            s1.append(float(giris.get()))
        except ValueError:
            giris.delete(0, 'end')
            giris.insert(0, "Hata")
            return
        hesap.append(x)
        giris.delete(0, 'end')
    elif x == "%":
        yuzde = True
        try:
            s1.append(float(giris.get()))
        except ValueError:
            giris.delete(0, 'end')
            giris.insert(0, "Hata")
            return
        giris.delete(0, 'end')
    else:
        giris.insert(END, x)

def hesapla():
    global s1
    global hesap
    global yuzde
    global yeni_islem

    try:
        if yuzde:
            yuzde_degeri = float(giris.get())
            s1[-1] = (yuzde_degeri / 100) * s1[-1]
            yuzde = False
        else:
            s1.append(float(giris.get()))

        sonuc = s1[0]
        for i in range(1, len(s1)):
            if hesap[i-1] == '+':
                sonuc += s1[i]
            elif hesap[i-1] == '-':
                sonuc -= s1[i]
            elif hesap[i-1] == '/':
                if s1[i] != 0:
                    sonuc /= s1[i]
                else:
                    giris.delete(0, 'end')
                    giris.insert(0, "Hata: Sıfıra bölme")
                    hesap = []
                    s1 = []
                    yeni_islem = True
                    return
            elif hesap[i-1] == '*':
                sonuc *= s1[i]

        sonuc_str = str(sonuc)
        if sonuc % 1 == 0:
            sonuc_str = str(int(sonuc))

        giris.delete(0, 'end')
        giris.insert(0, sonuc_str)
        hesap = []
        s1 = []
        yeni_islem = True  # Yeni işlem başladığını belirt
    except ValueError:
        giris.delete(0, 'end')
        giris.insert(0, "Hata")
        hesap = []
        s1 = []
        yeni_islem = True  # Yeni işlem başladığını belirt

def sil():
    giris.delete(len(giris.get()) - 1)

def temizle():
    global hesap
    global s1
    global yeni_islem
    giris.delete(0, 'end')
    hesap = []
    s1 = []
    yeni_islem = True

window = Tk()
window.title('Hesap Makinası')
window.geometry("300x400")
window.configure(background='black')
window.resizable(width=False, height=False)


def ikinci_pencere():
    ikinci_pencere= tk.Frame(window, bg="lightgray", bd=2,relief="ridge")
    ikinci_pencere.place(x=1, y=1,width=100, height=140)
    Button(ikinci_pencere, width=2, text="...", fg="black", font=("Helvetica", 9),  background='white',command=ikinci_pencere.destroy).place(height=25,x=1, y=1)

giris = tk.Entry(window, width=29, bd=4, justify=RIGHT, font=("Helvetica", 16))
giris.place(height=60, width=275, x=13, y=20)


# Odağı ve tıklamayı engelleme
window.bind("<Tab>", lambda event: "break")
giris.bind("<FocusIn>", lambda event: "break")
giris.bind("<Button-1>", lambda event: "break")

def secim_degisti(event):
    secilen = secim_var.get()
    print(f"Seçilen: {secilen}")

secim_var = tk.StringVar()

# Seçenekler listesi

def Octune(event):
    
    if event.char == 'O' or event.char == 'o':
        giris.insert(tk.END,"Ez")
        


style = ttk.Style()
style.configure('TButton', font=('Helvetica', 16))

ttk.Button(window, width=4, text="x",  command=lambda: islemler("*")).place(height=44,x=155, y=100)
ttk.Button(window, width=4, text="÷",  command=lambda: islemler("/")).place(height=44,x=85, y=100)
ttk.Button(window, width=4, text="C",  command=temizle)              .place(height=44,x=225, y=100)
ttk.Button(window, width=4, text="%",  command=lambda: islemler("%")).place(height=44,x=15, y=100)
ttk.Button(window, width=4, text="1",  command=lambda: yaz(1)).place(height=44,x=15, y=160)
ttk.Button(window, width=4, text="2",  command=lambda: yaz(2)).place(height=44,x=85, y=160)
ttk.Button(window, width=4, text="3",  command=lambda: yaz(3)).place(height=44,x=155, y=160)
ttk.Button(window, width=4, text="4",  command=lambda: yaz(4)).place(height=44,x=15, y=220)
ttk.Button(window, width=4, text="5",  command=lambda: yaz(5)).place(height=44,x=85, y=220)
ttk.Button(window, width=4, text="6",  command=lambda: yaz(6)).place(height=44,x=155, y=220)
ttk.Button(window, width=4, text="7",  command=lambda: yaz(7)).place(height=44,x=15, y=280)
ttk.Button(window, width=4, text="8",  command=lambda: yaz(8)).place(height=44,x=85, y=280)
ttk.Button(window, width=4, text="9",  command=lambda: yaz(9)).place(height=44,x=155, y=280)
ttk.Button(window, width=4, text=".",  command=lambda: yaz(".")).place(height=44,x=155, y=340)
ttk.Button(window, width=4, text="=",  command=hesapla).place(height=44,x=225, y=340)
ttk.Button(window, width=10,text="0",  command=lambda: yaz(0)).place(height=44, x=15, y=340)
ttk.Button(window, width=4, text="+",  command=lambda: islemler("+")).place(height=44,x=225, y=280)
ttk.Button(window, width=4, text="-",  command=lambda: islemler("-")).place(height=44,x=225, y=220)
ttk.Button(window, width=4, text="⌫", command=sil).place(height=44,x=225, y=160)
 #ttk.Button(window, width=1, text="...",command=ikinci_pencere).place(height=10,x=1, y=1)

# Klavye bağlamaları
window.bind("<Return>", lambda event: hesapla())
window.bind("<KP_Divide>", lambda event: islemler("/"))
window.bind("<KP_Multiply>", lambda event: islemler("*"))
window.bind("<KP_Subtract>", lambda event: islemler("-"))
window.bind("<KP_Add>", lambda event: islemler("+"))
window.bind("<percent>", lambda event: islemler("%"))
window.bind("<BackSpace>", lambda event: sil())
window.bind("<KP_Enter>", lambda event: hesapla())
window.bind("<Key>", lambda event: klavye_islemleri(event))
window.bind("<O>", lambda event: Octune(event))
 

def klavye_islemleri(event):
    if event.char in '0123456789':
        yaz(event.char)
    elif event.char in '+-*/%':         
        islemler(event.char)
    elif event.char == '\r':
        hesapla()
    elif event.char == '.':
        yaz('.')
    elif event.char == 'o':
        Octune(event)
        



window.mainloop()
