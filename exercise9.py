print(f''' 開始python 小學堂了喔 , exercise 9''')

# primes = [2,3,5,7,11,13,17,19,23,29,31]
# primes [4:9:3]


# data = primes [len(primes)-1] #回覆最後一個數字 31 
# data = primes[-1] , #回覆 最後一個數字 31  --> 從最後面數來第一個

# data = primes[0: -4] , #回覆 [2, 3, 5, 7, 11, 13, 17]
# data = primes[3:12:3] , #回覆 [7, 17, 29]
# print (data)

array01 = ['food' , 'other']
array02 = ['clothing' , 'electronics' , 'household']
all = array01 + array02

distincts = {
        "1" : 'Nankan' , 
        "2" : "Zongli",
        "3" : "Taipei-Nei-Hu",
        "4" : "Taipei-Zhong He"
        }
electronics = ['electronics', 5 , 2, 17 , 29 , 1 , 1 , 4 ]
shipments = ['food' , 11 , 52 , 190 , 14 , 73 , 8 , 391 , 61 , 215 , 97 , 10 , 151 , 15 ,3 ]



# Task 1. 貨品為 電子 衣服 家庭用品 則加總
# Task 2. 貨品為 食品 或 其他 則 列出 產品: 數量 ex. 產品1:20 ,  產品2: 30 etc
eachData = input("請輸入你要找啥資訊地方的資訊  :")

dataList = []
x = 0
dataCount = 0
write = ""
sendTO = ""
count = 0

for item in all:
    if item not in all: 
        print ('資料不在選項內')
    elif item == eachData :
        print ('已確定資訊 正在幫您找相對應的data :')
        if item in array01 :
            if item == 'food':
                shop = shipments[-1]
                
                # 送出到 ... 
                for distinct in distincts:
                    if distinct == str(shop) : 
                        sendTO = distincts[distinct]
                        print ('sendTO  :' , sendTO)
                        

                for data in shipments: 
                    # print ('輸入food 後的data' , data )
                    if type(data) != str and data != electronics[-1] : 
                        dataCount += int(data)
            print ('food : ' , dataCount)
                    
        elif item in array02:
            if item == 'electronics':
                for data in electronics:
                    bars = electronics[1:-1]
                    # print ("bar 是啥東西  :",bars)
                    shop = electronics[-1]

                    # 送出到 ... 
                    for distinct in distincts:
                        if distinct == str(shop) : 
                            sendTO = distincts[distinct]
                            
                    
                    for bar in bars :
                        # print('bar now :' , bar)
                        count += 1   
                        dataSend = f''' 產品{count} :  {bar}'''
                                     
                        dataList.append(dataSend)
                        
        print ('dataList  :' , dataList)
        print ('sendTO  :' , sendTO)
    else :
        write = "你找的東西不再類別內"

    if write != "" :
        print (write)







