import game
import player

# Create a new game instance
tic_tac_toe = game.TickTacToe()

# Get player symbols
letter1 = input("Player 1: Choose your letter (X or O): ").upper()
letter2 = 'O' if letter1 == 'X' else 'X'

# Initialize players
player1 = player.HumanPlayer(letter1)
player2 = player.HumanPlayer(letter2)
#player2=player.ComputerPlayer(letter2)
#player1 = player.superplayer(letter1)
#player2 = player.superplayer(letter2)

# Game loop

"""current_player = player2  # Player 1 starts the game
while tic_tac_toe.check_winner() is None and len(tic_tac_toe.available_squares()) > 0:
    tic_tac_toe.printbord()
    
    # Current player makes a move
    if isinstance(current_player, player.superplayer):
        move = current_player.position(tic_tac_toe)
        i, j = tic_tac_toe.get_element_index(move)
        tic_tac_toe.playingbord[i][j] = current_player.letter
        print(f"{current_player.letter} moves to position {move}")

    # Check if there is a winner after the move
    if tic_tac_toe.check_winner() is not None:
        break

    # Switch player turn
    current_player = player1 if current_player == player2 else player2

# Announce the result
winner = tic_tac_toe.check_winner()
tic_tac_toe.printbord()
if winner:
    print(f"The winner is: {winner}!")
else:
    print("It's a draw!")
    """
# Game loop
while tic_tac_toe.check_winner() is None:
    tic_tac_toe.printbord()
   
    # Player 1's turn
    pos1 = int(input(f"Player 1 ({player1.letter}), choose a position: "))
    if tic_tac_toe.availibility(pos1):
        player1.position(pos1, tic_tac_toe)
    else:
        print("Position already taken or invalid, try again!")

    # Check if player 1 won
    if tic_tac_toe.check_winner():
        break

    # Player 2's turn
    pos2 = int(input(f"Player 2 ({player2.letter}), choose a position: "))
    if tic_tac_toe.availibility(pos2):
        player2.position(pos2, tic_tac_toe)
    else:
        print("Position already taken or invalid, try again!")
    #computer player
    #player2.position(tic_tac_toe)
# Announce winner
winner = tic_tac_toe.check_winner()
if winner:
    print(f"The winner is: {winner}!")
else:
    print("It's a draw!")

        
    
    
    
    
