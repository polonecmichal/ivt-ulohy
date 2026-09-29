txt = input('zadaj text')
ans = ''
num = {}
slovo = ''
for letter in txt:
    if letter == ' ':
        pocitadlo = 1
        ans = '0'
    else:
        ciselko = ord(letter) - ord('A')    
        ans = str(ciselko // 3 + 1)
        pocitadlo = int(ciselko%3 + 1)
    for i in range(pocitadlo):
        print(ans, end='')
        num[ans] = num.get(ans,0) + 1
    print(' ', end='')
print(txt, '\n')
print(max(num, key=num.get))