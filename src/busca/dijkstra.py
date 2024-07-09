def dijkstra(graph, start: int, goal: int) -> (int, float, [int]):
    nodes_explored = 0
    distancias = {no: float('inf') for no in graph}
    distancias[start] = 0
    prioridade = [(0, start)]
    caminho = {}

    while prioridade:
        distancia_atual, no_atual = heapq.heappop(prioridade)
        nodes_explored += 1

        if no_atual == goal:
            caminho_invertido = []
            while no_atual in caminho:
                caminho_invertido.append(no_atual)
                no_atual = caminho[no_atual]
            caminho_invertido.append(start)
            caminho_invertido = caminho_invertido[::-1]
            caminho_custo = sum(graph[caminho_invertido[i]][caminho_invertido[i + 1]] for i in range(len(caminho_invertido) - 1))
            return nodes_explored, caminho_custo, caminho_invertido

        for vizinho, peso in graph[no_atual].items():
            distancia = distancia_atual + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                caminho[vizinho] = no_atual
                heapq.heappush(prioridade, (distancia, vizinho))

    return nodes_explored, float('inf'), []
