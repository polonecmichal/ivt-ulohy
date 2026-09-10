txt = open('/home/polonec/Downloads/sutaz_vbehu.txt', 'r')
linecount = 0
ans = ''
spolu = []
meno = ''
cas = ''
for lines in txt:
    if len(lines) != 0:
        linecount += 1
    spolu = lines.split(' ')
    meno = spolu[0]
    cas = int(spolu[1])
    minuty = cas//60
    sekundy = cas%60
    print('Súťažiaci', meno, 'dobehol do cieľa za', cas, 'sekúnd, alebo', minuty, 'minuty a ', sekundy, 'sekund')
print('Počet zúčastnených športovcov:', linecount)