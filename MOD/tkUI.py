import tkinter as tk
from PIL import Image, ImageTk
used_picture = [
    ("BG", 450, 800),
    ("Title", 450, 253),
    ("QST", 150, 200),
    ("Gss", 150, 200),
    ("Hhh", 150, 200),
    ("Hentai", 150, 200),
    ("Handsun", 150, 200),
    ("Kachu", 150, 200),
    ("Rrr", 150, 200),
    ("BeginPIC", 150, 50),
    ("SB", 450, 169)
]
class frameUnit:
    def __init__(self, window, bg_pic) -> None:
        # 創建frame
        self.Frame = tk.Frame(window, width=450, height=800, bg='lightblue')
        self.Canvas = tk.Canvas(self.Frame, width=450, height=800)
        self.Canvas.pack(fill="both", expand=True)
        self.Canvas.create_image(0, 0, image = bg_pic, anchor="nw")
        self.PIC = {name: self.img2tk(name, (w, h)) for name, w, h in used_picture}

    def img2tk(self, pic_name, size: tuple[int, int]):
        pc = Image.open(f'.\\Asset\\{pic_name}.png')
        pc = pc.resize(size , Image.LANCZOS)  # 調整圖片大小
        pic = ImageTk.PhotoImage(pc)
        return pic
    
    def load_pic(self, pic_name, pos: tuple[int, int]):
        self.Canvas.create_image(pos[0], pos[1], image = self.PIC[pic_name], anchor = 'nw', tags = pic_name)
        
