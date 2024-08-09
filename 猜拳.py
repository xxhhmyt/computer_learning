import random
num=1
yin_num=0
shu_num=0
while num <= 3:
    if shu_num == 2 or yin_num == 2:
        break
    user=int(input('请出拳 0(石头)，1（剪刀），2（布）'))
    if user > 2:
        print('不能出拳')
    else:
        data=('石头','剪刀','布')
        com=random.randint(0,2)
        print("您输入的是{},电脑输入的是{}".format(data[user],data[com]))
        if user == com:
            print('平局')
            continue
        elif (user==0 and com==1) or (user == 1 and com == 2) or (user == 2 and com == 0):
            print('你赢了')
            yin_num += 1
        else:
            print('你输了')
            shu_num += 1
    num += 1



