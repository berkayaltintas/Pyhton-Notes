
"""class Product:
    def __init__(self): #Self burda içine gönderdiğimiz ürünleri temsil edecektir.
        self.name="Mercedes A" #fonksiyon 2 defa okunduğunda hep aynı gelcek.name parametresini atamamız lazım.  
        self.price="600000" 
        print("Product nesnesi oluşturuldu")

p1=Product()
p2=Product() # Objelerimizi oluşturduk

print(p1.name,p1.price) #Bu kullanım olduğunda yanlış olcaktır.Fonksiyon 2 defa çalışacaktır. 
print(p2.name,p2.price)"""
#her bir ürün için self parametresi ürünümüzü ifade ediyor.Name parametresi adını price parametresi fiyatını belirtiyor.
class Product:
    def __init__(self,name,price,isActive): #Self burda içine gönderdiğimiz ürünleri temsil edecektir.
        self.name= name #fonksiyon 2 defa okunduğunda hep aynı gelcek.name parametresini atamamız lazım.  
        self.price=price
        self.isActive=isActive #Bunu teker teker tanımlamak için isActive=True default değer olarak ta atayabiliriz.
        print("Product nesnesi oluşturuldu")

p1=Product("Mercedes A","600000",True)
p2=Product("BMW 320","500000",False) # Argümanlarımızı vermemiz gerekecektir.
p3=Product("Passat","450000",True)
print(p1.name,p1.price,p1.isActive)
print(p2.name,p2.price,p2.isActive)
print(p3.name,p3.price,p3.isActive)

#Stokta var mı yok mu onu belirtmek için isActive olarak tanımlama yapabiliriz.
