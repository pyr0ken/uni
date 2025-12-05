def main():
    n, m = map(int, input().split())
    if n <= 1:
        if n == 1:
            print(1)
        return

    inf = float('inf')
    dist = [[inf] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dist[i][i] = 0

    for _ in range(m):
        u, v, c = map(int, input().split())
        dist[u][v] = min(dist[u][v], c)
        dist[v][u] = min(dist[v][u], c)

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] != inf and dist[k][j] != inf:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    min_eccentricity = inf
    center_node = -1

    for i in range(1, n + 1):
        current_max_dist = 0
        for j in range(1, n + 1):
            if dist[i][j] == inf:
                current_max_dist = inf
                break
            current_max_dist = max(current_max_dist, dist[i][j])
        
        if current_max_dist < min_eccentricity:
            min_eccentricity = current_max_dist
            center_node = i

    print(center_node)

main()
