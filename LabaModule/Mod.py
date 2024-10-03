import tkinter as tk
from random import randint

from LabaModule.Var import (SuperHHH, GreenWei,
                            BG,Title,SuperQST,
                            
                            SuperRate, SuperFirst,
                            SuperRam, SuperTimes,super_acc,
                            SuperBG, SuperTitle, SuperPOP, SuperQST, super_hhh,

                            GreenRate, GreenFirst,
                            GreenRam, GreenTimes, 
                            GreenBG, GreenTitle, GreenPOP, GreenQST, GreenLeft, GreenMid, GreenRight, green_wei
                            )
from LabaModule.UI import img_button, delete_button, update_pic
from LabaModule.Sound import switch_music, super_up, green_up

def now_mod(): #現在模式
    global SuperHHH, GreenWei
    mod = ""
    if SuperHHH :
        mod = "SuperHHH"
    elif GreenWei :
        mod = "GreenWei"
    else :
        mod = "Normal"
    
    return mod

#region 超級阿禾模式(SuperHHH)
def SuperFalse():
    global SuperHHH
    SuperHHH = False

def super_double(win, canvas_Game, all_SB, score, add):
    """超級阿禾加倍 獲得當前分數0.5倍的分數"""
    global GreenWei
    if all_SB :
        double_score = int(round(score / 2))
        add += double_score
        if GreenWei:
            print(f"(超級阿禾x綠光阿瑋加倍分:{double_score * 3})")
            win.after(3000,lambda : canvas_Game.itemconfig("mod_2", text = f"(超級阿禾x綠光阿瑋加倍分:{double_score * 3})", fill = "yellow"))
        else:
            print(f"(超級阿禾加倍分:{double_score})")
            win.after(3000,lambda : canvas_Game.itemconfig("mod_2", text = f"(超級阿禾加倍分:{double_score})", fill = "yellow"))
        return add

def three_super(win, canvas_Game, all_p, score, add):
    global SuperHHH, SuperTimes, SuperFirst
    """"檢查是否三個超級阿禾"""
    print(SuperHHH)
    if all(p == "B" for p in all_p) and SuperHHH and SuperFirst:
        print("全超級阿禾")
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
    CANVA.itemconfig("mod_2", text = f"")

def judge_super(win, canvas_Game, all_p, game_running = True, ModEnd = False):
    """判斷超級阿禾"""
    global SuperRate, SuperRam, SuperHHH, SuperTimes, SuperFirst
    if game_running :
        mod = now_mod()
        if mod == "SuperHHH" : #正處於超級阿禾模式
            if all(p == "B" for p in all_p): #超級阿禾次數未用完且全阿禾
                SuperTimes += 2
                print("全阿禾，次數不消耗且+1！")
            if SuperTimes <= 0 : #超級阿禾次數用完
                SuperHHH = False
                win.after(3000 , lambda : super_screen(win,canvas_Game))

        elif mod == "Normal" or ModEnd: #未處於任何模式或在其他模式結尾
            hhh_appear = False
            #判斷是否有出現阿和
            if any(x == "B" for x in all_p):
                hhh_appear = True

            if SuperRam <= SuperRate and hhh_appear :#超級阿禾出現的機率
                SuperHHH = True
                SuperFirst = True
                SuperTimes = 6
                win.after(2800 , lambda : change_hhh(canvas_Game,all_p))
                win.after(3500 , lambda : super_screen(win, canvas_Game))
    else :
        SuperHHH = False
        win.after(3000 , lambda : super_screen(win,canvas_Game, False))

def super_times(win,canvas_Game) :
    global SuperHHH, SuperTimes, SuperFirst
    if SuperHHH :
        SuperFirst =False
        SuperTimes -= 1
        print(f"超級阿禾剩餘次數:{SuperTimes}次")
        win.after(3000 , lambda : canvas_Game.itemconfig("mod_1", text = f"超級阿禾剩餘次數:{SuperTimes}次", fill = "#FF00FF"))

def switch_rate(normal_acc):
    global super_acc
    mod = now_mod()
    if mod == "SuperHHH" :
        return super_acc
    elif mod == "Normal" or mod == "GreenWei" :
        return normal_acc
    
#endregion

#region 綠光阿瑋模式(GreenWei)
def GreenFalse():
    global GreenWei
    GreenWei = False

def green_ram():
    """阿瑋隨機數"""
    global GreenRam
    GreenRam = randint(1,100)
    print(f"綠光阿瑋隨機數為：{GreenRam}")

def change_gss(canvas_Game, all_p, gss_all = True):
    """把咖波變成阿瑋"""
    global GreenLeft, GreenMid, GreenRight
    if gss_all :
        all_p[0], all_p[1], all_p[2] = "GW", "GW", "GW"
        canvas_Game.itemconfig("LP" , image = GreenLeft)
        canvas_Game.itemconfig("MP" , image = GreenMid)
        canvas_Game.itemconfig("RP" , image = GreenRight)
    else:
        if all_p[0] == "A":
            all_p[0] = "GW"
            canvas_Game.itemconfig("LP" , image = green_wei)
        if all_p[1] == "A":
            all_p[1] = "GW"
            canvas_Game.itemconfig("MP" , image = green_wei)
        if all_p[2] == "A":
            all_p[2] = "GW"
            canvas_Game.itemconfig("RP" , image = green_wei)
    green_up()


def green_screen(win,canvas_Game :tk.Canvas, game_running = True):
    """超級阿禾版面"""
    global GreenWei, GreenTimes
    if GreenWei :
        green_pop = img_button(win, lambda: delete_button(green_pop), canvas_Game, GreenPOP, 225 , 400, "flat", 0)
        print("綠光阿瑋出現了！")
        canvas_Game.itemconfig("BG", image = GreenBG)
        canvas_Game.itemconfig("Title", image = GreenTitle)
        canvas_Game.itemconfig("mod_1", text = f"綠光阿瑋剩餘次數:{GreenTimes}次", fill = "#00FF00")
        switch_music('.\\Asset\\GreenMusic.mp3')
        

    else :
        canvas_Game.itemconfig("BG", image = BG)
        canvas_Game.itemconfig("Title", image = Title)
        canvas_Game.itemconfig("mod_1", text = "")
        switch_music('.\\Asset\\bgm.mp3',game_running)


def judge_green(win, canvas_Game, all_p,  game_running = True):
    global GreenRam, GreenWei, GreenTimes, GreenFirst
    if game_running:
        mod = now_mod()
        if mod == "GreenWei" : #處於綠光阿瑋模式
            if all(p == "A" for p in all_p) :#綠光次數未用完且全部咖波
                GreenTimes += 1
                print("全咖波，次數不消耗！")
            if GreenTimes <= 0 : #綠光次數用完
                GreenWei = False
                win.after(3000 , lambda : green_screen(win, canvas_Game))
                judge_super(win, canvas_Game, all_p, ModEnd = True)
            
        elif mod == "Normal" : #未處於任何模式
            gss_all = False
            #判斷是否有出現並全部咖波
            if all(x == "A" for x in all_p):
                gss_all = True

            if GreenRam <= GreenRate and gss_all :
                GreenWei = True
                GreenFirst = True
                GreenTimes = 2
                win.after(2800 , lambda : change_gss(canvas_Game,all_p))
                win.after(3500 , lambda : green_screen(win, canvas_Game))
    else :
        GreenWei = False
        win.after(3000 , lambda : green_screen(win, canvas_Game, False))

def green_times(win,canvas_Game) :
    global GreenWei, GreenTimes, GreenFirst
    if GreenWei :
        GreenFirst = False
        GreenTimes -= 1
        print(f"綠光阿瑋剩餘次數:{GreenTimes}次")
        win.after(3000 , lambda : canvas_Game.itemconfig("mod_1", text = f"綠光阿瑋剩餘次數:{GreenTimes}次", fill = "#00FF00"))

def switch_times():
    """加分倍數"""
    mod = now_mod()
    if mod == "GreenWei" :#綠光阿瑋使得分增加2倍(*3)
        t = 3
    elif mod == "Normal" or mod == "SuperHHH" :
        t = 1
    print(f"加分倍數為： {t} 倍")
    return t
        
    

def Green_init(CANVA, score, times, ed):
    
    update_pic(CANVA , "LP" , GreenQST)
    update_pic(CANVA , "MP" , GreenQST)
    update_pic(CANVA , "RP" , GreenQST)

    CANVA.itemconfig("Add", text=f"")
    CANVA.itemconfig("Score", text= f"目前分數：{score}")
    CANVA.itemconfig("Times", text= f"剩餘次數：{times - ed}")
    CANVA.itemconfig("mod_2", text = f"")
