# 2026.01.10 上午
one = "My name is Albert"
two = "I havd 1 younger brother"
three = "1 prefer coca cola"
four = "My favorite song is \" I'm Yours \""



if all (isinstance (i , str) for i in [one , two , three , four]):
    print ("Confirm")


print (
    one + "\n" +
    two + "\n" +
    three + "\n" +
    four
    )

# 多筆可直接空格 不用加上 /n (會自動加入)
print ('''
    My name is Albert
    I havd 1 younger brother
    1 prefer coca cola
    My favorite song is \" I'm Yours \"
    ''')
