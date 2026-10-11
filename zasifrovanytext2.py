import random
posun = 0
metoda = input('(d/z)')
if metoda == 'd':
    txt = open('/home/polonec/Downloads/zasifrovany_text_2.txt','r', encoding='cp1250')
else:
    txt = open('/home/polonec/Downloads/vstupny_text.txt','r', encoding='cp1250')
ans =  ''
special = {'ľ','š','č','ť','ž','ý','á','í','é','ô','ä','ú','ň','ď','ĺ','ŕ'}
    
for line in txt:
    if metoda == 'd':
        posun = -(ord(line[0])-ord('a'))-1
        line = line[1::]
    else:
        posun = random.randrange(1, 26)
        ans += chr(posun+ord('a'))

    for letter in line:
        if letter.islower() and letter.isalpha() and not letter in special:
            letter = chr(((ord(letter) - ord('a') + posun) %26)+ord('a'))
            ans += letter
        else:
            ans += letter
print(ans)