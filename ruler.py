from math import sqrt
import tkinter
import pyautogui
from win32api import GetSystemMetrics


sc_width = GetSystemMetrics(0)
sc_height = GetSystemMetrics(1)


def distance(dx, dy):
    return sqrt(dx ** 2 + dy ** 2)


root = tkinter.Tk()
root.attributes("-alpha", 0.4)
root.state("zoomed")
root.resizable(0, 0)
root.option_add("*Font", '30')

cvs = tkinter.Canvas(root, width=200, height=200)

line_beg = 100, 100
line_end = 200, 100
text = 0
f_line_beg = True

line = cvs.create_line(line_beg[0], line_beg[1],
                       line_end[0], line_end[1], width=2)


def onclick_handler(event):
    global f_line_beg

    pos = pyautogui.position()
    # print(pos)
    deltax = pos.x - line_beg[0]
    deltay = pos.y - line_beg[1]
    dis_beg = distance(deltax, deltay)

    deltax = pos.x - line_end[0]
    deltay = pos.y - line_end[1]
    dis_end = distance(deltax, deltay)

    f_line_beg = True
    if (dis_beg > dis_end):
        f_line_beg = False


def ondrag_handler(event):
    global line
    global line_beg
    global line_end
    global text
    if line:
        cvs.delete(line)

    if f_line_beg:
        line_beg = event.x, event.y
    else:
        line_end = event.x, event.y

    line = cvs.create_line(
        line_beg[0], line_beg[1], line_end[0], line_end[1], width=2)

    if text:
        cvs.delete(text)
    text = cvs.create_text(sc_width/2, sc_height * 0.15, text=str(distance(line_beg[0] - line_end[0], line_beg[1] - line_end[1])),
                           fill="red", font=('Helvetica 35 bold'),)


cvs.bind("<Button-1>", onclick_handler)
cvs.bind("<B1-Motion>", ondrag_handler)


cvs.pack(expand=tkinter.YES, fill=tkinter.BOTH)
root.mainloop()
