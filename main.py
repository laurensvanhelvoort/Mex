import random
from tkinter import *

dim = [900, 600]

root = Tk()
root.geometry(f"{dim[0]}x{dim[1]}")
root.title("Mex")
root.iconbitmap("dice.ico")

lbl = Label(root, font=("times", 200))

num = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
d1 = None
d2 = None
throw_txt = None
cnt_txt = None
mex_cnt = 0


def roll_dice():
    global d1, d2

    # 'throw' dice
    d1 = random.choice(num)
    d2 = random.choice(num)

    # update and display dice
    lbl.config(text=f"{d1}{d2}")
    lbl.pack()
    lbl.place(x=dim[0] / 3.8, y=50)

    # update and display new throw
    txt.config(text=check_throw(convert_symbol()))

    # update and display mex counter
    if mex_cnt != 0:
        cnt.config(text=f"Aantal mexen: {mex_cnt}")


def convert_symbol():
    d1_num = None
    d2_num = None

    # find index in num list according to throw
    for n in num:
        if n == d1:
            # increment by 1 to account for zero-indexing
            d1_num = num.index(n) + 1
        if n == d2:
            d2_num = num.index(n) + 1
    # largest die throw becomes first digit in number
    if d2_num > d1_num:
        throw = f"{d2_num}{d1_num}"
    else:
        throw = f"{d1_num}{d2_num}"
    return throw


def check_throw(t):
    num_t = int(t)
    if num_t == 21:
        global mex_cnt
        mex_cnt += 1
        return "Mex"
    # if multiple of 11 (55, 22, 66 etc.), outcome is koning
    elif num_t % 11 == 0:
        # if 100 is thrown, player becomes koning
        if num_t == 11:
            return "Jij bent de koning!"
        else:
            return f"Koning: {int(num_t / 11 * 100)}"
    elif num_t == 31:
        return "Slok uitdelen"
    else:
        return str(num_t)


# ------------ TKinter elements ----------------------
roll_btn = Button(root, text="Gooi!", width=10, bg='#42aaf5', activebackground='#88c6f2', command=roll_dice)
roll_btn.config(font=("bahnschrift", 20))
roll_btn.pack()
roll_btn.place(x=dim[0] / 2.5, y=25)

txt = Label(root, text=throw_txt)
txt.config(font=("bahnschrift", 40))
txt.pack(side=TOP)
txt.place(x=dim[0] / 2, y=400, anchor='center')

cnt = Label(root, text=cnt_txt)
cnt.config(font=("bahnschrift", 20))
cnt.pack(side=TOP)
cnt.place(x=dim[0] / 7, y=300, anchor='center')

root.mainloop()
