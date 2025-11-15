#create a program that accepts float value
#determine temparature reading
#negative infinity freezing cold temperature
#1 to 20 cold
#21 to 30 lukewarm
#31 to 40 warm
#41 to 50 hot
#51 and above boiling hot

temp = eval(input("Enter temperature --> "))
	
if temp <= 0:
	print("Temperature is Freezing")
elif temp >= 1 and temp <= 20:
	print("Temperature outside cold")
elif temp >= 21 and temp <= 30:
	print("Temperature ouutside lukewarm")
elif temp >= 31 and temp <= 40:
	print("Temperature ouutside warm")
elif temp >= 41 and temp <= 50:
	print("Temperature ouutside hot")
elif temp >= 51 and temp <=100:
	print("Temperature ouutside boiling hot")

else:
	print("invalid temperature")
