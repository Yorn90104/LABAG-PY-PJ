#超級阿禾模式
import tkinter as tk
from PIL import Image, ImageTk
from random import randint

from LabaModule.Var import (SuperHHH,
                            BG,Title,
                            SuperRam, SuperTimes,
                            SuperBG, SuperTitle, super_hhh, SuperPOP, SuperQST
                            
                            )
from LabaModule.UI import img_button, delete_button
from LabaModule.Sound import super_up, switch_music, bgm_on_off

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
    super_up()

def super_screen(win,canvas_Game :tk.Canvas , button_music, game_running = True):
    """超級阿禾版面"""
    global SuperHHH, SuperTimes
    if SuperHHH :
        super_pop = img_button(win, lambda: delete_button(super_pop), canvas_Game, SuperPOP, 225 , 400, "flat", 0)
        canvas_Game.itemconfig("BG", image = SuperBG)
        canvas_Game.itemconfig("Title", image = SuperTitle)
        canvas_Game.itemconfig("mod_time", text = f"超級阿禾剩餘次數:{SuperTimes}次", fill = "#FF00FF")

        button_music.config(command = lambda : bgm_on_off(button_music,'.\\Asset\\SuperMusic.mp3'))
        switch_music('.\\Asset\\SuperMusic.mp3')
        

    else :
        canvas_Game.itemconfig("BG", image = BG)
        canvas_Game.itemconfig("Title", image = Title)
        canvas_Game.itemconfig("mod_time", text = "")
        
        button_music.config(command = lambda : bgm_on_off(button_music,'.\\Asset\\bgm.mp3'))
        switch_music('.\\Asset\\bgm.mp3',game_running)


def judge_super(win, canvas_Game, all_p, button_music, game_running = True):
    """判斷超級阿禾"""
    global SuperRam, SuperHHH, SuperTimes
    if game_running :
        if SuperHHH : #正處於超級阿禾狀態
            if SuperTimes <= 0 : #超級阿禾次數用完
                SuperHHH = False
                win.after(3500 , lambda : super_screen(win,canvas_Game, button_music))

        else : #未處於超級阿禾狀態
            hhh_appear = False
            #判斷是否有出現阿和
            if any(x == "B" for x in all_p):
                hhh_appear = True

            if SuperRam <= 50 and hhh_appear :
                SuperHHH = True
                SuperTimes = 6
                win.after(3000 , lambda : change_hhh(canvas_Game,all_p))
                win.after(3500 , lambda : super_screen(win, canvas_Game, button_music))
    else :
        SuperHHH = False
        win.after(3500 , lambda : super_screen(win,canvas_Game, button_music, False))

def super_times(win,canvas_Game) :
    global SuperHHH, SuperTimes
    if SuperHHH :
        SuperTimes -= 1
        win.after(3000 , lambda : canvas_Game.itemconfig("mod_time", text = f"超級阿禾剩餘次數:{SuperTimes}次", fill = "#FF00FF"))
        