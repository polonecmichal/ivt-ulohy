txt = open('/home/polonec/Downloads/meteo_stanice.txt', 'r')

linecount = 0
teploty = ''
zoz = []
n = 0
for lines in txt:
    if len(lines) != 0:
        linecount += 1
    riadok = lines.strip()
    teploty += riadok[21:26] + ' '
    temp = riadok[21:26].replace(',','.')
    zoz.append(float(temp))
linecount = 0
print(teploty, max(zoz), round(sum(zoz)/len(zoz), 2))
n = zoz.index(max(zoz))
txt.seek(0)
for lines in txt:
    if linecount == n:
        print('najvacsia je', lines[:3])
        break
    if len(lines) != 0:
        linecount += 1