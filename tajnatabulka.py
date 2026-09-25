txt = input('zadaj text')
ans = ''
pismena = {}
for letter in txt:
    pismena[letter] = pismena.get(letter, 0) + 1
    if letter == ' ':
        pocitadlo = 1
        ans = '0'
    else:
        ciselko = ord(letter) - ord('A')    
        ans = str(ciselko // 3 + 1)
        pocitadlo = int(ciselko%3 + 1)
    for i in range(pocitadlo):
        print(ans, end='')
    print(' ', end='')
print(txt, '\n', pismena, '\n',  max(pismena, key=pismena.get))