import sys

word = str(sys.stdin.readline())


def ReverseWord(word):
    res = []
    for i in range(1, len(word) + 1):
        res.append(word[-i])
    return ("").join(res)


if word == ReverseWord(word):
    print("1")
else:
    print("0")
