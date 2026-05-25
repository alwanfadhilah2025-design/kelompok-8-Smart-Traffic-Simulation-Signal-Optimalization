from data_structures.graph import GraphJalan

def cek_isolasi(graph):

    start = next(iter(graph.adj))

    visited = graph.dfs(start)

    return [
        v
        for v in graph.adj
        if v not in visited
    ]
