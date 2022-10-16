from ssl import enum_certificates


diller=["python","javascript","Flutter"]
#index=0
#for i in diller:
#print(diller[index])
    #index+=1

#obje=enumerate(diller) ile yapılabilir.


#for i in enumerate(diller):
    #print(i)
for index,value in enumerate(diller,1):# Buradaki biri bu şekilde kullanabilmekteyiz. 1 burda başlangıçı temsil etmektedir.
    print(f'{index}-{value}')