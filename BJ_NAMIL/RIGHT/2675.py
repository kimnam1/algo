import sys

for i in range(int(sys.stdin.readline())):
    repeat, strCase = sys.stdin.readline().split()
    repeat = int(repeat)
    result = ""
    for i in range(len(strCase)):
        result += strCase[i] * repeat
    print(result)