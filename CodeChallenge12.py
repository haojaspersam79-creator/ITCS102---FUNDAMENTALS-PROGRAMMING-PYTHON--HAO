#print("\t\t",end=" ")
for j in range(1, 7, 1):
    for p in range(7, j, -1):
        print(" ", end =' ') 
    for a in range(j, 0, -1):
        print(a, end =" ") 
    for s in range(2, j + 1,1):
          print(s, end=" ")
    print()
