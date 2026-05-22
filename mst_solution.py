def run_kruskal(graph_name, vertices, edges):
    print(f"\n=========================================")
    print(f"RUNNING MST ANALYSIS: {graph_name}")
    print("=========================================")
    
    edges.sort()
    parent = {v: v for v in vertices}

    def find(i):
        if parent[i] == i:
            return i
        return find(parent[i])

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        parent[root_i] = root_j

    mst_edges = []
    total_tree_cost = 0

    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, weight))
            total_tree_cost += weight

    print("Optimal links included in the Spanning Tree:")
    for u, v, w in mst_edges:
        print(f" -> Connection {u} to {v} [Weight: {w}]")
    print(f"FINAL MINIMUM SPANNING TREE COST = {total_tree_cost}\n")

def main():
    # GRAPH 1: Connected Graph (7 Nodes, 11 Edges)
    vertices_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edges_1 = [
        (7, 'A', 'B'), (5, 'A', 'D'), (8, 'B', 'C'), 
        (7, 'B', 'E'), (6, 'B', 'D'), (5, 'C', 'E'), 
        (15, 'D', 'E'), (6, 'D', 'F'), (8, 'E', 'F'), 
        (9, 'E', 'G'), (11, 'F', 'G')
    ]
    run_kruskal("GRAPH 1 (Primary 7-Node, 11-Edge Target)", vertices_1, edges_1)

    # GRAPH 2: Connected Graph (5 Nodes, 8 Edges)
    vertices_2 = ['A', 'B', 'C', 'D', 'E']
    edges_2 = [
        (2, 'A', 'B'), (4, 'A', 'C'), (1, 'B', 'C'), (3, 'B', 'D'),
        (7, 'C', 'D'), (5, 'C', 'E'), (2, 'D', 'E'), (6, 'A', 'E')
    ]
    run_kruskal("GRAPH 2 (Test 1: 5-Node, 8-Edge Variant)", vertices_2, edges_2)

    # GRAPH 3: Connected Graph (5 Nodes, 9 Edges)
    vertices_3 = ['V', 'W', 'X', 'Y', 'Z']
    edges_3 = [
        (3, 'V', 'W'), (6, 'V', 'X'), (2, 'W', 'X'), (4, 'W', 'Y'),
        (5, 'X', 'Y'), (8, 'X', 'Z'), (1, 'Y', 'Z'), (7, 'V', 'Y'), (9, 'W', 'Z')
    ]
    run_kruskal("GRAPH 3 (Test 2: 5-Node, 9-Edge Variant)", vertices_3, edges_3)

if __name__ == "__main__":
    main()
