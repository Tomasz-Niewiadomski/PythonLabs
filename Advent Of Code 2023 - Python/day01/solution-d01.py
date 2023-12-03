"""
    Language : Python 🐍
    Project : Advent Of Code 2023 🎄
    Stage : day #1 / ⭐️ #1
    Brief : Find net value from corrupted instructions
    Author : blue-neptune8
    Date : Noon 01122023
"""

import re # Standard regex library

word_to_num = {'one': '1',
               'two': '2',
               'three': '3',
               'four': '4',
               'five': '5',
               'six': '6',
               'seven': '7',
               'eight': '8',
               'nine': '9'}

pattern1 = r"\d"                                                # Regex pattern for subtask 1: grab digits
pattern2 = r"\d|one|two|three|four|five|six|seven|eight|nine"   # Regex patter for subtask 2: grab digits or 'one','two',...




def get_clean_data(path="day01-puzzle.txt"):
    with open(path, "r") as f:
        data = f.read()
        return list(filter(None, data.split("\n"))) # Split by newline, drop empty elements (data can end with '/n')


def get_net_calibration_values(data = get_clean_data()):
    
    denoised_data = [re.findall(pattern2, line) for line in data] # Get data matching pattern
    numeric_data = [''.join(
                            [word_to_num[item] if item in word_to_num else item for item in line]) # Turn to corresp. num. if item is a word, keep otherwise
                    for line in denoised_data]
    calibration_values = list(map(int, list(map(lambda x: x[0] + x[-1] , numeric_data)))) # Concat 1st and last digit

    return sum(calibration_values)

if __name__ == "__main__":
    print("We have managed to recover the calibration document! 🎄")
    print("I can be safely loaded into a trebuchet now ⛄️")
    print(f"Net calibration values are: {get_net_calibration_values()}")
