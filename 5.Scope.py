# Scope
# A variable is only available from inside the region it is created
# - Global Scope = variables available from within any scope
   
#-   Local Scope = variables created inside function
#   can only be used inside that function 

second_converter =  24 * 60 * 60
unit = "seconds"

def days_to_second_converter(number_of_days, custom_message):
    print(f"{number_of_days} Days are {number_of_days * second_converter} {unit}") 
    print(custom_message)
    
#days_to_second_converter(20, "Looks Good!!")



def scope_check(number_of_days):
    my_var = "Variable Inside Function !!"
    print(f"Global Variable : {unit}")
    print(f"Internal Variable: {number_of_days}")
    print(f"Internal Variable defined inside function : {my_var}")
    
scope_check(20)