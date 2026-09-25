import tkinter as tk

win = tk.Tk()

canvas = tk.canvas(width=1000,height=1000,bg='green')
canvas.pack()

def triangle(a,x,y):
    canvas.create_line(x,y,x+a,y,fill='yellow')
    