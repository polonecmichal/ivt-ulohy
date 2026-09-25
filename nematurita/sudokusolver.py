from PIL import Image, ImageDraw, ImageFont
sudoku = []

def create_sudoku(sudoku):
    txt = open('/home/polonec/Documents/Ivt/sudoku.txt', 'r')
    for row in txt:
        row = row.strip()
        temp = []
        for char in row:
            temp.append(int(char))
        sudoku.append(temp)
create_sudoku(sudoku)

def over(y,x,number):
    for i in range(0,9):
        if sudoku[y][x] == number:
            return False
        if sudoku[y][i] == number:
            return False
    x = x // 3*3
    y = y // 3*3
    for i in range(x,x + 3):
        for j in range(y,y+3):
            if sudoku[j][i] == number:
                return False
    return True

def sudoku_solver():
    global sudoku
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for i in range(1,10):
                    if over(x,y,i):
                        sudoku[y][x] = i
                        if sudoku_solver():
                            return True
                        sudoku[y][x] = 0
                return False
    print(sudoku)
    return True
create_sudoku(sudoku)
over(1,2,7)
sudoku_solver()
buf = 10
img = Image.new('RGB', (630, 630), 'white')
draw = ImageDraw.Draw(img)
#font = ImageFont.truetype("Arial.ttf", 9)
for i in range(9):
    for j in range(9):
        draw.rectangle((i*70,j*70, (i+1)*70, (j+1)*70), fill='white', outline='black')
        if sudoku[j][i] != 0:
            draw.text(str(i*70+buf), "a")#,str(j*70+buf)) #, str((i+1)*70-buf),str((j+1)*70-buf))


img.save('jano.png')
img.show()