"""
Program 10: Represent a Graph Using an Adjacency List
Print all vertices and edges given the adjacency list.
"""


def print_graph(adj_list):
    """Print vertices and edges from an adjacency list."""
    print("\n" + "=" * 45)
    print("  GRAPH (Adjacency List Representation)")
    print("=" * 45)

    # Vertices
    vertices = list(adj_list.keys())
    print(f"\nVertices ({len(vertices)}): {vertices}")

    # Adjacency list display
    print("\nAdjacency List:")
    for vertex, neighbors in adj_list.items():
        print(f"  {vertex} -> {neighbors}")

    # Edges (undirected: store once as (u, v) with u <= v if comparable)
    edges = []
    seen = set()
    for u, neighbors in adj_list.items():
        for v in neighbors:
            edge = tuple(sorted((u, v), key=str))
            if edge not in seen:
                seen.add(edge)
                edges.append((u, v))

    print(f"\nEdges ({len(edges)}):")
    for u, v in edges:
        print(f"  ({u}, {v})")

    print(f"\nTotal Vertices: {len(vertices)}")
    print(f"Total Edges:    {len(edges)}")


def build_from_input():
    """Optionally build an adjacency list from user input."""
    print("\nEnter the graph (undirected).")
    try:
        n = int(input("Number of vertices: "))
    except ValueError:
        print("Invalid number.")
        return None

    vertices = []
    for i in range(n):
        v = input(f"  Name of vertex {i + 1}: ").strip()
        vertices.append(v)

    adj = {v: [] for v in vertices}

    try:
        e = int(input("Number of edges: "))
    except ValueError:
        print("Invalid number.")
        return None

    print("Enter each edge as: vertex1 vertex2")
    for i in range(e):
        parts = input(f"  Edge {i + 1}: ").strip().split()
        if len(parts) != 2:
            print("  Skipped (need two vertices).")
            continue
        u, v = parts
        if u not in adj or v not in adj:
            print(f"  Skipped (unknown vertex in {u}, {v}).")
            continue
        if v not in adj[u]:
            adj[u].append(v)
        if u not in adj[v]:
            adj[v].append(u)

    return adj


def main():
    # Sample undirected graph:
    #     A --- B
    #     |   / |
    #     |  /  |
    #     C --- D
    sample_graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D"],
        "D": ["B", "C"],
    }

    print("Using a sample graph:")
    print_graph(sample_graph)

    choice = input("\nDo you want to enter your own graph? (y/n): ").strip().lower()
    if choice == "y":
        user_graph = build_from_input()
        if user_graph:
            print_graph(user_graph)

    print("\nProgram completed successfully.")


if __name__ == "__main__":
    main()
