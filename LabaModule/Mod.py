import tkinter as tk
from random import randint

from LabaModule.Var import (SuperHHH, GreenWei,
                            BG,Title,SuperQST,
                            
                            SuperRate, SuperFirst,
                            SuperRam, SuperTimes,super_acc,
                            SuperBG, SuperTitle, SuperPOP, SuperQST, super_hhh,

                            GreenRate, GreenFirst,
                            GreenRam, GreenTimes, gss_times,
                            GreenBG, GreenTitle, GreenPOP, GreenQST, GreenLeft, GreenMid, GreenRight, green_wei,

                            PiKaChu, kachu_times,
                            KachuBG, KachuTitle, KachuPOP, KachuQST, pikachu
                            )
from LabaModule.UI import img_button, delete_button, update_pic
from LabaModule.Sound import switch_music, super_up, green_up

def now_mod(): #現在模式
    global SuperHHH, GreenWei, PiKaChu
    mod = ""
    if SuperHHH :
        mod = "SuperHHH"
    elif GreenWei :
        mod = "GreenWei"
    elif PiKaChu :
        mod = "PiKaChu"
    else :
        mod = "Normal"
    
    return mod

#region 超級阿禾模式(SuperHHH)
def SuperFalse():
    global SuperHHH
    SuperHHH = False

def super_double(win, canvas_Game, all_SB, score, add, use_times):
    """超級阿禾加倍 獲得當前分數0.5倍的分數"""
    if all_SB :
        double_score = int(round(score / 2))
        add += double_score
        if use_times == 3:
            print(f"(超級阿禾x綠光阿瑋加倍分:{double_score * 3})")
            win.after(3000,lambda : canvas_Game.itemconfig("mod_2", text = f"(超級阿禾x綠光阿瑋加倍分:{double_score * 3})", fill = "yellow"))
        else:
            print(f"(超級阿禾加倍分:{double_score})")
            win.after(3000,lambda : canvas_Game.itemconfig("mod_2", text = f"(超級阿禾加倍分:{double_score})", fill = "yellow"))
        return add

def three_super(win, canvas_Game, all_p, score, add, use_times = 1):
    global SuperHHH, SuperTimes, SuperFirst
    """"檢查是否三個超級阿禾"""
    if all(p == "B" for p in all_p) and SuperHHH and SuperFirst:
        print("全超級阿禾")
        all_SB = True
        add = super_double(win, canvas_Game, all_SB, score, add, use_times)
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
        switch_music('.\\Asset\\SuperMusic.wav')
        

    else :
        canvas_Game.itemconfig("BG", image = BG)
        canvas_Game.itemconfig("Title", image = Title)
        canvas_Game.itemconfig("mod_1", text = "")
        switch_music('.\\Asset\\bgm.wav',game_running)

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
    if not game_running :
            SuperHHH = False
            win.after(2000 , lambda : super_screen(win,canvas_Game, False))
            return
    #遊戲進行
    mod = now_mod()
    if mod == "SuperHHH" : #正處於超級阿禾模式
        if all(p == "B" for p in all_p): #超級阿禾次數未用完且全阿禾
            SuperTimes += 2
            print("全阿禾，次數不消耗且+1！")
        if SuperTimes <= 0 : #超級阿禾次數用完
            SuperHHH = False
            win.after(2000 , lambda : super_screen(win,canvas_Game))

    elif mod == "Normal" or mod == "PiKaChu" or ModEnd: #未處於任何模式 or 皮卡丘模式 or 在其他模式結尾
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
            KachuFalse(canvas_Game)
    
def super_times(canvas_Game) :
    global SuperHHH, SuperTimes, SuperFirst
    if SuperHHH :
        SuperFirst =False
        SuperTimes -= 1
        print(f"超級阿禾剩餘次數:{SuperTimes}次")
        canvas_Game.itemconfig("mod_1", text = f"超級阿禾剩餘次數:{SuperTimes}次", fill = "#FF00FF")

def switch_rate(normal_acc):
    global super_acc
    mod = now_mod()
    if mod == "SuperHHH" :
        return super_acc
    elif mod == "Normal" or mod == "GreenWei" or mod == "PiKaChu" :
        return normal_acc
    
#endregion

#region 綠光阿瑋模式(GreenWei)
def GreenFalse(canvas_Game):
    global GreenWei, gss_times
    GreenWei = False
    gss_times = 0
    gss_txt(canvas_Game)

def gss_txt(canvas_Game):
    canvas_Game.itemconfig("gss", text = f"咖波累積數：{gss_times}")

def gss_acc_times(win, canvas_Game, all_p):
    """增加咖波累積數"""
    global gss_times
    if any(p == "A" for p in all_p) :
        for i in range(0,len(all_p)):
            if all_p[i] == "A" and gss_times < 20 :
                gss_times += 1
    print(f"咖波累積數：{gss_times}")
    win.after(3000, lambda : gss_txt(canvas_Game))

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
    elif any(p == "A" for p in all_p):
        if all_p[0] == "A":
            all_p[0] = "GW"
            canvas_Game.itemconfig("LP" , image = green_wei)
        if all_p[1] == "A":
            all_p[1] = "GW"
            canvas_Game.itemconfig("MP" , image = green_wei)
        if all_p[2] == "A":
            all_p[2] = "GW"
            canvas_Game.itemconfig("RP" , image = green_wei)
    else :
        canvas_Game.itemconfig("LP" , image = green_wei)
        canvas_Game.itemconfig("MP" , image = green_wei)
        canvas_Game.itemconfig("RP" , image = green_wei)
    green_up()


def green_screen(win,canvas_Game :tk.Canvas, game_running = True):
    """綠光阿瑋版面"""
    global GreenWei, GreenTimes
    if GreenWei :
        green_pop = img_button(win, lambda: delete_button(green_pop), canvas_Game, GreenPOP, 225 , 400, "flat", 0)
        print("綠光阿瑋出現了！")
        canvas_Game.itemconfig("BG", image = GreenBG)
        canvas_Game.itemconfig("Title", image = GreenTitle)
        canvas_Game.itemconfig("mod_1", text = f"綠光阿瑋剩餘次數:{GreenTimes}次", fill = "#00FF00")
        switch_music('.\\Asset\\GreenMusic.wav')
        

    else :
        canvas_Game.itemconfig("BG", image = BG)
        canvas_Game.itemconfig("Title", image = Title)
        canvas_Game.itemconfig("mod_1", text = "")
        switch_music('.\\Asset\\bgm.wav',game_running)


def judge_green(win, canvas_Game, all_p,  game_running = True, Kachu = False):
    """判斷綠光阿瑋"""
    global GreenRam, GreenWei, GreenTimes, GreenFirst, gss_times
    if not game_running:
        GreenWei = False
        if Kachu == False: #不是進入皮卡丘模式
            gss_times = 0
        win.after(2000 , lambda : green_screen(win, canvas_Game, False))
        return
    #遊戲進行
    mod = now_mod()
    gss_acc_times(win, canvas_Game, all_p)
    if mod == "GreenWei" : #處於綠光阿瑋模式
        if all(p == "A" for p in all_p) :#綠光次數未用完且全部咖波
            GreenTimes += 1
            canvas_Game.itemconfig("mod_1", text = f"綠光阿瑋剩餘次數:{GreenTimes}次", fill = "#00FF00")
            print("全咖波，次數不消耗！")
        if GreenTimes <= 0 : #綠光次數用完
            GreenWei = False
            win.after(2000 , lambda : green_screen(win, canvas_Game))
            judge_super(win, canvas_Game, all_p, ModEnd = True)
        
    elif mod == "Normal" or mod == "PiKaChu" : #未處於任何模式 or 皮卡丘模式
        gss_all = False

        #判斷是否有出現並全部咖波
        if all(x == "A" for x in all_p):
            gss_all = True

        if GreenRam <= GreenRate and gss_all : #3咖波
            GreenWei = True
            GreenFirst = True
            GreenTimes = 2
            win.after(3000, lambda : gss_txt(canvas_Game))
            win.after(2800 , lambda : change_gss(canvas_Game,all_p))
            win.after(3500 , lambda : green_screen(win, canvas_Game))
            KachuFalse(canvas_Game)

        elif gss_times >= 20 : #咖波累積數達到20
            GreenWei = True
            GreenFirst = True
            GreenTimes = 2
            gss_times = 0
            win.after(3000, lambda : gss_txt(canvas_Game))
            win.after(2800 , lambda : change_gss(canvas_Game,all_p, False))
            win.after(3500 , lambda : green_screen(win, canvas_Game))
            KachuFalse(canvas_Game)

def green_times(canvas_Game) :
    global GreenWei, GreenTimes, GreenFirst
    if GreenWei :
        GreenFirst = False
        GreenTimes -= 1
        print(f"綠光阿瑋剩餘次數:{GreenTimes}次")
        canvas_Game.itemconfig("mod_1", text = f"綠光阿瑋剩餘次數:{GreenTimes}次", fill = "#00FF00")

def switch_times():
    """加分倍數"""
    mod = now_mod()
    if mod == "GreenWei" :#綠光阿瑋使得分增加2倍(*3)
        t = 3
    elif mod == "Normal" or mod == "SuperHHH" or mod == "PiKaChu" :
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

#region 皮卡丘充電區(PiKaChu)
def KachuFalse(canvas_Game):
    """關掉皮卡丘"""
    global PiKaChu
    PiKaChu = False
    canvas_Game.itemconfig("mod_1", text = f"")

def change_kachu(canvas_Game, all_p):
    """把皮卡丘變成皮卡丘"""
    global super_hhh
    switch_music('.\\Asset\\KachuMusic.wav')
    if all_p[0] == "E":
        canvas_Game.itemconfig("LP" , image = pikachu)
    if all_p[1] == "E":
        canvas_Game.itemconfig("MP" , image = pikachu)
    if all_p[2] == "E":
        canvas_Game.itemconfig("RP" , image = pikachu)


def kachu_screen(win,canvas_Game :tk.Canvas, game_running = True):
    """皮卡丘版面"""
    global PiKaChu
    if PiKaChu :
        kachu_pop = img_button(win, lambda: delete_button(kachu_pop), canvas_Game, KachuPOP, 225 , 400, "flat", 0)
        print("皮卡丘充電！！")
        canvas_Game.itemconfig("BG", image = KachuBG)
        canvas_Game.itemconfig("Title", image = KachuTitle)
        canvas_Game.itemconfig("mod_1", text = "")
        
        
        

    else :
        canvas_Game.itemconfig("BG", image = BG)
        canvas_Game.itemconfig("Title", image = Title)
        canvas_Game.itemconfig("mod_1", text = "")
        switch_music('.\\Asset\\bgm.wav',game_running)

def judge_kachu(win, canvas_Game, all_p, times, ed,  game_running = True):
    """判斷皮卡丘"""
    global PiKaChu, kachu_times
    if not game_running:
        PiKaChu = False
        win.after(2000 , lambda : kachu_screen(win, canvas_Game, False))
        kachu_times =0
        return
    #遊戲進行
    if ed + 1 >= times:
        kachu_appear = False
        if any(p == "E" for p in all_p) :
            kachu_appear = True
        if kachu_appear:
            PiKaChu = True
            ed -= 5
            #關掉其他模式
            judge_super(win, canvas_Game, all_p, False)
            judge_green(win, canvas_Game, all_p, False, True)
            win.after(2500 , lambda : change_kachu(canvas_Game,all_p))
            win.after(3500 , lambda : kachu_screen(win, canvas_Game))

            win.after(3500 , lambda : kachu_time(canvas_Game))
    return ed
    
def Kachu_init(CANVA, score, times, ed):
    
    update_pic(CANVA , "LP" , KachuQST)
    update_pic(CANVA , "MP" , KachuQST)
    update_pic(CANVA , "RP" , KachuQST)

    CANVA.itemconfig("Add", text=f"")
    CANVA.itemconfig("Score", text= f"目前分數：{score}")
    CANVA.itemconfig("Times", text= f"剩餘次數：{times - ed}")
    CANVA.itemconfig("mod_2", text = f"")

def kachu_time(canvas_Game):
    global kachu_times
    kachu_times += 1
    print(f"已觸發 {kachu_times} 次皮卡丘充電")
    canvas_Game.itemconfig("mod_1", text = f"已觸發 {kachu_times} 次皮卡丘充電", fill = "#FFFF00")
#endregion 


