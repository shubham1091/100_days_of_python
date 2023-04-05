"""
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.
"""
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
combined_string = name1+name2
lower_case_string = combined_string.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')

true_score = str(t+r+u+e)
love_score = str(l+o+v+e)

score = int(true_score+love_score)
if (score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40 and score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
