import sys

A = int(sys.stdin.readline())
operator = str(sys.stdin.readline().strip())
B = int(sys.stdin.readline())

if operator == "+":
    print(A + B)
elif operator == "*":
    AinTens = len(str(A)) - 1
    BinTens = len(str(B)) - 1
    answerInTens = AinTens + BinTens
    print(10 ** answerInTens)