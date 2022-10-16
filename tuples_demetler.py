#Tuples (Demetler) Değiştirelemezlerdir.
list1=[1,3,5,13,3]#Lİstede normal parantez kullanılır.
thistuple=(1,3,"altı",False,2)#Tuple oluştururken normal parantez kullanırız.
thistuple2=(1,4,"beş",True,2)
print(type(list1))
#print(type(thistuple)) #Typlarını bulmak için böyle diyoruz.
#print(list1[0])
#print(thistuple[1]) #içindeki indexlerini böyle buluyoruz
#print(len(list1))
#print(len(thistuple))# Burda uzunluğu ölçmekteyiz.
#Tuple(Demetler) değiştirelemezler.Yani append metodu veya insertmetodu pop metodu remove metodu kullanılmaz.
#Bir elemanın kaç defa geçtiğini ,indexini hesaplatabiliriz.
#print(list1.count(3))
#print(thistuple.count(3))
#İki demet birbiriyle toplanabilmektedir.
print(thistuple+thistuple2)
#Bilgilerin kalıcı olmasını istediğimizde bu metodu kullanıyoruz.


