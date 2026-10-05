INF = float("inf")

def tsp(graph):
    n = len(graph)

    memo = {}

    parent = {}

    def dp(mask, pos):

        if (mask, pos) in memo:
            return memo[(mask, pos)]

        if mask == (1 << n) - 1:
            return graph[pos][0]

        best = INF
        next_city = -1

        for city in range(n):
            if mask & (1 << city) == 0:
                cost = graph[pos][city] + dp(mask | (1 << city), city)
                if cost < best:
                    best = cost
                    next_city = city

        memo[(mask, pos)] = best
        parent[(mask, pos)] = next_city

        return best


    minimum_cost = dp(1, 0)

    path = [0]
    mask = 1
    pos = 0

    while True:

        if (mask, pos) not in parent:
            break

        city = parent[(mask, pos)]

        path.append(city)

        mask |= (1 << city)

        pos = city

    path.append(0)

    return minimum_cost, path


graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cost, path = tsp(graph)

print("Minimum =", cost)

for i in range(len(path)):
    if i != len(path) - 1:
        print(path[i], end=" -> ")
    else:
        print(path[i])