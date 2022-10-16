#iki tane liste oluşturalım
sayilar=[100,3,90,14,37,36,3,3]
harfler=["a","b","f","k","s","v"]
sonuc=min(sayilar) #min veya max bulunan listesinin en küçük en büyüğünü alacaktır.Harfler için sonra gelen max olur.
sonuc1=min(harfler)
#print(sonuc1)
#Ekleme işlmeleri için #append ve #insert metodlarını kullanmaktayız.
#sayilar.append(20)# append dersek indexi en sona atacaktır.
#harfler.append("p") #append dedik harfler için ve en sona atmış durumda
#sayilar.insert(3,20)# insert komutumuzda istediğimiz yere ekleyebiliyoruz.Append fonksiyonundan farkı budur.
#harfler.insert(4,"ğ")#Dördüncü indexe eklemiş olduk.
#print(harfler)
#Silme işlemlerinde Pop ve Remove methodlarını kullanmaktayız.
#sayilar.pop()      #Pop fonksiyonun yerine bir şey yazmaya egrek yok en son elemanı ,indexi silmektedir
#harfler.pop()
#sayilar.remove(9) #Remove daha çok kullanılır.İstediğimiz indexi burda seçebiliyoruz.
#harfler.remove("ğ")
#print(harfler)
#Lİstelerde sıralama işlemleri Sort metodu küçükten büyüğe doğru sıralama yapacaktır.Reverse emtodu ile ters çevirme işlemi yapıyoruz
#sayilar.sort() #Görüldüğü gibi küçükten büyüğe doğru sıralnmıştır.Alfabe için alfabetik sıra gerçekleşir.
#harfler.sort() # Zatern sıralı olduğu için bunları görebilmekteyiz.
#sayilar.reverse() #Görüldüğü gibi ters çevirme işlemi yapılmıştır.Lİstenin en sonunu en başına getirir.
#harfler.reverse()
#COUNT metodumuzda liste içinde kaç tane geçtiğini hesaplıyor.
#print(sayilar.count(3)) # görüldüğüğ gibi 3 tane olduğu görülmüştür.
#index metodu ile kaçıncı da o indexin olduğu gözkür
#print(sayilar.index(90))
sayilar.clear()
print(sayilar) #Clear metodu ise listenin içini temizleyen fonksiyondur.
#print(sayilar)
