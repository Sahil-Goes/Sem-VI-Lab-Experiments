#DFS Goal Search using Shortest Path
tree = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F','G',],
    'D':[],
    'E':[],
    'F':[],
    'G':[],
}

def dfs(tree, start, goal):
    close = []
    open = [start]
    if start == goal:
        print("Start node is goal node")
        return open
    
    while open:
        path = open.pop()
        node = path[-1]
        if node not in close:
            close.append(node)
        neighbour = tree[node]
        for i in neighbour:
            new_path = list(path)
            new_path.append(i)
            open.append(new_path)
            if i == goal:
                return new_path
    return "Goal Not Found!"

start = input("Enter start node: ")
goal = input("Enter goal node: ")
print("DFS search: ", dfs(tree, start, goal))
