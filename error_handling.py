#Hata yönetimi 
while True:#Döngü döndürüyoruz.
    try:
        a=int(input("a : "))
        b=int(input("b : "))
        print(a/b)
    except (ZeroDivisionError,ValueError)as e:
        print("bir hata alındı.")
        print(e)
    except Exception:
        print("Bilinmeyen bir hata oluştu.")
    else:
       break
    finally:
        print("Finally bloğu çalıştı.")