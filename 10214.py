import sys

t = int(sys.stdin.readline())

for i in range(t):
    y, k = map(int, sys.stdin.readline().split())

    if y > k:
        print("Yonsei")
    elif y < k:
        print("Korea")
    elif y == k:
        print("Draw")
