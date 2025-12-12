# ==============================================================
# ITCS102 – FINAL PROJECT
# Python Fundamentals – Interactive Menu Program 
# ==============================================================

def pause():
    input("\nPress E to continue ---> ")

# -------------------------
#PROGRAM FUNCTIONS
# -------------------------

def activity1():
    print("\n Activity 1")
    print("Hi, I am Jasper Sam M. Hao, student from BSIT First Year section 1A.\n"
          "This is my first file in the repository.\n"
          "I am 18 yrs old, from Brgy. 3 Lucena City.\n"
          "I am a working student. I love eating and playing games.")

def activity2():
    print("\n Activity 2")
    name = input("What is your name? ")
    print(f"Hi, {name}! Welcome to the Matrix.")

def activity3():
    print("\n Activity 3")
    print("Happy\n\t\tMonday,\t\t" 
    "BSIT 1A \n from DLL\n" 
    "The Quick Brown Fox Jumps Over the Lazy Dog.")

def activity4():
    print("\n Activity 4")
    name = input("Enter a string -> ")
    print("Your name has ", len(name), "character")

def activity5():
    print("\n Activity 5")
    something =eval(input("Input something --> "))
    print("The data type of something is",type(something))
    answer = 1 + something
    print("the answer is", answer)

def activity6():
    print("\n Activity 6")
    n1 = eval(input("Enter the first number: "))
    n2 = eval(input("Enter the second number: "))
    s = n1 + n2
    d = n1 - n2
    p = n1 * n2
    q = n1 / n2
    #solution = ((n1/n2) * 1005) // 300
    print("\nThe sum of", n1, "and", n2, "is", s)
    print("The difference of", n1, "and", n2, "is", d)
    print("The product of", n1, "and", n2, "is", p)
    print("The quotient of", n1, "and", n2, "is", q)
    print(n1, "exponent by", n2, "is", n1**n2)
    print("The remainder of", n1, "and", n2, "is", n1 % n2)
    print("The floor division of", n1, "and", n2, "is", n1//n2)

def activity7():
    print("\n Activity 7")
    a = 5

    print("the value of a is ",a)
    a += 5
    print("the value of a is ",a)

    a = a + 5
    a += 3
    a += 8
    a *= 2
    a -= 3

    print("the value of a is ",a)

def activity8():
    print("\n Activity 8")
    balance = 1000
    withdrawal = 1000

    b = 5
    a = 5
    name1 = 'Jasper'
    name2 = 'Jasper'
    #print(b = a)
    print (name1 != name2)

def activity9():
    print("\n Activity 9")
    username = 'JasperSam'
    password = 'CuteniSelf'

    #print(username == 'JasperSam')
    #print((username == 'JasperSam') and (password == 'CuteniSelf'))
    #print((username == 'JasperSam') or (password == 'CuteniSelf'))
    print(not((username == 'JasperSam') or (password == 'CuteniSelf')))

def activity10():
    print("\n Activity 10")
    # Grocery
    print("---------------------------\n        Welcome \n---------------------------")
    
    name = input("What is your Name? ")
    food = input("What Food (Rice/Pasta): ")
    many = eval(input("How many (1-10): "))
    fr = eval(input("How much? "))
    pwd = input("Are you PWD or Senior (Yes/No): ")

    equal = many * fr * 0.05
    man = many * fr
    more = man - equal

    print("---------------------------")

    if pwd.lower() == "yes":
        print("Hello", name,
              "\nItem:", food,
              "\nQuantity:", many,
              "\nPrice each:", fr,
              "\nTotal:", man,
              "\nDiscount:", equal,
              "\nTotal w/ discount:", more)
    else:
        print("Hello", name,
              "\nItem:", food,
              "\nQuantity:", many,
              "\nPrice each:", fr,
              "\nTotal:", man,
              "\nDiscount: 0",
              "\nTotal w/ discount:", man)

def activity11():
    print("\n Activity 11")
    # create a program that accepts float value
    # determine temperature reading

    temp = float(input("Enter temperature --> "))

    if temp <= 0:
        print("Temperature is Freezing")
    elif 1 <= temp <= 20:
        print("Temperature is Cold")
    elif 21 <= temp <= 30:
        print("Temperature is Lukewarm")
    elif 31 <= temp <= 40:
        print("Temperature is Warm")
    elif 41 <= temp <= 50:
        print("Temperature is Hot")
    elif temp >= 51:
        print("Temperature is Boiling Hot")
    else:
        print("Invalid temperature")

def activity12():
    print("\n Activity 12")
    #print hello world 10 times
    #stopping point is not included on the count 
    for understand in range(1, 51, 3):
        print(understand, "- Understand ikot, understand")

def activity13():
    print("\n Activity 13")
    #using for loop, ask user to input 10 numbers
    #after input, get the summation all the numbers 
    for P in range (1, 11):
        num = 0
        number = eval(input("Enter a number "))
        num += number
        print("Siomai Rice", num)
    print(num)

def activity14():
    print("\n Activity 14")
    for j in range(20 ,0 ,-1):
        print(j ,"Halo")

def activity15():
    print("\n Activity 15")
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

def activity16():
    print("\n Activity 16")
    #new line in print
    #using loop, print 1 to 10 horizontally

    for x in range(1,11,1):
        print(x,end="+")

def activity17():
    print("\n Activity 17")
    #NESTED FOR LOOP

    for j in range(1,11,1):
        print(j, end= "\n")
    for p in range(1,j,1):
        print(p,end=" ")
    print()

def activity18():
    print("\n Activity 18")
    for j in range(1,21):
        for p in range(1,j):
            print(p,end=" ")
    print()

def activity19():
    print("\n Activity 19")
    for j in range(1,11,1):
        for p in range(1, j, 1):
            print("*", end=' ') #1 2 3 4 5 6 7 8 9 10
    print()

def activity20():
    print("\n Activity 20")
    #for j in range(1,11,1):
    #for p in range(1,j,1):
       #print(" ", end= ' ')
    #for a in range("1",10,-1):
        #print("*",end = " ")
    #print()

    for j in range(1,11,1):
        for p in range(1,j,1):
            print(" ", end= ' ')
    for a in range(1,10,-1):
        print("*",end = " ")
    print()

    for j in range(1,11,1):
        for p in range(1,j,1):
            print(" ", end= ' ')
    for a in range("1",10,-1):
        print("*",end = " ")
    print()

def activity21():
    print("\n Activity 21")
    #while loop

    me = True

    while me == True:
        moon = input("(Yes or No): ")

        if moon.lower() == "yes":
            print("Continue")
            continue
        elif moon.lower() == "no":
            print("Stop")
        break
    else:
        print("Error input")

def activity22():
    print("\n Activity 22")
    import random

    num = random.randint(1, 10)
    tries = 0

    while True:
        g = int(input("What number do you guess (1–10): "))
        tries += 1

        if g == num:
            print("Congratulations!")
            print(f"The number is {num}")
            print(f"You only took {tries} tries")
            break
        else:
            print("You're wrong, try again!")

def activity23():
    print("\n Activity 23")
    #List and its function

    nm = ['apple','donut','coconut','mango','grapes']
    nm.append('orange')   #add an item to the last of the list
    print(nm)
    nm.pop()    #remove the last item
    (nm)
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

def activity24():
    print("\n Activity 24")
    def greet(name):
        print(f"Hi {name}, Happy Friday! ")

    greet("Sam")
    greet("Friends")

    def summation(j):
        sum = 0
    for j in range(j, 0, -1):
        sum += j
    print(f"The sum of {j} is {sum}")

    summation(1)
    summation(2)

def activity25():
    print("\n Activity 25")

    # Sub-functions
    def activity1():
        name = input("What is your name: ")
        print(f"Hello {name}!")

    def activity2():
        age = int(input("How old are you: "))
        print(f"You are {age} years old.")

    def activity3():
        hob = input("What is your hobby: ")
        print(f"Your hobby is {hob}.")

    # Welcome message
    name = input("What is your name: ")
    print(f"Welcome {name} to my File Compiler!\n")

    # Menu loop
    while True:
        print("\nSelect a program")
        print("1 - Activity 1")
        print("2 - Activity 2")
        print("3 - Activity 3")
        print("4 - Exit")

        new = input("What program would you like to run: ").strip()

        if new == "1":
            activity1()
        elif new == "2":
            activity2()
        elif new == "3":
            activity3()
        elif new == "4":
            print("Come Again!")
            break
        else:
            print("Error: Invalid input.")

def activity26():
    print("\n Activity 26")
    prog = {'Popular':'Python','Essential':'JavaScript', 'WidelyUsed':'Java', 'Powerful':'C++', 'MyHouse':'C#', }

    print(prog['MyHouse'])

def activity27():
    print("\n Activity 27")
    print("Adding Data to Dictionary")
    print(" ============================== ")

    empty_dictionary = {}

    # function to print all kdrama entries
    def print_kdrama():
        if not empty_dictionary:
            print("No Kdramas in the list yet.")
        else:
            for h, p in empty_dictionary.items():
                print(f"CODE: {h}  |  TITLE: {p}")

    # function to search by code
    def Search(code):
        if code in empty_dictionary:
            print("Searching...")
            print(f"Result: {empty_dictionary[code]}")
        else:
            print("Code not found in the database.")

    # main loop
    while True:
        keys = input("Input code for this Kdrama ---> ")
        value = input("Enter the title ---> ")

        # add data to dictionary
        empty_dictionary[keys] = value

        # menu choices
        choice = input(
            "Would you like to continue?\n"
            "y - Yes\n"
            "n - No\n"
            "p - Print all Kdramas\n"
            "s - Search Kdrama\n"
            "---> "
        ).lower()

        if choice == 'y':
            print("Continue...\n")
            continue

        elif choice == 'n':
            print("Program stops.")
            break

        elif choice == 'p':
            print_kdrama()
            print()
            continue

        elif choice == 's':
            code = input("Enter Kdrama code to search ---> ")
            Search(code)
            print()
            continue

        else:
            print("Invalid choice.\n")
            continue

def activity28():
    print("\n Activity 28")

def CodeChallenge1():
    print(f"\n Code Challenge 1")
    name = input("What's your name:")
    print ("\t\t\t\t*\n\t\t\t*\t\t*\n\t\t*\t\t\t\t*\n\t*\t\t\tHI\t\t\t*\n*\t\t\t\t",name,"\t\t\t\t*\n\t*\t\t\t\t\t\t*\n\t\t*\t\t\t\t*\n\t\t\t*\t\t*\n\t\t\t\t*")

def CodeChallenge2():
    print(f"\n Code Challenge 2")
    amount = int(input("Enter amount to deposit: "))

    a = amount // 1000
    amount = amount % 1000

    b = amount // 500
    amount = amount % 500

    c = amount // 200
    amount = amount % 200

    d = amount // 100
    amount = amount % 100

    e = amount // 50
    amount = amount % 50

    f = amount // 20
    amount = amount % 20

    g = amount // 10
    amount = amount % 10

    h = amount // 5
    amount = amount % 5

    i = amount // 1
    amount = amount % 1

    print("P1000:", a)
    print("P500 :", b)
    print("P200 :", c)
    print("P100 :", d)
    print("P50  :", e)
    print("P20  :", f)
    print("P10  :", g)
    print("P5   :", h)
    print("P1   :", i)

def CodeChallenge3():
    print("\n Code Challenge 3")

    # preset username and password
    username = 'jsam'
    password = 'cuteako'

    # user input
    userinput = input("Username --> ")
    passinput = input("Type your password --> ")

    # login check
    if userinput == username and passinput == password:
        print("Access Granted!")
    else:
        print("Access Denied")

def CodeChallenge4():
    print("\n Code Challenge 4")

    number = int(input("Input a number --> "))

    if number % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")

def CodeChallenge5():
    print("\n Code Challenge 5")
    print("Welcome to the Manga Selection!")
    print("Answer a few questions before we proceed.")

    print("\nWhat type of genre do you like?")
    genre = int(input("1. Action\n2. Comedy\n3. Horror\nAnswer: "))

    if genre == 1:
        print("Welcome to the list of Action Manga!")
    elif genre == 2:
        print("Welcome to the list of Comedy Manga!")
    elif genre == 3:
        print("Welcome to the list of Horror Manga!")
    else:
        print("Sorry! We don't have that kind of manga here. Try again!")
        return

    print("\nHow long should the manga be?")
    length = input("1. Short\n2. Medium\n3. Long\nAnswer: ")

    if length == "1":
        print("You chose SHORT. Now let’s proceed to decades.")
    elif length == "2":
        print("You chose MEDIUM. Now let’s proceed to decades.")
    elif length == "3":
        print("You chose LONG. Now let’s proceed to decades.")
    else:
        print("Invalid length choice, try again!")
        return

    print("\nWhat decade should it be from?")
    year = input("1. 1990s\n2. 2000s\n3. 2010s\nAnswer: ")

    if year == "1":
        print("You chose 1990s! Now Enjoy!")
    elif year == "2":
        print("You chose 2000s! Now Enjoy!")
    elif year == "3":
        print("You chose 2010s! Now Enjoy!")
    else:
        print("Invalid decade choice, try again!")
        return

    # Final Recommendations
    print("\nHere are some recommendations for you:")
    print("\nNaruto (1999–2014) – Masashi Kishimoto")
    print("One Piece (1997–present) – Eiichiro Oda")
    print("Bleach (2001–2016) – Tite Kubo")
    print("Attack on Titan (2009–2021) – Hajime Isayama")
    print("Jujutsu Kaisen (2018–present) – Gege Akutami")

def CodeChallenge6():
    print(f"\n Code Challenge 6")
    #factorial program
    #descending number
    #must be equal to 120
    #the factorial number of 5 is 120

    num = eval(input("Enter your number --> "))

    for x in range (num -1, 0, -1):
        num *= x
    print(x,"The factorial of", num)

def CodeChallenge7():
    print(f"\n Code Challenge 7")
    #Odd Number Summation
    #Initialize sum
    #Loop 10 times
    odd_sum = 0  #
    for x in range(10):
        num = int(input(f"Enter a number: "))
    if num % 2 != 0: 
        odd_sum += num

    print("The sum of all the odd numbers is", odd_sum)

def CodeChallenge8():
    print(f"\n Code Challenge 8")
    #Multiplication Table Form
    #Loop for 1 to 10 
    #Ask the user to input a number

    print("MULTIPLICATION TABLE MAKER")

    number = int(input("Enter a Number: "))

    print(f"\nMultiplication table for {number}:")

    for x in range (0, 11, 1):
        result = number * x
    print(f"{number} x {x} = {result}")

def CodeChallenge9():
    print(f"\n Code Challenge 9")
    #Countdown Timer Simulator
    #Ask the user to enter the starting number
    #Use a for loop to count down from the starting number to 1

    print("Countdown Timer Simulator")

    start = int(input("Please enter the number for countdown: "))

    print("\nCountdown Started")

    for x in range(start, 0, -1):
        print(x)

    print("Liftoff!")

def CodeChallenge10():
    print(f"\n Code Challenge 10")
    # print("\t\t *",end=" ")
    for j in range(1,11,-1):
        for p in range(10, j, -1):
            print(" ", end=' ')
    for a in range(1, j, -1):
        print("*",end = " ")
    for s in range(1, j, 1):
        print("*", end = " ")
        print()

def CodeChallenge11():
    print(f"\n Code Challenge 11")
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

def CodeChallenge12():
    print(f"\n Code Challenge 12")
    #print("\t\t",end=" ")
    for j in range(1, 7, 1):
        for p in range(7, j, -1):
            print(" ", end =' ') 
    for a in range(j, 0, -1):
        print(a, end =" ") 
    for s in range(2, j + 1,1):
          print(s, end=" ")
    print()

def CodeChallenge13():
    print(f"\n Code Challenge 13")
    #Christmas Tree
    for j in range(2,6,1):
        for p in range(0,7):
            print(" ",end=" ")
    for a in range(6,j,-1):
        print(" ",end=" ")
    for s in range(3,j):
        print("*",end=" ")
    for a in range(2,j,1):
        print("*",end=" ")
    print()    
    for m in range(1,3,1):
        for b in range(0,7):
            print(" ",end=" ")
    for a in range(0 - 1,m,1):
        print(" ",end=" ")
    for l in range(2,m,-1):
        print("*",end=" ")
    for o in range(3,m,-1):
        print("*",end=" ")
    print()    
    for v in range(2,9,1):
        for e in range(12,v,-1):
            print(" ",end=" ")
    for s in range(2,v,1):
        print("*",end=" ")
    for j in range(1,v):
        print("*",end=" ")
    print()
    for a in range(2,10,1):
        for s in range(12,a,-1):
            print(" ",end=" ")
    for p in range(1,a):
        print("*",end=" ")
    for e in range(2,a):
        print("*",end=" ")
    print()
    for r in range(2,13,1):
        for s in range(12,r,-1):
            print(" ",end=" ")
    for a in range(1,r):
        print("*",end=" ")
    for m in range(2,r):
        print("*",end=" ")
    print()
    for h in range(1,7):
        for a in range(1,9):
            print(" ",end=" ")
    for o in range(1,9):
        print("",end="*")
    print()

def CodeChallenge14():
    print("\n Code Challenge 14")
    print("All odd numbers will be calculated. Even numbers will be skipped.")

    name = input("What's your name: ")

    odd = 0
    numb = ""   # will store all odd numbers found

    while True:
        num = int(input("Put a number (0 to stop): "))

        if num == 0:   # stop condition
            print("Bye Bye!")
            break

        if num % 2 == 1:
            print("Odd detected")
            odd += num
            numb += str(num) + ", "
        else:
            print("Even detected — Skipping")

    print(f"\nTotal of all odd numbers: {odd}")
    print(f"All odd numbers: {numb}")

def CodeChallenge15():
    print(f"\n Code Challenge 15")
    #Anime list
    #Using list and while loop
    print("Anime Title List")

    anime = [] #empty list
    mn = True   

    while mn == True:
        num = input("Put a Title of an Anime: ")
    print("Anime Added to the your Anime List")
    anime.append(num) #all title that put will go to the list
    if num == "exit": #stopper
        print("All done,You are now exiting!! ")
        anime.pop() #will remove the string exit to list
        #to stop the loop

    print(f"Here All the Title of your Anime: ") 
    for r in anime:     #will print all the anime u putted,from up to down
        print(f"- {r}")

def CodeChallenge16():
    print(f"\n Code Challenge 16")
# -------------------------
# CODE CHALLENGE SELECTOR
# -------------------------

def CodeChallenge(num):
    if num == 1: CodeChallenge1()
    elif num == 2: CodeChallenge2()
    elif num == 3: CodeChallenge3()
    elif num == 4: CodeChallenge4()
    elif num == 5: CodeChallenge5()
    elif num == 6: CodeChallenge6()
    elif num == 7: CodeChallenge7()
    elif num == 8: CodeChallenge8()
    elif num == 9: CodeChallenge9()
    elif num == 10: CodeChallenge10()
    elif num == 11: CodeChallenge11()
    elif num == 12: CodeChallenge12()
    elif num == 13: CodeChallenge13()
    elif num == 14: CodeChallenge14()
    elif num == 15: CodeChallenge15()
    elif num == 16: CodeChallenge16()
    else:
        print("Invalid challenge number")

# -------------------------
# FIXED: Activity Selector
# -------------------------

def sample_activity(num):
    if num == 1:
        activity1()
    elif num == 2:
        activity2()
    elif num == 3:
        activity3()
    elif num == 4:
        activity4()
    elif num == 5:
        activity5()
    elif num == 6:
        activity6()
    elif num == 7:
        activity7()
    elif num == 8:
        activity8()
    elif num == 9:
        activity9()
    elif num == 10:
        activity10()
    elif num == 11:
        activity11()
    elif num == 12:
        activity12()
    elif num == 13:
        activity13()
    elif num == 14:
        activity14()
    elif num == 15:
        activity15()
    elif num == 16:
        activity16()
    elif num == 17:
        activity17()
    elif num == 18:
        activity18()
    elif num == 19:
        activity19()
    elif num == 20:
        activity20()
    elif num == 21:
        activity21()
    elif num == 22:
        activity22()
    elif num == 23:
        activity23()
    elif num == 24:
        activity24()
    elif num == 25:
        activity25()
    elif num == 26:
        activity26()
    elif num == 27:
        activity27()
    elif num == 28:
        activity28()
    else:
        print(f"\n--- Activity {num} ---")
        print("No specific code yet for this activity.")

# -------------------------
# SUBMENUS
# -------------------------

def activities_menu():
    while True:
        print("\n=== ACTIVITIES MENU ===")
        for i in range(1, 29):
            print(f"{i}) Activity {i}")
        print("29) Return to Main Menu")

        choice = input("Choose an activity: ")

        if not choice.isdigit():
            print("Invalid choice. Try again.")
            continue

        choice = int(choice)

        if 1 <= choice <= 28:
            sample_activity(choice)
            pause()
        elif choice == 29:
            break
        else:
            print("Invalid choice. Try again.")

def challenges_menu():
    while True:
        print("\n=== CHALLENGES MENU ===")
        for i in range(1,17):
            print(f"{i}) Code Challenge {i}")
        print("17) Return")

        c=input("Choose: ")
        if c.isdigit():
            c=int(c)
            if 1<=c<=16:
                CodeChallenge(c)
                pause()
            elif c==17:
                break

# -------------------------
# MAIN MENU
# -------------------------

def main_menu():
    while True:
        print("\n========== MAIN MENU ==========")
        print("1) Activities 1 to 28")
        print("2) Code Challenges 1 to 16")
        print("3) Exit Program")

        choice = input("Choose an option: ")

        if choice == "1":
            activities_menu()
        elif choice == "2":
            challenges_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid Option.")

# -------------------------
# PROGRAM START
# -------------------------
main_menu()