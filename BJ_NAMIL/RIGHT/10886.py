import sys

n = int(sys.stdin.readline())

cuteCount = 0

for i in range(n):
    temp = int(sys.stdin.readline())

    if temp == 1:
        cuteCount += 1
    else:
        cuteCount -= 1

if cuteCount > 0:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
