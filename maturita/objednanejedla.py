txt = open("/home/polonec/Downloads/objednane_jedla.txt", 'r')

linecount = 0
orange = 0
red = 0
green = 0
blue = 0
farby = []


#pocet jedal
for lines in txt:
    if len(lines) != 0:
        linecount += 1
    for letters in lines:
        if letters == 'o':
            orange += 1
        if letters == 'c':
            red += 1
        if letters == 'z':
            green += 1
        if letters == 'm':
            blue += 1

if red < 20:
    farby.append('c')
if orange < 20:
    farby.append('o')
if blue < 20:
    farby.append('m')
if green < 20:
    farby.append('z')
if red > 20 and orange > 20 and blue > 20 and green> 20:
    print('heppy brzdej')
txt.seek(0)

for lines in txt:
    for color in farby:
        if color in lines:
            print(lines, end = '')
        
print('Pocet obedov je', linecount,'zelenych je:', green, 'cervenych je:', red, 'modrych je:', blue, 'oranzovych je:', orange)

