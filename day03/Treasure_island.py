print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣄⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⠀⠀⠹⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣴⠾⠛⠉⠉⠉⠀⠀⠀⠀⠀⠉⠉⠉⠛⠷⣶⣼⣿⣉⣁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡾⠛⠉⠛⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡏⠉⠙⠛⢶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣧⠀⠀⠀⠀
⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠈⢿⡇⠀⠀⠀
⠀⠀⠹⣿⡎⠀⠀⠀⣠⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⢻⡆⠀⠀⣆⣿⡇⠀⠀⠀
⠀⠀⠀⣿⡀⠀⡀⠀⣿⠁⠀⢠⣾⣿⡿⠆⠀⠀⠀⠀⠀⠀⢀⣾⣿⡿⠆⠀⠀⠀⢈⣿⠀⣄⣾⡿⠁⠀⠀⠀
⠀⠀⠀⠘⣿⣧⣇⢀⣇⠀⠀⠘⣿⣿⣷⡆⠀⠀⠀⠀⠀⠀⠈⢿⣿⣷⠖⠀⠀⠀⢸⣿⣷⠿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠙⠻⣿⣆⡀⠀⠀⠉⠉⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣸⣿⠁⣀⣀⣀⠀⠀⠀⠀
⠀⢀⣠⡶⠾⠛⠓⠶⣿⡟⠀⠀⠀⠀⠀⠀⠠⣾⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠟⠋⠉⠛⠻⣦⡀⠀
⢀⣾⠋⠀⠀⠀⠀⠀⠘⣿⣠⣄⡀⠀⠀⠀⠀⠛⠿⠟⠁⠀⠀⠀⠀⠀⡀⡀⠀⣴⣾⡏⠀⠀⠀⠀⠀⠈⣿⡄
⢸⣯⠀⢠⠀⠀⢀⣄⣠⣿⠿⢿⣷⣤⣦⣀⣤⣤⣤⣤⣀⣀⣀⣼⣆⣼⣷⣿⡾⠿⢿⣧⣀⣦⠀⠀⣤⠀⣸⡧
⠘⠿⣷⣾⣷⣤⠾⠿⠛⠁⠀⠀⠀⠁⠀⠉⠉⠀⠀⠀⠈⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠉⠛⠻⠷⠾⠿⠟⠛⠁\n''')

print("Welcome to Max and Rufus' Treasure Hunt!\nYou are Max, a young boy on a treasure hunt with your loyal dog Rufus.\nYour adventure starts in front of a dark and mysterious forest.\nYou have two choices:")

print("1. Take the well-lit path\n2. Take the dark and overgrown path\n")

choice = input("Which path do you want to take: 1 or 2=> ")

if choice == "1":
    print("\033[H\033[J")
    print("you emerge on the other side of the forest and find a small wooden box with a map inside.\nThe map leads you to an old abandoned mansion on the outskirts of town.\nYou have two choices:")
    print("1. Enter through the front door\n2. Sneak in through a window")

    choice = input("Which path do you want to take: 1 or 2=> ")
    if choice == "1":
        print("\033[H\033[J")
        print("you find yourself in a room filled with valuable antiques and artifacts.\nYou pick up a golden scepter and examine it closely.\nSuddenly, the door slams shut and you hear a sinister laugh.\nYou are trapped! Game Over.")
    else:
        print("\033[H\033[J")
        print("you find yourself in a dusty old storage room. \nYou notice a faint scratching sound coming from one of the walls. \nYou investigate and find a hidden compartment containing a piece of parchment with a cryptic riddle on it. \nYou solve the riddle and find a key that leads you to the treasure. \nCongratulations, you win!")
else:
    print("\033[H\033[J")
    print(" in the first decision, you find yourself lost in the dark and overgrown forest.\nRufus leads you in a direction, but you soon realize you're going in circles. \nYou have two choices:")
    print("1. Keep following Rufus\n2. Strike out on your own")
    choice = input("Which path do you want to take: 1 or 2")
    if choice == "1":
        print("\033[H\033[J")

        print("you eventually stumble upon a clearing with a small pond. \nRufus jumps in and starts splashing around, but suddenly disappears beneath the surface. \nYou dive in to save him, but the water is murky and you can't find him.\n Game Over.")
    else:
        print("\033[H\033[J")

        print("you eventually find your way out of the forest and onto a beach. \nYou see a shipwreck in the distance and decide to investigate. \nYou have two choices:")
        print("1. Climb aboard the shipwreck\n2. Search the beach for clues")
        choice = input("Which path do you want to take: 1 or 2=> ")
        if choice == "1":
            print("\033[H\033[J")

            print(
                "you climb aboard the shipwreck and find a locked chest. \nYou have two choices:")
            print("1. Try to pick the lock\n2. Smash the shest open")
            choice = input("Which path do you want to take: 1 or 2=> ")
            if choice == "1":
                print("\033[H\033[J")

                print(
                    " you successfully pick the lock and find a treasure map inside. \nCongratulations, you win!")
            else:
                print("\033[H\033[J")

                print(" you smash the chest open and find a cursed amulet. \nThe amulet gives you the power to control the winds, but at a terrible cost.\n You become a slave to the amulet and are cursed to roam the seas forever. \nGame Over.")
        else:
            print("\033[H\033[J")

            print("you search the beach for clues and find an old bottle with a message inside. \nThe message contains a riddle that leads you to a hidden cave. \nYou have two choices:")
            print(
                "1. Explore the cave\n2. Leave the area and cotinue your search elsewhere")
            choice = input("Which path do you want to take: 1 or 2=> ")
            if choice == "1":
                print("\033[H\033[J")

                print(
                    "you explore the cave and find a chest filled with gold coins and precious jewels.\nCongratulations, you win!")
            else:
                print("\033[H\033[J")

                print("you leave the area and eventually stumble upon a small village.\nYou hear rumors of a treasure hidden in a nearby castle.\nYou have two choices:")
                print("1.Sneak into the castle\n2.Ask the villagers for help")
                choice = input("Which path do you want to take: 1 or 2=> ")
                if choice == "1":
                    print("\033[H\033[J")

                    print("you sneak into the castle and find a room filled with treasure.\nYou start to fill your pockets when you hear footsteps approaching.\nYou have two choices:")
                    print("1.Hide in the shadows\n2. Confront the intruder")
                    choice = input("Which path do you want to take: 1 or 2=> ")
                    if choice == "1":
                        print("\033[H\033[J")

                        print(
                            "you hide in the shadows and avoid getting caught.\nCongratulations, you win!")
                    else:
                        print("\033[H\033[J")
                        print(
                            "you confront the intruder and find out it's the castle's owner.\nYou are arrested and thrown into the dungeon.\nGame Over.")
                else:
                    print("\033[H\033[J")
                    print("they tell you that the castle is guarded by a ferocious dragon. \nThey suggest that you find a way to distract the dragon before entering the castle. \nYou have two choices:")
                    print(
                        "1.Find a nearby animal to use as bait\n2. Creat a diversion with fireworks")
                    choice = input("Which path do you want to take: 1 or 2=> ")
                    if choice == "1":
                        print("\033[H\033[J")
                        print("you find a nearby sheep and use it as bait to distract the dragon.\nYou sneak past the dragon and find the treasure in the castle.\nCongratulations, you win!")
                    else:
                        print("\033[H\033[J")
                        print("you create a diversion with fireworks and successfully distract the dragon.\nYou enter the castle and find the treasure.\nHowever, as you leave the castle, you realize that the fireworks have also attracted the attention of a nearby army.\nYou are caught and the treasure is taken from you.\nGame Over.")
