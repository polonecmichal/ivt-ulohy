import random
txt = open('/home/polonec/Downloads/poprehadzovany_text1_vstup.txt', encoding='cp1250')
slova = []
miesanie = []
for line in txt:
    line = line.strip()
    print(line)
    word = line.split()
    for i in range(len(word)):
        slova.append(word[i])
#print(slova)
for word in slova:
    word = word.strip()
    word = list(word)
    prve = word[0]
    posledne = word[len(word)-1]
    word = word[1:-1]
    random.shuffle(word)
    pes =''.join(word)
    prve += pes + posledne
    #print(prve)