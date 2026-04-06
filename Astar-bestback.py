# =========================
# A*算法（Open表 + Closed表）
# =========================

# 图结构（邻接表）
graph = {
    "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
    "Zerind": [("Arad", 75), ("Oradea", 71)],
    "Oradea": [("Zerind", 71), ("Sibiu", 151)],
    "Sibiu": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    "Timisoara": [("Arad", 118), ("Lugoj", 111)],
    "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],
    "Mehadia": [("Lugoj", 70), ("Drobeta", 75)],
    "Drobeta": [("Mehadia", 75), ("Craiova", 120)],
    "Craiova": [("Drobeta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)],
    "Rimnicu Vilcea": [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)],
    "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
    "Pitesti": [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],
    "Bucharest": [("Fagaras", 211), ("Pitesti", 101)]
}

# 启发函数 h(n)
heuristic = {
    "Arad": 366, "Zerind": 374, "Oradea": 380, "Sibiu": 253,
    "Timisoara": 329, "Lugoj": 244, "Mehadia": 241,
    "Drobeta": 242, "Craiova": 160, "Rimnicu Vilcea": 193,
    "Fagaras": 178, "Pitesti": 98, "Bucharest": 0
}


def a_star_open_closed(graph, heuristic, start, goal):
    # Open表：待扩展节点
    open_list = set([start])
    # Closed表：已扩展节点
    closed_list = set()

    # g(n)：起点到当前节点的最短距离
    g = {start: 0}

    # 父节点（用于回溯路径）
    parent = {start: None}

    while open_list:
        # ① 选 f(n)=g+h 最小的节点
        current = min(open_list, key=lambda x: g[x] + heuristic[x])

        print("当前节点:", current)

        # ② 到达目标
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], g[goal]

        # ③ 从Open移到Closed
        open_list.remove(current)
        closed_list.add(current)

        # ④ 扩展邻居
        for neighbor, cost in graph[current]:

            if neighbor in closed_list:
                continue

            new_g = g[current] + cost

            # ⑤ 更新条件
            if neighbor not in open_list or new_g < g.get(neighbor, float('inf')):
                g[neighbor] = new_g
                parent[neighbor] = current
                open_list.add(neighbor)

    return None, float('inf')


# =========================
# 主函数
# =========================
if __name__ == "__main__":
    start = "Arad"
    goal = "Bucharest"

    path, distance = a_star_open_closed(graph, heuristic, start, goal)

    print("\n最优路径:", path)
    print("最短距离:", distance)