import random
print('''
⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀
⠀⢀⣠⢋⡀⠔⠀⠉⠲⢤⢤⡀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⠀⣸⠀⠀⠀⠀
⡞⠁⠈⠀⠀⠀⠀⢠⠤⠌⣇⢱⢸⠉⠉⢳⠀⠀⡠⠋⠀⠀⡔⡡⠔⠒⠲⡄
⡸⠒⠤⠀⠀⠀⠠⠴⢒⣂⢸⢸⠀⢧⠀⠀⡧⠊⠀⠀⢀⠞⠉⠀⠀⣀⠴⠃
⢧⡀⠀⠀⠀⠀⠀⠈⠉⢀⠞⠋⠀⠸⠀⠀⠀⠀⠀⠠⠃⠀⢀⣤⠮⠥⠤⢤
⠀⠙⢍⣁⣀⣀⣀⠤⠖⠁⠀⠀⠠⢇⢀⡴⠂⣠⠀⠀⠀⠠⠋⠀⢀⡠⠴⠚
⠀⠀⢀⡤⣄⡤⠴⠒⡲⠤⡀⠀⢰⡘⣌⠐⣊⠤⠀⠀⠀⢀⠴⠊⠁⠀⠀⠀
⠀⢠⢋⡞⣁⡀⠀⠀⠘⢤⣘⡄⠀⠑⢌⣳⠤⠤⠤⠴⠚⠁⠀⠀⠀⠀⠀⠀
⠀⡇⡜⢐⠦⣈⡀⠀⠀⠀⠀⠈⠉⠉⠉⠒⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠉⢣⠈⠓⠀⠁⠀⠀⠐⠂⠠⢤⡤⠤⢄⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠳⣄⠀⠀⠀⠀⣀⡀⠀⠀⠉⠲⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠒⠤⠔⠒⠉⠑⠢⢄⡀⢨⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
choice = input("What do you choose?\nType 0 for Rock\nType 1 for Paper\nType 2 for Scissors\n")

usr_choose = int(choice)
pc_choose = random.randint(0, len(options)-1)

if usr_choose < 0 or usr_choose > len(options):
    print("You typed an invalid number, You loose!")
    exit()

print(f"You choose:\n {options[usr_choose]}")
print(f"Computer choose:\n {options[pc_choose]}")

if usr_choose == 0:
    if pc_choose == usr_choose:
        print("Game Draw")
    elif pc_choose == 1:
        print("You loose!")
    else:
        print("You win!")
elif usr_choose == 1:
    if pc_choose == usr_choose:
        print("Game Draw")
    elif pc_choose == 2:
        print("You loose!")
    else:
        print("You win!")
else:
    if pc_choose == usr_choose:
        print("Game Draw")
    elif pc_choose == 0:
        print("You loose!")
    else:
        print("You win!")
