from collections import deque


def neighbours(graph, vertex, graph_type="list"):
    if graph_type == "list":
        return graph[vertex]
    if graph_type == "matrix":
        return [
            neighbour
            for neighbour, has_edge in enumerate(graph[vertex])
            if has_edge
        ]
    raise ValueError("graph_type must be 'list' or 'matrix'")


def bfs(graph, start, graph_type="list"):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    order = []

    while queue:
        vertex = queue.popleft()

        for neighbour in neighbours(graph, vertex, graph_type):
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)

    return order


def is_connected(graph, source, destination, graph_type="list"):
    visited = [False] * len(graph)
    queue = deque([source])
    visited[source] = True

    while queue:
        vertex = queue.popleft()
        if vertex == destination:
            return True

        for neighbour in neighbours(graph, vertex, graph_type):
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)

    return False


def count_connected_vertices(graph, source, graph_type="list"):
    return len(bfs(graph, source, graph_type)) - 1


if __name__ == "__main__":
    adjacency_list = [
        [1, 2],
        [2, 0],
        [0, 1, 3, 4],
        [2],
        [2],
    ]

    adjacency_matrix = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
    ]

    for graph, graph_type in (
        (adjacency_list, "list"),
        (adjacency_matrix, "matrix"),
    ):
        print(f"BFS ({graph_type}):", bfs(graph, 0, graph_type))
        print(
            f"Path from 0 to 4 ({graph_type}):",
            is_connected(graph, 0, 4, graph_type),
        )
        print(
            f"Vertices connected to 0 ({graph_type}):",
            count_connected_vertices(graph, 0, graph_type),
        )
