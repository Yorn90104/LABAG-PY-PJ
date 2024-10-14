from Module.GUI import process_image_path
from pygame import mixer

BG = process_image_path('.\\Asset\\BG.png' , 450 , 800)
Title = process_image_path('.\\Asset\\Title.png' , 450 , 253)
QST = process_image_path('.\\Asset\\QST.jpg' , 150 , 200)  # ?


gss = process_image_path('.\\Asset\\Gss.jpg' , 150 , 200)  # A
hhh = process_image_path('.\\Asset\\Hhh.jpg' , 150 , 200)  # B
hentai = process_image_path('.\\Asset\\Hentai.jpg' , 150 , 200)  # C
handsun = process_image_path('.\\Asset\\Handsun.jpg' , 150 , 200)  # D
kachu = process_image_path('.\\Asset\\kachu.jpg' , 150 , 200)  # E
rrr = process_image_path('.\\Asset\\RRR.jpg' , 150 , 200)  # F


BeginPIC = process_image_path('.\\Asset\\BeginPIC.jpg' , 150 , 50)
AgainPIC = process_image_path('.\\Asset\\AgainPIC.jpg' , 150 , 50)
SB = process_image_path('.\\Asset\\SB.png' , 450 , 169) #記分板
back = process_image_path('.\\Asset\\back.png' , 30 , 30) #返回

Ding = mixer.Sound('.\\Asset\\Ding.wav')

#region 超級阿禾區

SuperCircle = process_image_path('.\\Asset\\SuperCircle.png' , 350 , 350)

SuperBG = process_image_path('.\\Asset\\SuperBG.png' , 450 , 800)
SuperTitle = process_image_path('.\\Asset\\SuperTitle.png' , 450 , 253)
SuperQST = process_image_path('.\\Asset\\SuperQST.png' , 150 , 200)
SuperPOP = process_image_path('.\\Asset\\SuperPOP.png' , 450 , 800)

super_hhh = process_image_path('.\\Asset\\super_hhh.jpg' , 150 , 200)

SuperUP = mixer.Sound('.\\Asset\\SuperUP.wav')

   


#endregion

#region 綠光阿瑋區

GreenBG = process_image_path('.\\Asset\\GreenBG.png' , 450 , 800)
GreenTitle = process_image_path('.\\Asset\\GreenTitle.png' , 450 , 253)
GreenQST = process_image_path('.\\Asset\\GreenQST.png' , 150 , 200)
GreenPOP = process_image_path('.\\Asset\\GreenPOP.png' , 450 , 800)

GreenLeft = process_image_path('.\\Asset\\GreenLeft.jpg' , 150 , 200)
GreenMid = process_image_path('.\\Asset\\GreenMid.jpg' , 150 , 200)
GreenRight = process_image_path('.\\Asset\\GreenRight.jpg' , 150 , 200)

green_wei = process_image_path('.\\Asset\\green_wei.jpg' , 150 , 200)

GreenUP = mixer.Sound('.\\Asset\\GreenUP.wav')
#endregion

#region 皮卡丘充電區

KachuBG = process_image_path('.\\Asset\\KachuBG.png' , 450 , 800)
KachuTitle = process_image_path('.\\Asset\\KachuTitle.png' , 450 , 253)
KachuQST = process_image_path('.\\Asset\\KachuQST.png' , 150 , 200)
KachuPOP = process_image_path('.\\Asset\\KachuPOP.png' , 450 , 800)

pikachu = process_image_path('.\\Asset\\pikachu.jpg' , 150 , 200)

#endregion
