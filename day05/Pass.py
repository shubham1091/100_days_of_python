import random
letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z','a', 'b', 'c', 'd','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v','w', 'x', 'y', 'z']
number = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['~','!','@','#','$','%','^','&','*','(',')','<','>','/','?','-','_','+','=']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))

result = []
tot = num_letters+num_symbols+num_numbers
n=0
s=0
l=0
for i in range(0,tot):
    if l<num_letters:
        result.append(random.choice(letter))
        l+=1
    if s<num_symbols:
        result.append(random.choice(symbol))
        s+=1
    if n<num_numbers:
        result.append(random.choice(number))
        n+=1
random.shuffle(result)

pas = ""
for char in result:
    pas+=char

print(f"Your password is {pas}")