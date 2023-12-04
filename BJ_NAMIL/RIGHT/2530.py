import sys

hour, minute, second = map(int, sys.stdin.readline().split())
cookTime = int(sys.stdin.readline())

timeInSeconds = hour*3600 + minute*60 + second
doneTime = timeInSeconds + cookTime
doneHour = (doneTime // 3600) % 24
doneMinute = (doneTime // 60) % 60
doneSecond = doneTime % 60
print(doneHour, doneMinute, doneSecond)