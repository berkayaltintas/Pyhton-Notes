#Biz args kullanırken tuple tarzında alıyordk.Kwargs larda ise sözlük olarak almaktayız.
#İlk olarak type larına bakalım.

# def userInfo(*args):
#     print(type(args))
# userInfo() #Type olarak TUPLE

# def userInfo(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
# userInfo(isim="Berkay",email="berkayaltintastr@gmail.com",soyad="Altıntas",telno="5324578901") #Type olarak DICTIONARY
def userInfo(**kwargs):
    for key,value in kwargs.items():#Dictionaryde bu şekilde sıralama yapılabilmektedir.Önemli. items unutma.
        print(f"{key}{value}")
userInfo(isim="Berkay",email="berkayaltintastr@gmail.com",soyad="Altıntas",telno="5324578901")