import sys

q1Point = 0
q2Point = 0
q3Point = 0
q4Point = 0
axisPoint = 0

for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())

    if a == 0 or b == 0:
        axisPoint += 1
    elif a > 0 and b > 0:
        q1Point += 1
    elif a > 0 and b < 0:
        q4Point += 1
    elif a < 0 and b > 0:
        q2Point += 1
    elif a < 0 and b < 0:
        q3Point += 1

print(f"Q1: {q1Point}")
print(f"Q2: {q2Point}")
print(f"Q3: {q3Point}")
print(f"Q4: {q4Point}")
print(f"AXIS: {axisPoint}")
