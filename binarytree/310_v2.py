import collections

def findMinHeightTrees(n, edges):
    if n == 1:
        return [0]

    graph = collections.defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    q = collections.deque()
    for x, y in graph.items():
        if len(y) == 1:
            q.append(x)

    while n > 2:
        n = n - len(q)
        for _ in range(len(q)):
            curr = q.popleft() # q에서 popleft 한 요소는 제거된다.
            for ele in graph[curr]:
                graph[ele].remove(curr)
                if len(graph[ele]) == 1:
                    q.append(ele)

    return print(list(q))


arr = [[0, 1], [1, 2], [2, 3], [3, 4], [1, 5]]
findMinHeightTrees(6, arr)