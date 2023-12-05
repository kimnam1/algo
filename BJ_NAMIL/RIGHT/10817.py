import sys

a, b, c = map(int, sys.stdin.readline().split())

if a >= b:
    if a >= c:
        if b >= c:
            print(b)
        else:
            print(c)
    else:
        print(a)
elif b >= a:
    if b >= c:
        if a >= c:
            print(a)
        else:
            print(c)
    else:
        print(b)
