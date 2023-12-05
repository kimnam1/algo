import sys

scoreList = []


for i in range(5):
    scoreList.append(int(sys.stdin.readline()))

sum = 0

for i in scoreList:
    if i < 40:
        sum += 40
    else:
        sum += i

print(sum // 5)
