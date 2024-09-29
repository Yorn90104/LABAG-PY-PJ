from pygame import mixer
from LabaModule.Var import bgm_playing

def Ding():
    """播放叮音效"""
    ding = mixer.Sound('.\\Asset\\Ding.mp3')  # 加載音效文件
    ding.set_volume(0.3)
    ding.play()  # 播放音效

def bgm_on_off(times = 30, ed = 0):
    global bgm_playing

    if bgm_playing or times - ed <= 0:
        mixer.music.stop()
        bgm_playing = False
        print("BGM已關閉")
    else :
        mixer.music.load('.\\Asset\\bgm.mp3')  # 背景音樂文件
        mixer.music.play(-1)  # -1 參數表示循環播放
        bgm_playing = True
        print("BGM已開啟")
