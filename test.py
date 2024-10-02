# #測試用
import requests 

web = requests.get("https://script.google.com/macros/s/AKfycbzWA0mMx_B14vrHGW6-QK4tOClSIj1lw7udLJwp7XCg2nZ8hDxt7d-dqnc6WenqBM8FBA/exec")
GetData = web.json()

data_dict= {}

del GetData[0] #刪除第一列的欄名
for row in GetData : #對每一列的資料做
    del row[0]  #刪除第一格的"時間戳記"
    if row[0] != "" and row[1] != "" :
        name = str(row[0]) #將名稱那格變為字串型態
        score = int(row[1]) #將分數那格變為整數型態
        if name in data_dict :
            if score > data_dict[name] :
                data_dict[name] = score
        else :
                data_dict[name] = score

for d in data_dict :
    print(f"{d}：{data_dict[d]:>6}")