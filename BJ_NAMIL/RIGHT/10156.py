import sys

oneSnack, snackAmount, currentMoney = map(int, sys.stdin.readline().split())

totalMoney = oneSnack * snackAmount
if totalMoney > currentMoney:
    print(totalMoney - currentMoney)
else:
    print(0)
