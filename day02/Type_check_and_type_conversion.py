num_char = len(input("What is your name? "))

# print("Your name has "+num_char+" characters") this will gives you error
#TypeError: can only concatenate str (not "int") to str

print(type(num_char))

# to convert this into string
new_num_char = str(num_char)
print("Your name has "+new_num_char+" characters")

# we can also convert into int , float etc...