#Steepest Ascent Hill Climbing Algorithm Implementation
tree = {
    'A': [('B', 3), ('C', 5), ('K', 10)],
    'B': [('D', 1), ('E', 0)],
    'C': [('F', 2), ('G', 1)],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
    'K': []
}

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

open = []
close = []

def Hill_Climbing(tree, start, goal):
    open.append(start)

    while open:
        node = open.pop(0)

        if node == goal:
            print("Goal node found")
            close.append(node)
            print("Visited Path:", close)
            return

        close.append(node)
        neighbour = sorted(tree[node], key=lambda x: x[1])  # Sort by heuristic value

        if neighbour:
            best_neighbour = neighbour[0][0]  # Pick neighbour with lowest heuristic
            open.append(best_neighbour)

    print("Goal node not found!")

Hill_Climbing(tree, start, goal)
