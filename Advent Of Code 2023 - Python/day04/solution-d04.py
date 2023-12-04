"""
    Language : Python 🐍
    Project : Advent Of Code 2023 🎄
    Stage : day #4 / ⭐️ #1&2
    Brief : Solve scratch cards ♠️♥️♣️♦️
    Author : Tomasz-Niewiadomski
    Date : Evening 04122023
"""

def get_clean_data(path="day04-puzzle.txt"):
    with open(path, "r") as f:
        data = f.read()
        return list(filter(None, data.split("\n"))) # Split by newline, drop empty elements

# t1 & t2
def cards_net(data = get_clean_data()):
    rows = [row.split(":")[1] for row in data] # Drop the "Card 1:" prefix
    winning_rows = [row.split("|")[0].split() for row in rows] # Get left side of string
    players_rows = [row.split("|")[1].split() for row in rows] # Get right side of string

    card_counts = [1 for i in range(len(rows))] # Track number of cards (original + copies)

    i = points = 0
    while i < len(rows):
    
        winning_card = set(map(int, winning_rows[i]))
        players_card = set(map(int, players_rows[i]))

        winning_numbers = players_card.intersection(winning_card)
        if winning_numbers:
            i_max = min(len(rows), len(winning_numbers))
            for c in range(i, i + len(winning_numbers)): # Go through the number of matches        
                for _ in range(0, card_counts[i]): # As many times as # of copies of current card
                    card_counts[c+1] += 1 # Incerement future cards by a copy
            points += 2**(len(winning_numbers) - 1) # Each match after 1st doubles card's value 
        i+=1
    return points, sum(card_counts)

if __name__ == "__main__":
    print("Uff... the scratchcard winnings have been counted finally! ♠️♥️♣️♦️")
    print(f"In total, the pile of scratchcards is worth {cards_net()[0]} points 🤑")
    print(f"At last, we end up with {cards_net()[1]} scratchcards.")