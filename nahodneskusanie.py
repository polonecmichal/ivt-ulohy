#mahodne skusanie
from random import randrange
otazky = []
ziaci = []
cnt1 = 0
cnt2 = 0
n = 0

pocetziak = int(input('zadaj pocet ziakov'))
potazky = int(input('zadaj pocet otazok'))

if potazky < pocetziak:
    print('chyba')
    exit()

while cnt1 < pocetziak:
    otazka = randrange(0,pocetziak)
    if otazka not in otazky:
        otazky.append(otazka)
        cnt1 += 1

while cnt2 < potazky:
    ziak = randrange(0, potazky)
    if ziak not in ziaci:
        ziaci.append(ziak)
        cnt2 += 1
while n < pocetziak:
    print(f'ziak cislo',ziaci[n],'ma otazku', otazky[n])
    n += 1
