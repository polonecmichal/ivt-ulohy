#input = input(str('zadaj input: '))
input = str(526)
hex = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
suma = 0
mocnina = 0
for i in input.upper()[::-1]:
    suma += hex[i] * 16**mocnina
    mocnina  +=1
print(suma)