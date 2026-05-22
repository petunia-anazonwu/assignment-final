import matplotlib
matplotlib.use('TkAgg')  # Forces Windows to pop up a visual window
import matplotlib.pyplot as plt

def run_kruskal(graph_name, vertices, edges, positions):
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

    # --- VISUAL POP-UP WINDOW BLOCK ---
    plt.figure(figsize=(7, 5))
    plt.title(f"{graph_name}\n(Total Optimal Tree Cost: {total_tree_cost})", fontsize=12, fontweight='bold')

    mst_pairs = [(u, v) for _, u, v in mst_edges]

    # Draw all graph lines
    for weight, u, v in edges:
        x1, y1 = positions[u]
        x2, y2 = positions[v]
        if (u, v) in mst_pairs or (v, u) in mst_pairs:
            plt.plot([x1, x2], [y1, y2], color='red', linewidth=3, zorder=1)
            plt.text((x1+x2)/2, (y1+y2)/2, str(weight), color='black', fontweight='bold', fontsize=11, bbox=dict(facecolor='white', edgecolor='none', pad=2))
        else:
            plt.plot([x1, x2], [y1, y2], color='gray', linestyle='--', linewidth=1, zorder=1)
            plt.text((x1+x2)/2, (y1+y2)/2, str(weight), color='gray', fontsize=9)

    # Draw the circular nodes
    for node, (x, y) in positions.items():
        plt.scatter(x, y, color='skyblue', s=600, edgecolors='black', zorder=2)
        plt.text(x, y, node, ha='center', va='center', fontweight='bold', fontsize=12)

    plt.axis('off')
    plt.show()  # Opens the actual pop-up window on your computer screen

def main():
    # GRAPH 1: Connected Graph (7 Nodes, 11 Edges)
    vertices_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edges_1 = [
        (7, 'A', 'B'), (5, 'A', 'D'), (8, 'B', 'C'), 
        (7, 'B', 'E'), (6, 'B', 'D'), (5, 'C', 'E'), 
        (15, 'D', 'E'), (6, 'D', 'F'), (8, 'E', 'F'), 
        (9, 'E', 'G'), (11, 'F', 'G')
    ]
    pos1 = {'A': (4, 2), 'B': (3, 3), 'C': (1.5, 4), 'D': (3, 1), 'E': (1.5, 2.3), 'F': (2, 0.5), 'G': (0.3, 1)}
    run_kruskal("GRAPH 1 (Primary 7-Node, 11-Edge Target)", vertices_1, edges_1, pos1)

    # GRAPH 2: Connected Graph (5 Nodes, 8 Edges)
    vertices_2 = ['A', 'B', 'C', 'D', 'E']
    edges_2 = [
        (2, 'A', 'B'), (4, 'A', 'C'), (1, 'B', 'C'), (3, 'B', 'D'),
        (7, 'C', 'D'), (5, 'C', 'E'), (2, 'D', 'E'), (6, 'A', 'E')
    ]
    pos2 = {'A': (0, 1), 'B': (1, 2), 'C': (1, 0), 'D': (2.5, 2), 'E': (2.5, 0)}
    run_kruskal("GRAPH 2 (Test 1: 5-Node, 8-Edge Variant)", vertices_2, edges_2, pos2)

    # GRAPH 3: Connected Graph (Exactly 5 Nodes, 8 Edges) - Test 2
    vertices_3 = ['1', '2', '3', '4', '5']
    edges_3 = [
        (1, '1', '2'), (2, '3', '4'), (3, '2', '3'), (4, '4', '5'),
        (5, '1', '3'), (6, '2', '4'), (7, '3', '5'), (8, '1', '5')
    ]
    pos3 = {'1': (0, 2), '2': (1.5, 3), '3': (1.5, 1), '4': (3, 2), '5': (4.5, 2)}
    run_kruskal("GRAPH 3 (Test 2: 5-Node, 8-Edge Variant)", vertices_3, edges_3, pos3)

if __name__ == "__main__":
    main()

