import tkinter as tk
from tkinter import *
from tkinter import ttk
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

def secim_degisti(event):
    secilen = secim_var.get()
    print(f"Seçilen: {secilen}")

window = Tk()
window.title('Birim Dönüştürücü')
window.geometry("293x460")
window.configure(background='black')
window.resizable(width=False, height=False)

giris = ttk.Entry(window, width=29, justify=RIGHT, font=("Helvetica", 16))
giris.place(height=60, width=265, x=15, y=92)

giris = ttk.Entry(window, width=29, justify=RIGHT, font=("Helvetica", 16))
giris.place(height=60, width=265, x=15, y=22)

# Seçim baloncuğu için bir StringVar oluştur
secim_var = tk.StringVar()

# Seçenekler listesi
secenekler = ["Kilometre","Hektometre","Dekametre","Metre","Desimetre",
"antimetre","Milimetre","Mikrometre","Nanometre","Pikometre","Femtometre","Attometre","Işık Yılı"]

# Combobox (Seçim baloncuğu) oluştur

combobox = ttk.Combobox(window, textvariable=secim_var, values=secenekler)
combobox.bind("<<ComboboxSelected>>", secim_degisti)
combobox.pack(pady=20)
combobox.place(width=83,height=14,x=15, y=65)

combobox = ttk.Combobox(window, textvariable=secim_var, values=secenekler)
combobox.bind("<<ComboboxSelected>>", secim_degisti)
combobox.pack(pady=20)
combobox.place(width=83,height=14,x=15, y=135)

def ikinci_pencere():
    ikinci_pencere= tk.Frame(window, bg="lightgray", bd=2,relief="ridge")
    ikinci_pencere.place(x=1, y=1,width=100, height=140)
    Button(ikinci_pencere, width=2, text="...", fg="black", font=("Helvetica", 9),  background='white',command=ikinci_pencere.destroy).place(height=25,x=1, y=1)


style = ttk.Style()
style.configure('TButton', font=('Helvetica', 16))

ttk.Button(window, width=6, text="C",  command=temizle).place(height=44,x=105, y=160)
ttk.Button(window, width=6, text="1",  command=lambda: yaz(1)).place(height=44,x=15, y=220)
ttk.Button(window, width=6,text="2", command=lambda: yaz(2)).place(height=44,x=105, y=220)
ttk.Button(window, width=6, text="3",  command=lambda: yaz(3)).place(height=44,x=195, y=220)
ttk.Button(window, width=6, text="4",command=lambda: yaz(4)).place(height=44,x=15, y=280)
ttk.Button(window, width=6, text="5",   command=lambda: yaz(5)).place(height=44,x=105, y=280)
ttk.Button(window, width=6, text="6",  command=lambda: yaz(6)).place(height=44,x=195, y=280)
ttk.Button(window, width=6, text="7",  command=lambda: yaz(7)).place(height=44,x=15, y=340)
ttk.Button(window, width=6, text="8",   command=lambda: yaz(8)).place(height=44,x=105, y=340)
ttk.Button(window, width=6,text="9",  command=lambda: yaz(9)).place(height=44,x=195, y=340)
ttk.Button(window, width=6, text=".",   command=lambda: yaz(".")).place(height=44,x=195, y=400)
ttk.Button(window, width=13,text="0",   command=lambda: yaz(0)).place(height=44, x=17, y=400)
ttk.Button(window, width=6, text="⌫",   command=sil).place(height=44,x=195, y=160)


window.mainloop()