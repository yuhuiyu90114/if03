driving = input ( '你開過車嗎? ( y / n )' )
if driving != 'y' and driving != 'n':
    print ( '請輸入 y / n')
    raise systemexit

age = input ( '你的年齡?' )
age = float ( age )
if driving == 'y':
   
    if age >= 18:
        print('你通過驗證')
    else:
        print('年紀太小孩不能開車!')
elif driving == 'n':
    
    if age >= 18:
        print('你可以嘗試去開車')
    else:
        print('再過幾年就可以開車!')