import sys

plates = str(sys.stdin.readline().strip())

height = 0
curDirection = ""

for i in plates:
    if curDirection != i:
        height += 10
        curDirection = i
    else:
        height += 5
        curDirection = i

print(height)
