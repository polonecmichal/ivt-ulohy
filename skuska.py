txt = open("/home/polonec/Downloads/spokojnost_1.txt", encoding='cp1250')
lc = 0
spokoj = {}
nespokoj = {}
for line in txt:
    if len(line) != 0: 
        lc += 1
    line = line.split()
    hodiny = line[0][:2]
    nazor = str(line[1]).strip()
    if nazor == 'nie':
        nespokoj[hodiny] = nespokoj.setdefault(hodiny, 0) + 1
    else:
        spokoj[hodiny] = spokoj.setdefault(hodiny, 0) + 1

print(max(spokoj, key=spokoj.get))
print(max(nespokoj, key=nespokoj.get))

for hodiny in spokoj:
    spokoj[hodiny] = str(round((int(spokoj.get(hodiny))/lc) * 100, 2)) + '%'
print(spokoj)

for hodiny in nespokoj:
    nespokoj[hodiny] = str(round((int(nespokoj.get(hodiny))/lc) *100, 2)) + '%'
print(nespokoj)