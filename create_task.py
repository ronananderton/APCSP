import random
rolls = ["Double Points" , "2" , "3" , "4" ]

point_values = [ -200 , -200 , -200 , 200 , 200 , 200 ]

total_points = 500

r = 3
print("")
while r > 0:
    die_choice = input(f'''You have {total_points} points. There are two dice in front of you. The first is a basic 6-sided die. 
If you roll a 1, 2,or a 3, you will lose 200 points. If you roll a 4, 5, or a 6, you will You have {r} roll(s) left. (answer 1 / 2) \n''')

    if die_choice == "1":
        r1 = random.randint(0, 6)
        if r1 <= 3:
            total_points -= 200
            print(f"You rolled a {r1}. You lost 200 points.")
        else:
            total_points += 200
            print(f"You rolled a {r1}. You gained 200 points.")
    elif die_choice == "2":
        pass
    r -= 1
    print()