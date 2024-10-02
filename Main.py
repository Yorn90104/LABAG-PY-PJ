#需先下載 Pillow 和 Pygame (pip install ******)

# main.py：主程序，負責設定遊戲視窗，設置圖片、按鈕，及整合各模組。
# Var.py：包含所有變量、圖片處理邏輯、機率和分數的配置。
# UI.py：用來設置 tkinter 視窗中的 UI 元素（如按鈕、文字、圖片等）。
# Sound.py：負責聲音效果和音樂控制的模組。
# SuperHhh.py：處理超級阿禾模式的邏輯和特效。
# Logic.py：負責遊戲的核心邏輯，包括圖片隨機選擇、分數計算及更新遊戲畫面。
import sys
sys.stdout.reconfigure(encoding='utf-8')

import tkinter as tk

# 主視窗
win = tk.Tk()
win.title("啦八機")
win.iconbitmap('.\\Asset\\Superhhh.ico')
win.geometry("450x800")
win.resizable(False, False)


from LabaModule.UI import setup_frame ,  load_pic , Text, img_button ,txt_button, input_box, get_input
from LabaModule.Var import (Name,
                            score, history_score,
                            times, ed,
                            Title, QST,back, BeginPIC, AgainPIC, SB, SuperCircle,
                            )
from LabaModule.Logic import Begin, game_start

#建立 HOME & GAME & END 畫面
frame_Home, canvas_Home =setup_frame(win)
frame_Game, canvas_Game = setup_frame(win, "BG")
frame_End, canvas_End =setup_frame(win)

#region HOME畫面
def into_game(win):
    """進入遊戲"""
    global Name
    Name = get_input(input_name)
    if Name != "" :
        canvas_Game.itemconfig("Name", text =  f"玩家名：{Name}")
    else :
        canvas_Game.itemconfig("Name", text =  "")

    game_start(win, canvas_Game, button_begin, frame_Game, frame_End, canvas_End, button_music, frame_Home, Name)
    win.unbind('<Return>')
    print("進入遊戲")

text_fanyu = Text(
                canvas_Home,
                225, 100,
                "作者IG：fan._.yuuu",
                30,
                "#00FFFF",
                "fanyu"
                )

pic_into = load_pic(canvas_Home, SuperCircle, 25, 130, "into")
canvas_Home.tag_bind("into", "<Button-1>", lambda event: into_game(win))

win.bind('<Return>', lambda event :into_game(win))
text_click = Text(
                canvas_Home,
                225, 550,
                "點擊上方圖片(或 ENTER )\n       進入遊戲 >>>>>",
                15,
                "#FFFFAA",
                "click" 
                )

input_name = input_box(win, canvas_Home, "", 225, 600, 18, 15)
text_hint = Text(
                canvas_Home,
                225, 625,
                "輸入你的稱呼",
                12,
                "white",
                "hint"
                )
#endregion

#region GAME畫面

pic_title = load_pic(canvas_Game , Title , 0 , 25 , "Title")

load_pic(canvas_Game , QST, 0, 250 , "LP")
load_pic(canvas_Game , QST, 150, 250 , "MP")
load_pic(canvas_Game , QST, 300, 250 , "RP")

text_name_Game = Text(
                canvas_Game,
                5, 50,
                "",
                15,
                "white",
                "Name",
                "w"
                )
text_add = Text(
                canvas_Game ,
                225 , 478 ,
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
#region 特殊模式顯示次數文字
text_mod1 = Text(
                canvas_Game ,
                225 , 650 ,
                "" ,
                16 ,
                "white",
                "mod_1",
                )

text_mod2 = Text(
                canvas_Game ,
                225 , 460 ,
                "" ,
                10 ,
                "white",
                "mod_2",
                )
#endregion

def back_home():
    """返回首頁"""
    frame_Game.pack_forget()
    bgm_on_off(button_music,False)
    frame_Home.pack(fill='both', expand=True)
    win.bind('<Return>', lambda event :into_game(win))
    print("返回首頁")
    
button_back = img_button(
                        win,
                        back_home,
                        canvas_Game,
                        back,
                        18, 18
                        )

button_music = txt_button(
                        win,
                        lambda : bgm_on_off(button_music),
                        canvas_Game,
                        "關",
                        33, 33,
                        415, 765,
                        14,
                        "black",
                        "#C0C0C0",
                        "button_music"
                        )
def press_m(event):
    if event.char == 'm':
        print("M 鍵被按下")
        bgm_on_off(button_music)
win.bind('<Key>', press_m) #綁定M鍵

button_begin = img_button(
                        win ,
                        lambda :Begin(win, canvas_Game, button_begin, frame_Game, frame_End, canvas_End, button_music) ,
                        canvas_Game,
                        BeginPIC,
                        225, 575
                        )
win.bind('<space>', lambda event :Begin(win , canvas_Game , button_begin, frame_Game, frame_End, canvas_End, button_music))# 綁定 space 鍵

#endregion

#region END畫面
text_name_End = Text(
                canvas_End,
                225, 175,
                "",
                22,
                "skyblue",
                "Name",
                )
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
                        lambda: game_start(win, canvas_Game, button_begin, frame_Game, frame_End, canvas_End, button_music, frame_End, Name),
                        canvas_End,
                        AgainPIC,
                        225, 400
                        )

pic_SB = load_pic(canvas_End , SB, 0, 500, "SB")
#endregion

frame_Home.pack(fill='both', expand=True)

from LabaModule.Sound import bgm_on_off

win.mainloop()