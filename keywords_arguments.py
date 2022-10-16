def fullName(firstName,lastName):
    return (f"Sisteme Hoş Geldiniz {firstName } {lastName}")
sonuc=fullName("Berkay","Altıntaş")
sonuc=fullName("Altıntaş","Berkay")#Keywordsler tamda burda  işimize yarar.Buralarda karmaşıklık olabilir.
sonuc=fullName(lastName="Altıntaş", firstName="Berkay")
print(sonuc)
#sonuc=fullName(lastName="Altıntaş", firstName="Berkay")
"""Bu şekilde kullanırsak sıkıntı olmicaktır.Karışma durumu vs olmayacaktır. """