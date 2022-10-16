#any ve all fonksiyonları true v eya false tarzında değer döndürmektedir.
# sonuc=all([True,False,True])#all hepsine bakmaktadır.Lİstede tel bir false değeri olsa dahi false değeri döndürür.
# sonuc=all([True,True,True])#hepsi true değerine sahip olduğu için true değeri gelmektedir.
# sonuc=any([True,False,False]) #any de bir tane true değeri varsa bile true değeri çıkar.
# print(sonuc)

# sayilar=[0,1,4,7,8,10,15]
# sonuc=[bool(sayi) for sayi in sayilar]
# sonuc=any([bool(sayi) for sayi in sayilar])
# sonuc=all([bool(sayi) for sayi in sayilar if sayi%2==1])#sadece tek sayıları almış olduk.
# sonuc=all([sayi%2==1 for sayi in sayilar ])
#print(sonuc)
isimler=["ali","arda","mehmet","didem"]
sonuc = [isim[0]=="a" for isim in isimler]
sonuc=any([isim[0]=="a" for isim in isimler])#ismi a ile başlayan en bir kişi var mı diye sormuş bulunduk

print(sonuc)

