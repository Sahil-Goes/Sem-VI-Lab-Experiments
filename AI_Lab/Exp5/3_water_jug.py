a = int(input("Enter the capacity of Jug A: "))
b = int(input("Enter the capacity of Jug B: "))
c = int(input("Enter the capacity of Jug C: "))

af = int(input("Enter the final water in Jug A: "))
bf = int(input("Enter the final water in Jug B: "))
cf = int(input("Enter the final water in Jug C: "))

path = []
visited = {}

def all_states(state):
    x, y, z = state

    # Goal state reached
    if (x, y, z) == (af, bf, cf):
        path.append(state)
        return True

    # Already visited
    if (x, y, z) in visited:
        return False

    visited[(x, y, z)] = True

    # Pour from Jug A
    if x > 0:

        # A → B
        if x + y <= b:
            if all_states((0, x + y, z)):
                path.append(state)
                return True
        else:
            if all_states((x - (b - y), b, z)):
                path.append(state)
                return True

        # A → C
        if x + z <= c:
            if all_states((0, y, x + z)):
                path.append(state)
                return True
        else:
            if all_states((x - (c - z), y, c)):
                path.append(state)
                return True

    # Pour from Jug B
    if y > 0:

        # B → A
        if x + y <= a:
            if all_states((x + y, 0, z)):
                path.append(state)
                return True
        else:
            if all_states((a, y - (a - x), z)):
                path.append(state)
                return True

        # B → C
        if y + z <= c:
            if all_states((x, 0, y + z)):
                path.append(state)
                return True
        else:
            if all_states((x, y - (c - z), c)):
                path.append(state)
                return True

    # Pour from Jug C
    if z > 0:

        # C → A
        if x + z <= a:
            if all_states((x + z, y, 0)):
                path.append(state)
                return True
        else:
            if all_states((a, y, z - (a - x))):
                path.append(state)
                return True

        # C → B
        if y + z <= b:
            if all_states((x, y + z, 0)):
                path.append(state)
                return True
        else:
            if all_states((x, b, z - (b - y))):
                path.append(state)
                return True

    return False


# Start from initial state
all_states((a, 0, 0))
path.reverse()

print("\nSolution Path:")
for state in path:
    print(state)
