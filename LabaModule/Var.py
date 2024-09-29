from PIL import Image, ImageTk

# 遊戲邏輯變數
ram1, ram2, ram3 = 0, 0, 0
p1, p2, p3 = '', '', ''
score, add, ed = 0, 0, 0
times = 3

same3 = [200, 600, 1600, 1800, 10000, 20000]
same2 = [100, 170, 780, 870, 5000, 10000]
same1 = [30, 50, 250, 290, 1200, 2500]

# 圖片

def IMAGE(file, w, h):
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

BG = IMAGE('.\\Asset\\BG.png' , 450 , 800)
Title = IMAGE('.\\Asset\\Title.png' , 450 , 253)
QST = IMAGE('.\\Asset\\QST.jpg' , 150 , 200)  # ?
Gss = IMAGE('.\\Asset\\Gss.jpg' , 150 , 200)  # A
Hhh = IMAGE('.\\Asset\\Hhh.jpg' , 150 , 200)  # B
Hentai = IMAGE('.\\Asset\\Hentai.jpg' , 150 , 200)  # C
Handsun = IMAGE('.\\Asset\\Handsun.jpg' , 150 , 200)  # D
Kachu = IMAGE('.\\Asset\\Kachu.jpg' , 150 , 200)  # E
Rrr = IMAGE('.\\Asset\\RRR.jpg' , 150 , 200)  # F
SB = IMAGE('.\\Asset\\SB.png' , 450 , 169) #記分板
BeginPIC = IMAGE('.\\Asset\\BeginPIC.jpg' , 150 , 50)
AgainPIC = IMAGE('.\\Asset\\AgainPIC.jpg' , 150 , 50)

picture = [Gss , Hhh , Hentai , Handsun , Kachu , Rrr]


