INF = int(1e9)

n = int(input())
m = int(input())

bus_cost = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    bus_cost[start][end] = min(cost, bus_cost[start][end])


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                bus_cost[a][b] = 0
            bus_cost[a][b] = min(bus_cost[a][b], bus_cost[a][k] + bus_cost[k][b])

for i in bus_cost[1:]:
    for j in i[1:]:
        print(j, end=" ")
    print("")