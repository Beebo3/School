years = 0
money = float(input("Deposit Money: "))

while years <= 10:
    money = money*0.06+money
    print(money)
    years+=1
    