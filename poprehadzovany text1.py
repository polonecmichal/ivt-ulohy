import random
txt = open('/home/polonec/Downloads/poprehadzovany_text1_vstup.txt', encoding='cp1250')
slova = []
miesanie = []
index = 0
for line in txt:
    #print(line)
    line = line.split()
    for word in line:
        if len(word) == 1:
            pass
        else:
            index = line.index(word)
            word = word.strip()
            word = list(word)
            prve = word[0]
            posledne = word[len(word)-1]
            word = word[1:-1]
            random.shuffle(word)
            pes =''.join(word)
            prve += pes + posledne
            line[index] = prve
    print(' '.join(line))