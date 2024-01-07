Graph_nodes = {
    'A':[('B',1),('C',2)],
    'B':[('D',3),('E',4)],
    'C':[('F',5)],
    'D':[('G',1)],
    'E':[('G',2)],
    'F':[('G',1)],
}

def heuristic_values(node):
    H_dist = {
        'A':10,
        'B':5,
        'C':4,
        'D':2,
        'E':3,
        'F':1,
        'G':0
    }
    return H_dist[node]

def get_neighbors(node):
    if node in Graph_nodes:
        return Graph_nodes[node]
    else:
        return None

def astarAlgo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        for v in open_set:
            if n == None or g[v]+heuristic_values(v) < g[n] + heuristic_values(n):
                n = v
        
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m,weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] +weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
                    
        if n == None:
                print("Path does not exists")
                return None
        if n == stop_node:
                path = []

                while parents[n] != n:
                    path.append(n)
                    n = parents[n]

                path.append(start_node)
                path.reverse()
                print("Path found {}".format(path))
                return path
        open_set.remove(n)
        closed_set.add(n)
    print("Path does not exists")
    return None

astarAlgo("A","G")
    
                        