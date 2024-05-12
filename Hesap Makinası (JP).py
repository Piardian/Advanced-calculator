import tkinter as tk
from tkinter import *
window = Tk()
def yaz(x):
    s = len(giris.get())
    giris.insert(s, str(x))

def islemler(x):
    global hesap
    global s1
    if x in "+-*/":
        hesap = x
        s1 = float(giris.get())
        giris.delete(0, 'end')
    elif x == "%":
        global yuzde
        yuzde = True
        s1 = float(giris.get())  # Yüzde işlemi için s1'i tanımla
        giris.delete(0, 'end')  # Yüzde işlemi için girilen değeri temizle
    else:
        giris.insert(END, x)

def hesapla():
    global s1
    global yuzde

    if 'yuzde' in globals() and yuzde:
        yuzde_degeri = float(giris.get())
        sonuc = (yuzde_degeri / 100) * s1
        sonuc_str = str(sonuc)
        giris.delete(0, 'end')  # Sonucu giris kutusuna eklemeden önce kutuyu temizleyin
        giris.insert(0, sonuc_str)
    else:
        try:
            s2 = float(giris.get())
            if hesap == '+':
                sonuc = s1 + s2
            elif hesap == '-':
                sonuc = s1 - s2
            elif hesap == '/':
                if s2 != 0:
                    sonuc = s1 / s2
                else:
                    sonuc_str = "Hata: Sıfıra bölme hatası!"
            elif hesap == '*':
                sonuc = s1 * s2
            sonuc_str = str(sonuc)

            if sonuc % 1 == 0:
                sonuc_str = str(int(sonuc))
            
            giris.delete(0, 'end')  # Sonucu giris kutusuna eklemeden önce kutuyu temizleyin
            giris.insert(0, sonuc_str)
        except ValueError: 
            giris.delete(0, 'end')
            giris.insert(0, "Hata: Geçersiz işlem!")

    if 'yuzde' in globals():
        yuzde = False  # Yüzde işleminin yapıldığını sıfırla

def sil():
    giris.delete(len(giris.get()) - 1)

def temizle():
    giris.delete(0, 'end')


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
window.bind("<Return>", lambda event: hesapla())
window.bind("<KP_Divide>", lambda event: islemler("/"),giris.delete(0, 'end'))  
window.bind("<KP_Multiply>", lambda event: islemler("*")) 
window.bind("<minus>", lambda event: islemler("-"))
window.bind("<plus>", lambda event: islemler("+"))
window.bind("<percent>", lambda event: islemler("%"))

window.mainloop()
