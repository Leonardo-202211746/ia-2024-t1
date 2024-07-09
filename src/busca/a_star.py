def a_star(graph, start: int, goal: int) -> (int, float, [int]):
    def heuristica(no):
        return 0

    nodes_explored = 0
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {no: float('inf') for no in graph}
    g_score[start] = 0
    f_score = {no: float('inf') for no in graph}
    f_score[start] = heuristica(start)

    while open_list:
        _, current = heapq.heappop(open_list)
        nodes_explored += 1

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path = path[::-1]
            path_cost = sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
            return nodes_explored, path_cost, path

        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph[current][neighbor]
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristica(neighbor)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return nodes_explored, float('inf'), []
