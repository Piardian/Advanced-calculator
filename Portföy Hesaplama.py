import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

# Global değişkenler
yeni_islem = True
hesap = []
s1 = []

# API anahtarlarınızı buraya ekleyin
EXCHANGE_RATE_API_KEY = '4eecc3612e92a51ef6045107'
EXCHANGE_RATE_BASE_URL = f'https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/latest'

ALPHA_VANTAGE_API_KEY = 'ONIF6EGUPLH8JJGC'
ALPHA_VANTAGE_BASE_URL = 'https://www.alphavantage.co/query'

# Döviz kurlarını çekmek için fonksiyon
def get_exchange_rate(from_currency, to_currency):
    url = f'{EXCHANGE_RATE_BASE_URL}/{from_currency}'
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

# Hisse senedi fiyatlarını çekmek için fonksiyon
def get_stock_price(symbol):
    url = f'{ALPHA_VANTAGE_BASE_URL}?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={ALPHA_VANTAGE_API_KEY}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTPError için kontrol
        data = response.json()
        time_series = data.get('Time Series (1min)')
        if time_series:
            latest_time = sorted(time_series.keys())[0]
            return time_series[latest_time]['1. open']
        else:
            print("API Hatası veya Geçersiz Sembol")
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

# Hisse senedi fiyatlarını görüntüleme fonksiyonu
def hisse_goruntule():
    symbol = hisse_giris.get()
    price = get_stock_price(symbol)
    if price is not None:
        hisse_sonuc_giris.delete(0, 'end')
        hisse_sonuc_giris.insert(0, str(price))
    else:
        hisse_sonuc_giris.delete(0, 'end')
        hisse_sonuc_giris.insert(0, 'Hata!')

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
window.title('Döviz ve Hisse Hesaplama')
window.geometry("293x240")
window.configure(background='black')
window.resizable(width=False, height=False)


def ikinci_pencere():
    ikinci_pencere= tk.Frame(window, bg="black" ,bd=2,relief="ridge")
    ikinci_pencere.place(x=1, y=1,width=80, height=100)
    Label=tk.Label(ikinci_pencere, text="Pia",fg="red",bg="black",font=("Times", 24))
    Label.place(x=15, y=35,width=40, height=30)
    Button(ikinci_pencere, width=1, text="...", fg="black", font=("Helvetica", 9),  background='white',command=ikinci_pencere.destroy).place(height=15,x=1, y=1)


# Giriş alanı
#giris = ttk.Entry(window, width=29, justify=tk.RIGHT, font=("Helvetica", 16))
#giris.place(height=60, width=265, x=15, y=22)

# Sonuç alanı
#sonuc_giris = ttk.Entry(window, width=29, justify=tk.RIGHT, font=("Helvetica", 16))
#sonuc_giris.place(height=60, width=265, x=15, y=90)

# Seçim baloncuğu için bir StringVar oluştur
secim_var1 = tk.StringVar()
secim_var2 = tk.StringVar()

# Hisse senedi sembol girişi
hisse_giris = ttk.Entry(window, width=29, justify=tk.RIGHT, font=("Helvetica", 16))
hisse_giris.place(height=60, width=265, x=15, y=22)
tk.Canvas(hisse_giris,Canvas=("hisse kodu giriniz"))
# Hisse senedi sonucu
hisse_sonuc_giris = ttk.Entry(window, width=29, justify=tk.RIGHT, font=("Helvetica", 16))
hisse_sonuc_giris.place(height=60, width=265, x=15, y=90)

# Hisse senedi butonu

# Seçenekler listesi
secenekler = ["USD", "TRY", "EUR", "GBP", "JPY", "CNY", "RUB", "NZD", "CHF", "CAD", "HKD"]

# 1. Combobox (Seçim baloncuğu) oluştur
combobox1 = ttk.Combobox(window, textvariable=secim_var1, values=secenekler, state="readonly")
combobox1.bind("<<ComboboxSelected>>", secim_degisti)
combobox1.place(width=60, height=17, x=15, y=133)

# 2. Combobox (Seçim baloncuğu) oluştur
#combobox2 = ttk.Combobox(window, textvariable=secim_var2, values=secenekler, state="readonly")
#combobox2.bind("<<ComboboxSelected>>", secim_degisti)
#combobox2.place(width=60, height=17, x=15, y=132)


# Hisse senedi butonu
ttk.Button(window, text="Hisse Fiyat", command=hisse_goruntule, width=20).place(height=44, x=20, y=170)

window.bind("<Tab>", lambda event: "break")
#giris.bind("<FocusIn>", lambda event: "break")
#giris.bind("<Button-1>", lambda event: "break")
#sonuc_giris.bind("<FocusIn>", lambda event: "break")
#sonuc_giris.bind("<Button-1>", lambda event: "break")
combobox1.bind("<FocusIn>", lambda event: "break")
#combobox2.bind("<FocusIn>", lambda event: "break")
hisse_sonuc_giris.bind("<FocusIn>", lambda event: "break")
hisse_sonuc_giris.bind("<Button-1>", lambda event: "break")
# Silme ve temizleme butonları
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 16))

# Sayı butonları



Button(window, width=1, text="...", fg="black", font=("Helvetica", 9),  background='white',command=ikinci_pencere).place(height=15,x=1, y=1)
# Yenileme butonu
#Button(window, text="↻",background='white',font=("Times", 15),width=2, command=yenile).place(height=23, x=130, y=1)

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

