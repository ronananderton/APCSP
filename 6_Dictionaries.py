
points = {
    'William': 0,
    'Ronan': 0,
    'Spencer': 0,
    'AJ': 0
}

def add_points(player, number):
    points[player] += number

def show_points(player):
    print(points[player])

def cheater(player):
    points[player] = 0
    print(f"{player} cheated.")

def end_game():
    
    for player, num_points in points.items():
        print(f"{player} has {num_points} points.")
    
    # max(points, key=lambda key: points[key])

    print(f"{max(points, key=points.get)} has won!")

add_points('Ronan', 5)

add_points('William', 8)
cheater('William')

add_points('Spencer', 4)

add_points('AJ', 12)

end_game()