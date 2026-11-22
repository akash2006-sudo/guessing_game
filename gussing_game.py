import random

wins = 0
losses = 0
play = "y"

while play == "y":
    print("---number guessing game---")
    print("1. Easy (1-50, 10 tries)")
    print("2. Medium (1-100, 7 tries)")
    print("3. Hard (1-200, 6 tries)")
    level = input("Choose 1, 2 or 3: ")

    if level == "1":
        max_number = 50
        max_tries = 10
    elif level == "2":
        max_number = 100
        max_tries = 7
    elif level == "3":
        max_number = 200
        max_tries = 6
    else:
        print("Invalid choice, using Medium")
        max_number = 100
        max_tries = 7

    secret = random.randint(1, max_number)
    tries = 0
    won = False

    while tries < max_tries:
        guess = int(input(f"Guess ({max_tries - tries} tries left): "))

        if guess < 1 or guess > max_number:
            print(f"Please guess between 1 and {max_number}")
            continue

        tries += 1

        if guess == secret:
            if tries == 1:
                print("Correct! You got it in 1 try.")
            else:
                print(f"Correct! You got it in {tries} tries!")
            wins += 1
            won = True
            break
        elif guess < secret:
            print("Too low")
        else:
            print("Too high")

    if not won:
        print(f"Out of tries! The number was {secret}.")
        losses += 1

    play = input("Play again? (y/n): ").lower()

print(f"Wins: {wins}, Losses: {losses}")
print("Thanks for playing!")