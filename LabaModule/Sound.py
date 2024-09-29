from pygame import mixer
from LabaModule.Var import bgm_playing

def Ding():
    """播放叮音效"""
    ding = mixer.Sound('.\\Asset\\Ding.mp3')  # 加載音效文件
    ding.set_volume(0.3)
    ding.play()  # 播放音效

def bgm_on_off(button_music, times = 30, ed = 0) :
    """音樂開關"""
    global bgm_playing
    #關
    if bgm_playing or times - ed <= 0 :
        mixer.music.stop()
        button_music.config(text="關", bg="#C0C0C0") 
        bgm_playing = False
        print("BGM已停止")
    #開
    else :
        mixer.music.load('.\\Asset\\bgm.mp3')  # 背景音樂文件
        mixer.music.play(-1)  # -1 參數表示循環播放
        button_music.config(text="開", bg="#00FF00")
        bgm_playing = True
        print("BGM已開啟")
