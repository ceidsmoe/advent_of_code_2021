class BingoCard:
    def __init__(self, numbers):
        self.numbers = numbers
        self.filled = []
        for _ in range(5):
            self.filled.append([0]*len(numbers))
        self.grid = {}
        for i in range(5):
            for j in range(5):
                self.grid[numbers[i][j]] = (i, j)
    
    def score(self, winning_num):
        retval = 0
        for i in range(5):
            for j in range(5):
                if self.filled[i][j] == 0:
                    retval += self.numbers[i][j]
        return retval * winning_num

    def setNumber(self, n):
        try:
            x, y = self.grid[n]
        except KeyError:
            return False
        self.filled[x][y] = 1

        i = 0
        while i < 5 and self.filled[i][y] == 1:
            i += 1
        if i == 5:
            return True
        
        j = 0
        while j < 5 and self.filled[x][j] == 1:
            j += 1
        if j == 5:
            return True
        
        return False


if __name__ == "__main__":
    with open("input") as f:
        numbers = list(map(lambda x: int(x), f.readline().rstrip().split(",")))
        
        bingo_cards = []

        line = f.readline()
        while line:
            if line == '\n':
                line = f.readline()
                continue
            else:
                card_numbers = []
                for _ in range(5):
                    card_numbers.append(list(map(lambda x: int(x), line.split())))
                    line = f.readline()
                bingo_cards.append(BingoCard(card_numbers))
        
        done = False
        for num in numbers:
            for i, card in enumerate(bingo_cards):
                done = card.setNumber(num)
                if done:
                    print(card.score(num))
                    break
            if done:
                break