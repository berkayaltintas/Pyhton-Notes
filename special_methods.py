liste=[1,2,3,4]
print(len(liste)) #bunu yaparak uzunluğunu bulabiliyorduk.

isim="BerkayAltıntaş"
print(len(isim))#Yine uzunluğu hersaplattık.(Kaç harf var)
#Bir sınıf oluşturalım.

class Urun:
    def __init__(self,urunKodu,urunAdı,fiyatı):
        self.urunKodu=urunKodu
        self.urunAdı=urunAdı
        self.fiyatı=fiyatı #objelerimizi bu şekilde tanımladık.
    def __len__ (self):
        return self.fiyatı #BU şekilde dersek print(len(urun1)) çalışacaktır
    def __str__(self):
        return f"İsmi ={self.urunAdı}  kodu= {self.urunKodu} ürün listelendi"
    def __repr__(self):
        return f"İsmi ={self.urunAdı}  kodu= {self.urunKodu} ürün listelendi" #__str__ ve __repr__ aynı dır.
    def __del__ (self):
        print("Ürün silindi") #Ürünü silmek için bu fonksiyonu yazmaktayız.


urun1=Urun("123456","Tv",10000)
print(len(urun1)) #Bu şekilde çalıştırmak için fonksiyona ihtiyac duymaktayız.
print(str(urun1))
del urun1