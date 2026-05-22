import matplotlib.pyplot as plt

def draw_and_run_mst(graph_num, vertices, edges, positions):
    # 1. Run Kruskal's Algorithm to find MST edges
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
    total_weight = 0

    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v))
            total_weight += weight

    # 2. Plot the visual graph diagram
    plt.figure(figsize=(7, 5))
    plt.title(f"Visual Graph Layout {graph_num}\n(Total Optimal Tree Cost: {total_weight})", fontsize=12, fontweight='bold')

    # Draw all initial network edges
    for weight, u, v in edges:
        x1, y1 = positions[u]
        x2, y2 = positions[v]
        # If the edge is part of the MST, draw it in thick red. Otherwise, dashed gray.
        if (u, v) in mst_edges or (v, u) in mst_edges:
            plt.plot([x1, x2], [y1, y2], color='red', linewidth=3, zorder=1)
            plt.text((x1+x2)/2, (y1+y2)/2, str(weight), color='black', fontweight='bold', fontsize=10, bbox=dict(facecolor='white', edgecolor='none', pad=2))
        else:
            plt.plot([x1, x2], [y1, y2], color='gray', linestyle='--', linewidth=1, zorder=1)
            plt.text((x1+x2)/2, (y1+y2)/2, str(weight), color='gray', fontsize=9)

    # Draw the circular nodes with text labels
    for node, (x, y) in positions.items():
        plt.scatter(x, y, color='skyblue', s=600, edgecolors='black', zorder=2)
        plt.text(x, y, node, ha='center', va='center', fontweight='bold', fontsize=12)

    plt.axis('off')
    print(f"Graph {graph_num} displayed. Close the window to view the next graph.")
    plt.show()

def main():
    print("=========================================")
    print("GENERATING VISUAL MST GRAPH PLOTS")
    print("=========================================")

    # GRAPH 1 Layout Configurations
    v1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    e1 = [(7, 'A', 'B'), (5, 'A', 'D'), (8, 'B', 'C'), (7, 'B', 'E'), (6, 'B', 'D'), 
          (5, 'C', 'E'), (15, 'D', 'E'), (6, 'D', 'F'), (8, 'E', 'F'), (9, 'E', 'G'), (11, 'F', 'G')]
    pos1 = {'A': (4, 2), 'B': (3, 3), 'C': (1.5, 4), 'D': (3, 1), 'E': (1.5, 2.3), 'F': (2, 0.5), 'G': (0.3, 1)}
    draw_and_run_mst(1, v1, e1, pos1)

    # GRAPH 2 Layout Configurations
    v2 = ['1', '2', '3', '4']
    e2 = [(2, '1', '3'), (4, '1', '2'), (6, '3', '4'), (8, '2', '3')]
    pos2 = {'1': (0, 1), '2': (2, 1), '3': (0, 0), '4': (2, 0)}
    draw_and_run_mst(2, v2, e2, pos2)

    # GRAPH 3 Layout Configurations
    v3 = ['X', 'Y', 'Z', 'W']
    e3 = [(5, 'X', 'Y'), (7, 'W', 'Y'), (12, 'W', 'X'), (14, 'Y', 'Z')]
    pos3 = {'W': (0, 1), 'X': (2, 1), 'Y': (1, 0), 'Z': (1, -1)}
    draw_and_run_mst(3, v3, e3, pos3)

if __name__ == "__main__":
    main()

