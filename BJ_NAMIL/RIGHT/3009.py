import sys

x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())
x3, y3 = map(int, sys.stdin.readline().split())
tempX = None
tempY = None

if x1 == x2:
    tempX = x3
elif x1 == x3:
    tempX = x2
elif x2 == x3:
    tempX = x1

if y1 == y2:
    tempY = y3
elif y2 == y3:
    tempY = y1
elif y1 == y3:
    tempY = y2

print(tempX, tempY)
