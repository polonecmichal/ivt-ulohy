#vytazenost dopravneho podniku
txt = open(r'/home/polonec/Downloads/bus_vytazenost.txt', encoding='1250')
counter = 0
ans = ''
ludia = 0
ludmax = 0
#pocet zastavok
for line in txt:
    if len(line) > 3:
        counter += 1
        riadok = line.split()
        zastavka = riadok[2:]
        ans += ' ' + ' '.join(zastavka) + ','
        ludia += int(riadok[0])
        ludia -= int(line[3:5])
        if ludia > 50:
            print('na zastavke', riadok[2:])
        if ludmax < ludia:
            ludmax = ludia
print('max je', ludmax, ans)