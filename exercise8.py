print(f''' 開始python 小學堂了喔 , exercise 8''')
import time  # 1. 必須導入模組


message = "Hello everyone"

# lost 
# list(message)
# print (list(message))
# 輸出 == ['H', 'e', 'l', 'l', 'o', ' ', 'e', 'v', 'e', 'r', 'y', 'o', 'n', 'e']cls

# 學會 list 跟 dict
x2 = ['a' , 'b' , 'c' , 'x2']
x = {'a': x2, 'b': 200 ,'c': 300 , 'd':400}
x1 = {'a' , 'b' , 'c' , 'd'}


# print (type(x))
# print (type(x1))

# print (x['a'])
# print (x1)

# 確認type是啥 : 
# if type(x['b']) == int : 
#     print ('可以這樣寫喔' , x['b'] , '確定type :' , type(x['b']))


# Range 寫法會包含第一位不包含最後一位 ex 1-10 == 0,1,2,3,4,5,6,7,8,9
# print(list (range (x['b'])))

xConfirm = range (10 , -2 , -2)
# print (list(xConfirm))
# 卻認為 10 到 2 每次 -2 但不包含 2
# 回覆 [10, 8, 6, 4] 

xTest = range (1 , 10)
# print(list(xTest))
# 不設定減低邏輯寫法則不要加最後一個數字 
# 回覆 [1, 2, 3, 4, 5, 6, 7, 8, 9]



timeInit = 0
# 2. 使用 while 讓它重複執行，直到達到 100 (倒數計時100秒)
# while timeInit < 100:
#     timeInit += 1
#     print(f"目前計數: {timeInit}")
    
#     time.sleep(1)

# print("計時結束！", timeInit)


numbers = [10 ,20 , 30 , 40 , 50]
numbers2 = [10 , 30 , 60 , 80 , 100]
numberFinal = []

# for index in range(len(numbers)):
#     xx = numbers[index]
#     print (xx)
    # 回覆 10 20 30 40 50 



numbers_01 = [10, 20, 30, 40, 50]
numbers2_01 = [10, 30, 60, 80, 100]
numberFinal_01 = []

for i in range(len(numbers_01)):
    # 同時取兩個清單中相同位置的數字
    total = numbers_01[i] + numbers2_01[i]
    numberFinal.append(total)

# print(numberFinal) 
# 預期結果: [20, 50, 90, 120, 150]


# 學習 insert 資訊 
primes = [2 , 3 , 5 ,7 ,11 ,17 ,19]
primes.insert(5 , "13") # 插入 13 到 第5個位置
primes.insert(0 , "-1")
check = []

# print (f''' 確認一下 primes : {primes} , 確認資訊長度 : {len(primes)}''')

# for i in range(len(primes)) :
#     item = primes[i]
    
#     if type(item) != int :
#         check.append(item)
#         print (item , '總和array :' , check )

# 學習矩陣相乘
# list1 = [0.3 , 0.0 , 0.4]
# list2 = [0.2  , 0.5 , 0.6]
# total = 0

# for index in range (len(list1)):
#     total = list1[index] +list2[index]
#     print (total)

# 回覆 [0.5 ,0.5 ,1.0]

list1 = [ 3, 5 , 15]
list2 = [ 2 , 1 , 6]
total = 0
newList = []

for i in range(len(list1)) :
    other = list1[i] - list2[i]
    newList.append(other)
    total += other ** 2  # **為平方
print (" total : " ,total ,"newList :" ,  newList)