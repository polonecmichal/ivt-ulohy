kluc = 'abc' #input('zadaj kluc')
sifra = input('zasifrovat ci desifrovat (z/d)')
text = 'kqcp'     #input('zadaj text')
cislokluc = 0
vysledok = ''
special = {'ľ','š','č','ť','ž','ý','á','í','é','ô','ä','ú','ň','ď','ĺ','ŕ'}

if sifra == 'z':
    metoda = 1
elif sifra == 'd':
    metoda = -1
for letter in text:
    cislokluc %= len(kluc)
    posun = (ord(kluc[cislokluc]) - ord('a') + 1) * metoda
    print(letter)
    if letter.islower() and letter.isalpha() and not letter in special:
        letter = chr(((ord(letter) - ord('a') + posun) %26)+ord('a'))
        vysledok += letter
    else:
        vysledok += letter
    cislokluc += 1
print(vysledok)