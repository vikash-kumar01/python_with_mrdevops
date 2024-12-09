# Functions 197
# - A function is defined using the def keyword
# - Block of code which only runs when it is called


second_converter =  24 * 60 * 60
unit = "seconds"

def days_to_second_converter():
    print(f"20 Days are {20 * second_converter} {unit}") 
    
days_to_second_converter()


print("--------------------------------------------------------------")

# Function with Parameter

def days_to_second_converter(number_of_days):
    print(f"{number_of_days} Days are {number_of_days * second_converter} {unit}") 
    
days_to_second_converter(20)
days_to_second_converter(35)
days_to_second_converter(50)
days_to_second_converter(110)


