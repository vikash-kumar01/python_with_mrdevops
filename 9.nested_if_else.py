hour_calculater =  24
unit = "hours"

def days_to_units(number_of_days):
     return f"{number_of_days} Days are {number_of_days * hour_calculater} {unit}" 
  
def validate_and_execute():
    if user_input.isdigit():
        input_number = int(user_input)
        if input_number > 0:
            output = days_to_units(int(input_number))
            print(output)
        elif input_number == 0 :
            print("Invalid Input 0, please enter a correct value !! \n")
    else:
        print(f"Your input is Invalid, Choose a number as input !!")

user_input = input("Hey User, enter number of days and I will conver it to hours ! \n")  
validate_and_execute()