txt= open('/home/polonec/Downloads/hlasovanie_1.txt')
txt2 =  open('/home/polonec/Downloads/hlasovanie_vypadnuti.txt')
lc = 0
vypadnuty = []
dict = {}
for line in txt2:
    vypadnuty.append(line)
for line in txt:
    line = line.strip()
    if line not in vypadnuty:
        dict.setdefault(line,0)
        dict[line] = dict.get(line,0) + 1
    if len(line) != 0:
        lc += 1
print(lc, dict, max(dict), min(dict))