def dijkstra_rute(graph, asal):
    """O(V^2 + E) tanpa heap"""
    INF = float('inf')
    dist = {v: INF for v in graph.adj}
    parent = {v: None for v in graph.adj}
    visited = set()
    dist[asal] = 0

    while len(visited) < len(graph.adj):
        u = min((v for v in graph.adj if v not in visited), key=lambda x: dist[x])
        visited.add(u)
        curr = graph.adj[u]
        while curr:
            if dist[u] + curr.jarak < dist[curr.dest]:
                dist[curr.dest] = dist[u] + curr.jarak
                parent[curr.dest] = u
            curr = curr.next
    return dist, parent
