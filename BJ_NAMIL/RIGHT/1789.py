import sys

number = int(sys.stdin.readline())
sub = 1
residue = number
counter = 0

while residue > sub:
    residue -= sub
    sub += 1
    counter += 1

if residue == sub:
    counter += 1
else:
    pass

print(counter)
