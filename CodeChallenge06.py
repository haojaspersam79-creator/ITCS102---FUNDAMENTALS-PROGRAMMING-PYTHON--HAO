#factorial program
#descending number
#must be equal to 120
#the factorial number of 5 is 120

num = eval(input("Enter your number --> "))

for x in range (num -1, 0, -1):
    num *= x
    print(x,"The factorial of", num)
    
