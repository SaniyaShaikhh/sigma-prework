from datetime import datetime
current_date = datetime.now()

user_input = input("Please enter date in the format dd-mm-yyyy: ")
user_input_date = datetime.strptime(user_input, "%d-%m-%Y")
year_diff = current_date.year - user_input_date.year

if current_date.month - user_input_date.month < -6:
    year_diff -= 1

print(f"Age is {year_diff} years")
