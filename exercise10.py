print("歡迎光臨0131課程")

import random 
# help("modules") -->要進python 專屬 cmd 才可用 



# sample of first function 
# num = int(6)
# def squre (num):
#     result = num**2 
#     result2 = num + num 


#     return {f''' 
# 資料次方是 : {result}  , 
# 資料加上自己是 : {result2}
# '''}

# print (squre(num))


# number = 6
# total = 0 

# def userInput ():
    
#     global total
#     resp = input("你猜哪個數字?")
#     secret = random.randint(1,10)
    
    
#     if int(resp) == int(secret): 
#         return f''' 被你找到了! 答案是 {secret} , 你猜了 {total + 1}次才猜中 '''
#     elif int(resp) != int(secret):
#         total += 1
#         return f''' 答案是 {secret} 你錯了!'''
#     else :
#         return f''' 無法辨認{resp}'''
        
    

# print (userInput())






# dictionary 教學

tel = {'TAIWAN': 886 , 'CHINA' : 86 , 'SPAIN' :344 , 'GERMANY' : 491}
country = input('Country  :' )
data = country.upper()


if data in tel.keys() :
    print (tel[data])
else : 
    print ('不在搜索列內喔')
