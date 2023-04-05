"""
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
"""
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
year = 90
year_left = year -int(age)
days = year_left*365
month = year_left*12
weeks = year_left*52
print("You have",days,"days,",weeks,"weeks,","and",month,"months left.")
