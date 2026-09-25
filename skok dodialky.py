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