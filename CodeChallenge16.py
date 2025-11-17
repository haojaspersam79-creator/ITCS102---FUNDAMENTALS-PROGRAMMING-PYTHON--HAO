import os

os.system("cls")
print("STUDENT INFORMATION SYSTEM ")
print("----------------------------------------\n")

#empty dictionary
student_records = {}

while True:
    print("SELECT FROM THE OPTIONS BELOW \n A- Add Information\nB - Search a Record\nC - Delete a record\nD - Modify a record\nE - Exit")

    choice = input("Your choice             --> ").lower()

    if choice == 'a':
        print("ADDING STUDENT INFORMATION")
        print(" ------------------------------- ")
        search_code = input("Key search for this student --> ")
        
        first_name = input("Input Student First Name --> ").upper()
        last_name = input("Input Student Last Name --> ").upper()
        course = input("Input Student Course --> ").upper()
        age = input("Input Student Age --> ").upper()
        email = input("Input student email address --> ")

        student_records = {search_code : {first_name, last_name, course, age, email} }
        print("DATA SAVED!")

        os.system("cls")
        continue 

    elif choice == 'b':
        #os.system("cls")
        code = input("Input search code --> ")

        for j in student_records.keys():
            if code in student_records.keys():
                print("RECORD FOUND")
                print("Records: ")
                print(" ------------- ")
                
                for p in student_records[code]:
                    print(p)
            else:
                print("NO RECORD FOUND")
        continue
    elif choice == 'c':
        pass 
        continue
    elif choice == 'd':
        print("EDITING EXISTING RECORD")
        continue
    elif choice == 'e':
        print("System Exit")
        break