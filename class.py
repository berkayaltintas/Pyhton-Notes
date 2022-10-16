#Tanımlamak için class keyword kullanmaktayız.
#class tan sonra taımladığımız sınıf adının ilk adı büyük harfle olmalıdır.
class Arac:
    #method
    #attribute 
    pass # İçine bir şey yazmadığımızda pass kullanarak hata almayabiliriz.

#ınstance,Objecet
#obje üretmeye çalışalım.
arac1=Arac()
arac2=Arac() #parantez içine özellikleri yazıcaz.
print(type(Arac)) # bunu yazarak arac şeklinde bir classa sahip olmuş oluyoruz.
print(arac1)#bunu yazarsak kayıtlı olduğu adresi görebiliriz.
print(arac1,arac2) #Adresleri görebilmekteyiz.

class Products:
    pass

p1=Products()#Monster Abra Serisi
p2=Products()#iphone13
p3=Products()#Ipad #Ürünlerimizi bu şekilde oluşturmuş olduk.

listProducts=[p1,p2,p3]

for p in listProducts:
    print(p)
    print(type(p)) # Böyle dersek classını alabiliriz.