############ COMMAND LINE ARGUMENTS ###############################
# import sys

# def add(num1, num2):
#    return num1 + num2

# def sub(num1, num2):
#    return num1 -  num2

# def mul(num1, num2):
#    return num1 * num2

# num1 = float(sys.argv[1])
# oper = sys.argv[2]
# num2 = float(sys.argv[3])

# if  oper == 'add':
#      output =  add(num1, num2)
#      print(f"Addition of {num1} and {num2} is {output}")
# elif oper == 'sub':
#      output = sub(num1, num2)
#      print(f"Substraction of {num1} and {num2} is {output}")
# elif oper == 'mul':
#      output = mul(num1, num2)
#      print(f"Multiplication of {num1} and {num2} is {output}")
# else:
#    print("Invalid operation !! \n")
   
   
##################### ENVIRONMENT VARIABLES ############################### 

import os

password = os.getenv('DBPASS')
print(password)

# How to run in Windows Powershell??
#--------------------------------------------
# PS D:\Python> $env:DBPASS = "imvikash123"
# PS D:\Python> python3 .\cmd_args_and_env_vars.py
# imvikash123

# How to run in Linux ??
#--------------------------------------------
# PS D:\Python> export DBPASS="imvikash123"
# PS D:\Python> python3 .\cmd_args_and_env_vars.py
# imvikash123