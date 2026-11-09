txt = open('/home/polonec/Downloads/ciernobiely_obrazok_1.txt', 'r')
lc = 0
pismena = ''
ans = ''
for line in txt:
    if lc == 0:
        ans += line
        lc = 1
        continue
    for letters in line:
        pismena += letters
        if len(pismena) == 2:
            if int(pismena, 16) > 0x80:
                ans += '1 '
            else:
                ans += '0 '
            pismena = ''
        if letters == '\n':
            ans += '\n'
            pismena = ''
print(ans)