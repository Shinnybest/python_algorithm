INF = int(1e9)

def dijkstra_naive(graph, start):
    def get_smallest_node():
        min_value = INF
        idx = 0
        for i in range(1, N): # vertex 의 개수만큼 for 문 반복
            if dist[i] < min_value and not visited[i]:
                # 0 < min_value
                min_value = dist[i]
                # min_value = 0
                idx = i
        return idx # idx = 1

    N = len(graph)
    visited = [False] * N # visited의 첫번째 값은 false
    dist = [INF] * N # dist의 첫번째 값은 INF?

    visited[start] = True
    dist[start] = 0

    for adj, d in graph[start]:
        dist[adj] = d

    # N개의 노드 중 첫 노드는 이미 방문했으므로,
    # N-1번 수행하면 된다.
    for _ in range(N - 1):
        # 가장 가깝고 방문 안한 녀석을 고르고,
        cur = get_smallest_node() # cur = 0 -> 4
        visited[cur] = True # visited[cur] = True, visited[4] = True
        # 최단거리를 비교, 수정한다.
        # 기존의 거리 + 다시 새로운 시작점에서 가는 거리
        for adj, d in graph[cur]:
            cost = dist[cur] + d # 4+3
            # 기존 것보다 작아야 replace 를 해준다.
            if cost < dist[adj]:
                dist[adj] = cost

    return dist

import heapq


def dijkstra_pq(graph, start):
    N = len(graph)
    dist = [INF] * N

    q = []
    # 튜플일 경우 0번째 요소 기준으로 최소 힙 구조.
    # 첫 번째 방문 누적 비용은 0이다.
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        # 누적 비용이 가장 작은 녀석을 꺼낸다.
        acc, cur = heapq.heappop(q)

        # 이미 답이 될 가망이 없다.
        if dist[cur] < acc:
            continue

        # 인접 노드를 차례대로 살펴보며 거리를 업데이트한다.
        for adj, d in graph[cur]:
            cost = acc + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist