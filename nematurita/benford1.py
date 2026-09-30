from random import randrange
opakovanie = 10000
cisla = {}
ans = ''
for i in range(1,10):
    cisla[i]=0
for n in range(1,opakovanie):
    cislo1 = randrange(1,100)
    cislo2 = randrange(1,100)
    cislo = cislo1**cislo2
    cifra = int(str(cislo)[0])
    cisla[cifra] += 1
print(cisla)

for i in cisla:
    numbers = cisla[i]/opakovanie*100
    numbers = round(numbers, 2)
    nom = str(numbers) + ' ' + '%'
    ans += nom + ' '
print(ans)
