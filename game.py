import random
class TickTacToe:
    
    def __init__(self):
        self.bord = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.playingbord = [row[:] for row in self.bord]  # Create a copy for gameplay

    def printbord(self):
        for row in self.playingbord:
            for element in row:
                print(element, end='|')
            print()  # New line at the end of each row

    def get_element_index(self, pos):
        for i, row in enumerate(self.bord):  # i is the row index
            if pos in row:
                j = row.index(pos)  # j is the column index
                return (i, j)  # Return as a tuple (i, j)
        return None  # Return None if the element is not found

    def availibility(self, pos):
        let1="x"
        let2="o"
        index = self.get_element_index(pos)
        if index is None:
            return False  # Position not found on the board
        i, j = index
        if self.playingbord[i][j] == let1.upper() or self.playingbord[i][j] == let2.upper():
            return False  # Position already taken
        return True
    def available_squares(self):
        availablesquares=[]
        for i in range(1,10):
            if self.availibility(i):
                availablesquares.append(i)
        return availablesquares
    def random_choice(self):
        pos=random.randint(1,9)
        while self.availibility(pos)==False:
            pos=random.randint(1,9)
        return pos
    def make_move(self,pos,letter):
        i, j = self.get_element_index(pos)
        self.playingbord[i][j] = letter
        
        
        
        
        pass
    def check_winner(self):
        
        # Check rows
        for row in self.playingbord:
            if row[0] == row[1] == row[2]:  # All elements in the row are the same
                return row[0]  # Return the winner ('x' or 'o')

        # Check columns
        for col in range(3):
            if self.playingbord[0][col] == self.playingbord[1][col] == self.playingbord[2][col]:
                return self.playingbord[0][col]

        # Check diagonals
        if self.playingbord[0][0] == self.playingbord[1][1] == self.playingbord[2][2]:
            return self.playingbord[0][0]
        if self.playingbord[0][2] == self.playingbord[1][1] == self.playingbord[2][0]:
            return self.playingbord[0][2]

        return None  # No winner yet

    
