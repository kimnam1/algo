import sys

for i in range(int(sys.stdin.readline())):
    noAdMoney, yesAdMoney, adExpense = map(int, sys.stdin.readline().split())

    if noAdMoney == yesAdMoney - adExpense:
        print("does not matter")
    elif noAdMoney > yesAdMoney - adExpense:
        print("do not advertise")
    elif noAdMoney < yesAdMoney - adExpense:
        print("advertise")
