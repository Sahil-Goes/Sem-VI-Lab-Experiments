#Iterative Deepening DFS
tree = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F','G',],
    'D':[],
    'E':[],
    'F':[],
    'G':[],
}

start = input("Enter start node: ")
goal = input("Enter goal node: ")
max_depth = int(input("Enter depth limit: "))
level = 0
path = []

def depth_limited_dfs(start, goal, tree, path, level, depth):
    print("Current Level: ", level)
    path.append(start)
    if start == goal:
        print("Start node is goal node")
        return path
        
    if level == depth:
        return False
        
    print("Expanding current node: ", start)
    neighbour = tree[start]
    for i in neighbour:
        print("Expanding current node: ", i)
        if depth_limited_dfs(i, goal, tree, path, level+1, depth):
            return True
        path.pop()
    return False
    
def Iterative_Deepening_DFS(start, goal, tree, max_depth):
    for i in range(max_depth):
        print("Iteration No: ", i+1)
        path = []
        if depth_limited_dfs(start, goal, tree, path, level, i):
            print("Goal Found!")
            print("Path: ", path)
            return True
    return False
    
Iterative_Deepening_DFS(start, goal, tree, max_depth)