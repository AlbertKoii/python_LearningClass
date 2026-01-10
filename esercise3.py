
# 2026.01.10 下午


myName = "Albert"
city = "New Taipei city"

# print (f'''Hello my name is {myName} located at {city} ''')
# print (f"Hello my name is {myName} located at {city}")
# print (f"Hello my name is " + myName + " located at " + city)

# f 用於解析類似 js `` 讓變數可用

#  ================================== #
# 以下寫法會相同 

# input() 為會等待使用者輸入內容 

# name = input("請你輸入你的名字  :") # 內部可以輸入內容 ex. name = input("請你輸入你的名字  :")
# 會跑 請輸入你的名字 然後等待 使用者於 termino 輸入內容  , input() 內的資訊類似 js placeholder 於前端的顯示 
# city = input("請你輸入你的城市  :")

result = (f'''Hello my name is {myName} located at {city} ''')
# print (result)




# float +　INT (number ) = float type

# print(9 % 2) 這是餘數 可以用於判斷  奇偶數


# 美金轉換台幣
usdTOntd = 30
usd = input("How much NT is this usd ? ") # USD 

dataFinal = usdTOntd * int(usd) # NTD 
print ( usd , "USD can transfer into " , dataFinal , "NTD")