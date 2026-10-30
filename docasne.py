n = int(input())
max1 = 0
max2 = 0

for i in range(len(str(n))):
    if i > 1:
        teraz = int(input())
        if teraz > max1:
            max2 = max1
            max1 = teraz
        elif teraz > max2:
            max2 = teraz
print(max1, max2)