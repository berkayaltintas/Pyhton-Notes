#Sistemde bazen durmasını isteyebiliyoruz.
#isim="Levent Öztunalılar"
#for harf in isim:
    #print(harf) #Bu şekilde yaptığımızda hangi harfin olup olmadığına bakabiliyorduk.
#for harf in isim:
   # if (harf=="v"):
        # break # Şu şekilde break içeriye yazılmış durumda olcaktır.Burada durduruyor.
   # print(harf) # Şekilde de görüldüğü gibi çıktısı l ve e olcaktır.

#i=0
#while (i<10):
    #i+=1 #Bu şart sağlansın fakat  aşağıda şart oalrak belirttiğimiz gibi 5 olmasın. Ara versin.Continue kullamı bu şekilde olcaktır.
    #if (i==5):
       # continue
    #print(i)
    #1 İLE 100 ARASINDAKİ TEK SAYILARINI TOPLAYALIM.
i=0
toplam=0
while (i<=100):
    i+=1
    if (i%2==0):
        continue
    toplam+=i
print(f'toplam:{toplam}') # Burada f string kullandık f'araya yazıyoruz'

    
