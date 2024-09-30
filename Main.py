#需先下載 Pillow 和 Pygame (pip install ******)
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


from LabaModule.UI import setup_frame ,  load_pic , Text, img_button ,txt_button
from LabaModule.Var import score, history_score, times, ed, Title, QST, BeginPIC, AgainPIC, SB,  L_pic, M_pic, R_pic, text_add, text_score, text_times
from LabaModule.Logic import Begin, game_again

#建立 GAME & END 畫面
frame_Game, canvas_Game = setup_frame(win, "BG")
frame_End, canvas_End =setup_frame(win)

#region GAME畫面

pic_title = load_pic(canvas_Game , Title , 0 , 25 , "Title")

L_pic = load_pic(canvas_Game , QST, 0, 250 , "LP")
M_pic = load_pic(canvas_Game , QST, 150, 250 , "MP")
R_pic = load_pic(canvas_Game , QST, 300, 250 , "RP")

text_add = Text(
                canvas_Game ,
                225 , 475 ,
                "" ,
                16 ,
                "yellow" ,
                "Add"
                )
text_score = Text(
                canvas_Game ,
                225 , 500 ,
                f"目前分數：{score}" ,
                16 ,
                "white" ,
                "Score"
                )
text_times = Text(
                canvas_Game ,
                225 , 525 ,
                f"剩餘次數：{times - ed}" ,
                16 ,
                "white" ,
                "Times"
                )
text_history_score = Text(
                canvas_Game ,
                5, 775 ,
                f"歷史最高分數：{history_score}" ,
                16 ,
                "#FFBF00",
                "history_score",
                "w" #靠左對齊
                )
#特殊模式顯示次數文字
text_mod = Text(
                canvas_Game ,
                225 , 650 ,
                "" ,
                16 ,
                "white",
                "mod_time",
                )

button_music = txt_button(
                        win,
                        lambda : bgm_on_off(button_music,'.\\Asset\\bgm.mp3'),
                        canvas_Game,
                        "開",
                        33, 33,
                        415, 765,
                        14,
                        "black",
                        "#00FF00",
                        "button_music"
                        )

button_begin = img_button(
                        win ,
                        lambda :Begin(win, canvas_Game, button_begin, frame_Game, frame_End, canvas_End, button_music) ,
                        canvas_Game,
                        BeginPIC,
                        225, 575
                        )
win.bind('<space>', lambda event :Begin(win , canvas_Game , button_begin, frame_Game, frame_End, canvas_End, button_music))# 綁定 Enter 鍵

#endregion

#region END畫面

text_over = Text(
                canvas_End ,
                225 , 260 ,
                "遊戲結束！" ,
                42 ,
                "white" ,
                "over"
                )
text_final_score = Text(
                        canvas_End ,
                        225 , 325 ,
                        "" ,
                        32 ,
                        "#FF0000" ,
                        "final_score"
                        )
text_HS = Text(
                canvas_End ,
                225, 450 ,
                f"歷史最高分數：{history_score}" ,
                16 ,
                "#FFBF00" ,
                "HS"
                )

button_again = img_button(
                        win,
                        lambda: game_again(win, canvas_Game, button_begin, frame_Game, frame_End, canvas_End, button_music),
                        canvas_End, AgainPIC,
                        225, 400
                        )

pic_SB = load_pic(canvas_End , SB, 0, 500, "SB")
#endregion

frame_Game.pack(fill='both', expand=True)

from LabaModule.Sound import bgm_on_off
bgm_on_off(button_music)

win.mainloop()