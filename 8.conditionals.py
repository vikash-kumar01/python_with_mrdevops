# Conditionals
# Expressions that evaluate to either true or false
# • Equals: a b
# • Not Equals: a != b
# • Less than: a < b
# • Less than or equal to: a <= b
# • Greater than: a > b
# • Greater than or equal to: a >= b


hour_calculater =  24
unit = "hours"

# 1st Way ----------------------------------------------------

# def days_to_units(number_of_days):
#     #if (number_of_days > 0): This also works
#     if number_of_days > 0:
#      return f"{number_of_days} Days are {number_of_days * hour_calculater} {unit}" 
#     elif number_of_days == 0 :
#       return f"You have entered 0, Which is invalid here!"
#     else:
#       return "Invalid Input, please enter a correct value !! \n"

# user_input = input("Hey User, enter number of days and I will conver it to hours ! \n")    

# if user_input.isdigit():
#     output = days_to_units(int(user_input))
#     print(output)
# else:
#     print(f"Your input is Invalid, Choose a number as input !!")
    
    
    
# 2nd Way  ----------------------------------------------------


def days_to_units(number_of_days):
    #if (number_of_days > 0): This also works
    if number_of_days > 0:
     return f"{number_of_days} Days are {number_of_days * hour_calculater} {unit}" 
    elif number_of_days == 0 :
      return f"You have entered 0, Which is invalid here!"
    else:
      return "Invalid Input, please enter a correct value !! \n"
  
def validate_and_execute():
    if user_input.isdigit():
        output = days_to_units(int(user_input))
        print(output)
    else:
        print(f"Your input is Invalid, Choose a number as input !!")

user_input = input("Hey User, enter number of days and I will conver it to hours ! \n")  
validate_and_execute()

# Here user_input variable is global so no need to pass as args  
