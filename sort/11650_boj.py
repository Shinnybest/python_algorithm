import sys

n = int(sys.stdin.readline())

arr = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x, y])

arr.sort() # x의 값이 같을 때는 y값을 기준으로 sort 해준다.

for i in range(n):
    print(arr[i][0], arr[i][1])