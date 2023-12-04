import sys

for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    sum = a+b
    print(f"Case #{i+1}:", str(sum))