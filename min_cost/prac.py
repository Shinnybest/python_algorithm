import sys
from collections import defaultdict
from pprint import pprint

from min_cost.dijkstra import dijkstra_naive, dijkstra_pq

with open('testcase1.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline
    n, m = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

assert dijkstra_naive(graph, start) == [1000000000, 0, 2, 3, 1, 2, 4]

with open('testcase1.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline
    n, m = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

assert dijkstra_naive(graph, start) == [1000000000, 0, 2, 3, 1, 2, 4]
assert dijkstra_pq(graph, start) == [1000000000, 0, 2, 3, 1, 2, 4]


from min_cost.floyd_warshall import floyd_warshall

with open('testcase_fw.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline

    N = int(input())
    M = int(input())

    graph = defaultdict(list)
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    pprint(floyd_warshall(graph))