class BingoNumber(object):
    def __init__(self,number:int):
        self.number:int = number
        self.marked:bool = False
    

class BingoCard(object):
    def __init__(self,numbers):
        self.numbers = [
            [
                BingoNumber(y) for y in x
            ] for x in numbers
        ]
        self.numbers_marked:int = 0
        self.bingo:bool = False

    def mark(self,number):
        self.numbers_marked += 1
        
        for row_index, row in enumerate(self.numbers):
            for col_index, n in enumerate(row):
                if  n.number == number:
                    n.marked = True
                    # After 5 marks, start checking for bingo winner and not already a winner
                    if self.numbers_marked >= 5 and not self.bingo:
                        self.bingo = self.check_row(row_index)
                        if self.bingo:
                            break
                        self.bingo = self.check_col(col_index)
                        if self.bingo:
                            break
            if self.bingo:
                break

    def get_unmarked_numbers(self):
        unmarked_numbers = []
        temp = [[
            y.number for y in x if not y.marked
        ] for x in self.numbers]
        for x in temp:
            for y in x:
                unmarked_numbers.append(y)
        
        return unmarked_numbers

    def check_row(self, row_index):
        return len([x for x in self.numbers[row_index] if x.marked]) == len(self.numbers[row_index])

    def check_col(self,col_index):
        col = self.get_col(col_index)
        return len([x for x in col if x.marked]) == len(col)

    def get_col(self, col_index):
        return [x[col_index] for x in self.numbers]

    def reset_card(self):
        self.bingo = False
        self.numbers_marked = 0
        for x in self.numbers:
            for y in x:
                y.marked = False
