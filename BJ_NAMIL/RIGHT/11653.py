import sys

number = int(sys.stdin.readline())

answerList = []


def Divide(number):
    divider = 2
    while divider <= number:
        if number % divider == 0:
            return number // divider, divider
        else:
            divider += 1
    return number, 10000001


while True:
    divided, residue = Divide(number)
    if residue == 10000001:
        break
    else:
        answerList.append(residue)
        number = divided
        continue

for i in answerList:
    print(i)
