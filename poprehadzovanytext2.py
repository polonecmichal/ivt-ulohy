import random
txt = open('/home/polonec/Downloads/poprehadzovany_text_vstup2.txt', encoding='cp1250')
slova = []
miesanie = []
index = 0
znamienko = ''
import random
def pomiesaj(retazec):
    pismenka = list(retazec)
    random.shuffle(pismenka)
    return ''.join(pismenka)
for line in txt:
    #print(line)
    line = line.split()
    for word in line:
        if len(word) <= 3:
            pass
        else:
            index = line.index(word)
            word = word.strip()
            for letter in word:
                if not letter.isalpha():
                    znamienko = ''
                    znamienko = letter
                    list(word).remove(znamienko)
            prve = word[0]
            posledne = word[len(word)-1]
            word = pomiesaj(word)
            pes =''.join(word)
            prve += pes + posledne + znamienko
            line[index] = prve
    print(' '.join(line))