def find_mst():
    print("=========================================")
    print("RUNNING MINIMUM SPANNING TREE (MST) TOOL")
    print("=========================================")
    
    # Graph edges: (weight, vertex1, vertex2)
    edges = [
        (1, 'A', 'B'), (3, 'A', 'C'), (4, 'B', 'C'),
        (2, 'B', 'D'), (5, 'C', 'D'), (6, 'D', 'E')
    ]
    edges.sort()
    
    parent = {v: v for v in ['A', 'B', 'C', 'D', 'E']}
    
    def find(i):
        if parent[i] == i:
            return i
        return find(parent[i])

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        parent[root_i] = root_j

    mst = []
    total_weight = 0
    
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))
            total_weight += weight

    print("Edges included in the Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"Edge {u} - {v} with weight {w}")
    print(f"\nTotal Minimum Spanning Tree Weight = {total_weight}")

if __name__ == "__main__":
    find_mst()
