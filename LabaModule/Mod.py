import tkinter as tk
from random import randint

from LabaModule.Var import (SuperHHH,
                            BG,Title,SuperQST,
                            SuperRam, SuperTimes,super_acc,
                            SuperBG, SuperTitle, super_hhh, SuperPOP, SuperQST,
                            )
from LabaModule.UI import img_button, delete_button, update_pic
from LabaModule.Sound import switch_music, super_up

def now_mod(): #現在模式
    global SuperHHH
    mod = ""
    if SuperHHH :
        mod = "SuperHHH"
    else :
        mod = "Normal"
    
    return mod

#region 超級阿禾模式(SuperHHH)

def super_double(win, canvas_Game, all_SB, score, add):
    """超級阿禾加倍 獲得當前分數0.5倍的分數"""
    if all_SB :
        double_score = int(round(score / 2))
        add += double_score
        print(f"(超級阿禾加倍分:{double_score})")
        win.after(3000,lambda : canvas_Game.itemconfig("mod_2", text = f"(超級阿禾加倍分:{double_score})", fill = "yellow"))
        return add

def three_super(win, canvas_Game, all_p, score, add):
    global SuperHHH, SuperTimes
    """"檢查是否三個超級阿禾"""
    if all(p == "B" for p in all_p) and SuperHHH and SuperTimes == 6:
        print("全超級阿和")
        all_SB = True
        add = super_double(win, canvas_Game, all_SB, score, add)
        return add
    else:
        return add
        

def super_ram():
    """阿禾隨機數"""
    global SuperRam
    SuperRam = randint(1,100)
    print(f"超級阿禾隨機數為：{SuperRam}")

def change_hhh(canvas_Game, all_p):
    """把普通阿禾變成超級阿禾"""
    global super_hhh
    if all_p[0] == "B":
        all_p[0] = "SB"
        canvas_Game.itemconfig("LP" , image = super_hhh)
    if all_p[1] == "B":
        all_p[1] = "SB"
        canvas_Game.itemconfig("MP" , image = super_hhh)
    if all_p[2] == "B":
        all_p[2] = "SB"
        canvas_Game.itemconfig("RP" , image = super_hhh)
    super_up()

def super_screen(win,canvas_Game :tk.Canvas, game_running = True):
    """超級阿禾版面"""
    global SuperHHH, SuperTimes
    if SuperHHH :
        super_pop = img_button(win, lambda: delete_button(super_pop), canvas_Game, SuperPOP, 225 , 400, "flat", 0)
        print("超級阿禾出現了！")
        canvas_Game.itemconfig("BG", image = SuperBG)
        canvas_Game.itemconfig("Title", image = SuperTitle)
        canvas_Game.itemconfig("mod_1", text = f"超級阿禾剩餘次數:{SuperTimes}次", fill = "#FF00FF")
        switch_music('.\\Asset\\SuperMusic.mp3')
        

    else :
        canvas_Game.itemconfig("BG", image = BG)
        canvas_Game.itemconfig("Title", image = Title)
        canvas_Game.itemconfig("mod_1", text = "")
        switch_music('.\\Asset\\bgm.mp3',game_running)

def Super_init(CANVA, score, times, ed):
    
    update_pic(CANVA , "LP" , SuperQST)
    update_pic(CANVA , "MP" , SuperQST)
    update_pic(CANVA , "RP" , SuperQST)

    CANVA.itemconfig("Add", text=f"")
    CANVA.itemconfig("Score", text= f"目前分數：{score}")
    CANVA.itemconfig("Times", text= f"剩餘次數：{times - ed}")

def judge_super(win, canvas_Game, all_p, game_running = True):
    """判斷超級阿禾"""
    global SuperRam, SuperHHH, SuperTimes
    if game_running :
        mod = now_mod()
        if mod == "SuperHHH" : #正處於超級阿禾狀態
            if SuperTimes <= 0 : #超級阿禾次數用完
                SuperHHH = False
                win.after(3500 , lambda : super_screen(win,canvas_Game))

        elif mod == "Normal" : #未處於超級阿禾狀態
            hhh_appear = False
            #判斷是否有出現阿和
            if any(x == "B" for x in all_p):
                hhh_appear = True

            if SuperRam <= 100 and hhh_appear :#超級阿禾出現的機率
                SuperHHH = True
                SuperTimes = 6
                win.after(2800 , lambda : change_hhh(canvas_Game,all_p))
                win.after(3500 , lambda : super_screen(win, canvas_Game))
    else :
        SuperHHH = False
        win.after(3500 , lambda : super_screen(win,canvas_Game, False))

def super_times(win,canvas_Game) :
    global SuperHHH, SuperTimes
    if SuperHHH :
        SuperTimes -= 1
        print(f"超級阿禾剩餘次數:{SuperTimes}次")
        win.after(3000 , lambda : canvas_Game.itemconfig("mod_1", text = f"超級阿禾剩餘次數:{SuperTimes}次", fill = "#FF00FF"))

def switch_rate(normal_acc):
    global super_acc
    mod = now_mod()
    if mod == "SuperHHH" :
        return super_acc
    elif mod == "Normal" :
        return normal_acc
    
#endregion