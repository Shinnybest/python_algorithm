# import sys
import heapq

INF = int(1e9)
#
# with open('testcase_mars.txt') as f:
#     sys.stdin = f
#     input = sys.stdin.readline
#     total_case = int(input())
#     n = int(input())
#     graph = [[] for _ in range(n)]
#
#     for _ in range(m):
#         a, b, c = map(int, input().split())
#         graph[a].append((b, c))

def explore_mars(graph):
    # x축 왔다 갔다
    dr = [1, 0, -1, 0]
    # y축 왔다 갔다
    dc = [0, 1, 0, -1]

    N = len(graph)
    # 1억 숫자를 다 넣어, list 형식으로 len(graph) 만큼
    dist = [[INF] * N for _ in range(N)]
    print(dist)
    # 시작점은 정해주기
    dist[0][0] = graph[0][0]

    q = []
    # 첫번째 값과 row, col 값 넣어주기
    heapq.heappush(q, (graph[0][0], 0, 0))

    while q:
        # 한개씩 빼주면서
        acc, r, c = heapq.heappop(q)
        print(dist)
        # graph[0][0], row, col

        # 무슨 경우에 이렇게 되는거지?
        if dist[r][c] < acc:
            continue

        # 상하좌우로 움직이는 것
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 정사각형 범위에서 벗어나지 않으면
            if 0 <= nr < N and 0 <= nc < N:
                cost = dist[r][c] + graph[nr][nc] # 원래 있던 자리 + 이동하는 곳의 비용
                if cost < dist[nr][nc]:
                    dist[nr][nc] = cost
                    heapq.heappush(q, (cost, nr, nc))

    return print(dist[N-1][N-1])

route = [
    [3, 7, 2, 0, 1],
    [2, 8, 0, 9, 1],
    [1, 2, 1, 8, 1],
    [9, 8, 9, 2, 0],
    [3, 6, 5, 1, 5]
]

explore_mars(route)