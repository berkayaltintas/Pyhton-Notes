

#sayı 1 = 10 sayı 2 = 15x girilsin mesela.
#Alacağamız hata ş şekilde olacaktır.
# Value error olarak almaktayız.

# try:
    #hata olabilecek blok.
# expect:
     #hata mesajı
    # 
try:  
    a=int(input("sayı 1 : "))
    b=int(input("sayı 2: "))
    print(a+b)
except:
    print("Hata Oluştu.")
     
