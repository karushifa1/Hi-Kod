#1
r=int(input('yaricap: '))
alan=3.14*r**2
print(alan)
print('alan: '+ str(alan))

#2
def faktöriyel(n):
    faktoriyeldeger = 1
    for i in range(1, n + 1):
        faktoriyeldeger *= i
    return faktoriyeldeger

sayı = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))
print("{} sayısının faktöriyeli: {}".format(sayı, faktöriyel(sayı)))

#3
def yas():
    yıl=int(2024)
    yas=int(yıl-dogumyılı)
    return yas
dogumyılı=int(input('doğum yılınızı girin'))
yas = yas()
print(yas)

#4
def emeklilik():
    isim=input('isminizi girin')
    dogumyılı=int(input('doğum yılınızı girin'))

    def yas():
        yıl=int(2024)
        yas=int(yıl-dogumyılı)
        return yas
    yas = yas()

    if yas>=65:
        print('emekli oldunuz.')
    if yas<65:
        kalanyıl=65-yas
        print(f'{isim}, Emekli olmanıza {kalanyıl} yıl kadı.')
emeklilik()