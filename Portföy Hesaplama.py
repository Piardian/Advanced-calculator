import tkinter as tk
from tkinter import ttk
import yfinance as yf

# Küresel değişkenler
hesap = []
s1 = []
yeni_islem = True
toplam_fiyat = 0

def get_stock_price_yahoo(symbol):
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1d", interval="1m")
        if not hist.empty:
            latest_price = hist['Close'].iloc[-1]
            return latest_price
        else:
            print("Geçersiz Sembol veya Veri Yok")
            return None
    except Exception as e:
        print(f"Hata: {e}")
        return None

def yaz(x):
    global yeni_islem
    if yeni_islem:
        toplam_fiyat_entry.delete(0, 'end')
        yeni_islem = False
    s = len(toplam_fiyat_entry.get())
    toplam_fiyat_entry.insert(s, str(x))

def islemler(x):
    global hesap
    global s1
    global yeni_islem

    if yeni_islem and x not in "+-*/%":
        toplam_fiyat_entry.delete(0, 'end')
        yeni_islem = False

    if x in "+-*/":
        try:
            s1.append(float(toplam_fiyat_entry.get()))
        except ValueError:
            toplam_fiyat_entry.delete(0, 'end')
            toplam_fiyat_entry.insert(0, "Hata")
            return
        hesap.append(x)
        toplam_fiyat_entry.delete(0, 'end')
    elif x == "%":
        try:
            s1.append(float(toplam_fiyat_entry.get()))
        except ValueError:
            toplam_fiyat_entry.delete(0, 'end')
            toplam_fiyat_entry.insert(0, "Hata")
            return
        toplam_fiyat_entry.delete(0, 'end')
    else:
        toplam_fiyat_entry.insert(END, x)

def hesapla():
    global s1
    global hesap
    global yeni_islem

    try:
        s1.append(float(toplam_fiyat_entry.get()))

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
                    toplam_fiyat_entry.delete(0, 'end')
                    toplam_fiyat_entry.insert(0, "Hata: Sıfıra bölme")
                    hesap = []
                    s1 = []
                    yeni_islem = True
                    return
            elif hesap[i-1] == '*':
                sonuc *= s1[i]

        sonuc_str = str(sonuc)
        if sonuc % 1 == 0:
            sonuc_str = str(int(sonuc))

        toplam_fiyat_entry.delete(0, 'end')
        toplam_fiyat_entry.insert(0, sonuc_str)
        hesap = []
        s1 = []
        yeni_islem = True
    except ValueError:
        toplam_fiyat_entry.delete(0, 'end')
        toplam_fiyat_entry.insert(0, "Hata")
        hesap = []
        s1 = []
        yeni_islem = True

def sil():
    toplam_fiyat_entry.delete(len(toplam_fiyat_entry.get()) - 1)

def temizle():
    global hesap
    global s1
    global yeni_islem
    global toplam_fiyat

    toplam_fiyat_entry.delete(0, 'end')
    hesap = []
    s1 = []
    yeni_islem = True
    toplam_fiyat = 0
    total_sonuc.delete(0, 'end')

def hisse_goruntule():
    global toplam_fiyat

    symbol = hisse_giris.get()
    try:
        lot_sayisi = int(Lot_giris.get())
    except ValueError:
        hisse_sonuc_giris.delete(0, 'end')
        hisse_sonuc_giris.insert(0, 'Geçersiz Lot Sayısı')
        return
    
    price = get_stock_price_yahoo(symbol)
    if price is not None:
        birim = secim_var1.get()

        if lot_sayisi >= 1:
            total_price = price * lot_sayisi
            toplam_fiyat += total_price

            toplam_fiyat_entry.delete(0, 'end')
            toplam_fiyat_entry.insert(0, f"{total_price:.2f} {birim}")

            total_sonuc.delete(0, 'end')
            total_sonuc.insert(0, f"{toplam_fiyat:.2f} {birim}")
        
        hisse_sonuc_giris.delete(0, 'end')
        hisse_sonuc_giris.insert(0, f"{price:.2f} {birim}")
    else:
        hisse_sonuc_giris.delete(0, 'end')
        hisse_sonuc_giris.insert(0, 'Hata!')

def sadece_rakam_girisi(char):
    return char.isdigit()

# Pencere ayarları
window = tk.Tk()
window.title('Porföy Hesaplama')
window.geometry("293x580")
window.configure(background='black')
window.resizable(width=False, height=False)

secim_var1 = tk.StringVar()

# Hisse kodu girişi
hisse_giris_text = tk.StringVar()
hisse_giris = ttk.Entry(window, width=29, justify=tk.RIGHT, font=("Times",10), textvariable=hisse_giris_text)
hisse_giris.place(height=30, width=130, x=15, y=22)
Label = tk.Label(hisse_giris, text="Hisse Kodu", fg="black", bg="white", font=("Helvetica", 9))
Label.place(height=15, width=70, x=0, y=0)

# Girilen metni büyük harfe çevirme
hisse_giris_text.trace_add("write", lambda *args: hisse_giris_text.set(hisse_giris_text.get().upper()))

# Lot sayısı girişi
Lot_giris = ttk.Entry(window, width=29, justify=tk.RIGHT, font=("Times",10), validate="key")
Lot_giris['validatecommand'] = (Lot_giris.register(sadece_rakam_girisi), '%S')
Lot_giris.place(height=30, width=130, x=15, y=60)
Label = tk.Label(Lot_giris, text="Lot sayısı", fg="black", bg="white", font=("Helvetica", 9))
Label.place(height=15, width=60, x=0, y=0)

# Hisse senedi sonucu
hisse_sonuc_giris = ttk.Entry(window, width=29, justify=tk.RIGHT, font=("Times",10))
hisse_sonuc_giris.place(height=30, width=135, x=150, y=22)
Label = tk.Label(hisse_sonuc_giris, text="Fiyat", fg="black", bg="white", font=("Helvetica", 9))
Label.place(height=15, width=30, x=0, y=0)

# Toplam fiyat girişi
toplam_fiyat_entry = ttk.Entry(window, width=29, justify=tk.RIGHT, font=("Helvetica", 16))
toplam_fiyat_entry.place(height=50, width=265, x=15, y=170)
Label = tk.Label(toplam_fiyat_entry, text="Toplam Fiyat", fg="black", bg="white", font=("Helvetica", 9))
Label.place(height=15, width=80, x=0, y=0)

total_sonuc = ttk.Entry(window, width=29, justify=tk.RIGHT, font=("Helvetica", 16))
total_sonuc.place(height=50, width=265, x=15, y=100)
Label = tk.Label(total_sonuc, text="Toplam Sonuç", fg="black", bg="white", font=("Helvetica", 9))
Label.place(height=15, width=80, x=0, y=0)

secenekler = ["$", "TRY", "EUR", "GBP", "JPY", "CNY", "RUB", "NZD", "CHF", "CAD", "HKD"]
combobox1 = ttk.Combobox(toplam_fiyat_entry, textvariable=secim_var1, values=secenekler, state="readonly")
combobox1.place(width=60, height=17, x=0, y=35)

ttk.Button(window, text="Hisse Fiyat", command=hisse_goruntule, width=20).place(height=44, x=20, y=230)

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 16))

buttons = [
    {"text": "1", "command": lambda: yaz(1), "pos": (15, 340)},
    {"text": "2", "command": lambda: yaz(2), "pos": (85, 340)},
    {"text": "3", "command": lambda: yaz(3), "pos": (155, 340)},
    {"text": "4", "command": lambda: yaz(4), "pos": (15, 400)},
    {"text": "5", "command": lambda: yaz(5), "pos": (85, 400)},
    {"text": "6", "command": lambda: yaz(6), "pos": (155, 400)},
    {"text": "7", "command": lambda: yaz(7), "pos": (15, 460)},
    {"text": "8", "command": lambda: yaz(8), "pos": (85, 460)},
    {"text": "9", "command": lambda: yaz(9), "pos": (155, 460)},
    {"text": ".", "command": lambda: yaz("."), "pos": (155, 520)},
    {"text": "0", "command": lambda: yaz(0), "pos": (15, 520), "width": 10},
    {"text": "x", "command": lambda: islemler("*"), "pos": (225, 340)},
    {"text": "÷", "command": lambda: islemler("/"), "pos": (225, 400)},
    {"text": "+", "command": lambda: islemler("+"), "pos": (225, 460)},
    {"text": "-", "command": lambda: islemler("-"), "pos": (225, 520)},
    {"text": "=", "command": hesapla, "pos": (85, 520)},
    {"text": "C", "command": temizle, "pos": (225, 580)},
    {"text": "⌫", "command": sil, "pos": (225, 580)},
]

# Create buttons
for button in buttons:
    width = button.get("width", 4)
    ttk.Button(window, width=width, text=button["text"], command=button["command"]).place(height=44, x=button["pos"][0], y=button["pos"][1])

# Klavye bağlamaları
window.bind("<Return>", lambda event: hesapla())
window.bind("<KP_Divide>", lambda event: islemler("/"))
window.bind("<KP_Multiply>", lambda event: islemler("*"))
window.bind("<KP_Subtract>", lambda event: islemler("-"))
window.bind("<KP_Add>", lambda event: islemler("+"))
window.bind("<BackSpace>", lambda event: sil())
window.bind("<KP_Enter>", lambda event: hesapla())

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
