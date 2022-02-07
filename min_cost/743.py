import collections
import heapq

INF = int(1e9)

def network_time(times, n, k):
    # n: the number of nodes
    # k: the starting node
    # times: the list of start node, end node and the time it takes from the start to the end
    graph = [[] for _ in range(n+1)]
    for i in range(len(times)):
        graph[times[i][0]].append((times[i][1], times[i][2]))

    dist = [INF for _ in range(n+1)]
    dist[0] = dist[k] = 0

    q = []

    # 소요시간, 시작점
    heapq.heappush(q, (0, k))

    while q:
        prev_time, present_point = heapq.heappop(q)
        # acc = 0, cur = k

        for next_point, time in graph[present_point]:
            added_time = prev_time + time
            if added_time < dist[next_point]:
                dist[next_point] = added_time
                heapq.heappush(q, (dist[next_point], next_point)) # (걸린 시간, 현재 위치)

    print(dist)

    if INF in dist:
        return -1

    print(max(dist))
    return max(dist)

# example = [[1, 2, 1], [2, 1, 3]]
# example = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
example = [[1, 2, 1],[2, 3, 2],[1, 3, 2]]

# network_time(example, 2, 2)
# network_time(example, 4, 2)
network_time(example, 3, 1)


def networkDelayTime(times, N, K):
    graph = collections.defaultdict(list)

    for u, v, w in times:
        graph[u].append((v, w))

    Q = [(0, K)]
    dist = collections.defaultdict(list)

    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            print(dist)
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
    print(dist)

    if len(dist) == N:
        return max(dist.values())

    return -1

example_1 = [[2,1,1],[2,3,1],[3,4,1]]
networkDelayTime(example_1, 4, 2)