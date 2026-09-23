#du dorobit, zisti ci ten weekly death zodpovedaju benfordovmu zakonu, csv
import csv
cislo = {}
for i in range(1,10):
    cislo[i] = 0
txt = open("D:\\škola\\Downloads\\data.csv")
for line in txt:
    death = line[18:19] #death neni univerzalne treba spravit 
    cislo[death] += 1
print(cislo)

