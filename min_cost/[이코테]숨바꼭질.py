import heapq

INF = int(1e9)

def seek_and_hide(graph):
    N = len(graph)
    start = 1
    dist = [INF for _ in range(N + 1)]

    dist[0] = dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        acc, cur = heapq.heappop(q)
        if dist[cur] < acc:
            continue

        for adj in graph[cur]:
            cost = acc + 1
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

        max_dist = max(dist[1:])
        cnt = sum([1 for idx in range(1, N + 1) if dist[idx] == max_dist])

        return dist.index(max_dist), max_dist, cnt