txt = open('/home/polonec/Downloads/kompresia_obrazka_1.txt')
ans = ''
lastlet = ''
letcount = 0
lc = 0
def spracuj_riadok(line):
    global ans, lastlet, letcount, lc
    for line in txt:
        if lc == 0:
            ans += line
            lc = 1
            continue
        line = list(line)
        if line[0] == '1':
            ans += '0 '
        for letter in line:
            if letter == '\n':
                ans += str(letcount) + '\n'
            elif letter != str(lastlet):
                if letcount != 0:
                    ans += str(letcount) + ' '
                lastlet = letter
                letcount = 1
            elif letter == lastlet:
                letcount += 1
        letcount = 0    
spracuj_riadok(lastlet)
print(ans[:-1])
