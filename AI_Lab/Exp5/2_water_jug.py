a = int(input("Enter capacity of Jug A: "))        
b = int(input("Enter capacity of Jug B: "))
ai = int(input("Enter initial water in Jug A: "))   
bi = int(input("Enter initial water in Jug B: "))
af = int(input("Enter final water in Jug A: "))    
bf = int(input("Enter final water in Jug B: "))

print("\nList of operations you can perform:")
print("Op1: Fill Jug A completely")
print("Op2: Fill Jug B completely")
print("Op3: Empty Jug A completely on ground")
print("Op4: Empty Jug B completely on ground")
print("Op5: Pour water from Jug A to Jug B until full")
print("Op6: Pour water from Jug B to Jug A until full")
print("Op7: Pour all water from Jug A to B")
print("Op8: Pour all water from Jug B to A")

while ai != af or bi != bf:
    op = int(input("\nEnter the operation choice: "))

    if op == 1:
        ai = a

    elif op == 2:
        bi = b

    elif op == 3:
        ai = 0

    elif op == 4:
        bi = 0

    elif op == 5:
        # Pour A → B (until B is full or A is empty)
        if b - bi > ai:
            bi = bi + ai
            ai = 0
        else:
            ai = ai - (b - bi)
            bi = b

    elif op == 6:
        # Pour B → A (until A is full or B is empty)
        if a - ai > bi:
            ai = ai + bi
            bi = 0
        else:
            bi = bi - (a - ai)
            ai = a

    elif op == 7:
        # Pour all from A → B
        bi = ai + bi
        ai = 0

    elif op == 8:
        # Pour all from B → A
        ai = ai + bi
        bi = 0

    else:
        print("Invalid operation! Try again.")
        continue

    print("Current state → Jug A:", ai, "| Jug B:", bi)

print("\nGoal State Reached!")
print("Final State → Jug A:", ai, "| Jug B:", bi)
