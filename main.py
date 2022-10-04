print("Welcome to the Casino!\n")

print("How many chips would you like to buy tonight?")
wallet = float(input("Enter a dollar amount ($): "))
print()

while True:
    print("Available Games")
    print("1- Single Coin Slot Machine")

    print()
    choice = int(input("Enter the number coorspoinding to the game you would like to play:"))

    if choice == 1:
        1