import sys
sys.stdout.reconfigure(encoding='utf-8')

import tkinter as tk
import pygame


# 主視窗
win = tk.Tk()
win.title("啦八機")
win.iconbitmap('.\\Asset\\Superhhh.ico')
win.geometry("450x800")
win.resizable(False, False)

# 初始化音效
from LabaModule.Sound import bgm_on_off
pygame.mixer.init()
bgm_on_off()

from LabaModule.UI import setup_frame ,  load_pic , Button , Text
from LabaModule.Var import score, times, ed, Title, QST, BeginPIC, AgainPIC, SB,  L_pic, M_pic, R_pic, text_add, text_score, text_times
from LabaModule.Logic import Begin, game_again

#建立 GAME & END 畫面
frame_Game, canvas_Game = setup_frame(win)
frame_End, canvas_End =setup_frame(win)

#region GAME畫面

pic_title = load_pic(canvas_Game , Title , 0 , 25 , "TITLE")

L_pic = load_pic(canvas_Game , QST, 0, 250 , "LP")
M_pic = load_pic(canvas_Game , QST, 150, 250 , "MP")
R_pic = load_pic(canvas_Game , QST, 300, 250 , "RP")

text_add = Text(canvas_Game , 225 , 475 , "" , 16 , "yellow" , "Add")
text_score = Text(canvas_Game , 225 , 500 , f"目前分數：{score}" , 16 , "white" , "Score")
text_times = Text(canvas_Game , 225 , 525 , f"剩餘次數：{times - ed}" , 16 , "white" , "Times")

button_begin = Button(win , lambda :Begin(win , canvas_Game , button_begin, frame_Game, frame_End, canvas_End) , canvas_Game , 225 , 575 , BeginPIC)
# 綁定 Enter 鍵啟動遊戲
win.bind('<Return>', lambda event :Begin(win , canvas_Game , button_begin, frame_Game, frame_End, canvas_End))

#endregion

#region END畫面

text_over = Text(canvas_End , 225 , 280 , "遊戲結束！" , 42 , "white" , "over")
text_final_score = Text(canvas_End , 225 , 345 , "" , 32 , "gold" , "final_score")

button_again = Button(win,lambda: game_again(win , canvas_Game , button_begin, frame_Game, frame_End, canvas_End), canvas_End, 225, 425, AgainPIC)

pic_SB = load_pic(canvas_End , SB, 0, 500, "SB")
#endregion

frame_Game.pack(fill='both', expand=True)

win.mainloop()