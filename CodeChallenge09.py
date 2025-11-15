#Countdown Timer Simulator
#Ask the user to enter the starting number
#Use a for loop to count down from the starting number to 1

print("Countdown Timer Simulator")

start = int(input("Please enter the number for countdown: "))

print("\nCountdown Started")

for x in range(start, 0, -1):
    print(x)

print("Liftoff!")
