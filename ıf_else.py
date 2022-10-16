#sayi=5
#if (sayi < 5 ): # if(eğer) koşuluından sonra bşluk koşulu yaz.Parantez aç sonra : koy alta şartı yaz.
   # print("Sayi negatiftir.")
#else: #else koşulu yukardaki şartın değili olarak yazabiliriz.
   #print("Sayi pozitfitir.")    
#giris= False
#if (giris):  #giris zaten değer aldığı için giris==True demezsekte çalıştırcaktır
    #print("Hoşgeldiniz.") # False dediğimiz zaman çıktı vermicektir. Şİmdi başka bir uygulama yapalım.

username="brkyaltntss"
password= "19971943"    #And operatörü ile iki şartı biribirine bağladık.#Or kullansaydık iki şarttan birini sağlaması yeterli olcaktı
#if (username=="brkyaltnts") and (password=="19971943"):
    #print("Sisteme giriş yaptınız")
#else:
    #print("Girilen bilgiler hatalıdır.")
    #Hangi bilgimizin hatalı olduğunu söyletebiliriz.
if (username=="brkyaltnts"):
    if(password=="19971943"): #İç taraflardaki else blokları birbirine  bağlıdır.Aynı hisaza olmasına dikkat et.
        print("Sisteme başarı ile giriş yaptınız.")
    else:
        print("Kullanıcı şifreniz hatalıdır!") #if içinde if kullanılabilmektedir.
else:
    print("Kullanıcı adınız hatalıdır!")#En dışardakiler birbirine bsğlı durumdadır.







