import random

die_2_rolls = ["Double Points" , "Gain A Roll" , "Gain 500 Points" , "Lose All Points" ]
r = 5

def run_dice_game(r):
    total_points = 500
    
    while r > 0 and total_points >= 0 and total_points < 1200:
        die_choice = input(f'''You have {total_points} points.  You have {r} roll(s) left. Choose your die. (answer 1 or 2) \n''')

        if die_choice == "1":
            print("You chose the first die.")
            r1 = random.randint(0, 6)
            if r1 <= 3:
                total_points -= 200
                print(f"You rolled a {r1}. You lost 200 points.")
            else:
                total_points += 200
                print(f"You rolled a {r1}. You gained 200 points.")
        elif die_choice == "2":
            print("You chose the second die.")
            r2 = random.choice(die_2_rolls)
            if r2 == "Double Points":
                total_points *= 2
                print("You doubled your points!")
            elif r2 == "Gain A Roll":
                r += 2
                print("You gained a roll.")
            elif r2 == "Gain 500 Points":
                total_points += 500
                print("You gained 500 points.")
            elif r2 == "Lose All Points":
                total_points = 0
                print("You lost all of your points.")
        else:
            print("Please select '1' or '2'")
            r += 1

        r -= 1
    
    return total_points

print('''Welcome to the dice game! There are two dice in front of you. The first 
is a basic 6-sided die. If you roll a 1, 2, or a 3, you will lose 200 points. If you roll a 4, 5, or a 6, 
you will gain 200 points. The second is a special four-sided die. This die will result in doublng your 
points, gaining a roll, gaining 500 points, or losing all of your points. Your goal is to obtain 1,200 points. 
You lose if your points go below 0 or if you did not reach the goal. ''')

ending_points = run_dice_game(r)
print()

if ending_points >= 1200:
    print("You Win!")
elif ending_points <= 0:
    print("You lost all your points. You lose.")
else:
    print("You did not gain 1200 points. You lose.")