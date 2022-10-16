# *args kullanımında değişken sayıda parametre gönderebiliyoruz.
# numbers=[5,10,15,20]
# def topla(a,b):
#     return a+b

# def topla(a,b,c):
#     return a+b+c

# def topla(sayilar):
#     sonuc=0
#     for i in sayilar:
#         sonuc+=i
#     return f"Sayıların toplamı : {sonuc}"
# print(topla(numbers))
#--------------------Parametre sayısını bilmediğimiz durumlarda istediğimiz kadar parametre gönderebiliyoruz.*args kullanımı ile.
def topla(*args):# *args ile değişken sayıda parametre gönderiyoruz.
    sonuc=0
    for i in args: # * = Değişken sayıda parametre kullanımı yapıyoruz demek.
        sonuc+=i
    return sonuc
print(topla(1,2,3)) # return ile sonuc döndürüyoruz.#Burada herhangi bir liste tanımlamaya gerek kalmıyor.
print(topla(50,60,70,80))
print(topla(1,2,3,4,5,6,7,8,9))