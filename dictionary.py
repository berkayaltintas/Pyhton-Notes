#34->İstanbul 35->İzmir
#sehirler=["İstanbul","İzmir"] #İki tane liste oluşturmuş durumdayız.
#plakalar=[34,35]
#Bunları eşleştirmek istediğimizde şu şekilde yapabliirz.
#print(sehirler[0],plakalar[0]) #Şekildeki gibi indexleri çekebilirilz.
#print(sehirler[1],plakalar[1])
#print(plakalar[sehirler.index("İstanbul")])
#Dictionary=Sözlük kalıplarında key=value değerleri bulunmaktadır. şimdi szölük oluşturalım
plakalar={"İstanbul": 34 ,"İzmir":35}# Sözlüklerde süslü parantez kullanılmaktadır.
#print(plakalar["İzmir"])#Kısaca böyle yapılabilmektedir.
#EĞER SÖZLÜĞE BİR ŞEY EKLEMEK İSTERSEK
plakalar["Eskişehir"]=26
print(plakalar)
# Bir şeyin birdeb fazla çeşidi olabilir
urunler ={100 : { "urunadı":"screen",
"urunacıklaması":"onaltı ınch", # Burada birden fazla olacak şekilde listeler oalbilmektedir.Süslü parantez kullanımı olcak.
"garantisuresi": "üçyıl",
"fiyatı":[600,650]}, 
101:
{ "urunadı":"ssd",
"urunacıklaması":"256gb",
"garantisuresi": "ikiyıl",
"fiyatı":[600,800] } }
sonuc=urunler

print(sonuc)
tutar=urunler[100]["fiyatı"][1] + urunler[101]["fiyatı"][1]

print(tutar)
