print("Welcome to the tip calculator!")
string_total_bill = input("What was the total bill?") #input data as, for example; $150.00
if "$" not in string_total_bill:
    print("You must append $ in front of total bill, now skip it. I have done it for you.")
string_total_bill = "$"+string_total_bill
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15?")) #input data as, for example; 12
total_members_to_split = input("How many people to split the bill?") #input data as, for example; 5
total_bill = string_total_bill[1:] #this is done to remove $ sign from total bill
actual_total_bill = round(float(total_bill), 2)
actual_total_members_to_split = int(total_members_to_split)
actual_percentage_tip = percentage_tip / 100
new_percentage = 1 + actual_percentage_tip
tip = (actual_total_bill / actual_total_members_to_split) * new_percentage
actual_tip = round(float(tip), 2)
print(f"Each person should pay ${actual_tip}")