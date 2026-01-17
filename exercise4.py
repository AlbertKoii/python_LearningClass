Q01 = 'sparrow' > 'edgle' 
print(Q01)  # false

Q02 = ( 50< 50/2+5*3 or 20-45/5-10 >= 1)
print (Q02) # true

Q03 = "dog" > "cat" and 45%3 == 0
print(Q03)  # true 



#  =========================================== 下面是 bool 比較 ===========================================
# += 與 = 的差別
# += 會直接修改原始記憶體內容 , 而 = 則是建立一個新的記憶體空間

# sample of + : 
# list1 = [1, 2]
# list2 = list1
# list1 = list1 + [3]

# print(list1) # [1, 2, 3]
# print(list2) # [1, 2] -> list2 沒變，因為 list1 指向了新產生的物件


# sample of += : 
# list1 = [1, 2]
# list2 = list1
# list1 += [3]
# print(list1) # [1, 2, 3]
# print(list2) # [1, 2, 3] -> list2 也變了！因為 += 直接修改了原始記憶體內容
# print(bigger > smaller) # True



#  =========================================== 下面是 bool 比較 ===========================================
# python 可以用string 判斷 大小 , if dog > cat 會回傳 True 因為 d 的 ascii 比 c 大
# 先大小在小寫 ''' !@#$ ABCDD...abcd... 中文字 ''' 左邊小 右邊大 sample : 'cat' < 'dog'
# python 上面不可以空行

# bigger = 15
# smaller = 10
# diff = 5
# print("你好" > "cat")


# bool()　, 內部有任一東西都會回傳 True , 只有空的東西會回傳 False ex . bool(0) bool("") bool([]) bool({}) bool(None) 會回傳 False , 但 bool( ) 會回傳 True
# print(bool(0)) # False
# print(bool(1)) # True
# print(bool("")) # False
# print(bool(" ")) # True
# print(bool("Hello")) # True
# print(bool([])) # False
# print(bool([1, 2, 3])) # True
# print(bool(None)) # False
# print(bool(())) # False
# print(bool((1, 2, 3))) # True


# bool 比較 and 類似於 js 的 && , 只要有一個是 False 就會回傳 False , 兩個都是 True 才會回傳 True
# print((bigger > smaller) and (smaller < bigger)) # True
# print((bigger > smaller) and (smaller < diff)) # False
# print((bigger > smaller) and (diff < bigger)) # True


# bool 比較 or 類似於 js 的 || , 只要有一個是 True 就會回傳 True , 兩個都是 False 才會回傳 False
# print((bigger > smaller) or (smaller < bigger)) # True


# not 類似於 js 的 ! , 會把 True 變成 False , 把 False 變成 True
# print(not (bigger > smaller)) # False