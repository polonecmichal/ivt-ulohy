txt = open('/home/polonec/Downloads/meteo_stanice.txt', 'r')

linecount = 0
max = '-inf'
kod = ''
sum = 0

for lines in txt:
        lines = lines.replace(',', '.')
        print(lines[21:26])
        if float(max) < float(lines[21:26]):
                max = float(lines[21:26])
                kod = lines[0:4]
        sum += float(lines[21:26])
        if len(lines) != 0:
                linecount += 1
print('pocet merani je:', linecount)
print('max je:', max, kod, 'avge je', round(sum/linecount, 2))