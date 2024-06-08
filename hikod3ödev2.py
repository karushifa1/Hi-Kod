#ödev1
maas=int(input('Maaşınız nedir?'))
if maas<=10000:
    print('Yeni maaaşınız ',maas-(maas*5/100))
elif maas<=25000:
    print('Yeni maaşınız ',maas-(maas*10/100))
elif maas<=45000:
    print('Yeni maaşınız ',maas-(maas*25/100))
else:
    print('Yeni maaşınız ',maas-(maas*30/100))
#ödev2
kullanıcı_adı=input('kullanıcı adı oluşturun')
sifre=input('şifre oluşturun')
sifreuzunluk=int(len(sifre))
if sifreuzunluk>=6:
    print('Hesabınız oluşturuldu')
if sifreuzunluk<6:
    print('Şifreniz en az 6 haneli olmalıdır.')
#ödev3
while True:
    kullanıcı_adı1 = input('Kullanıcı adı oluşturun: ')
    sifre1 = input('Şifre oluşturun: ')
    sifreuzunluk1 = len(sifre1)
    
    if 5 <= sifreuzunluk1 <= 10:
        print('Hesabınız oluşturuldu.')
        break 
    else:
        print('Şifreniz en az 5 en çok 10 haneli olmalıdır.')

#ödev4
kkullanıcıadı2 = input('Kullanıcı adınızı kaydedin: ')
sifre2 = input('Şifrenizi kaydedin: ')

for i in range(3):
    hesapacmaişlem1 = input('Şifrenizi giriniz: ')
    
    if hesapacmaişlem1 == sifre2:
        print('Giriş yapıldı.')
        break 
    else:
        yanlıs_hak = 2 - i  
        if yanlıs_hak > 0:
            print(f'Yanlış şifre girildi! Kalan hakkınız: {yanlıs_hak}')
        else:
            print('Üzgünüz, üç yanlış deneme hakkınızı kullandınız.')
            break  













