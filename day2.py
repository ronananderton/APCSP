number_chosen = input("Pick a number 1-10\n")
num_siblings = input("How many siblings do you have?\n")

if int(number_chosen) >= 6:
    large_number = True
else:
    large_number = False

if int(num_siblings) >= 2:
    sibling = True
else:
    sibling = False

if large_number and sibling:
    print("You will die in a house fire")
elif not large_number and sibling:
    print("You are going to lose your job")
elif large_number and not sibling:
    print("You will end up alone")
else:
    print("Have you ever heard of Krunker.io?")