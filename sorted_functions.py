sayilar=[2,7,88,13,6]
# #sayilar.sort()#sort burda sıralama işlemi yapmaktaydı.
# sonuc=sorted(sayilar)
# print(sonuc)
# print(sayilar)
#Sorted fonksiyonunu kullanırken yeni bir değişkene yeni halini atıyoruz. 
#Listenin sıralaması değişmemektedir.
sonuc=sorted(sayilar, reverse=True) #Eğer böyle dersekte büyükten küçüğe sıralamış oluruz.
sonuc=sorted((2,67,81,9,64,55)) # içine tuple koyduk.
#içine tuple koymamıza rağmen çıkan sonuç Sıralanmış bir liste şeklindedir.
print(sonuc)
#Sorted sıralama için kullanılır.