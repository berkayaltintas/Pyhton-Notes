
#open(dosya_adı,dosya_erisme_modu) -->Bu şekilde dosyaları açabiliyoruz.
#Dosya açma modu hangi amaçla açtığımızı belirtiyor.
#UTF-8 Türkçe karakterleri kabul eden türkçe bir format.
f = open("text.txt") #hiç bir şey yazmaz isek #r=read olarak düşünebiliriz.
# print(f)
# print(help(f))
print(f.read())