txt = open('/home/polonec/Downloads/mena_zamestnancov.txt', encoding='cp1250')
meno = []
priezvisko = []
linecnt = 0
ans = ''
for lines in txt:
    if linecnt < 4:
        meno.append(lines)
        linecnt += 1
    else:
        priezvisko.append(lines)
        linecnt += 1
print(meno, priezvisko)
for i in meno, priezvisko:
    ans += meno[i].strip() + ' ' + priezvisko[i].strip() + ', ' #nejde
print(str)
