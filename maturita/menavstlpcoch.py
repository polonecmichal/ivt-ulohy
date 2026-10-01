txt = open('/home/polonec/Downloads/mena_zamestnancov.txt', encoding='cp1250')
meno = []
priezvisko = []
linecnt = 0
ans = ''
max = 0
maxmeno = ''
maxpriez = ''
for lines in txt:
    lines = lines.strip()
    if linecnt < 4:
        meno.append(lines)
        linecnt += 1
        if len(lines) > max:
            max = len(lines)
            maxmeno = lines
    else:
        priezvisko.append(lines)
        linecnt += 1
        if len(lines) > max:
            max = len(lines)
            maxpriez = lines
print(meno, priezvisko)
for i in range(linecnt//2):
    medzera = ' '*(len(maxmeno)-len(meno[i]) + 1)
    ans += meno[i].strip() + medzera + priezvisko[i].strip() + '\n'
print(maxmeno, len(maxmeno))
print(maxpriez, len(maxpriez))
print(ans, linecnt//2)
vystup = open('/home/polonec/Documents/Ivt/vystup.txt', 'a')
vystup.write(ans)

def bs():
    txt = open('/home/polonec/Downloads/mena_zamestnancov.txt', encoding='cp1250')
    lc = 0
    mena = []
    prizv = []
    max = ''
    ans = ''

    for lines in txt:
        lc += 1
        lines = lines.strip()
        if lc <= 4:
            mena.append(lines)
            if len(lines) > len(max):
                max = lines
        else:
            prizv.append(lines)
    for i in range(lc//2):
        medzera = ' '*(len(max)-len(mena[i])+1) 
        ans += mena[i] + medzera + prizv[i] + '\n'
    print(ans)
    print(lc//2, max)
