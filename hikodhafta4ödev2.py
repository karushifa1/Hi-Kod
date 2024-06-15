liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]

# "3" değerine ulaşmak için indexleme
print(liste[3])  

# "Hi-Kod" değerine ulaşmak için indexleme
print(liste[5])  

# 4.7 değerine ulaşmak için indexleme
print(liste[7])  

# 9, "3", 8.4, "Hi-Kod" değerlerine ulaşmak için slicing
print(liste[2:6])  

# 8.4, "Hi-Kod", "False", 4.7 değerlerine ulaşmak için slicing
print(liste[4:8]) 

liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]

# Boş bir liste 
yeni_liste = []

for string in liste:
    # Eğer öğe string veri tipindeyse yeni_liste'ye ekle
    if type(string)==str:
        yeni_liste.append(string)
print(yeni_liste)

meyveler = ['0 için boşluk elemanı',"elma", "portakal", "erik", "şeftali"]

for index, meyve in enumerate(meyveler):
    print("{}. meyve: {}".format(index, meyve))


