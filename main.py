# Dice Simulator Small Project...
import random

total_score = 0
face_occurrences = [0] * 6  # To store the occurrences of each face
roll_history = []

print("Welcome in Dice Rolling Game...")
choice = input("Roll The Dice By Clicking on The 'y' Button (y/n): ")
while(choice.lower() == 'y'):
    num = random.randint(1,6)
    face_occurrences[num - 1] += 1  # Update face occurrences
    total_score += num  # Update total score
    roll_history.append(num)  # Add the roll to the history

    if num == 1:
        print("-")
        print(" ")
        print("0")
        print(" ")
        print("-")

    elif num == 2:
        print("--")
        print("  ")
        print("00")
        print("  ")
        print("--")

    elif num == 3:
        print("---")
        print("   ")
        print("000")
        print("   ")
        print("---")

    elif num == 4:
        print("----")
        print("    ")
        print("0000")
        print("    ")
        print("----")

    elif num == 5:
        print("-----")
        print("     ")
        print("00000")
        print("     ")
        print("-----")

    else:
        print("------")
        print("      ")
        print("000000")
        print("      ")
        print("------")

    choice = input("Roll The Dice By Clicking on The 'y' Button (y/n): ")

    if choice.lower() == 't':
        print(f"Total Score: {total_score}")
        print("Face Occurances:", face_occurrences)
        print("Total Score:", roll_history)

    if choice.lower() == 'n':
        break

print("Exiting the Dice Rolling Game...")








