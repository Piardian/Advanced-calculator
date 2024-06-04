import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

# Global değişkenler
yeni_islem = True
hesap = []
s1 = []

# API anahtarınızı buraya ekleyin
API_KEY = '4eecc3612e92a51ef6045107'
BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest'

# Döviz kurlarını çekmek için fonksiyon
def get_exchange_rate(from_currency, to_currency):
    url = f'{BASE_URL}/{from_currency}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTPError için kontrol
        data = response.json()
        if data['result'] == 'success':
            return data['conversion_rates'][to_currency]
        else:
            print("API Hatası:", data['error-type'])
            return None
    except requests.exceptions.RequestException as e:
        print(f"HTTP Hatası: {e}")
        return None
    except ValueError:
        print("JSON Decode Hatası")
        return None

# Döviz dönüştürme fonksiyonu
def birim_donustur():
    from_currency = secim_var1.get()
    to_currency = secim_var2.get()
    try:
        amount = float(giris.get())
    except ValueError:
        sonuc_giris.delete(0, 'end')
        sonuc_giris.insert(0, 'Geçersiz Miktar')
        return

    rate = get_exchange_rate(from_currency, to_currency)
    if rate is not None:
        converted_amount = amount * rate
        sonuc_giris.delete(0, 'end')
        sonuc_giris.insert(0, str(converted_amount))
    else:
        sonuc_giris.delete(0, 'end')
        sonuc_giris.insert(0, 'Hata!')

# Kur bilgilerini yenileme fonksiyonu
def yenile():
    from_currency = secim_var1.get()
    to_currency = secim_var2.get()
    if from_currency and to_currency:
        rate = get_exchange_rate(from_currency, to_currency)
        if rate is not None:
            try:
                amount = float(giris.get())
                converted_amount = amount * rate
                sonuc_giris.delete(0, 'end')
                sonuc_giris.insert(0, str(converted_amount))
            except ValueError:
                sonuc_giris.delete(0, 'end')
                sonuc_giris.insert(0, 'Geçersiz Miktar')
        else:
            sonuc_giris.delete(0, 'end')
            sonuc_giris.insert(0, 'Hata!')

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
    sonuc_giris.delete(0, 'end')
    hesap = []
    s1 = []
    yeni_islem = True

def secim_degisti(event):
    secilen1 = secim_var1.get()
    secilen2 = secim_var2.get()
    print(f"Seçilen 1: {secilen1}")
    print(f"Seçilen 2: {secilen2}")

# Pencere ayarları
window = tk.Tk()
window.title('Para Birim Dönüştürücü')
window.geometry("293x460")
window.configure(background='black')
window.resizable(width=False, height=False)

def ikinci_pencere():
    ikinci_pencere= tk.Frame(window, bg="black" ,bd=2,relief="ridge")
    ikinci_pencere.place(x=1, y=1,width=80, height=100)
    Label=tk.Label(ikinci_pencere, text="Pia",fg="red",bg="black",font=("Times", 24))
    Label.place(x=15, y=35,width=40, height=30)
    Button(ikinci_pencere, width=1, text="...", fg="black", font=("Helvetica", 9),  background='white',command=ikinci_pencere.destroy).place(height=15,x=1, y=1)


# Giriş alanı
giris = ttk.Entry(window, width=29, justify=tk.RIGHT, font=("Helvetica", 16))
giris.place(height=60, width=265, x=15, y=22)

# Sonuç alanı
sonuc_giris = ttk.Entry(window, width=29, justify=tk.RIGHT, font=("Helvetica", 16))
sonuc_giris.place(height=60, width=265, x=15, y=90)

# Seçim baloncuğu için bir StringVar oluştur
secim_var1 = tk.StringVar()
secim_var2 = tk.StringVar()

# Seçenekler listesi
secenekler = ["USD", "TRY", "EUR", "GBP", "JPY", "CNY", "RUB", "NZD", "CHF", "CAD", "HKD"]

# 1. Combobox (Seçim baloncuğu) oluştur
combobox1 = ttk.Combobox(window, textvariable=secim_var1, values=secenekler, state="readonly")
combobox1.bind("<<ComboboxSelected>>", secim_degisti)
combobox1.place(width=60, height=17, x=15, y=64)

# 2. Combobox (Seçim baloncuğu) oluştur
combobox2 = ttk.Combobox(window, textvariable=secim_var2, values=secenekler, state="readonly")
combobox2.bind("<<ComboboxSelected>>", secim_degisti)
combobox2.place(width=60, height=17, x=15, y=132)

window.bind("<Tab>", lambda event: "break")
giris.bind("<FocusIn>", lambda event: "break")
giris.bind("<Button-1>", lambda event: "break")
sonuc_giris.bind("<FocusIn>", lambda event: "break")
sonuc_giris.bind("<Button-1>", lambda event: "break")
combobox1.bind("<FocusIn>", lambda event: "break")
combobox2.bind("<FocusIn>", lambda event: "break")

# Silme ve temizleme butonları
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 16))

# Sayı butonları
buttons = [
    {"text": "Dönüştür", "command": birim_donustur, "x": 145, "y": 400, "width": 10},
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
    {"text": ".", "command": lambda: yaz("."), "x": 15, "y": 160},
    {"text": "0", "command": lambda: yaz(0), "x": 17, "y": 400, "width": 9}
]

# Butonları oluştur ve yerleştir
for button in buttons:
    ttk.Button(
        window, 
        text=button["text"], 
        command=button["command"], 
        width=button.get("width", 6)
    ).place(height=44, x=button["x"], y=button["y"])

Button(window, width=1, text="...", fg="black", font=("Helvetica", 9),  background='white',command=ikinci_pencere).place(height=15,x=1, y=1)
# Yenileme butonu
Button(window, text="↻",background='white',font=("Times", 15),width=2, command=yenile).place(height=23, x=130, y=1)

window.bind("<Return>", lambda event: birim_donustur())
window.bind("<BackSpace>", lambda event: sil())
window.bind("<KP_Enter>", lambda event: birim_donustur())
window.bind("<Key>", lambda event: klavye_islemleri(event))

def klavye_islemleri(event):
    if event.char in '0123456789':
        yaz(event.char)
    elif event.char == '\r':
        birim_donustur()
    elif event.char == '.':
        yaz('.')

window.mainloop()
