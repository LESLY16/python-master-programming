#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Here round function doesn't round the final tip to 2 decimal places
#hence format the result to 2 decimal places thus we get 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇
'''
: introduces the format spec
0 enables sign-aware zero-padding for numeric types
.2 sets the precision to 2
f displays the number as a fixed-point number
'''
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill in $?"))
percentage_tip = int(input("What percentage of tip would you like to give? 10, 12 or 15?"))
modified_percentage_tip = percentage_tip/100
persons_to_split = int(input("How many persons to split the bill?"))
tip_by_each_person = total_bill/persons_to_split *(1+modified_percentage_tip)
#final_tip_by_each_person = round(tip_by_each_person,2)
final_tip_by_each_person = "{:.2F}".format(tip_by_each_person)
print(f"Each person should pay ${final_tip_by_each_person}")

# FAQ: How to round to 2 decimal places in python?
# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048
