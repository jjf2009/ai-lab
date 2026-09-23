"""
Program 11: Represent a Graph Using an Adjacency Matrix
"""


def print_matrix(vertices, matrix):
    """Pretty-print the adjacency matrix with labels."""
    n = len(vertices)
    col_width = max(3, max(len(str(v)) for v in vertices) + 1)

    # Header row
    header = " " * col_width + "".join(f"{v:>{col_width}}" for v in vertices)
    print(header)
    print("-" * len(header))

    for i in range(n):
        row = f"{vertices[i]:<{col_width}}"
        row += "".join(f"{matrix[i][j]:>{col_width}}" for j in range(n))
        print(row)


def print_graph_info(vertices, matrix):
    """Print vertices and edges derived from the adjacency matrix."""
    n = len(vertices)
    print("\n" + "=" * 50)
    print("  GRAPH (Adjacency Matrix Representation)")
    print("=" * 50)

    print(f"\nVertices ({n}): {vertices}")

    print("\nAdjacency Matrix:")
    print_matrix(vertices, matrix)

    # Collect edges (undirected: only upper triangle to avoid duplicates)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                edges.append((vertices[i], vertices[j]))

    # Also check for directed edges if matrix is not symmetric
    directed_extra = []
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] == 1 and matrix[j][i] == 0:
                directed_extra.append((vertices[i], vertices[j]))

    print(f"\nEdges ({len(edges)} undirected pairs):")
    for u, v in edges:
        print(f"  ({u}, {v})")

    if directed_extra:
        print("\nDirected-only edges (matrix not symmetric):")
        for u, v in directed_extra:
            print(f"  {u} -> {v}")

    print(f"\nTotal Vertices: {n}")
    print(f"Total Edges:    {len(edges)}")


def adjacency_list_to_matrix(adj_list):
    """Convert adjacency list to adjacency matrix."""
    vertices = list(adj_list.keys())
    index = {v: i for i, v in enumerate(vertices)}
    n = len(vertices)
    matrix = [[0] * n for _ in range(n)]

    for u, neighbors in adj_list.items():
        for v in neighbors:
            matrix[index[u]][index[v]] = 1

    return vertices, matrix


def main():
    # Sample undirected graph (same as program 10):
    #     A --- B
    #     |   / |
    #     |  /  |
    #     C --- D
    sample_adj_list = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D"],
        "D": ["B", "C"],
    }

    vertices, matrix = adjacency_list_to_matrix(sample_adj_list)
    print("Using a sample graph:")
    print_graph_info(vertices, matrix)

    # Manual matrix example
    print("\n" + "=" * 50)
    print("  MANUAL MATRIX EXAMPLE (3 vertices)")
    print("=" * 50)
    verts = ["X", "Y", "Z"]
    mat = [
        [0, 1, 1],  # X connected to Y, Z
        [1, 0, 1],  # Y connected to X, Z
        [1, 1, 0],  # Z connected to X, Y
    ]
    print_graph_info(verts, mat)

    print("\nProgram completed successfully.")


if __name__ == "__main__":
    main()
