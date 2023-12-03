"""
    Language : Python 🐍
    Project : Advent Of Code 2023 🎄
    Stage : day #2 / ⭐️ #1
    Task : Cube Conundrum
    Brief : Possible colored cubes games 
    Author : blue-neptune8
    Date : Noon 01122023
"""

import re # Standard regex library

regex_num = r"\b\d{0,1}\b" # Finds any 1/2-digit integer number
regex_color = r"red|green|blue"
bag_limits = {'red':12, 'green': 13, 'blue': 14}


def get_clean_data(path="day02-puzzle.txt"):
    with open(path, "r") as f:
        data = f.read()
        return list(filter(None, data.split("\n"))) # Split by newline, drop empty elements
    
# t1
def get_possible_games(data = get_clean_data()):
    
    games = [line.split(":")[1] for line in data]
    sets = [set.split(";") for set in games]

    colors_in_sets = [[re.findall(r"red|green|blue", set) for set in game_set] 
                      for game_set in sets]
    counts_in_sets = [[re.findall(r"\b\d{1,2}\b", set) for set in game_set] 
                      for game_set in sets]

    
    feasible_indices = []
    for g in range(len(games)): # Iterate through all games
        feasibility_tests = [] # Stores feasibility of every set in a game
        for s in range(len(sets[g])): # Iterate through all sets
            feasibility_test = [bag_limits[colors_in_sets[g][s][i]] >= int(counts_in_sets[g][s][i]) # Check if count within limit
                                for i in range(len(colors_in_sets[g][s]))] # For every draw in a set
            feasibility_tests.append(all(feasibility_test))

        if all(feasibility_tests): # Check if game is feasible
            feasible_indices.append(g + 1) # Games numbering from 1

    return feasible_indices

def get_sum_possible_games(feasible_indices = get_possible_games()):
    return sum(feasible_indices)

#t2
from functools import reduce

def get_power_of_sets(data = get_clean_data()):
    bag_limits = {'red':12, 'green': 13, 'blue': 14}
    games = [line.split(":")[1] for line in data]
    sets = [set.split(";") for set in games]

    colors_in_sets = [[re.findall(r"red|green|blue", set) for set in game_set] for game_set in sets]
    counts_in_sets = [[re.findall(r"\b\d{1,2}\b", set) for set in game_set] for game_set in sets]

    feasible_indices = []
    max_rgbs = []
    for g in range(len(games)):
        feasibility_tests = []
        max_rgb = [0, 0, 0]
        for s in range(len(sets[g])):

            feasibility_test = []


            for d in range(len(colors_in_sets[g][s])):
                count = int(counts_in_sets[g][s][d])
                color = colors_in_sets[g][s][d]
                color_map = {'red': 0, 'green': 1, 'blue': 2}

                feasibility_test.append(bag_limits[color] >= count)
                max_rgb[color_map[color]] = max(count,  max_rgb[color_map[color]])

            feasibility_tests.append(all(feasibility_test))
        max_rgbs.append(max_rgb)
        if all(feasibility_tests):
            feasible_indices.append(g + 1)
    return max_rgbs

def get_total_power(max_rgbs = get_power_of_sets()):
    return sum([reduce(lambda x, y: x * y, max_rgb) for max_rgb in max_rgbs])


    


if __name__ == "__main__":
    print("The Cube Conundrum on the Snow Island ❄️ has been solved! 🎄")
    print(f"The sum of the possible cube games is: {get_sum_possible_games()}")
    print(f"The total power of the set is: {get_total_power()}")

