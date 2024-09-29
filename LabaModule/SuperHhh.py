import tkinter as tk
from PIL import Image, ImageTk
from random import randint

from LabaModule.Var import (
                            BG,Title,
                            SuperRam, SuperHHH, SuperBG, SuperTitle, super_hhh, SuperPOP
                            )
from LabaModule.UI import img_button, delete_button

def super_ram():
    """阿禾隨機數"""
    global SuperRam
    SuperRam = randint(1,100)
    print(f"超級阿禾隨機數為：{SuperRam}")

def change_hhh(canvas_Game, all_p):
    """把普通阿禾變成超級阿禾"""
    global super_hhh
    if all_p[0] == "B":
        canvas_Game.itemconfig("LP" , image = super_hhh)
    if all_p[1] == "B":
        canvas_Game.itemconfig("MP" , image = super_hhh)
    if all_p[2] == "B":
        canvas_Game.itemconfig("RP" , image = super_hhh)

def super_screen(win,canvas_Game :tk.Canvas):
    global SuperHHH
    if SuperHHH :
        super_pop = img_button(win, lambda: delete_button(super_pop), canvas_Game, SuperPOP, 225 , 400)
        canvas_Game.itemconfig("BG", image = SuperBG)
        canvas_Game.itemconfig("Title", image = SuperTitle)
    else :
        canvas_Game.itemconfig("BG", image = BG)
        canvas_Game.itemconfig("Title", image = Title)

def judge_super(win, canvas_Game, all_p):
    """判斷超級阿禾"""
    global SuperRam, SuperHHH
    if SuperHHH == False:
        hhh_appear = False
        #判斷是否有出現阿和
        if any(x == "B" for x in all_p):
            hhh_appear = True

        if SuperRam <= 15 and hhh_appear :
            SuperHHH = True
            win.after(3000 , lambda : change_hhh(canvas_Game,all_p))
            win.after(3500 , lambda : super_screen(win,canvas_Game))

