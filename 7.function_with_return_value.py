hour_calculater =  24
unit = "hours"

def days_to_units(number_of_days):
    return f"{number_of_days} Days are {number_of_days * hour_calculater} {unit}" 


user_input = input("Hey User, enter number of days and I will conver it to hours ! \n")    
output = days_to_units(int(user_input))
print(output)


# Input() Always returns a string
