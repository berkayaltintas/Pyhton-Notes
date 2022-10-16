from posixpath import split


#yazi="benim adım levent öztunanılılar.İstanbul'da yaşıyorum.".split()
#Split fonksiyonu teker teker (boşluklu olarak ayrıştırmaktadır)'benim', 'adım', 'levent', "öztunanılılar.İstanbul'da", 'yaşıyorum.'
#print(yazi)
#print(yazi[0]) # indexleme işlemi yapmaktayız.İlk eleman 0 ile başlıyor.
#print(yazi[2][0]) #iki defa üst üste indexleme yaptık.(yazinın içinden ikini index 2 aldık.ikinci içinden 0 ırı aldık.)
#sayilar=[1,2,3,4,5,6]# [] kapalı parantez liste oluşturmak için kullanılır.
#sonuc=sayilar
#sonuc=sayilar[4] #dördüncü index olan 5 i verir.
#sonuc=sayilar[6] #list index of range hatası ( 6 ıncı index yok anlammında)
#print(sonuc)
isimler=["mert", "ceyda","ahmet","berke"]
#print(type(isimler[2])) #burada classını yazdırıyoruz.Eğer içine inersek [] yazarsak str olduğu gözükür.
#her bir kişiye liste yapabilirz.Bir liste string,float ,int değerler içerebilir.Sıralıdırlar.
listemert=["mert",18]
listeceyda=["ceyda",24]
ogrenciler=[listemert,listeceyda]

sonuc=ogrenciler[1]
print(sonuc) 
