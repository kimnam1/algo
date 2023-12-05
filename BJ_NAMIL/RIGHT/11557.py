import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())

    uni = ""
    drink = 0

    for j in range(n):
        uniTemp, drinkTemp = list(sys.stdin.readline().split())

        if int(drinkTemp) > drink:
            uni = uniTemp
            drink = int(drinkTemp)
    print(uni)
