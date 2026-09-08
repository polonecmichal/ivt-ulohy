import os
txt = open("/home/polonec/Downloads/hada.txt", "r")

lastlet = ''
counter = 0
counterline = 0
ans = ''
lenght = 0

if os.path.exists("/home/polonec/Documents/Ivt/answ"):
    answ = open("/home/polonec/Documents/Ivt/answ", "w")
else:
    answ = open("/home/polonec/Documents/Ivt/answ", "x")
# ak dam namiesto x alebo w a spravi tento proces
for line in txt:
    if lenght < len(line):
        lenght = len(line)

    if len(line) != 0:
        counterline += 1

    for letters in line:
        if letters == lastlet or len(lastlet) == 0:
            counter += 1
        else:
            ans += lastlet + " " + str(counter) + " "
            counter = 1
        lastlet = letters
    print(ans)
    answ.write(ans + '\n')
    ans  = ""
    lastlet = ""
    counter = 0

print('pocet riadkov je', counterline)
print('dlzka je', lenght)