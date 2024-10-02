from random import randint
from LabaModule.Var import (Name,
                        ram1, ram2, ram3,
                        p1, p2, p3, all_p,
                        normal_acc,
                        score, history_score, add,all_score,
                        ed, times,
                        same1, same2, same3, picture
                        )
from LabaModule.UI import  init , update_pic, result_txt 
from LabaModule.Sound import Ding , bgm_on_off
from LabaModule.sheet import commit_score, find_history_score

from LabaModule.Mod import (now_mod,
                        super_ram,super_times,Super_init,
                        judge_super,three_super, switch_rate,
                        )

# 主要邏輯流程：
# 按鈕或鍵盤事件觸發 Begin 函數。
# 重置畫面，並初始化變量。
# 生成三個隨機數，每個隨機數對應不同的圖片。
# 按時間間隔改變畫面中的三張圖片，每隔 0.5 秒更新一張圖片。
# 計算得分，根據三張圖片的組合（是否相同）來計算加分。
# 顯示結果，更新畫面上的分數、加分和剩餘次數。


def result(canvas_Game):
      """計算和顯示結果"""
      global score, add, ed, all_p
      ed += 1
      score += add
      print(f"\n第{ed}次")
      print(f' | {all_p[0]} | {all_p[1]} | {all_p[2]} |')
      print(f"+{add}")
      print(f"目前分數：{score}")
      result_txt(canvas_Game , score , add , ed , times)
      add = 0

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

def PrizePIC(p):
    """根據歸屬選擇圖 (歸屬)"""
    if p == "A":
        return picture[0]
    elif p == "B":
        return picture[1]
    elif p == "C":
        return picture[2]
    elif p == "D":
        return picture[3]
    elif p == "E":
        return picture[4]
    elif p == "F":
        return picture[5]

def change_picture(CANVA , tg , p):
    """哪個變圖 (畫面, 標籤, 歸屬)"""
    new_pic = PrizePIC(p)
    update_pic(CANVA, tg , new_pic)
    Ding()

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

def button_unable(win , button) :
      win.unbind('<space>')  # 取消space鍵的綁定
      button.config(state='disabled')  # 停用按鈕

def button_able(win , canvas_Game , button_begin, frame_Game, frame_End, canvas_End, button_music):
      win.bind('<space>', lambda event: Begin(win , canvas_Game , button_begin, frame_Game, frame_End, canvas_End, button_music))
      button_begin.config(state='normal')

def history_score_txt(canvas_End):
      global score, history_score
      all_score.append(score)
      history_score = max(all_score)
      canvas_End.itemconfig("HS", text=f"歷史最高分數：{history_score}" ) 

def game_over(frame_Game, frame_End, canvas_End, button_music):
      global Name, score, history_score, times, ed
      print("")
      print(f"遊戲已結束，最終分數為：{score}。")
      commit_score(Name,score)
      bgm_on_off(button_music, game_running = False)
      """遊戲結束，切換到結果頁面"""
      frame_Game.pack_forget()  # 隱藏遊戲畫面
      print("切換End畫面")
      frame_End.pack(fill='both', expand=True)  # 顯示遊戲結束畫面
      canvas_End.itemconfig("Name", text =  f"{Name}")
      canvas_End.itemconfig("over", text="遊戲結束！") 
      canvas_End.itemconfig("final_score", text=f"最終分數：{score}")  # 最終分數顯示
      history_score_txt(canvas_End) #歷史分數更新
      Ding()

def game_start(win , canvas_Game , button_begin, frame_Game, frame_End, canvas_End, button_music, Frame, name= "") :
      """遊戲開始，最後一個FRAME要指定"""
      global ram1 , ram2 , ram3 , p1 , p2 , p3 , score , add , ed  , times, history_score, Name
      Name = name
      ram1, ram2, ram3 = 0 , 0 , 0
      p1, p2, p3 = '', '', ''
      score, add, ed = 0 , 0 , 0

      init(canvas_Game, score, times , ed)
      bgm_on_off(button_music)
      history_score = find_history_score(Name)
      canvas_Game.itemconfig("history_score", text=f"歷史最高分數：{history_score}" ) 
      button_able(win , canvas_Game , button_begin, frame_Game, frame_End, canvas_End, button_music)
      Frame.pack_forget()
      print("切換Game畫面")
      frame_Game.pack(fill='both', expand=True)

def Begin(win , canvas_Game , button_begin, frame_Game, frame_End, canvas_End, button_music) :
      global ram1, ram2, ram3, p1, p2, p3, all_p,  score, add, ed, normal_acc

      print(u"\n開始按鈕被點擊了！")
      super_times(win,canvas_Game)
      button_unable(win , button_begin)

      mod = now_mod()
      if mod == "Normal":
            init(canvas_Game, score, times , ed)
      elif mod == "SuperHHH":
           Super_init(canvas_Game, score, times , ed)

      if ed  < times :

            #隨機數
            ram1 , ram2 , ram3 = randint(1,100) , randint(1,100) , randint(1,100)
            print(f"圖片隨機數為：{ram1} | {ram2} | {ram3}")
            super_ram()
            

            #機率找歸屬
            use_rate = switch_rate(normal_acc)
            print(f"機率區間：{use_rate}")
            p1 = change_rate(use_rate, ram1)
            p2 = change_rate(use_rate, ram2)
            p3 = change_rate(use_rate, ram3)
            
            all_p = [p1, p2, p3]
            judge_super(win, canvas_Game, all_p)

            #每隔0.5秒改圖片
            win.after(500 , lambda : change_picture(canvas_Game , "LP" , p1))
            win.after(1000 , lambda : change_picture(canvas_Game , "MP" , p2))
            win.after(1500 , lambda : change_picture(canvas_Game , "RP" , p3))

            #增加分數

            add = calculate_score(p1 , p2 , p3 , add)
            add = three_super(win, canvas_Game, all_p, score, add)
            
            win.after(3000 , lambda : result(canvas_Game))

            if ed + 1 >= times:
                # 判斷遊戲結束
                # 停用按鈕和鍵盤事件
                win.after(3500, lambda : button_unable(win, button_begin))

                # 切換到結束畫面
                win.after(3500, lambda : game_over(frame_Game , frame_End , canvas_End, button_music))
                
                #若在超級阿禾模式則還原
                judge_super(win, canvas_Game, all_p, False)

                
            else:
                judge_super(win, canvas_Game, all_p)
                # 遊戲繼續
                win.after(3500 , lambda : button_able(win, canvas_Game, button_begin, frame_Game, frame_End, canvas_End, button_music))