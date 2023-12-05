import sys

maxMoney = 0

for i in range(int(sys.stdin.readline())):
    a, b, c = map(int, sys.stdin.readline().split())

    caseNumber = 0
    sameNumber = 0

    if a == b:
        if a == c:
            caseNumber = 1
            sameNumber = a
        else:
            caseNumber = 2
            sameNumber = a
    elif a == c:
        caseNumber = 2
        sameNumber = a
    elif b == c:
        caseNumber = 2
        sameNumber = b
    else:
        caseNumber = 3

    if caseNumber == 1:
        maxMoney = max(maxMoney, 1000 * sameNumber + 10000)
    elif caseNumber == 2:
        maxMoney = max(maxMoney, 100 * sameNumber + 1000)
    elif caseNumber == 3:
        maxMoney = max(maxMoney, max(a, b, c) * 100)

print(maxMoney)
