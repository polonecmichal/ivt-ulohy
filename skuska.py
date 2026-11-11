txt = open('/home/polonec/Downloads/ciernobiely_obrazok_1.txt', 'r')
lc = 0
ans = ''
def spracuj_riadok(line):
    global ans
    pismena = ''
    for letter in line:
        pismena += letter
        if len(pismena) == 2:
            if int(pismena, 16) > 0x80:
                ans += '1 '
            else:
                ans += '0 '
            pismena = ''
    return ans
for line in txt:
    if lc == 0:
        print(line[:-1])
        lc = 1
        continue
    spracuj_riadok(line)
    print(ans)
    ans = ''