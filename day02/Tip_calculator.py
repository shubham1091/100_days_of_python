#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
amount = float(input("Enter the bill amount: "))
people = int(input("number of people in the group: "))
contribute = amount/people*1.12
print("Your total bill was",amount,"$\nsplit between",people,"people\nso each person nead's to pay",round(contribute,2),"$ at 12% tip ")