#Varsayılan parametre gönderiyoruz.Şu şekilde yapıyoruz.
# def selamla(isim,mesaj): # def selamla(isim="Kullanıcı", mesaj="Hosgeldin") şeklinde atama yapmaktayız.
#     print(f"{mesaj} {isim}")
# selamla("Mehmet", "Merhaba")
# selamla("Kaya") # Bu şekilde tek bir parametre gönderirsek ( İki parametre vardı.) Type hatası alıyoruz.
"""Şu şekilde yapalım."""
def selamla(isim, mesaj="Hosgeldin"): #Varsayılan parametreyi yapmasaydık Type hatası almış olacaktık.
    print(f"{mesaj} {isim}")
selamla("Selin") # Bu şekilde yaptığımızda doğol olarak parametreyi atama yapmış oluruz.
