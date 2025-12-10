graph = [
    ['A', 'B', 1, 3], ['A', 'C', 2, 4], ['A', 'H', 7, 0],
    ['B', 'D', 4, 2], ['B', 'E', 6, 6],
    ['C', 'F', 3, 3], ['C', 'G', 2, 2],
    ['D', 'E', 7, 6], ['D', 'H', 5, 0],
    ['F', 'H', 1, 0], ['G', 'H', 2, 0]
]

start = input("Enter the Start Node: ")
goal = input("Enter the Goal Node: ")

temp = []
temp1 = []

for i in graph:
    temp.append(i[0])
    temp1.append(i[1])

node = set(temp).union(set(temp1))  # A, B, C, D, E, F, G, H

cost = {i: float('inf') for i in node}
path = {i: '' for i in node}
open_set = set()
close_set = set()

open_set.add(start)
cost[start] = 0
path[start] = start

def astar(graph, open_set, close_set, cost, cur_node):
    if cur_node in open_set:
        open_set.remove(cur_node)
    close_set.add(cur_node)

    for i in graph:
        if i[0] == cur_node and cost[i[0]] + i[2] + i[3] < cost[i[1]]:
            open_set.add(i[1])
            cost[i[1]] = cost[i[0]] + i[2] + i[3]
            path[i[1]] = path[i[0]] + '->' + i[1]

    cost[cur_node] = float('inf')
    smallest = min(cost, key=cost.get)

    if smallest not in close_set:
        astar(graph, open_set, close_set, cost, smallest)

astar(graph, open_set, close_set, cost, start)

if path[goal]:
    print("Path of the goal node:", path[goal])
else:
    print("Path doesn’t exist!")
