#測試最大值
import sys , math
sys.stdout.reconfigure(encoding='utf-8')

from random import randint #隨機數字

#region 定義區
AllScore = []
AllSuper = []
#初始設定
game_running = True

ram1 , ram2 , ram3 = 0 , 0 , 0
SuperRam = 0
GreenRam = 0

p1 , p2 , p3 = '' , '' , ''
all_p = []

score = 0
add = 0
times = 30
ed = 0

SuperTimes = 0
SuperHHH = False
SuperFirst = False
superS = 0

GreenTimes = 0
GreenWei = False
GreenFirst = False
greenS = 0

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
same3 = [200 , 600 , 1600 , 1800 , 10000 , 20000]
same2 = [100 , 170 , 780 , 870 , 5000 , 10000]
same1 = [30 , 50 , 250 , 290 , 1200 , 2500]

#endregion
def now_mod(): #現在模式
    global SuperHHH, GreenWei
    mod = ""
    if SuperHHH :
        mod = "SuperHHH"
    elif GreenWei :
        mod = "GreenWei"
    else :
        mod = "Normal"
    
    return mod

#region 超級阿禾區
def super_times(Times) :
      global SuperHHH, SuperFirst
      if SuperHHH :
            SuperFirst = False
            Times -= 1
      return Times

def super_ram(SuperRam):
    """阿禾隨機數"""
    SuperRam = randint(1,100)
    return SuperRam

def judge_super(all_p, game_running = True, ModEnd = False):
      """判斷超級阿禾"""
      global SuperRam, SuperHHH, SuperTimes, SuperFirst, superS
      if game_running :#遊戲進行
            mod = now_mod()
            if mod == "SuperHHH" : #正處於超級阿禾狀態
                  if all(x == "B" for x in all_p):
                        SuperTimes += 2
                  if SuperTimes <= 0 : #超級阿禾次數用完
                        SuperHHH = False
                        judge_super(all_p, ModEnd = True)
            elif mod == "Normal" or ModEnd : #未處於超級阿禾狀態
                  hhh_appear = False
                  #判斷是否有出現阿和
                  if any(x == "B" for x in all_p):
                        hhh_appear = True
                  if SuperRam <= 15 and hhh_appear :#超級阿禾出現的機率
                        SuperHHH = True
                        SuperFirst = True
                        superS += 1
                        SuperTimes = 6
      else :
            SuperHHH = False


def switch_rate(normal_acc):
    global super_acc
    mod = now_mod()
    if mod == "SuperHHH" :
        return super_acc
    elif mod == "Normal" :
        return normal_acc
    
def super_double(all_SB, score, add):
      """超級阿禾加倍 獲得當前分數0.5倍的分數"""
      if all_SB :
            double_score = int(round(score / 2))
            add += double_score
            return add

def three_super(all_p, score, add):
    global SuperHHH, SuperTimes, SuperFirst
    """"檢查是否三個超級阿禾"""
    if all(p == "B" for p in all_p) and SuperHHH and SuperFirst:
        all_SB = True
        add = super_double(all_SB, score, add)
        return add
    else:
        return add
#endregion

#region 綠光阿瑋區
def green_ram():
    """阿瑋隨機數"""
    global GreenRam
    GreenRam = randint(1,100)

def judge_super(all_p, game_running = True):
      """判斷超級阿禾"""
      global GreenRam, GreenWei, GreenTimes, GreenFirst, greenS
      if game_running :
            mod = now_mod()
            if mod == "GreenWei" : 
                  if all(x == "A" for x in all_p):
                        GreenTimes += 1
                  if GreenTimes <= 0 : 
                        GreenWei = False
                        judge_super(all_p, ModEnd = True)
            elif mod == "Normal"  : 
                  hhh_appear = False

                  if any(x == "B" for x in all_p):
                        hhh_appear = True
                  if SuperRam <= 15 and hhh_appear :#超級阿禾出現的機率
                        SuperHHH = True
                        SuperFirst = True
                        superS += 1
                        SuperTimes = 6
      else :
            SuperHHH = False
#endregion

#region 普通函式區
def change_rate(rate, y):
      """根據隨機數和機率找歸屬 (隨機數)"""
      if y <= rate[0] :
            return 'A'
      elif y <= rate[1] :
            return 'B'
      elif y <= rate[2] :
            return 'C'
      elif y <= rate[3] :
            return 'D'
      elif y <= rate[4] :
            return 'E'
      elif y <= rate[5] :
            return 'F'


def ADD(x,y,lst) :
      '(歸屬,增加分,分數清單)'
      if x == 'A':
            y = y + lst[0]
      elif x == 'B' :
            y = y + lst[1]
      elif x == 'C' :
            y = y + lst[2]
      elif x == 'D' :
            y = y + lst[3]
      elif x == 'E' :
            y = y + lst[4]
      elif x == 'F' :
            y = y + lst[5]
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

def result() :
    global score , add , ed , p1 , p2 , p3
    ed += 1
    score += add
    add = 0
#endregion

test = int (input("請輸入測試次數"))
LOG = int (math.log10(test) + 2)

for i in range(1 ,test + 1) :
      game_running = True

      ram1 , ram2 , ram3 = 0 , 0 , 0
      SuperRam = 0

      p1 , p2 , p3 = '' , '' , ''
      all_p = []

      score = 0
      add = 0
      times = 30
      ed = 0
      
      SuperTimes = 0
      SuperHHH = False
      superS = 0

      while ed < times :
            SuperTimes = super_times(SuperTimes)
            #隨機數
            ram1 , ram2 , ram3 = randint(1,100) , randint(1,100) , randint(1,100)
            SuperRam = super_ram(SuperRam)

            #歸屬
            use_rate = switch_rate(normal_acc)
            p1 = change_rate(use_rate,ram1)
            p2 = change_rate(use_rate,ram2)
            p3 = change_rate(use_rate,ram3)
            
            all_p = [p1, p2, p3]
            judge_super(all_p)

            #增加分數
            add = calculate_score(p1 , p2 , p3 , add)
            add = three_super(all_p, score, add)

            result()
            #遊戲繼續
            
      #遊戲結束
      game_running = False
      judge_super(all_p, game_running)
      
      AllScore.append(score)
      AllSuper.append(superS)

      print(f"第{i : {LOG}}次 分數：{score : 8} ({superS : 2} 次 超級阿禾 )")
      
MIN = min(AllScore) 
min_Idx = int(AllScore.index(MIN) + 1)
min_super = AllSuper[AllScore.index(MIN)]

MAX = max(AllScore) 
max_Idx = int(AllScore.index(MAX) + 1)
max_super = AllSuper[AllScore.index(MAX)]

print (f"最低分數為第{min_Idx: {LOG}}次： {MIN} ({min_super : 2} 次超級阿禾 )")  
print (f"最高分數為第{max_Idx: {LOG}}次： {MAX} ({max_super : 2} 次超級阿禾 )")  


