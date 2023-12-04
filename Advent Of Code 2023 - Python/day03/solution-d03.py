"""
    Language : Python 🐍
    Project : Advent Of Code 2023 🎄
    Stage : day #3 / ⭐️ #1
    Brief : Find numbers that neighbour a symbol
    Author : Tomasz-Niewiadomski
    Date : Evening 03122023
"""
# Final version inspired by @keithstellyes as my first solution was terrible

import re

def get_data(path="day03-puzzle.txt"):
    with open(path, "r") as f:
        data = f.read()
        return list(filter(None, data.split("\n")))
    
rows = get_data()
num_pattern = re.compile('[0-9]+')
sym_pattern = re.compile(r'.*[\*' + r'@/=\-\$&\+#%]')


def sum_nums_with_symbol(rows = get_data()):
    i = total = 0
    n_rows = len(rows)
    
    while i < n_rows:
        row = rows[i]
        numbers = num_pattern.finditer(row) # Finds start & end index and value of matching pattern 
        for number in numbers: # Iterate through all numbers in row (groups of digits)
            found_symbol = False # Does number neighbour a symbol? 
            j_min = max(0, number.start() - 1) # Smallest admissible column index
            j_max = min(len(row) - 1, number.end() +1) # Biggest admissible column index
            number_value = int(number[0]) # Value of the matched pattern (number)
            if i > 0: 
                matches_above = sym_pattern.match(rows[i - 1][j_min:j_max]) # Find symbol in row above
                found_symbol = matches_above is not None
            if i < n_rows - 1 and not found_symbol:
                matches_below = sym_pattern.match(rows[i+1][j_min:j_max]) # Find symbol in row below
                found_symbol = matches_below is not None
            if not found_symbol:
                found_symbol = row[j_min] in '@*/=-$&+#%' or row[j_max -1] in '@*/=-$&+#%' # Find symbol in current row - edge cases
            if found_symbol:
                total += number_value
        i += 1

    return total

if __name__ == "__main__":
    print("We have managed to understand the engine schematic! ⚙️")
    print(f"The sum of all of the part numbers in the engine schematic is : {sum_nums_with_symbol()}")
