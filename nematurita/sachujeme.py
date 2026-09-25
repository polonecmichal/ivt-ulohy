chboard = []
counter = 0
def create_chboard():
    global chboard
    for i in range(8):
        row = [0] * 8
        chboard.append(row)


        

def check_it(x,y):
    for i in range(0,8):
        if chboard[y][x] == 1:
            return False
        if chboard[i][x] == 1:
            return False
    for i in range(0,8):
        for j in range(0,8):
            if j + i == x + y:
                if chboard[i][j] == 1:
                    return False
            if i - j == y - x:
                if chboard[i][j] == 1:
                    return False
    return True




import PIL.Image, PIL.ImageDraw

def board():
    global counter
    img = PIL.Image.new(mode="RGB", size=(640, 640))
    img1 = PIL.ImageDraw.Draw(img)
    sol = 0
    size = 80  
    stvorec = 80
    #budis sachovnica
    for riadok in range(8):
        for stlpec in range(8):
            if (riadok + stlpec) % 2 == 0:
                x0 = stlpec * size
                y0 = riadok * size
                x1 = x0 + size
                y1 = y0 + size
                img1.rectangle(xy=[x0, y0, x1, y1], fill='white')



    #karlovnuj sa
    for row in range(8):
        for col in range(8):
            if chboard[row][col] == 1:
                x0 = col * stvorec
                y0 = row * stvorec
                x1 = (col + 1) * stvorec
                y1 = (row + 1) * stvorec
                img1.ellipse([x0, y0, x1, y1], fill="red")
                sol += 1  
    img.save(f"riesenie_{counter}.png")





def queens(n):
    global chboard
    global counter
    cislo = 0
    if n == 8:
        counter += 1
        print(chboard)
        print("---------------------------------------------")
        board() 
    else:
        for i in range(0,8):
            if check_it(i,n):
                chboard[n][i] = 1
                queens(n+1)
                chboard[n][i] = 0

create_chboard()
queens(0)