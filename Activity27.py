print("Adding Data to dictionary")
print(" ============================== ")
yes = True

empty_dictionary = {}

def print_kdrama():
    for h,p in empty_dictionary.items():
        print(f"CODE {h} TITLE -- {p}")

def Search(keys):
    print("Searching... ")
    print(f"result_shows {empty_dictionary[keys]} on our database")

while yes == True:
    keys = input("Input keys for this kdrama ---> ")
    value = input("Enter a title ---> ")

    ##adding data to a dictionary
    empty_dictionary[keys] = value

    choice = input("Would you like to continue adding kdrama \ny-Yes\nn-No\np-Print\ns-Search\n---> ").lower()
    if choice == 'y':
        print("Continue...")
        continue
    elif choice == 'n':
        print("Program stops")
        break
    elif choice == 'p':
        print_kdrama()
        continue
    elif choice == 's':
        code = input("Please input the code of the kdrama ---> ")
        Search(keys)
    else:
        print("invalid choice")
        continue
