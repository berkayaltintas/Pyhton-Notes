#Bizim fonksiyon içerisine listelere istediğimiz işlemi yaptırıp yeni liste oluşturabilceğimiz fonksiyonlardır.
# map fonksiyonu kullanmadan yapalım.
sayilar=[-1,5,-6,7,-12]
str_sayilar=["1","5","6","7","12"] #Bu şekilde oluştururken str tarzında oluşturduk.
isimler=["ayşe","fatma","hayriye","ahmet"]
kareleri=[]
kullanicalar=[ {"ad":"Berkay", "soyad":"Altıntaş"},
{"ad":"Berke","soyad":"Gümüştekin"} ]#Şeklinde bir liste oluşturabiliriz.

# for sayi in sayilar:
#     kareleri.append(sayi**2) #append ekleme metodu idi.
# print(kareleri) #map fonksiyonu kullanmadan bu şekilde yapabiliyoruz.
#----------
def kareAl(sayi):
    return sayi**2
sonuc=list(map(kareAl,sayilar)) # map(1,2)---> 1=fonksiyonu yaz. 2=Hangi listeyi kullanacağını yaz.
sonuc=list(map(lambda sayi: sayi**2,sayilar))#lambda fonksiyonunu kullanırken fonksiyonu çağırmamıza gerek kalmıyor.
sonuc=list(map(int,str_sayilar)) #int dönüştürmek istiyoruz nerden str_sayılardan
sonuc=list(map(abs,sayilar)) #Burada kullanılan abs pozitif tam sayıya çevirmek için kullanılırdı.sayilar=[-1,5,-6,7,-12] alındı.
sonuc=list(map(float,sayilar))#Bu şekilde ondalıklı sayılara çevrildi.
sonuc=list(map(str.capitalize,isimler))# str.capitalize baş harfleri büyütüyordu.
sonuc=list(map(str.upper,isimler))#İsimlerin harflerini büyüttü.
sonuc=list(map(len,isimler))#len fonksiyonu uzunluk ölçmek için kullanırdı.
sonuc=list(map(lambda x:x["ad"],kullanicalar)) # Bu şekilde bilgileri alabilmekteyiz.lambda ile fonksiyon çağırmamıza gerek yoktur.
sonuc=list(map(lambda x:x["soyad"],kullanicalar))
print(sonuc)
