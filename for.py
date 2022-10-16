#For Döngüsü
from re import X


sayilar=[1,3,6,8,12,16] #Bir liste oluşturduk.[] ile liste oluşturuyorduk.
#print(sayilar[0]) #Bu şekilde indeximizi içinden çekebiliyorduk.Sırasıyla indexlerimizi çekebiliyoruz.
#For kullanımı

#for i in sayilar:
    #print(i) # Bu şekilde dediğimizde sırasıyla kullanmaktayız. Burada i değişkeni atamış durumdayız.
    #String bir ifadeyle yazalım.
#for i in sayilar:
   # print("Merhaba") #Bu bir döngü olduğundan dolayı o kadar merhaba getircektir.
#String ifadelerlede oluşturabiliriz.
#isimler=["sinem", "barış","mert","ayşe"]
#for isim in isimler: #For dan sonra in geliyor.For ile in arası bir değişken ataması yapmaktayız.
    #print(isim)
#isim="Berkay Altıntaş"
#for i in isim:
    #print(i) # Bu ifade teker teker sıralatçaktır.
#Bir tuple(demet) oluşturalım.
#_tuple=[(1,2),(3,4),(6,9)] #Tuple oluşturulurken () kullanılmaktadır.#Burada bir eşleşme durumu vardır.
#for x,y in _tuple:
    #print(x) #Sadece x dersek x kısımlarındadiki alcaktır.
    #print(x,y) şeklinde dersek eşleşmiş bir şekilde gelecektir.
#Şimdi bir sözcük oluşturalım.
iller={"01":"Adana","02":"Adıyaman","03":"Afyon","04":"Ağrı"} #Bir key=value oluşturduk.Sözlük oluşturduğumuzda {} kullanıyoruz.
#for i in iller:
   # print(i) #= Bu şekilde dersek x olduğu için sadece plakalar getirecektir.
    #print(iller[i]) # Burada şunu diyoruz.İllerin içindeki indexlere göre getirmeni istiyorum.
    #Ya da şuı şekilde yapabiliriz.
   # for key,value in iller.items():
        #print(key,value)
for i in iller.values(): # Bu values şeklinde değerleri getirebiliriz.
    print(i)







