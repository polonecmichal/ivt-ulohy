txt = open('/home/polonec/Downloads/kompresia_obrazka_1.txt')
ans = ''
lastlet = ''
def spracuj_riadok(line):
    global ans, lastlet
    line = line.split()
    if line[0] == '1':
        ans += '0 '
        line = line[1::]
    for letter in line:
        if letter != str(lastlet):
            ans += str(lastlet) + ' '
            lastlet = 0
        else:
            lastlet += 1

for line in txt:
    spracuj_riadok(lastlet)
    print(ans)