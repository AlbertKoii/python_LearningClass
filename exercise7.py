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

for number in numbers :
    if int(number)%2 == 0 :
        arrayCollect.append(number)
        print ( number , f'''是偶數喔! ''' )

if len(arrayCollect)> 0  :
    print (f'''總數量為 : , {len(arrayCollect)},  這邊是總表 , {arrayCollect} ''')
        

    # else :
    #     print ('錯瞜')