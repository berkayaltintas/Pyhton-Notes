#While döngüsünde bir koşul vererek başlıyoruz.

#while i<10:
    #print(i)
    #i+=1 # Görüldüğü gibi 0 dan 9 a kada döngü devam edene kadar yazdırmıştır.
    
#0 dan 100 e kadar tek sayıları bulalım.
"""i=0
while i<100:
    if ( i%2==0 ):# Burada i%2 demek kalanının çift sayıya eşit olması demek
        print("çift sayı :", i)
    else:
        print("tek sayi:", i)
    i+=1 # Buranın 1 altında if altında arttığına dikkat etmelisin. """
email = "" # Email burda boş bir şeyi temsil ediyor.
while not email:
    email=(input("Mail adresinizi giriniz."))
print("girediğiniz email adresi:", email )
