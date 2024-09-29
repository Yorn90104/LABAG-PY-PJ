from pygame import mixer
from LabaModule.Var import bgm_playing

# 初始化音效
mixer.init()

def Ding():
    """播放叮音效"""
    ding = mixer.Sound('.\\Asset\\Ding.mp3')  # 加載音效文件
    ding.set_volume(0.3)
    ding.play()  # 播放音效

def play_music(file):
    """播放音樂"""
    mixer.music.load(file) # 背景音樂文件
    mixer.music.play(-1) # -1 參數表示循環播放

def stop_music() :
    """停止當前音樂"""
    mixer.music.stop()

def bgm_on_off(button_music, file = '.\\Asset\\bgm.mp3', game_running = True) :
    """音樂開關"""
    global bgm_playing
    #關
    if bgm_playing or game_running == False :
        stop_music()
        button_music.config(text="關", bg="#C0C0C0") 
        bgm_playing = False
        print("BGM已停止")
    #開
    else :
        play_music(file) 
        button_music.config(text="開", bg="#00FF00")
        bgm_playing = True
        print("BGM已開啟")

def super_up():
    """播放阿禾升級音效"""
    sup = mixer.Sound('.\\Asset\\SuperUP.mp3')  # 加載音效文件
    sup.set_volume(0.3)
    sup.play()  # 播放音效

def switch_music(file ,game_running = True) :
    global bgm_playing
    if bgm_playing:
        stop_music()
        if game_running :
            play_music(file)
