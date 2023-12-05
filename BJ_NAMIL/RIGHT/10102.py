import sys

judgeAmount = int(sys.stdin.readline())
judgeResult = str(sys.stdin.readline())

aCount = 0
bCount = 0

for res in judgeResult:
    if res == "A":
        aCount += 1
    elif res == "B":
        bCount += 1

if aCount > bCount:
    print("A")
elif aCount == bCount:
    print("Tie")
elif aCount < bCount:
    print("B")
