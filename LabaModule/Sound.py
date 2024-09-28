from pygame import mixer

def Ding():
    """播放叮音效"""
    mixer.music.load('.\\Asset\\Ding.mp3')  # 加載音效文件
    mixer.music.set_volume(0.3)
    mixer.music.play()  # 播放音效
