#Burada sınıfa olan dahil attributes ları öğrenmeye çalışacağız(objelere olan değil.)
#Aktif kullanıcı sayısının belitmemiz gereken yer sınıfın içidir.
class User:
    active_users=0
    def __init__(self,username,name,surname,age):
        self.username=username
        self.name= name
        self.surname= surname #Yeni kişiyi burda oluşturuyoruz.
        self.age=age #init kavramı objeden bağımsız bir kavramdır.Tanımlamadır.
        User.active_users+=1 #Class üzerinden erişiyoruz.

    def userName(self):
        return f"{self.username}"
    def logout(self):
        User.active_users-=1
        return f"{self.username} programdan çıkış yaptı."
        User.active_users-=1 #Sistemden çıkışları gösteriyoruz.
print( f"Aktif kullanıcı sayısı {User.active_users}")
user1=User("BerkayAlt","Berkay","Altıntaş",24)
user2=User("Kayasrc","Kaya","Sarıçiçek",39)
user3=User("FernandoM","Fernando","Muslera",35)
user4=User("FernandooM","Fernandoo","Musleraa",36)
print(user2.logout())
print( f"Aktif kullanıcı sayısı {User.active_users}")