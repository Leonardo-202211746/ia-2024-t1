def branch_and_bound(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca em graph, um caminho entre start e goal usando Branch and Bound."""
    def copy_to_final(curr_path):
        nonlocal caminho_final
        caminho_final = curr_path[:] + [curr_path[0]]

    def first_min(i):
        min_val = sys.maxsize
        for k in graph[i]:
            if graph[i][k] < min_val:
                min_val = graph[i][k]
        return min_val

    def second_min(i):
        first, second = sys.maxsize, sys.maxsize
        for j in graph[i]:
            if graph[i][j] <= first:
                second = first
                first = graph[i][j]
            elif graph[i][j] <= second and graph[i][j] != first:
                second = graph[i][j]
        return second

    def tsp_rec(curr_bound, curr_weight, level, curr_path, visited):
        nonlocal final_res, nodes_explored
        if level == len(graph):
            if graph[curr_path[level - 1]].get(curr_path[0], 0) != 0:
                curr_res = curr_weight + graph[curr_path[level - 1]][curr_path[0]]
                if curr_res < final_res:
                    copy_to_final(curr_path)
                    final_res = curr_res
            return

        for i in graph[curr_path[level - 1]]:
            if not visited[i]:
                temp = curr_bound
                curr_weight += graph[curr_path[level - 1]][i]

                if level == 1:
                    curr_bound -= (first_min(curr_path[level - 1]) + first_min(i)) / 2
                else:
                    curr_bound -= (second_min(curr_path[level - 1]) + first_min(i)) / 2

                if curr_bound + curr_weight < final_res:
                    curr_path[level] = i
                    visited[i] = True
                    nodes_explored += 1

                    tsp_rec(curr_bound, curr_weight, level + 1, curr_path, visited)

                curr_weight -= graph[curr_path[level - 1]][i]
                curr_bound = temp

                visited = [False] * len(visited)
                for j in range(level):
                    if curr_path[j] != -1:
                        visited[curr_path[j]] = True

    nodes_explored = 0
    caminho_final = []
    final_res = sys.maxsize
    curr_bound = 0
    curr_path = [-1] * (len(graph) + 1)
    visited = [False] * len(graph)
    visited[start] = True
    curr_path[0] = start

    for i in range(len(graph)):
        curr_bound += (first_min(i) + second_min(i))

    curr_bound = int(curr_bound / 2)

    tsp_rec(curr_bound, 0, 1, curr_path, visited)

    if caminho_final:
        caminho_final.pop()  # Remover o nó inicial adicionado no final
        caminho_custo = sum(graph[caminho_final[i]][caminho_final[i + 1]] for i in range(len(caminho_final) - 1))
        return nodes_explored, caminho_custo, caminho_final
    else:
        return nodes_explored, float('inf'), []
