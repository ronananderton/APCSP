import random
die_2_rolls = ["Double Points" , "Gain Two Rolls" , "Lose half points" , "Lose all points" ]

total_points = 1000

r = 3
print("Welcome to the dice game!")
while r > 0 and total_points >= 0:
    die_choice = input(f'''You have {total_points} points. There are two dice in front of you. The first 
is a basic 6-sided die. If you roll a 1, 2,or a 3, you will lose 200 points. If you roll a 4, 5, or a 6, 
you will gain 200 points. You have {r} roll(s) left. (answer 1 / 2) \n''')

    if die_choice == "1":
        r1 = random.randint(0, 6)
        if r1 <= 3:
            total_points -= 200
            print(f"You rolled a {r1}. You lost 200 points.")
        else:
            total_points += 200
            print(f"You rolled a {r1}. You gained 200 points.")
    elif die_choice == "2":
        r2 = random.choice(die_2_rolls)
        if r2 == "Double Points":
            total_points += total_points
        elif r2 == "Gain Two Rolls":
            r += 2
        elif r2 == "Lose half points":
            total_points = total_points/2
        elif 

        pass
    r -= 1
    print()
if total_points >= 1000:
    print("You Win!")
elif total_points <= 0:
    print("You lost all your points. You lose.")
else:
    print("You did not gain 1000 points. You lose.")