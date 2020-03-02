# MEXIKO
import random

# open/create mexiko log -> type in the results later
with open("Mexiko_log.txt", "a") as mexiko_log:
    mexiko_log.write("")

# Throw fnc
def throw(min=1, max=6):
    num1 = random.randint(min, max)
    num2 = random.randint(min, max)
    win_comb = ""
    if (num1 == 1 and num2 == 2):
        win_comb = "!!Mexiko!!"
    elif (num1 == 2 and num2 == 1):
        win_comb = "!!Mexiko!!"
    elif num1 >= num2:
        win_comb = str(num1) + str(num2)
    else:
        win_comb = str(num2) + str(num1)
    return win_comb

# New roll - single
def new_roll():
    x = "y"
    while x == "y" or x == "yes":
        print("Rolling...")
        print(throw() + "\n")
        x = input("New roll? ")
    while x == "no" or x == "n":
        print("End of the game.")
        break

#Game human vs computer + score counting
def versus():
    x = "y"
    human_score = 0
    computer_score = 0
    while x == "y" or x == "yes":
        human_throw = throw()
        computer_throw = throw()
        print(f"Human throwing...\nRolling...\n{human_throw}\n")
        print(f"Computer's turn.\n{computer_throw}")
        if human_throw == "!!Mexiko!!" and computer_throw == "!!Mexiko!!":
            print("Mexiko tie!")
        elif human_throw == "!!Mexiko!!":
            print("Mexiko beats everything.")
            human_score = human_score + 1
        elif computer_throw == "!!Mexiko!!":
            print("Mexiko beats everything.")
            computer_score = computer_score + 1
        elif human_throw > computer_throw:
            human_score = human_score + 1
            print("Human won this round!")
        elif human_throw < computer_throw:
            computer_score = computer_score + 1
            print("Haha, computer won! Coincidence?")
        else:
            print("It's tie!\nHave an extra round.")
        print(f"Score is: {human_score} vs {computer_score}")
        x = input("\n\nNew roll? ")

    while x == "no" or x == "n":
        print("End of the game.")
        break

# Game start
def start():
    ready = input("Are you ready to play? (yes/no) ")
    if ready == "yes" or ready == "y":
        game_type = input("Do you want to play single throwing(1) or versus computer(2)? (1/2)")
        if game_type == "1":
            print(new_roll())
        else:
            print("Playing versus computer:\n")
            print(versus())
    if ready == "no" or ready == "n":
        print("Good bye.")

#START!
start()

#Writing and reading file
"""with open("mexiko_log.txt", "w") as mexiko_log:
    mexiko_log.write(f"Mexikos thrown:{mexiko_counter}")

with open("mexiko_log.txt") as mexiko_log:
    mexiko_log_content = mexiko_log.read()
print(mexiko_log_content)"""
