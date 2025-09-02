import random
# ● ┌ ─ ┐ │ └ ┘
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │", 
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"),    
}
dice = []
total = 0
num_dice = int(input("How many dices do you want? "))
for die in range(num_dice):
    dice.append(random.randint(1, 6))
    
arts = [dice_art[val] for val in dice]
for line in zip(*arts):
    print("   ".join(line))
      
total = sum(dice)
print(f"Your rolled: {dice}")
print(f"Total: {total}")