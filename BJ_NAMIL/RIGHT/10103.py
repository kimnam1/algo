import sys

n = int(sys.stdin.readline())
a = 100
b = 100


for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x > y:
        b -= x
    elif x < y:
        a -= y
    else:
        pass

print(a)
print(b)
