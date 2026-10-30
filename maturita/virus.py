txt = open('/home/polonec/Downloads/virus.txt', encoding='cp1250')
import random
riadky = []
def slovo(word):
    return word[::-1]
def coin():
    return random.choice([0,1])

for line in txt:
    line = line.split()
    if coin():
        random.shuffle(line)
    for word in line:
        if coin():
            index = line.index(word)
            word = slovo(word)
            line[index] = word 
    riadky.append(line)
if coin():
    random.shuffle(riadky)
for line in riadky:
    print(' '.join(line))
