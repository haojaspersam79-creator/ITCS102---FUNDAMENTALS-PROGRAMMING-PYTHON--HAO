#Make a Diamond using loops
print("\t\t *")
for j in range(2,10,1):
    for p in range(10,j,-1):
        print(" ",end=" ")
    for a in range(1,j,1):
        print("*",end=" ")
    for s in range(1,j,1):
        print("*",end=" ")
    print()
for j in range(1,10,1):
    for p in range(1,j,1):
        print(" ",end=" ")
    for a in range(10,j,-1):
        print("*",end=" ")
    for s in range(10,j,-1):
        print("*",end=" ")
    print()
print("\t\t *")
