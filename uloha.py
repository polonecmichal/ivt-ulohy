import random
cisla = input()
y = 0
hrac = cisla.split()
vyhra = []
vyhcis = ''
pocetvyhcis = 0
for cisla in range(6):
    vyhra.append(str(random.randrange(1,49)))
while y < 6:
    if hrac[y] in vyhra:
        vyhcis += hrac[y]
        pocetvyhcis += 1
    y += 1
print('hrac vyhral', pocetvyhcis, 'a boli to', vyhcis)

txt = open('/home/polonec/Downloads/loteria_1.txt')
vyherci = [0,0,0,0,0,0]
nieco = 0
for line in txt:
    riadok = line.split()
    for num in line:
        if num in vyhra:
            nieco += 1
    if nieco != 0:
        vyherci[nieco-1] += 1
    nieco = 0
print(vyherci)