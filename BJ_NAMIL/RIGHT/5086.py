import sys

while True:
    factor = False
    multiple = False
    neither = False

    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    else:
        if a % b == 0:
            multiple = True
        elif a // b == 0:
            factor = True
        else:
            neither = True
    if factor:
        print("factor")
    elif multiple:
        print("multiple")
    else:
        print("neither")
