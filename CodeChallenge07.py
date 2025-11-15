#Odd Number Summation
#Initialize sum
#Loop 10 times
odd_sum = 0  #
for x in range(10):
    num = int(input(f"Enter a number: "))
    if num % 2 != 0: 
        odd_sum += num

print("The sum of all the odd numbers is", odd_sum)
