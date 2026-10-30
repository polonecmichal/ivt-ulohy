names = ['zero', 'one', 'two', 'three', 'four','five', 'six', 'seven' , 'eight' ,'nine' ]
cslo = []
def spracuj():
    global cislo
    for cislo in range(len(names)):
        txt = open('/home/polonec/Downloads/cisla/'+cislo+'.txt', 'r')
        print(txt.readlines())
        cisla[cislo] = []
        for line in txt:
            line = line.strip('\n')
            cisla[cislo].append(line)

def vykresli(number):
    for riadok in range(0,7):
        for index_cisla in range(len(str(number))):
            temp = int(str(number)[index_cisla])

vykresli(7)
spracuj()