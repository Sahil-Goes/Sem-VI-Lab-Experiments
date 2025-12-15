#Exp6: Hill Climbing Algorithm Implementation
tree = {
    'A': [('B', 3), ('C', 5), ('K', 10)],  
    'B': [('D', 1), ('E', 0)],
    'C': [('F', 2), ('G', 2)],
    'K': [],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

start = input("Enter start node: ")
goal = input("Enter goal node: ")

open = []
close = []

def hill(tree, start, goal):
    open.append(start)

    while open:
        node = open.pop(0)

        if node == goal:
            print("Goal found!")
            close.append(node)
            print("Visited Path:", close)
            return

        close.append(node)
        neighbours = tree[node]

        # Sort neighbours by heuristic value (2nd element of tuple)
        neighbours = sorted(neighbours, key=lambda x: x[1])

        # Pick the best (lowest heuristic)
        for nxt, h in neighbours:
            if nxt not in open and nxt not in close:
                open.append(nxt)
                break

    print("Goal not found!")

hill(tree, start, goal)

