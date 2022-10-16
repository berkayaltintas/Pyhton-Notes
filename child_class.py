class Person:
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
        print("Person nesnesi oluşturuldu.")
    
    def info(self):
        print(self.name,self.surname,self.age)

class Student(Person):
    def __init__(self,name,surname,age,number):
        Person.__init__(self,name,surname,age)#Parametreleri gönderebilmek için inite ihtiyaç var.
        self.number=number
        print("Student  nesnesi eklendi.")
    def ortalama_al(self):
        print(f"{self.number} bu numaralı öğrencinin not ort alındı")
      
    #number dahil etmemiz gerekiyor.


class Teacher(Person):
    def __init__(self,name,surname,age,branch):
     
        Person.__init__(self,name,surname,age)        # Person yerine super kullabiliriz.Self ile super eşleşmektedir.
        self.branch=branch                       #Person kullanırsak(class adı) => self yazmak zorundayız. 
  
        print("Teacher  nesnesi eklendi.")  
    def teach(self):
        print(f"{self.name} nın mesleği {self.branch}" )

p1=Person("Ilgım","Şentürk",23)
p1.info()#print(p1.name,p1.surname,p1.age)

s1=Student("Berkay","Altıntaş",25,5160000588)
#s1.info()#print(s1.name,s1.surname,s1.age)
#s1.ortalama_al()
t1=Teacher("Nazlı","Altan",26,"Mathematic Teacher")
#t1.info()#print(t1.name,t1.surname,t1.age)
t1.teach()

