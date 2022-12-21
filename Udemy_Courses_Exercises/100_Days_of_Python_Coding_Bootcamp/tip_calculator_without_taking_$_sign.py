#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇
print("Welcome to the tip calculator")
total_bill = input("What was the total bill in $?")
modified_total_bill = float(total_bill)
percentage_tip = input("What percentage of tip would you like to give? 10, 12 or 15?")
int_percentage_tip = int(percentage_tip)/100
persons_to_split = input("How many persons to split the bill?")
int_persons_to_split = int(persons_to_split)
tip_by_each_person = modified_total_bill/int_persons_to_split *(1+int_percentage_tip)
modified_tip_by_each_person = round(float(tip_by_each_person),2)
print(f"Each person should pay ${modified_tip_by_each_person}")