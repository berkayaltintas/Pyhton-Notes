#Yeni bir liste oluşturalım
iller=["İstanbul","Ankara","İzmir","Bursa"]
sonuc=iller[0]
sonuc=iller[0][2] #Sıfırıncı ındexin içindeki içndeki ikilnci index e ulaştık.
sonuc=iller[0:2]  #Burada ilk şart sağlanması gerekir fakat ikinci şart dahil değil.
sonuc=iller[:3]   #Burada başlangıç şartı vermiyoruz.3 e kadar 3 dahil değil a diyoruz.
sonuc=iller[-1]   #Burada -1 dersek sonuncu indexi al demek istiyoruz.
iller[0]="Tekirdağ" # Burada ilk indeximizi değişitirdik.Değiştirmek istediğimiz indeximizi yazıyoruz.Yerine alcak şeyi yazdık.
sonuc=len(iller) #Burada len fonksiyonu içinde bulunan fomksiyonu sayıyor uzunluğu ölçüyor.
sonuc= iller +["Adana","Sivas"] #Burada listemize eleman nasıl eklenir onu görmüş olduk
del iller[1] #Burada silme işlemi nasıl yapılıyor görmüş olduk.
print(sonuc)
