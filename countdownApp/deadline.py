import datetime

user_input = input("Enter your goal and deadline separated by colon! \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
print(deadline_date)

todays_date = datetime.datetime.today()
remaining_time = deadline_date - todays_date
print(remaining_time)

hours_till = int(remaining_time.total_seconds()/ 60 /60)
print (f"Dear user! Time remaining for your goal: {goal} is {hours_till} hours ")
