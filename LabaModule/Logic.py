from random import randint
from LabaModule.Var import ram1 , ram2 , ram3 , p1 , p2 , p3 , score , add , ed ,times , same1 , same2 ,same3 , L_PIC , M_PIC , R_PIC , text_ADD , text_Score , text_Times
from LabaModule.UI import  init , Local , Result_TXT 


def result(CANVA):
      """計算和顯示結果"""
      global score, add, ed, p1, p2, p3 , text_ADD, text_Score, text_Times
      ed += 1
      score += add
      print(f"第{ed}次")
      print(f' | {p1} | {p2} | {p3} |')
      print(f"+{add}")
      print(f"目前分數：{score}")
      Result_TXT(CANVA , score , add , ed , times , text_Score , text_ADD , text_Times)
      add = 0

def ChangeA( y):
      """根據隨機數生成圖片的歸屬 (歸屬, 隨機數)"""
      if y <= 36:
            return 'A'
      elif 36 < y <= 60:
            return 'B'
      elif 60 < y <= 77:
            return 'C'
      elif 77 < y <= 89:
            return 'D'
      elif 89 < y <= 97:
            return 'E'
      else:
            return 'F'

def ADD(x, y, lst):
    """增加分數 (歸屬, 增加分數, 分數清單)"""
    if x == 'A':
        y += lst[0]
    elif x == 'B':
        y += lst[1]
    elif x == 'C':
        y += lst[2]
    elif x == 'D':
        y += lst[3]
    elif x == 'E':
        y += lst[4]
    elif x == 'F':
        y += lst[5]
    return y

def calculate_score(p1 , p2 , p3 , a):
      """計算分數"""
      #3個相同
      if p1 == p2 == p3 :
            a = ADD(p1 , a , same3)

      #2個相同=(2個相同的+1個不同的)/1.3
      # 1 & 2
      elif p1 == p2 :
            a = ADD(p1 , a , same2)
            #不同的
            a = ADD(p3 , a , same1)

            a = round( a / 1.3 )

      # 2 & 3
      elif p2 == p3 :
            #2個同
            a = ADD(p2 , a , same2)
            #不同的
            a = ADD(p1 , a , same1)

            a = round( a / 1.3 )

      # 1 & 3
      elif p1 == p3 :
            #2個同
            a = ADD(p3 , a , same2)
            #不同的
            a = ADD(p2 , a , same1)

            a = round( a / 1.3 )

      #3個都不同 加總/3
      elif p1 != p2 != p3 :
            #1
            a = ADD(p1 , a , same1)
            
            #2
            a = ADD(p2 , a , same1)
            
            #3
            a = ADD(p3 , a , same1)

            a = round( a / 3 )
      return a

def Begin(win ,canvas_Game) :
      global ram1 , ram2 , ram3 , p1 , p2 , p3 , score , add , ed , times ,  L_PIC , M_PIC , R_PIC

      print(u"按鈕被點擊了！")
      
      init(canvas_Game)
      

      if ed  < times :

            #隨機數
            ram1 , ram2 , ram3 = randint(1,100) , randint(1,100) , randint(1,100)

            #歸屬
            p1 = ChangeA(ram1)
            p2 = ChangeA(ram2)
            p3 = ChangeA(ram3)

            #每隔0.5秒改圖片
            win.after(500 , lambda : Local(canvas_Game , L_PIC , p1 , 0 , 250))
            win.after(1000 , lambda : Local(canvas_Game , M_PIC , p2 , 150 , 250))
            win.after(1500 , lambda : Local(canvas_Game , R_PIC , p3 , 300 , 250))

            #增加分數
            add = calculate_score(p1 , p2 , p3 , add)
            
            win.after(3000 , lambda : result(canvas_Game))