ogrenci_bilgileri = {"ayşe öztürk":{"Matematik":"48","Kimya":"73","Fizik":'66'},
                    "merve kaya":{"Matematik":"85","Kimya":"43","Fizik":'75'}, 
                    "enes ekici":{"Matematik":"93","Kimya":"76","Fizik":'58'},
                    "sevgi yılmaz":{"Matematik":"90","Kimya":"30","Fizik":'6'}}
isim = input("Öğrencinin ismini giriniz: ").strip().lower()
ders = input("Hangi ders notunu öğrenmek istiyorsunuz: ").strip().title()
print(ogrenci_bilgileri[isim][ders])

ogrenci_bilgileri["fatma özdemir"]={"Matemetik":67,'Kimya':30,'Fizik':46}
ogrenci_bilgileri["sevgi yılmaz"]["Matemetik"] = 45
print(ogrenci_bilgileri)

if isim in ogrenci_bilgileri:
    if ders in ogrenci_bilgileri[isim]:
        print(f"{isim} öğrencisinin {ders} dersi notu: {ogrenci_bilgileri[isim][ders]}")
    else:
        print(f"{isim} öğrencisinin bu dersi bulunmamaktadır.")
else:
    print("Bu öğrencinin bilgileri bulunmamaktadır.")
