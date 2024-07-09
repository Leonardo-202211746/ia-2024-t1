def bfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando busca em largura."""
    from collections import deque

    nodes_explored = 0
    visitados = set()
    fila = deque([(start, [start])])

    while fila:
        v, caminho = fila.popleft()
        nodes_explored += 1
        if v == goal:
            caminho_custo = sum(graph[caminho[i]][caminho[i + 1]] for i in range(len(caminho) - 1))
            return nodes_explored, caminho_custo, caminho
        for neighbor in graph[v]:
            if neighbor not in visitados:
                visitados.add(neighbor)
                fila.append((neighbor, caminho + [neighbor]))
    
    return nodes_explored, float('inf'), []
