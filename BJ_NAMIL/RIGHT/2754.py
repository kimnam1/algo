import sys

score = sys.stdin.readline()

if score != "F":
    mainScore = score[0]
    subScore = score[1]

    scoreInNumber = 0

    if mainScore == "A":
        scoreInNumber = 4.0
    elif mainScore == "B":
        scoreInNumber = 3.0
    elif mainScore == "C":
        scoreInNumber = 2.0
    elif mainScore == "D":
        scoreInNumber = 1.0
else:
    scoreInNumber = 0.0

if scoreInNumber == 0.0:
    print(0.0)
else:
    if subScore == "+":
        print(scoreInNumber + 0.3)
    elif subScore == "0":
        print(scoreInNumber)
    elif subScore == "-":
        print(scoreInNumber - 0.3)
