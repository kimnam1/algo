import sys

t = int(sys.stdin.readline())

a = 0  # 300s
b = 0  # 60s
c = 0  # 10s
can = True

temp = t

while temp >= 300:
    temp -= 300
    a += 1
while temp >= 60:
    temp -= 60
    b += 1
while temp >= 10:
    temp -= 10
    c += 1
if temp > 0:
    can = False

if can:
    print(a, b, c)
else:
    print(-1)
