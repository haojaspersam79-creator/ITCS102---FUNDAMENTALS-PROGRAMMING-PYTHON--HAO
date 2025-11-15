from Activity25_1 import *

name  = input("Whats is your name: ")

print(f"Welcome {name} to my File compiler")

t = True

while t == True:
    print("Select a program")
    print("1 - Activity1\n2 - Activity2\n3 - Activity3\n4 - Exit")

    new = input("What program would you like to run: ").lower()

    if new == "1":
        activity1()
        continue
    elif new == "2":
        activity2()
        continue
    elif new == "3":
        activity3()
        continue
    elif new == "4":
        print("Come Again!")
        break
    else:
        print("error input")
