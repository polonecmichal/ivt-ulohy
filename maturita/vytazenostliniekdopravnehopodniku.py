pocetzastavok = 0
zastavky = []
ans = ''
ludze = 0
max = 0
txt = open(r'/home/polonec/Downloads/bus_vytazenost.txt', encoding='cp1250')
for line in txt:
    if len(line) > 3:
        line = line.strip()
        pocetzastavok += 1
        zastavka = line.split(' ')
        zastavka = ' '.join(zastavka[2:])
        zastavky.append(zastavka)
        ans = ', '.join(zastavky)
        ####
        nastup = line[:2]
        vystup = line[3:5]
        ludze += int(nastup)
        ludze -= int(vystup)
        if ludze > max:
            max = ludze
            alert = zastavka
        if ludze > 50:
            print('COAL ALARM!!!!!!!!, na stanici', zastavka)
print('pocet zastavok je:', pocetzastavok, ans, ludze, 'najviac bolo', max, alert)