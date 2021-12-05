from bingo import BingoCard

input_file_name = "inputs_test.csv"
numbers_called = []
bingo_cards = []

# Load input data into memory
input_data = open(input_file_name).read().split("\n")
# Load called numbers
numbers_called = [int(x) for x in input_data[0].split(",")]
# Load all bingo cards
card_index = 2
while card_index < len(input_data):
    bingo_card_matrix = [list(filter(None,x.split(" "))) for x in input_data[card_index:card_index+5]]  
    bingo_card_matrix = [[int(y) for y in x] for x in bingo_card_matrix]
    bingo_cards.append(BingoCard(bingo_card_matrix))
    card_index += 6
# Remove input data from memory
input_data.clear()
input_data = None


# Part 1
winning_number = 0
unmarked_numbers = []

# Play until first card wins
for n in numbers_called:
    for bc in bingo_cards:
        bc.mark(n)
        if bc.bingo:
            unmarked_numbers = bc.get_unmarked_numbers()
            winning_number = n
            break
    if bc.bingo: 
        break

print("Part 1")
print("============================")
print(f"Winning number: {winning_number}")
print(f"Solution: {winning_number * sum(unmarked_numbers)}")

# Reset bingo cards
for x in bingo_cards:
    x.reset_card()

# Part 2
last_winning_card_index=0
winning_number=0
# Play all numbers keeping track of last winning card & winning number
for n in numbers_called:
    for i, bc in enumerate(bingo_cards):
        if not bc.bingo: #Only play cards that have not won
            bc.mark(n)
            if bc.bingo:
                last_winning_card_index = i
                winning_number = n

print("\nPart 2")
print("============================")
print(f"Last card to win: {last_winning_card_index + 1}")
print(f"Wining number: {winning_number}")
unmarked_numbers = bingo_cards[last_winning_card_index].get_unmarked_numbers()
print(f"Solution: {winning_number * sum(unmarked_numbers)}")

