# Lists
# - To store multiple items in a single variable
# - A List can contain different data types

# For Loop
# · Is used for iterating over a sequence (like a list)
# - So we can execute smth for each item in a list

hour_calculater =  24
unit = "hours"

def days_to_units(number_of_days):
     return f"{number_of_days} Days are {number_of_days * hour_calculater} {unit}" 
  
def validate_and_execute():
   try:
        input_number = int(no_of_day_element)
        if input_number > 0:
            output = days_to_units(int(input_number))
            print(output)
        elif input_number == 0 :
            print("Invalid Input 0, please enter a correct value !! \n")
        else:
            print("You have entered a negative number, Please enter valid positive number \n")
   except:
        print(f"Your input is Invalid, Choose a number as input !!")


user_input = ""
while user_input != "exit":
    user_input = input("Hey User, enter number of days in comma searated list eg; and I will conver it to hours ! \n")
    for no_of_day_element in  user_input.split(","):
         validate_and_execute()
         
# String - split() 
# "10, 22, 50, 100" --> [10, 22, 50, 100]
# splits a string into a list 
# Default split is a space
# "10 22 50 100" --> [10, 22, 50, 100]