import pyautogui
import time
import threading

# Sürekli tıklama fonksiyonu
def auto_click(interval):
    while auto_clicking:
        pyautogui.click()
        time.sleep(interval)

# Makroyu başlatıp durdurmak için tuş kontrol fonksiyonu
def toggle_auto_click():
    global auto_clicking
    if auto_clicking:
        auto_clicking = False
        print("Auto-clicker durduruldu.")
    else:
        auto_clicking = True
        print("Auto-clicker başlatıldı.")
        threading.Thread(target=auto_click, args=(0.1,)).start()

# Başlangıç durumu
auto_clicking = False

# Kullanıcıdan giriş alarak makroyu başlatıp durdurmak
print("Auto-clicker'ı başlatmak ve durdurmak için 'enter' tuşuna basın.")
while True:
    input()
    toggle_auto_click()

    
