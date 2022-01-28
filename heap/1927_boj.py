import heapq
import sys

input = sys.stdin.readline

cnt = int(input())
heap = []


for _ in range(cnt):
    num = int(input())
    if num == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)