print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill? "))
float_percentage = percentage / 100 + 1
result = total_bill * float_percentage / people
formatted_result = "{:.2f}".format(result)
print(f"Each person should pay: ${formatted_result}")
