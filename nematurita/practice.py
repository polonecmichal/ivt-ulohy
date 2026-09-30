txt = open('/home/polonec/Downloads/skok_do_dialky.txt')
staty = []
dict = {}
max = 0
win = []
for line in txt:
    riadok = line.split()
    stat = riadok[1]
    staty.append(stat)
    dict.setdefault(stat, 0)
    dict[stat] += 1
    for i in range(2,6):
        if int(riadok[i]) > int(max):
            max =  riadok[i]
            win.clear()
            win.append(riadok[0]) 
        elif int(riadok[i]) == int(max):
            win.append(riadok[0])
print(win,dict)