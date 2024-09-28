import sys
sys.stdout.reconfigure(encoding='utf-8')

import tkinter as tk
from pygame import mixer
from MOD.tkUI import frameUnit

# 音效初始化
mixer.init()

# 主視窗
win = tk.Tk()
win.title("啦八機")
win.iconbitmap('.\\Asset\\Superhhh.ico')
win.geometry("450x800")
win.resizable(False, False)

# 標題畫面
frame_title = frameUnit(win)
frame_title.Canvas.create_image()



frame_game = frameUnit(win)
frame_end = frameUnit(win)




win.mainloop()