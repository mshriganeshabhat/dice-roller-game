import random

print("🎲 gitWelcome to the Dice Rolling Simulator!")

while True:
    input("\nPress Enter to roll the dice...")
    dice = random.randint(1, 6)
    print(f"You rolled: {dice}")

    choice = input("Roll again? (yes/no): ").lower()

    if choice != "yes":
        print("👋 Thanks for playing!")
        break