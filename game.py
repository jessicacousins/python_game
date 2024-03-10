import random
import sys

print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("\nWelcome to the Heads or Tails game!")

user = input("Choose Heads (H) or Tails (T) then press enter:\n").strip().upper()

if user not in ['H', 'T']:
    sys.exit("🚫 Invalid choice, please enter H for Heads or T for Tails!")

user_full = "Heads" if user == 'H' else "Tails"

outcome = random.choice(['H', 'T'])
outcome_full = "Heads" if outcome == 'H' else "Tails"


print(f"\nYour choice: {user_full}")
print(f"The coin flip is... {outcome_full}!")

print("")

if user == outcome:
    print("🥳 Congratulations! You won! 🎉 ")
else:
    print("💥 Sorry, you lost... \nTry again!🍀 💚")

print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")