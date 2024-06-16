import tkinter as tk
from tkinter import *
from tkinter import ttk

# Küresel değişkenler
hesap = []
s1 = []
yeni_islem = True
yuzde = False

class Screen1:
    def __init__(self, master):
        self.master = master
        self.master.title("Screen 1")
        self.master.geometry("300x400")
        self.master.configure(background='black')
        self.master.resizable(width=False, height=False)

        self.giris = tk.Entry(self.master, width=29, bd=4, justify=RIGHT, font=('Times', 19))
        self.giris.place(height=60, width=275, x=13, y=20)

        self.master.bind("<Tab>", lambda event: "break")
        self.giris.bind("<FocusIn>", lambda event: "break")
        self.giris.bind("<Button-1>", lambda event: "break")

        self.master.bind("<Return>", lambda event: self.hesapla())
        self.master.bind("<KP_Divide>", lambda event: self.islemler("/"))
        self.master.bind("<KP_Multiply>", lambda event: self.islemler("*"))
        self.master.bind("<KP_Subtract>", lambda event: self.islemler("-"))
        self.master.bind("<KP_Add>", lambda event: self.islemler("+"))
        self.master.bind("<percent>", lambda event: self.islemler("%"))
        self.master.bind("<BackSpace>", lambda event: self.sil())
        self.master.bind("<KP_Enter>", lambda event: self.hesapla())
        self.master.bind("<Key>", lambda event: self.klavye_islemleri(event))
        self.master.bind("<O>", lambda event: self.Octune(event))

        buttons = [
            {"text": "1", "command": lambda: self.yaz(1), "pos": (15, 160)},
            {"text": "2", "command": lambda: self.yaz(2), "pos": (85, 160)},
            {"text": "3", "command": lambda: self.yaz(3), "pos": (155, 160)},
            {"text": "4", "command": lambda: self.yaz(4), "pos": (15, 220)},
            {"text": "5", "command": lambda: self.yaz(5), "pos": (85, 220)},
            {"text": "6", "command": lambda: self.yaz(6), "pos": (155, 220)},
            {"text": "7", "command": lambda: self.yaz(7), "pos": (15, 280)},
            {"text": "8", "command": lambda: self.yaz(8), "pos": (85, 280)},
            {"text": "9", "command": lambda: self.yaz(9), "pos": (155, 280)},
            {"text": ".", "command": lambda: self.yaz("."), "pos": (155, 340)},
            {"text": "0", "command": lambda: self.yaz(0), "pos": (15, 340), "width": 10},
            {"text": "x", "command": lambda: self.islemler("*"), "pos": (155, 100)},
            {"text": "÷", "command": lambda: self.islemler("/"), "pos": (85, 100)},
            {"text": "%", "command": lambda: self.islemler("%"), "pos": (15, 100)},
            {"text": "+", "command": lambda: self.islemler("+"), "pos": (225, 280)},
            {"text": "-", "command": lambda: self.islemler("-"), "pos": (225, 220)},
            {"text": "=", "command": self.hesapla, "pos": (225, 340)},
            {"text": "C", "command": self.temizle, "pos": (225, 100)},
            {"text": "⌫", "command": self.sil, "pos": (225, 160)},
        ]

        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 16))

        for button in buttons:
            width = button.get("width", 4)
            ttk.Button(self.master, width=width, text=button["text"], command=button["command"]).place(height=44, x=button["pos"][0], y=button["pos"][1])

        Button(self.master, width=1, text="...", fg="black", font=("Helvetica", 9), background='white', command=self.ikinci_pencere).place(height=15, x=1, y=1)

        self.button = tk.Button(master, text="Go to Screen 2", command=self.goto_screen2)
        self.button.place(x=100, y=380)

    def yaz(self, x):
        global yeni_islem
        if yeni_islem:
            self.giris.delete(0, 'end')
            yeni_islem = False
        s = len(self.giris.get())
        self.giris.insert(s, str(x))

    def islemler(self, x):
        global hesap
        global s1
        global yuzde
        global yeni_islem

        if yeni_islem and x not in "+-*/%":
            self.giris.delete(0, 'end')
            yeni_islem = False

        if x in "+-*/":
            try:
                s1.append(float(self.giris.get()))
            except ValueError:
                self.giris.delete(0, 'end')
                self.giris.insert(0, "Hata")
                return
            hesap.append(x)
            self.giris.delete(0, 'end')
        elif x == "%":
            yuzde = True
            try:
                s1.append(float(self.giris.get()))
            except ValueError:
                self.giris.delete(0, 'end')
                self.giris.insert(0, "Hata")
                return
            self.giris.delete(0, 'end')
        else:
            self.giris.insert(END, x)

    def hesapla(self):
        global s1
        global hesap
        global yuzde
        global yeni_islem

        try:
            if yuzde:
                yuzde_degeri = float(self.giris.get())
                s1[-1] = (yuzde_degeri / 100) * s1[-1]
                yuzde = False
            else:
                s1.append(float(self.giris.get()))

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
                        self.giris.delete(0, 'end')
                        self.giris.insert(0, "Hata: Sıfıra bölme")
                        hesap = []
                        s1 = []
                        yeni_islem = True
                        return
                elif hesap[i-1] == '*':
                    sonuc *= s1[i]

            sonuc_str = str(sonuc)
            if sonuc % 1 == 0:
                sonuc_str = str(int(sonuc))

            self.giris.delete(0, 'end')
            self.giris.insert(0, sonuc_str)
            hesap = []
            s1 = []
            yeni_islem = True  # Yeni işlem başladığını belirt
        except ValueError:
            self.giris.delete(0, 'end')
            self.giris.insert(0, "Hata")
            hesap = []
            s1 = []
            yeni_islem = True  # Yeni işlem başladığını belirt

    def sil(self):
        self.giris.delete(len(self.giris.get()) - 1)

    def temizle(self):
        global hesap
        global s1
        global yeni_islem
        self.giris.delete(0, 'end')
        hesap = []
        s1 = []
        yeni_islem = True

    def goto_screen2(self):
        self.master.withdraw()
        screen2 = Screen2(tk.Toplevel(self.master))

    def ikinci_pencere(self):
        ikinci_pencere = tk.Frame(self.master, bg="black", bd=2, relief="ridge")
        ikinci_pencere.place(x=1, y=1, width=80, height=100)
        label = tk.Label(ikinci_pencere, text="Pia", fg="red", bg="black", font=("Times", 24))
        label.place(x=15, y=35, width=40, height=30)
        destroy_button = tk.Button(ikinci_pencere, width=1, text="...", fg="black", font=("Helvetica", 9), background='white', command=ikinci_pencere.destroy)
        destroy_button.place(height=15, x=1, y=1)
        
    def Octune(self, event):
        if event.char == 'O' or event.char == 'o':
            self.giris.insert(tk.END, "Ez")

    def klavye_islemleri(self, event):
        if event.char in '0123456789':
            self.yaz(event.char)
        elif event.char in '+-*/%':
            self.islemler(event.char)
        elif event.char == '\r':
            self.hesapla()
        elif event.char == '.':
            self.yaz('.')
        elif event.char == 'o':
            self.Octune(event)


class Screen2:
    def __init__(self, master):
        self.master = master
        self.master.title("Uzunluk")
        self.master.geometry("293x460")
        self.master.configure(background='black')
        self.master.resizable(width=False, height=False)

        self.giris = tk.Entry(self.master, width=29,  justify=tk.RIGHT, font=('Helvetica', 16))
        self.giris.place(height=60, width=265, x=15, y=22)

        # Sonuç alanı
        self.sonuc_giris = ttk.Entry(self.master, width=29, justify=tk.RIGHT, font=("Helvetica", 16))
        self.sonuc_giris.place(height=60, width=265, x=15, y=90)

        # Seçim baloncuğu için bir StringVar oluştur
        self.secim_var1 = tk.StringVar()
        self.secim_var2 = tk.StringVar()

        # Seçenekler listesi
        secenekler = ["Milimetre", "Santimetre", "Desimetre", "Metre", "Dekametre", "Hektometre", "Kilometre"]

        # 1. Combobox (Seçim baloncuğu) oluştur
        self.combobox1 = ttk.Combobox(self.master, textvariable=self.secim_var1, values=secenekler, state="readonly")
        self.combobox1.bind("<<ComboboxSelected>>", self.secim_degisti)
        self.combobox1.place(width=83, height=17, x=15, y=64)

        # 2. Combobox (Seçim baloncuğu) oluştur
        self.combobox2 = ttk.Combobox(self.master, textvariable=self.secim_var2, values=secenekler, state="readonly")
        self.combobox2.bind("<<ComboboxSelected>>", self.secim_degisti)
        self.combobox2.place(width=83, height=17, x=15, y=132)
       
        
        buttons = [
            {"text": "Dönüştür", "command": self.birim_donustur, "x": 145, "y": 400, "width": 10},
            {"text": "C", "command": self.temizle, "x": 105, "y": 160},
            {"text": "⌫", "command": self.sil, "x": 195, "y": 160},
            {"text": "1", "command": lambda: self.yaz(1), "x": 15, "y": 220},
            {"text": "2", "command": lambda: self.yaz(2), "x": 105, "y": 220},
            {"text": "3", "command": lambda: self.yaz(3), "x": 195, "y": 220},
            {"text": "4", "command": lambda: self.yaz(4), "x": 15, "y": 280},
            {"text": "5", "command": lambda: self.yaz(5), "x": 105, "y": 280},
            {"text": "6", "command": lambda: self.yaz(6), "x": 195, "y": 280},
            {"text": "7", "command": lambda: self.yaz(7), "x": 15, "y": 340},
            {"text": "8", "command": lambda: self.yaz(8), "x": 105, "y": 340},
            {"text": "9", "command": lambda: self.yaz(9), "x": 195, "y": 340},
            {"text": ".", "command": lambda: self.yaz("."), "x": 15, "y": 160},
            {"text": "0", "command": lambda: self.yaz(0), "x": 17, "y": 400, "width": 9}
        ]

        for button in buttons:
            ttk.Button(
                self.master, 
                text=button["text"], 
                command=button["command"], 
                width=button.get("width", 6)
            ).place(height=44, x=button["x"], y=button["y"])


        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 16))

        self.ikinci_pencere_button = tk.Button(master, width=1, text="...", fg="black", font=("Helvetica", 9), background='white', command=self.ikinci_pencere)
        self.ikinci_pencere_button.place(height=15, x=1, y=1)

    def yaz(self, x):
        self.giris.insert(tk.END, str(x))

    def secim_degisti(self, event):
        secilen1 = self.secim_var1.get()
        secilen2 = self.secim_var2.get()
        print(f"Seçilen 1: {secilen1}")
        print(f"Seçilen 2: {secilen2}")

    def sil(self):
        self.giris.delete(len(self.giris.get()) - 1)

    def temizle(self):
        self.giris.delete(0, tk.END)
        self.sonuc_giris.delete(0, tk.END)

    def goto_screen1(self):
        self.master.withdraw()
        screen1 = Screen1(tk.Toplevel(self.master))

    def goto_screen3(self):
        self.master.withdraw()
        screen3 = Screen3(tk.Toplevel(self.master))

    def birim_donustur(self):
        try:
            deger = float(self.giris.get())
            birim1 = self.secim_var1.get()
            birim2 = self.secim_var2.get()
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
                self.sonuc_giris.delete(0, 'end')
                self.sonuc_giris.insert(0, sonuc)
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

            self.sonuc_giris.delete(0, 'end')
            self.sonuc_giris.insert(0, str(sonuc))
        except ValueError:
            self.sonuc_giris.delete(0, 'end')
            self.sonuc_giris.insert(0, "Geçersiz giriş")

        self.master.bind("<Return>", lambda event: self.birim_donustur())
        self.master.bind("<BackSpace>", lambda event: self.sil())
        self.master.bind("<KP_Enter>", lambda event: self.birim_donustur())
        self.master.bind("<Key>", lambda event: self.klavye_islemleri(event))

    def klavye_islemleri(self, event):
        if event.char in '0123456789':
            self.yaz(event.char)
        elif event.char == '\r':
            self.birim_donustur()
        elif event.char == '.':
            self.yaz('.')


    def ikinci_pencere(self):
        ikinci_pencere = tk.Frame(self.master, bg="black", bd=2, relief="ridge")
        ikinci_pencere.place(x=1, y=1, width=100, height=100)
        label = tk.Label(ikinci_pencere, text="Pia", fg="red", bg="black", font=("Times", 24))
        label.place(x=15, y=35, width=70, height=30)
        destroy_button = tk.Button(ikinci_pencere, width=1, text="...", fg="black", font=("Helvetica", 9), background='white', command=ikinci_pencere.destroy)
        destroy_button.place(height=15, x=1, y=1)
        destroy_button.pack()
        scr1_button = tk.Button(ikinci_pencere, width=10, fg="black", font=("Helvetica", 9), background='white', text="Go back to Screen 1", command=self.goto_screen1)
        scr1_button.place(height=15, x=1, y=15)
        scr1_button.pack()
        scr3_button = tk.Button(ikinci_pencere, width=10, fg="black", font=("Helvetica", 9), background='white', text="Go back to Screen 3", command=self.goto_screen3)
        scr3_button.place(height=15, x=1, y=30)
        scr3_button.pack()

        
class Screen3:
    def __init__(self, master):
        self.master = master
        self.master.title("xx")
        self.master.geometry("293x460")
        self.master.configure(background='black')
        self.master.resizable(width=False, height=False)
        self.giris = tk.Entry(self.master, width=29,  justify=tk.RIGHT, font=('Helvetica', 16))
        self.giris.place(height=60, width=265, x=15, y=22)

        # Sonuç alanı
        self.sonuc_giris = ttk.Entry(self.master, width=29, justify=tk.RIGHT, font=("Helvetica", 16))
        self.sonuc_giris.place(height=60, width=265, x=15, y=90)

        # Seçim baloncuğu için bir StringVar oluştur
        self.secim_var1 = tk.StringVar()
        self.secim_var2 = tk.StringVar()

        # Seçenekler listesi
        secenekler = ["Milimetre", "Santimetre", "Desimetre", "Metre", "Dekametre", "Hektometre", "Kilometre"]

        # 1. Combobox (Seçim baloncuğu) oluştur
        self.combobox1 = ttk.Combobox(self.master, textvariable=self.secim_var1, values=secenekler, state="readonly")
        self.combobox1.bind("<<ComboboxSelected>>", self.secim_degisti)
        self.combobox1.place(width=83, height=17, x=15, y=64)

        # 2. Combobox (Seçim baloncuğu) oluştur
        self.combobox2 = ttk.Combobox(self.master, textvariable=self.secim_var2, values=secenekler, state="readonly")
        self.combobox2.bind("<<ComboboxSelected>>", self.secim_degisti)
        self.combobox2.place(width=83, height=17, x=15, y=132)
       
        
        buttons = [
            {"text": "Dönüştür", "command": self.birim_donustur, "x": 145, "y": 400, "width": 10},
            {"text": "C", "command": self.temizle, "x": 105, "y": 160},
            {"text": "⌫", "command": self.sil, "x": 195, "y": 160},
            {"text": "1", "command": lambda: self.yaz(1), "x": 15, "y": 220},
            {"text": "2", "command": lambda: self.yaz(2), "x": 105, "y": 220},
            {"text": "3", "command": lambda: self.yaz(3), "x": 195, "y": 220},
            {"text": "4", "command": lambda: self.yaz(4), "x": 15, "y": 280},
            {"text": "5", "command": lambda: self.yaz(5), "x": 105, "y": 280},
            {"text": "6", "command": lambda: self.yaz(6), "x": 195, "y": 280},
            {"text": "7", "command": lambda: self.yaz(7), "x": 15, "y": 340},
            {"text": "8", "command": lambda: self.yaz(8), "x": 105, "y": 340},
            {"text": "9", "command": lambda: self.yaz(9), "x": 195, "y": 340},
            {"text": ".", "command": lambda: self.yaz("."), "x": 15, "y": 160},
            {"text": "0", "command": lambda: self.yaz(0), "x": 17, "y": 400, "width": 9}
        ]

        for button in buttons:
            ttk.Button(
                self.master, 
                text=button["text"], 
                command=button["command"], 
                width=button.get("width", 6)
            ).place(height=44, x=button["x"], y=button["y"])


        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 16))

        self.ikinci_pencere_button = tk.Button(master, width=1, text="...", fg="black", font=("Helvetica", 9), background='white', command=self.ikinci_pencere)
        self.ikinci_pencere_button.place(height=15, x=1, y=1)

    def yaz(self, x):
        self.giris.insert(tk.END, str(x))

    def secim_degisti(self, event):
        secilen1 = self.secim_var1.get()
        secilen2 = self.secim_var2.get()
        print(f"Seçilen 1: {secilen1}")
        print(f"Seçilen 2: {secilen2}")

    def sil(self):
        self.giris.delete(len(self.giris.get()) - 1)

    def temizle(self):
        self.giris.delete(0, tk.END)
        self.sonuc_giris.delete(0, tk.END)

   
   
    def goto_screen1(self):
        self.master.withdraw()
        screen1 = Screen1(tk.Toplevel(self.master))

    def goto_screen2(self):
        self.master.withdraw()
        Screen2 = Screen1(tk.Toplevel(self.master))

    def ikinci_pencere(self):
        ikinci_pencere = tk.Frame(self.master, bg="black", bd=2, relief="ridge")
        ikinci_pencere.place(x=1, y=1, width=80, height=100)
        label = tk.Label(ikinci_pencere, text="Pia", fg="red", bg="black", font=("Times", 24))
        label.place(x=15, y=35, width=70, height=30)
        destroy_button = tk.Button(ikinci_pencere, width=1, text="...", fg="black", font=("Helvetica", 9), background='white', command=ikinci_pencere.destroy)
        destroy_button.place(height=15, x=1, y=1)
        destroy_button.pack()
        scr1_button = tk.Button(ikinci_pencere, width=10, fg="black", font=("Helvetica", 9), background='white', text="Go back to Screen 1", command=self.goto_screen1)
        scr1_button.place(height=15, x=1, y=15)
        scr2_button = tk.Button(ikinci_pencere, width=10, fg="black", font=("Helvetica", 9), background='white', text="Go back to Screen 2", command=self.goto_screen2)
        scr2_button.place(height=15, x=1, y=30)
        scr2_button.pack()
        
        self.ikinci_pencere_button = tk.Button(master, width=1, text="...", fg="black", font=("Helvetica", 9), background='white', command=self.ikinci_pencere)
        self.ikinci_pencere_button.place(height=15, x=1, y=1)

   


root = tk.Tk()
screen1 = Screen1(root)

root.mainloop()





