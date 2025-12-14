#DFS Depth Limited Search
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
depth = int(input("Enter depth limit: "))
level = 0
path = []

def depth_limited_dfs(tree, start, goal, depth, level, path):
    print("Current Level: ", level)
    path.append(start)
    if start == goal:
        print("Start node is goal node")
        return path
        
    if level == depth:
        return False
        
    print("Expanding Current Node: ", start)
    neighbour = tree[start]
    for i in neighbour:
        if depth_limited_dfs(tree, i, goal, depth, level+1, path):
            return True
        path.pop()
    return False
    
result = depth_limited_dfs(tree, start, goal, depth, level, path)
if(result):
    print("Goal Found!")
    print("Path: ",path)
else:
    print("Goal Not Found! using depth of ", depth)