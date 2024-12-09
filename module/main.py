# import helper

# user_input = ""
# while user_input != "exit":
#     day_hour_input = input("Hey User, enter number of days and conversion unit  ! \n")
#     days_and_unit =  day_hour_input.split(":")
#     print(days_and_unit)
#     days_and_unit_dict = {"days": days_and_unit[0], "units": days_and_unit[1]}
#     print(days_and_unit_dict)
#     helper.validate_and_execute(days_and_unit_dict)
    

# From the module import the function directly
from helper import validate_and_execute, input_message

user_input = ""
while user_input != "exit":
    day_hour_input = input(input_message)
    days_and_unit =  day_hour_input.split(":")
    print(days_and_unit)
    days_and_unit_dict = {"days": days_and_unit[0], "units": days_and_unit[1]}
    print(days_and_unit_dict)
    validate_and_execute(days_and_unit_dict)
    

# import helper as h
