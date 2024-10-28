import game
import math
class Player:
    def __init__(self, letter):
        self.letter = letter

    def position(self, pos, game):
        pass

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def position(self, game):
        pos=game.random_choice()
        i,j=game.get_element_index(pos)
        game.playingbord[i][j]=self.letter
        print("The computer choose the  position  ",pos)

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def position(self, pos, game):
        if game.availibility(pos):
            i, j = game.get_element_index(pos)
            game.playingbord[i][j] = self.letter

class superplayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def position(self, game):
        if len(game.available_squares()) == 9:
            pos = game.random_choice()  # Randomly pick any available position
        else:
            best_move = self.minmax(game, self.letter)
            pos = best_move['position']  # Extract the best move from the result of minmax
        return pos  # Return the position to be used

    def minmax(self, game, letter):
        max_player = self.letter
        other_player = "X" if max_player == "O" else "O"

        # Base cases
        if game.check_winner() == other_player:
            return {'position': None, 'score': 1 * (len(game.available_squares()) + 1) if other_player == max_player else -1 * (len(game.available_squares()) + 1)}
        elif len(game.available_squares()) == 0:
            return {'position': None, 'score': 0}

        # Recursive case
        if letter == max_player:
            best = {'position': None, 'score': -math.inf}  # Maximize for max_player
        else:
            best = {'position': None, 'score': math.inf}   # Minimize for other_player

        for possible_move in game.available_squares():
            # Make a move
            game.make_move(possible_move, letter)
            sim_score = self.minmax(game, other_player)  # Simulate the game recursively
            game.playingbord[game.get_element_index(possible_move)[0]][game.get_element_index(possible_move)[1]] = possible_move  # Undo move
            
            sim_score['position'] = possible_move  # Store the move

            # Compare scores to find the best move
            if letter == max_player:  # Maximize score for max_player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:  # Minimize score for other_player
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best

        