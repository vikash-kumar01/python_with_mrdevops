def days_to_units(number_of_days, unit):
    if unit == "hours":
       return f"{number_of_days} Days are {number_of_days * 24} {unit}" 
    elif unit == "seconds":
        return f"{number_of_days} Days are {number_of_days * 24 * 60 * 60} {unit}" 
    else:
        return "Unsupported Units !!"
  
def validate_and_execute(days_and_unit_dict):
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


input_message = "Hey User, enter number of days and conversion unit  ! \n"