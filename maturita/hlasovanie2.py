txt = open('/home/polonec/Downloads/hlasovanie_1.txt')
lc = 0
list1 = []
for i in range(5220,5230):
    with open(f"/home/polonec/Documents/Ivt/{i}.txt", 'a') as f:
        for line in txt:
            lc += 1
            if line.strip() == str(i):
                f.write(str(lc) + '\n')
        lc = 0
        txt.seek(0)
