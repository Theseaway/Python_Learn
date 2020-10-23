from random import randint
import matplotlib.pyplot as plt

def func1():
    money=2000
    moneyl=[2000]
    index=[0]
    num=0
    while(money>0):
        print("目前资金为：",money)
        debt=200
        re=randint(1,6)+randint(1,6)
        temp=0
        if re==7 or re==11:
            print("运气不错")
            money+=debt
            print("目前资金为：",money)
            moneyl.append(money)
            num+=1
            index.append(num)
        elif re==2 or re==3 or re==12:
            print("有点可惜，再战一次")
            money-=debt
            print("目前资金为：",money)
            moneyl.append(money)
            num+=1
            index.append(num)
        else:
            while money>0:
                temp=randint(1,6)+randint(1,6)
                if temp==re:
                    print("运气不错")
                    money+=debt
                    print("目前资金为：",money)
                    moneyl.append(money)
                    num+=1
                    index.append(num)
                elif temp==7:
                    print("有点可惜，再战一次")
                    money-=debt
                    print("目前资金为：",money)
                    moneyl.append(money)
                    num+=1
                    index.append(num)
    return [index,moneyl]

test=func1()
