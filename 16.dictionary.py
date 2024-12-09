# Dictionary 
# - Are used to store values in key:value pairs
# - Is a collection, which does not allow duplicate values

# Allow user to input:
# 1) number of days, e.g. 50
# 2) unit to convert to, e.g. hours

# "45:hours" --> ["45", "hours"]

hour_calculater =  24
unit = "hour"

def days_to_units(number_of_days, unit):
    if unit == "hours":
       return f"{number_of_days} Days are {number_of_days * 24} {unit}" 
    elif unit == "seconds":
        return f"{number_of_days} Days are {number_of_days * 24 * 60 * 60} {unit}" 
    else:
        return "Unsupported Units !!"
  
def validate_and_execute():
   try:
        days = int(days_and_unit_dict["days"])
        if days > 0:
            output = days_to_units(days, days_and_unit_dict["units"])
            print(output)
        elif days == 0 :
            print("Invalid Input 0, please enter a correct value !! \n")
        else:
            print("You have entered a negative number, Please enter valid positive number \n")
   except:
        print(f"Your input is Invalid, Choose a number as input !!")


user_input = ""
while user_input != "exit":
    user_input = input("Hey User, enter number of days and conversion unit  ! \n")
    days_and_unit =  user_input.split(":")
    print(days_and_unit)
    days_and_unit_dict = {"days": days_and_unit[0], "units": days_and_unit[1]}
    print(days_and_unit_dict)
    validate_and_execute()
 
 

# my_dict = {"days": 20, "hours": 20 * 24}
# print(my_dict["days"])