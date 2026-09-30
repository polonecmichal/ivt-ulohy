txt = open('/home/polonec/Downloads/skok_do_dialky.txt', 'r')
max = 0
pocty = {}
ans = []
for line in txt:
    riadok = line.split()
    stat = riadok[1]
    pocty.setdefault(stat, 0)
    pocty[str(stat)] += 1
    for i in range(2,6): 
        if int(riadok[i]) > int(max):
            max = riadok[i]
            ans.clear()
            ans.append(riadok[1])
        elif int(riadok[i]) == int(max):
            ans.append(riadok[1])
for i in pocty:
    print(i, end=' ')
print(pocty, max, 'z',ans)

def bs():
        #skok do dialky
    txt = open('/home/polonec/Downloads/skok_do_dialky.txt', 'r')
    dct = {}
    max = 0
    maxi = []
    for line in txt:
        line = line.split()
        for n in range(2,6):
            if int(line[n]) > int(max):
                max = line[n]
                maxi.clear()
                maxi.append(line[0])
            elif int(line[n]) == int(max):
                maxi.append(line[0])
        stat = line[1]
        dct.setdefault(stat, 0)
        print(stat)
        if stat in dct:
            dct[stat] +=  1
    print(dct, maxi)