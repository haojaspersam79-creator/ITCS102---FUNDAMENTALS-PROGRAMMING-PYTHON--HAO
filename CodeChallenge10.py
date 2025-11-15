# print("\t\t *",end=" ")
for j in range(1,11,-1):
    for p in range(10, j, -1):
        print(" ", end=' ')
    for a in range(1, j, -1):
        print("*",end = " ")
    for s in range(1, j, 1):
        print("*", end = " ")
        print()
