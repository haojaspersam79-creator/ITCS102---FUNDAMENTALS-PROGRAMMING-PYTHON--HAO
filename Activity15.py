#STRING FORMATTING
#firstname = "Sam"
#food = "Spaghetti"
#color = "Blue"

#print("My name is",(firstname),"I love",(food),"and I like the color",(color))

#Input 10 Numbers, and get all the summation of all the even numbers

even_sum = 0

for x in range(1,11,1):
    num = eval(input(f"{x} - Enter a Number --> "))

    if num % 2 == 1:
        even_sum += num

print(f"The sum of all the EVEN numbers given is {even_sum}")
