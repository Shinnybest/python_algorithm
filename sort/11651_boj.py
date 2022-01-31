import sys

n = int(sys.stdin.readline())

arr = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x, y])

arr.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(arr[i][0], arr[i][1])

import sys

n = int(sys.stdin.readline())

arr = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([y, x])

arr.sort()

for i in range(n):
    print(arr[i][1], arr[i][0])