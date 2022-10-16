"""yaslar=[7,15,18,24,36]
def yetiskinmi(x):
    if (x<18):
        return False
    else:
        return True
sonuc=list(filter(yetiskinmi,yaslar))
sonuc=list(filter(lambda x:x>=18,yaslar))
print(sonuc)"""
"""sayilar=[1,5,6,8,19,26,77,789]
sonuc=list(filter(lambda x:x%2==1,sayilar))#--->Tek sayıları getiren,fltrekeyen bir sınırlama yaptık.
print(sonuc)"""
"""isimler=["ali","kemal","sinem","kaan","eray"]
sonuc=list(filter(lambda x:x[0]=="k",isimler))#--->İsimleri k ile başlayanları sınırladık.
secim=filter(lambda x:x[0]=="k",isimler) #-----> Burda yine ismi k ile başlayan iismleri aldık.Kullanacağız.
sonuc=list(map(lambda x:x.capitalize(),secim))#---->Burda seçtiğimiz k ile başlayan kişilerin isimlerinin baş harflerini büyük yaptık.
print(sonuc)"""
users=[{"username":"brkyalt","posts":[]},
{"username":"brkyaltintas","posts":["post1","post2"]},
{"username":"berkayaltintas","posts":["post1","post2","post3"]}
]
sonuc=list(filter(lambda u: len(u["posts"])>0,users))#post sayısı 1 den büyük olanları getirmiş oldu.
sonuc=list(map(lambda u:u["username"],filter(lambda u:len(u["posts"])>0,users)))#-->Burada  0 dan fazla paylaşımı olanların isimlerini getirdik.
sonuc=[user["username"] for user in users if len(user["posts"])>0]#BU DAHA KISA YOLU.
print(sonuc)