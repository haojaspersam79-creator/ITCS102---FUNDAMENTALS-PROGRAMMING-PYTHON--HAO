#List and its function


nm = ['apple','donut','coconut','mango','grapes']
nm.append('orange')   #add an item to the last of the list
print(nm)
nm.pop()    #remove the last item
print(nm)
nm.insert(0,'Monggo')   #add item in dif position
print(nm)
for i in nm:
    print(f"{i}  in the basket")    #all fruits one by one with 'in the basket' at the last

mi = 'Jasper and Him'
for u in mi:
    print(u)    #Will print my name from J to M
print("\nReversed\n")
for q in mi[::-1]:  #will print my name in reverse from M to J
    print(q)
