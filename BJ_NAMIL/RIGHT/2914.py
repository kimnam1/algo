import sys

songs, mean = map(int, sys.stdin.readline().split())

print(songs * (mean - 1) + 1)