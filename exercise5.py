print("====  Exercise 4 : Boolean Comparison  ====")
#  =========================================== 下面是 if 學習 ===========================================
# if 條件判斷式 : 後面要加冒號
# if 裡面的程式碼要縮排 (通常是 4 個空格或 1 個 tab 鍵)
# if 條件判斷式 為 True 時 , 就會執行 if 裡面的程式碼
# if 條件判斷式 為 False 時 , 就不會執行 if 裡面的程式碼




array = ["A" , "B" , "C" , "D" , "F"]


if all (isinstance (i , str) for i in array):
    grade = int(input("請輸入你的成績  :"))
    if grade >= 90 and grade <= 100:
        print(array[0]) # A
    elif grade >= 80 and grade < 90:
        print(array[1]) # B
    elif grade >= 70 and grade < 80:
        print(array[2]) # C
    elif grade >= 60 and grade < 70:
        print(array[3]) # D
    elif grade >= 0 and grade < 60:
        print(array[4]) # F
    else:
        print("你別亂搞") # 你別亂搞


    