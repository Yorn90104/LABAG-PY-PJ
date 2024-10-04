from PIL import Image, ImageTk

Name = ""
#試算表 sheet
GetData = []

data_dict = {}

# 遊戲邏輯變數
times = 30 #可遊玩次數 正常30
ed = 0
score, add= 0, 0
all_score = [0]
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
    pc = Image.open(file).convert("RGBA")
    pc = pc.resize((w , h) , Image.LANCZOS)  # 調整圖片大小
    pic = ImageTk.PhotoImage(pc)
    return pic

BG = poccess_image('.\\Asset\\BG.png' , 450 , 800)
Title = poccess_image('.\\Asset\\Title.png' , 450 , 253)
QST = poccess_image('.\\Asset\\QST.jpg' , 150 , 200)  # ?
SB = poccess_image('.\\Asset\\SB.png' , 450 , 169) #記分板
back = poccess_image('.\\Asset\\back.png' , 30 , 30) #返回

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
SuperRate = 15 #正常 15

SuperHHH = False
SuperFirst = False
SuperRam = 0
SuperTimes = 0

SuperCircle = poccess_image('.\\Asset\\SuperCircle.png' , 350 , 350)

SuperBG = poccess_image('.\\Asset\\SuperBG.png' , 450 , 800)
SuperTitle = poccess_image('.\\Asset\\SuperTitle.png' , 450 , 253)
SuperQST = poccess_image('.\\Asset\\SuperQST.png' , 150 , 200)
SuperPOP = poccess_image('.\\Asset\\SuperPOP.png' , 450 , 800)

super_hhh = poccess_image('.\\Asset\\super_hhh.jpg' , 150 , 200)


#endregion

#region 綠光阿瑋區
GreenRate = 35 #正常 35

GreenWei = False
GreenFirst = False
GreenRam = 0
GreenTimes = 0
gss_times = 0 #咖波累積數

GreenBG = poccess_image('.\\Asset\\GreenBG.png' , 450 , 800)
GreenTitle = poccess_image('.\\Asset\\GreenTitle.png' , 450 , 253)
GreenQST = poccess_image('.\\Asset\\GreenQST.png' , 150 , 200)
GreenPOP = poccess_image('.\\Asset\\GreenPOP.png' , 450 , 800)

GreenLeft = poccess_image('.\\Asset\\GreenLeft.jpg' , 150 , 200)
GreenMid = poccess_image('.\\Asset\\GreenMid.jpg' , 150 , 200)
GreenRight = poccess_image('.\\Asset\\GreenRight.jpg' , 150 , 200)

green_wei = poccess_image('.\\Asset\\green_wei.jpg' , 150 , 200)

#endregion

#region 皮卡丘充電區

PiKaChu = False
kachu_times = 0
KachuBG = poccess_image('.\\Asset\\KachuBG.png' , 450 , 800)
KachuTitle = poccess_image('.\\Asset\\KachuTitle.png' , 450 , 253)
KachuQST = poccess_image('.\\Asset\\KachuQST.png' , 150 , 200)
KachuPOP = poccess_image('.\\Asset\\KachuPOP.png' , 450 , 800)

pikachu = poccess_image('.\\Asset\\pikachu.jpg' , 150 , 200)

#endregion
