import sys

hour, minute = map(int, sys.stdin.readline().split())

if minute >= 45:
    print(hour, minute - 45)
else:
    if hour == 0:
        print(23, minute + 15)
    else:
        print(hour - 1, minute + 15)
