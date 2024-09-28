from random import randint
class GameAPI:
    def __init__(self):
        self.price_score = {'A': [30, 100, 200],
                            'B': [50, 170, 600],
                            'C': [250, 780, 1600],
                            'D': [290, 870, 1800],
                            'E': [1200, 5000, 10000],
                            'F': [2500, 10000, 20000]}
        self.price_picture = {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}
        self.rnd = [0, 0, 0]
        self.price = ['', '', '']
        self.total_scores = 0
    
    def price_decide(self, num) -> str:
        '''依據數字回傳格子結果'''
        if num <= 36:
            return 'A'
        elif num <= 60:
            return 'B'
        elif num <= 77:
            return 'C'
        elif num <= 89:
            return 'D'
        elif num <= 97:
            return 'E'
        else:
            return 'F'
        
    def score_decide(self) -> int:
        '''回傳目前三個格子相加後總分'''
        count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}
        score = 0
        same_count = 0

        # 獲取重複次數
        for p in self.price:
            count[p] += 1
            same_count = max(same_count, count[p])

        # 獲取格子對應分數
        for c in count:
            if count[c]:
                score += self.price_score[c][count[c]-1]

        # 回傳結果
        if same_count == 1:
            return round(score / 3)
        elif same_count == 2:
            return round(score / 1.3)
        elif same_count == 3:
            return score
        else:
            return 0

    def rnd_price(self, idx, res = -1):
        '''改變第idx(0~2)號格子，若傳入res(0~6)則將idx格的結果定為res，否則隨機結果'''
        if res not in [0, 1, 2, 3, 4, 5]:
            res = randint(0, 5)
        self.price[idx] = self.price_decide(res)

