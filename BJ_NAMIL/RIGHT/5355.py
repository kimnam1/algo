import sys

for i in range(int(sys.stdin.readline())):
    equation = list(map(str, sys.stdin.readline().split()))
    number = float(equation[0])
    for j in range(1, len(equation)):
        if equation[j] == "@":
            number = number * 3
        elif equation[j] == "%":
            number = number + 5
        elif equation[j] == "#":
            number = number - 7
    print(f"{number:.2f}")