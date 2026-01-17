print("====  Exercise 4 : Boolean Comparison  ====")
#  =========================================== 下面是 if 學習 ===========================================
# if 條件判斷式 : 後面要加冒號
# if 裡面的程式碼要縮排 (通常是 4 個空格或 1 個 tab 鍵)
# if 條件判斷式 為 True 時 , 就會執行 if 裡面的程式碼
# if 條件判斷式 為 False 時 , 就不會執行 if 裡面的程式碼


# def get_grade_letter(score):
#     """根據分數回傳對應的等第"""
#     grades = ["A", "B", "C", "D", "F"]
#     if 90 <= score <= 100:
#         return grades[0]
#     elif 80 <= score < 90:
#         return grades[1]
#     elif 70 <= score < 80:
#         return grades[2]
#     elif 60 <= score < 70:
#         return grades[3]
#     elif 0 <= score < 60:
#         return grades[4]
#     else:
#         return "超出範圍"

# # --- 主程式迴圈 ---
# while True:
#     user_input = input("請輸入你的成績 (輸入 q 離開): ")
    
#     # 讓使用者可以隨時退出
#     if user_input.lower() == 'q':
#         break
        
#     try:
#         grade_num = int(user_input)
        
#         # 取得等第
#         result = get_grade_letter(grade_num)
        
#         if result == "超出範圍":
#             print("❌ 分數必須在 0 到 100 之間！")
#         else:
#             print(f"✅ 你的成績是 {grade_num} 分，等第為: {result}")
#             break # 成功得到結果，跳出迴圈
            
#     except ValueError:
#         # 當 user_input 無法轉成 int 時執行
#         print(f"❌ 你輸入的是 '{user_input}'，請輸入整數數字好嗎？")

    

# ==== page 47exercise =====

payment = input("請輸入金額: ") 

while True:
    finalOutPut = ""
    try:
        amount = int(payment)
        if payment.isdigit() and amount > 0:
            print(f"您輸入的金額是: {amount} 元")
            if amount >= 1000:
                finalOutPut += '請刷卡 不支援付現!'
            if amount <= 1000: 
                finalOutPut += '可以用1000元來付款!\n'
            if amount <= 500:
                finalOutPut += '可以用500元來付款!\n'
            if amount <= 100:
                finalOutPut += '可以用100元來付款!\n'
            if amount <= 50:
                finalOutPut += '可以用50元來付款!\n'
            if amount <= 10:
                finalOutPut += '可以用10元來付款!\n'

            print(finalOutPut)
            break
        elif amount < 0:
            finalOutPut += '賣給小 , 給我輸入正確數字喔!\n'
            print(finalOutPut)
            payment = input("請重新輸入金額: ")
    except ValueError:
        print("請輸入有效的數字金額！")
        payment = input("請重新輸入金額: ")

