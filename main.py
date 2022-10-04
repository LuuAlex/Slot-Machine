import os
import games.single_coin_slot_machine


# Clears terminal screen
def clear():
    os.system('cls||clear')


# Prints amount of chips player has
def wallet_print():
    print("Chips:", wallet)


# Clears terminal and prints chips to reset after each round
def reset():
    clear()
    wallet_print()


print("Hello! Welcome to the Slot Machine Casino!\n")

print("How many chips would you like to buy tonight?")
wallet = float(input("Enter a dollar amount ($): "))
print()

while True:
    print("Available Games")
    print("1- Single Coin Slot Machine")

    print()
    choice = int(input("Enter the number coorspoinding to the game you would like to play: "))
    reset()

    if choice == 1:
        games.single_coin_slot_machine.play()

