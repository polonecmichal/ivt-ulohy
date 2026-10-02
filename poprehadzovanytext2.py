import random

txt = open('/home/polonec/Downloads/poprehadzovany_text1_vstup.txt', encoding='cp1250')
def pomiesaj(retazec):
    pismenka = list(retazec)
    prve = retazec[0]
    posledne = retazec[len(retazec)-1]
    pismenka = list(pismenka).pop(0)
    pismenka = list(pismenka).pop(len(pismenka)-1)
    print(pismenka)
    random.shuffle(pismenka)
    prve += ''.join(pismenka) + posledne
    return prve
for retazec in txt:
    retazec = retazec.strip()
    print(pomiesaj(retazec))