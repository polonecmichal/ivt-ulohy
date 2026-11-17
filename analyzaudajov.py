txt = open("/home/polonec/Downloads/spokojnost_1.txt", encoding='cp1250')
lc = 0
vyjadr = {}
den = 1
reakcie = 0
predhod = 0
for line in txt:
    if len(line) != 0: 
        lc +=1
    line = line.split()
    hodiny = line[0][:2]
    nazor = str(line[1]).strip()
    vyjadr[hodiny] = vyjadr.setdefault(hodiny, 0) + 1
    hodiny = int(hodiny)
    if hodiny < int(predhod):
        print('v den', den, 'bolo', reakcie, 'reakcii')
        den += 1
        reakcie = 0
    reakcie += 1
    predhod = hodiny
print('v den', den, 'bolo', reakcie, 'reakcii')
