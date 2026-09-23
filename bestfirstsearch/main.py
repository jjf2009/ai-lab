from heapq import heappush, heappop


def neighbours(graph, vertex):
    return graph[vertex]


def best_first_search(graph, start, goal, heuristics):
    visited = set()
    heap = [(heuristics[start], start)]
    order = []

    while heap:
        _, vertex = heappop(heap)

        if vertex in visited:
            continue
        visited.add(vertex)
        order.append(vertex)

        if vertex == goal:
            break

        for neighbour in neighbours(graph, vertex):
            if neighbour not in visited:
                heappush(heap, (heuristics[neighbour], neighbour))

    return order


if __name__ == "__main__":
    adjacency_list = {
        "S": ["A", "B", "C"],
        "A": ["D"],
        "B": ["D", "H"],
        "C": ["G"],
        "D": ["F"],
        "F": [],
        "G": ["H"],
        "H": ["E"],
        "E": [],
    }
    heuristics = {
        "S": 0, "A": 9, "B": 7, "C": 8,
        "D": 8, "E": 0, "F": 6, "G": 6, "H": 3,
    }

    print(
        "Best-First Search S -> E:",
        best_first_search(adjacency_list, "S", "E", heuristics),
    )
