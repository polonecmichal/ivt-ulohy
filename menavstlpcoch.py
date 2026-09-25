txt = open('/home/polonec/Downloads/mena_zamestnancov.txt', encoding='cp1250')
meno = []
priezvisko = []
linecnt = 0
ans = ''
max = 0
maxmeno = ''
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
print(meno, priezvisko)
for i in meno, priezvisko:
    ans += meno[i].strip() + ' ' + priezvisko[i].strip() + ', ' #nejde

print(str)

for i in range(0,4):
    ans += meno[i].strip() + ' ' + priezvisko[i].strip() + ', '
print(maxmeno)
print(ans, linecnt//2)
