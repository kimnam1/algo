import sys

hour, minute = map(int, sys.stdin.readline().split())
cookTime = int(sys.stdin.readline())

timeInMinutes = hour*60 + minute
doneTime = timeInMinutes + cookTime
doneHour = (doneTime // 60) % 24
doneMinute = doneTime % 60
print(doneHour, doneMinute)