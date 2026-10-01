txt = open('/home/polonec/Downloads/tabulka_pocetnosti.txt', 'r')
pismena = {}
abc = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
print(abc)
for line in txt:
    line = line. strip()
    for letter in line:
        letter = letter.upper()
        if letter.isalpha():
            pismena.setdefault(letter, 0)
            if letter in pismena:
                pismena[letter] += 1
for pissmeno,pocet in pismena.items():
        print(pissmeno, pocet)
        if pissmeno in abc:
            abc.remove(pissmeno)
print(line)
print(pismena)
print(abc)