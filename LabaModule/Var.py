from PIL import Image, ImageTk

# 遊戲邏輯變數
times = 30 #可遊玩次數
ed = 0
score, add= 0, 0
history_score = 0

#遊戲後臺變數
ram1, ram2, ram3 = 0, 0, 0
p1, p2, p3 = '', '', ''
all_p = []

#機率
def acc_rate(original_rate):
    result_rate= []
    acc = 0
    for x in original_rate:
        acc += x
        result_rate.append(acc)
    return result_rate

normal_rate = [36, 24, 17, 12, 8, 3]
normal_acc = acc_rate(normal_rate)

super_rate = [19, 5, 19, 19, 19, 19]
super_acc = acc_rate(super_rate)

#分數清單
same3 = [200, 600, 1600, 1800, 10000, 20000]
same2 = [100, 170, 780, 870, 5000, 10000]
same1 = [30, 50, 250, 290, 1200, 2500]

# 圖片

def poccess_image(file, w, h):
    """處理成TK可識別的圖 (路徑, 長, 寬)"""
    pc = Image.open(file)
    pc = pc.resize((w , h) , Image.LANCZOS)  # 調整圖片大小
    pic = ImageTk.PhotoImage(pc)
    return pic

L_pic = None
M_pic = None
R_pic = None
text_add = None
text_score = None
text_times = None

BG = poccess_image('.\\Asset\\BG.png' , 450 , 800)
Title = poccess_image('.\\Asset\\Title.png' , 450 , 253)
QST = poccess_image('.\\Asset\\QST.jpg' , 150 , 200)  # ?
SB = poccess_image('.\\Asset\\SB.png' , 450 , 169) #記分板

BeginPIC = poccess_image('.\\Asset\\BeginPIC.jpg' , 150 , 50)
AgainPIC = poccess_image('.\\Asset\\AgainPIC.jpg' , 150 , 50)

gss = poccess_image('.\\Asset\\Gss.jpg' , 150 , 200)  # A
hhh = poccess_image('.\\Asset\\Hhh.jpg' , 150 , 200)  # B
hentai = poccess_image('.\\Asset\\Hentai.jpg' , 150 , 200)  # C
handsun = poccess_image('.\\Asset\\Handsun.jpg' , 150 , 200)  # D
kachu = poccess_image('.\\Asset\\kachu.jpg' , 150 , 200)  # E
rrr = poccess_image('.\\Asset\\RRR.jpg' , 150 , 200)  # F

picture = [gss , hhh , hentai , handsun , kachu , rrr]

bgm_playing = False

#region 超級阿禾區

SuperHHH = False
SuperRam = 0
SuperTimes = 0

SuperBG = poccess_image('.\\Asset\\SuperBG.png' , 450 , 800)
SuperTitle = poccess_image('.\\Asset\\SuperTitle.png' , 450 , 253)
SuperQST = poccess_image('.\\Asset\\SuperQST.png' , 150 , 200)
SuperPOP = poccess_image('.\\Asset\\SuperPOP.png' , 450 , 800)

super_hhh = poccess_image('.\\Asset\\super_hhh.jpg' , 150 , 200)

#endregion


