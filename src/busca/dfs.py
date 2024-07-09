def dfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando busca em profundidade."""
    def dfs_recursive(v, visitados):
        nonlocal nodes_explored
        visitados.add(v)
        nodes_explored += 1
        if v == goal:
            return True
        for neighbor in graph[v]:
            if neighbor not in visitados:
                caminho.append(neighbor)
                if dfs_recursive(neighbor, visitados):
                    return True
                caminho.pop()
        return False

    nodes_explored = 0
    visitados = set()
    caminho = [start]
    if dfs_recursive(start, visitados):
        caminho_custo = sum(graph[caminho[i]][caminho[i + 1]] for i in range(len(caminho) - 1))
        return nodes_explored, caminho_custo, caminho
    else:
        return nodes_explored, float('inf'), []
