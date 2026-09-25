import random
otazky = []
studenti = []
cnt1 = 0
cnt2 = 0
ziak = 0
otazka = 0
n = 0

while cnt2 <30:
    ziak = random.randrange(0,30)
    if ziak not in studenti:
        studenti.append(ziak)
        cnt2 += 1
print(studenti, len(studenti))

while cnt1 <50:
    otazka = random.randrange(0,50)
    if otazka not in otazky:
        otazky.append(otazka)
        cnt1 += 1
print(otazky, len(otazky))
while n < 30:
    print(f'ziak cislo',studenti[n],'dostane otazku',otazky[n])
    n += 1