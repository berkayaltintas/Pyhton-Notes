"""
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
print( f"Aktif kullanıcı sayısı {User.active_users}")"""
#Burada class attributes kullanmıştık.Şimdi sınıf metodlaraını kullancağız.

class User:
    active_users=0
    @classmethod #Bunun class metodu olabilmesi için bir decorator kullanmamız lazım.Bunun altında kullandığımız şeyi class method yapar.
    def display_active_users(cls):
        return f"{cls.active_users} tane aktif kullanıcı vardır." 
    @classmethod
    def  from_string(cls,data_str):
        username,name,surname,age=data_str.split(",")
        return cls(username,name,surname,age)

    def __init__(self,username,name,surname,age):
        self.username=username
        self.name= name
        self.surname= surname 
        self.age=age
        User.active_users+=1 #Burada kullanıcıları oluşturuyorduk.
        #Class metodu oluşturarak kullanıcıları oluşturalım.

    def userName(self):
        return f"{self.username}"
    def logout(self):
        User.active_users-=1
        return f"{self.username} programdan çıkış yaptı."
        User.active_users-=1 
#print( User.display_active_users())
# user1=User("BerkayAlt","Berkay","Altıntaş",24)
# user2=User("Kayasrc","Kaya","Sarıçiçek",39)
# user3=User("FernandoM","Fernando","Muslera",35)
# user4=User("FernandooM","Fernandoo","Musleraa",36)
user5=User.from_string("crseven,Cristano,Ronaldo,36")
# print(user2.logout())
print(User.display_active_users())