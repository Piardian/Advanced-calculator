import tkinter as tk
from tkinter import ttk

# Global değişkenler
yeni_islem = True
hesap = []
s1 = []

# Fonksiyonlar
def yaz(x):
    global yeni_islem
    if yeni_islem:
        giris.delete(0, 'end')
        yeni_islem = False
    s = len(giris.get())
    giris.insert(s, str(x))

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
    secilen1 = secim_var1.get()
    secilen2 = secim_var2.get()
    print(f"Seçilen 1: {secilen1}")
    print(f"Seçilen 2: {secilen2}")

def birim_donustur():
    try:
        deger = float(giris.get())
        birim1 = secim_var1.get()
        birim2 = secim_var2.get()
        # Önce birimi metreye çevir
        if birim1 == "Kilometre":
            deger_metre = deger * 1000
        elif birim1 == "Hektometre":
            deger_metre = deger * 100
        elif birim1 == "Dekametre":
            deger_metre = deger * 10
        elif birim1 == "Metre":
            deger_metre = deger
        elif birim1 == "Desimetre":
            deger_metre = deger * 0.1
        elif birim1 == "Santimetre":
            deger_metre = deger * 0.01
        elif birim1 == "Milimetre":
            deger_metre = deger * 0.001
        elif birim1 == "Mikrometre":
            deger_metre = deger * 1e-6
        elif birim1 == "Nanometre":
            deger_metre = deger * 1e-9
        elif birim1 == "Pikometre":
            deger_metre = deger * 1e-12
        elif birim1 == "Femtometre":
            deger_metre = deger * 1e-15
        elif birim1 == "Attometre":
            deger_metre = deger * 1e-18
        elif birim1 == "Işık Yılı":
            deger_metre = deger * 9.461e+15
        else:
            sonuc = "Geçersiz birim"
            sonuc_giris.delete(0, 'end')
            sonuc_giris.insert(0, sonuc)
            return

        # Metreden hedef birime çevir
        if birim2 == "Kilometre":
            sonuc = deger_metre / 1000
        elif birim2 == "Hektometre":
            sonuc = deger_metre / 100
        elif birim2 == "Dekametre":
            sonuc = deger_metre / 10
        elif birim2 == "Metre":
            sonuc = deger_metre
        elif birim2 == "Desimetre":
            sonuc = deger_metre / 0.1
        elif birim2 == "Santimetre":
            sonuc = deger_metre / 0.01
        elif birim2 == "Milimetre":
            sonuc = deger_metre / 0.001
        elif birim2 == "Mikrometre":
            sonuc = deger_metre / 1e-6
        elif birim2 == "Nanometre":
            sonuc = deger_metre / 1e-9
        elif birim2 == "Pikometre":
            sonuc = deger_metre / 1e-12
        elif birim2 == "Femtometre":
            sonuc = deger_metre / 1e-15
        elif birim2 == "Attometre":
            sonuc = deger_metre / 1e-18
        elif birim2 == "Işık Yılı":
            sonuc = deger_metre / 9.461e+15
        else:
            sonuc = "Geçersiz birim"
        
        sonuc_giris.delete(0, 'end')
        sonuc_giris.insert(0, str(sonuc))
    except ValueError:
        sonuc_giris.delete(0, 'end')
        sonuc_giris.insert(0, "Geçersiz giriş")

# Pencere ayarları
window = tk.Tk()
window.title('Birim Dönüştürücü')
window.geometry("293x460")
window.configure(background='black')
window.resizable(width=False, height=False)

# Giriş alanı
giris = ttk.Entry(window, width=29, justify=tk.RIGHT, font=("Helvetica", 16))
giris.place(height=60, width=165, x=105, y=22)

# Seçim baloncuğu için bir StringVar oluştur
secim_var1 = tk.StringVar()
secim_var2 = tk.StringVar()

# Seçenekler listesi
secenekler = ["Kilometre","Hektometre","Dekametre","Metre","Desimetre",
"Santimetre","Milimetre","Mikrometre","Nanometre","Pikometre","Femtometre","Attometre","Işık Yılı"]

# 1. Combobox (Seçim baloncuğu) oluştur
combobox1 = ttk.Combobox(window, textvariable=secim_var1, values=secenekler)
combobox1.bind("<<ComboboxSelected>>", secim_degisti)
combobox1.place(width=83,height=25,x=15, y=65)

# 2. Combobox (Seçim baloncuğu) oluştur
combobox2 = ttk.Combobox(window, textvariable=secim_var2, values=secenekler)
combobox2.bind("<<ComboboxSelected>>", secim_degisti)
combobox2.place(width=83, height=25, x=15, y=135)

# Sonuç alanı
sonuc_giris = ttk.Entry(window, width=29, justify=tk.RIGHT, font=("Helvetica", 16))
sonuc_giris.place(height=60, width=165, x=105, y=90)

# Silme ve temizleme butonları
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 16))

# Sayı butonları
buttons = [
    {"text": "Dönüştür", "command": birim_donustur, "x": 15, "y": 160},
    {"text": "C", "command": temizle, "x": 105, "y": 160},
    {"text": "⌫", "command": sil, "x": 195, "y": 160},
    {"text": "1", "command": lambda: yaz(1), "x": 15, "y": 220},
    {"text": "2", "command": lambda: yaz(2), "x": 105, "y": 220},
    {"text": "3", "command": lambda: yaz(3), "x": 195, "y": 220},
    {"text": "4", "command": lambda: yaz(4), "x": 15, "y": 280},
    {"text": "5", "command": lambda: yaz(5), "x": 105, "y": 280},
    {"text": "6", "command": lambda: yaz(6), "x": 195, "y": 280},
    {"text": "7", "command": lambda: yaz(7), "x": 15, "y": 340},
    {"text": "8", "command": lambda: yaz(8), "x": 105, "y": 340},
    {"text": "9", "command": lambda: yaz(9), "x": 195, "y": 340},
    {"text": ".", "command": lambda: yaz("."), "x": 195, "y": 400},
    {"text": "0", "command": lambda: yaz(0), "x": 17, "y": 400, "width": 13}
]

# Butonları oluştur ve yerleştir
for button in buttons:
    ttk.Button(
        window, 
        text=button["text"], 
        command=button["command"], 
        width=button.get("width", 6)
    ).place(height=44, x=button["x"], y=button["y"])

window.mainloop()
