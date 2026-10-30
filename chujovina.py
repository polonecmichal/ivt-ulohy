input = input().split()
lc = 0
sutaz = []
pocet = input[0]
nas1 = int(input[1])
nas2 = int(input[2])
for i in range(1, int(pocet)+1):
    sutaz.append(i)
dvojica = []
for i in sutaz:
    lc += 1
    dvojica.append(sutaz[i])
    if len(dvojica) == 2:
        if nas1 and nas2 in dvojica:
            print(lc)
            break
        if nas1 in dvojica:
            print('To bude epicke!')
            break
        if nas2 in dvojica:
            print('To bude epicke!')
            break
        else:
            dvojica.clear()
