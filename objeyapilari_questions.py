# 1) Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.
#a=int(input("a:"))
#b=int(input("b:"))
#c=int(input("c:"))
#carpım = a * b * c
#print(carpım) # bunu bu şekilde yapabilmekteyiz.
#print("{} X {} X {} = {} dir" .format(a,b,c,carpım))#format kullanımı şekilde gibi bir düzen içine şekilde ki gibi yazdırıyoruz.
#Süslü parantez açıp şekilde ki gibi yazdırılmıştır.
# 2)Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
#Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
#kilo=int(input("kilonuz:"))
#boy=float(input("boyunuz:"))
#bdi=kilo/(boy**2)
#print("beden kitle endeksi:", bdi) # Bu şekilde kısaltılmış halde yapabiliriz.
# 3)Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
#yakan_miktar=float(input("Km başına yakılan : "))
#km=int(input("km : "))
#toplam_harcama= yakan_miktar * km
#print("toplam_harcama:" ,toplam_harcama)
# 4) Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
#ad=str(input("Adınız: "))
#soyad=str(input("Soyadınız"))
#numara=int(input("Numaranız")) # \n alta yazdırmak istediğimizde bu bilgiyi kullanıyoruz.
#print("\nBilgiler....")
# 5)Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
#print("{}\n{}\n{}" .format(ad,soyad,numara))
#a=int(input("a:"))
#b=int(input("b:"))
#print("değiştirilmeden önceki hali:\na:{} b:{}".format(a,b) )
#a,b=b,a
#print("değiştirildikten sonraki hali:\na:{} b:{}".format(a,b) )
# 6)Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
kenar1=int(input("kenar :"))
kenar2=int(input("kenar :"))
uzunluk = (kenar1**2 +kenar2**2)**0.5 #**2 hali ile karesini almaktayız.
print("Hipotenüs Uzunluğu:",uzunluk)
