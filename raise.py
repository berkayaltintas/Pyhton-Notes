
def users(username,city):#username city str girmediği durumda
    cities=["İstanbul","Ankara","İzmir","Bursa"]
    if type(username) is not str:
        raise TypeError("username str tipinde olmalıdır.")
    if type(city) is not str:
        raise TypeError("city str tipinde olmalıdır.")
    if city not in cities:
        raise ValueError("Böyle bir şehir bulunmamaktadır.")
try:
    users("berkay","istanbul")
except Exception as e:#Herhangi bir hata hepsini kapsaması açısından exception dedik.
    print(e)
else:
    print("giriş başarı ile tamamlandı")