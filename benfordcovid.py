#du dorobit, zisti ci ten weekly death zodpovedaju benfordovmu zakonu, csv
import csv
cislo = {}
count = 0
for i in range(1,10):
    cislo[i] = 0
txt = open("/home/polonec/Downloads/data.csv")
for line in txt:
    count += 1
    riadok = line.split(',')
    death = riadok[5]
    if death.isnumeric() and int(death[0]) > 0:
        prvy = int(death[0])
        cislo[prvy] += 1
print(cislo, count)

for i in cislo:
    percenta = (cislo[i]/count)*100
    ans = str(percenta) + '%' + ' '
    print(ans)
