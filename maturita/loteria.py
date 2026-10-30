import random
input = input('zadaj cisla')
user = input.split()
vyhra = []
y = 0
pocetvyhr = 0
vyhcis = ''
for i in range(6):
    vyhra.append(str(random.randrange(1,49)))
while y < 6:
    if user[y] in vyhra[y]:
        vyhcis += user[y]
        pocetvyhr += 1
    y += 1
if pocetvyhr == 0:
    print('nevyhral si nic')
else:
    print(vyhcis, pocetvyhr)

txt = open('/home/polonec/Downloads/loteria_1.txt')
pocetvyh = 0
vyherci = [0,0,0,0,0,0]
for line in txt:
    line.strip()
    for num in line:
        if num in vyhra:
            pocetvyh += 1
    if pocetvyh != 0:
        vyherci[pocetvyh-1] += 1
    pocetvyh = 0
print(vyherci)
