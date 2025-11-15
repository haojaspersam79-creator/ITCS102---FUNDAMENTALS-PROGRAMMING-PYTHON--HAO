#Multiplication Table Form
#Loop for 1 to 10 
#Ask the user to input a number

print("MULTIPLICATION TABLE MAKER")

number = int(input("Enter a Number: "))

print(f"\nMultiplication table for {number}:")

for x in range (0, 11, 1):
    result = number * x
    print(f"{number} x {x} = {result}")


