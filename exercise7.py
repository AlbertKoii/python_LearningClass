print(f''' 開始python 小學堂了喔 , exercise 7''')

# words = ['The' , 'cat' , 'sat' , 'on' , 'the' ,'mat']
# wordData = ['If The data be create in .....?']

# for word in words:
#     if word in wordData:
#         print (word)
#     else: 
#         print ('false print')
       


numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11]
arrayCollect = []
numberTotal = 0
numberUseSum = 0 

for number in numbers :
    if int(number)%2 == 0 :
        arrayCollect.append(number) # append 類似於 js 的 push
        numberTotal += number
        numberUseSum = sum(arrayCollect)
        print ( number , f'''是偶數喔! ''' )

if len(arrayCollect)> 0  :
    print (f'''總數量為 : {len(arrayCollect)},  
           這邊是總表 {arrayCollect}  , 
           加總數量為  {numberTotal}
           確認 sum 函數 {numberUseSum}     
''')
    

    # else :
    #     print ('錯瞜')