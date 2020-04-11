import re
#------ Global Variable -----
# Game board 
board =["-","-","-",
        "-","-","-",
        "-","-","-"]
# if game is dtill goimg 
game_still_going =True
# who won or Tie
winner = None
#Players 
player_1="x"
player_2="o"
current_player=player_1

def display_board():
  print(board[0]+"|"+board[1]+"|"+board[2])
  print(board[3]+"|"+board[4]+"|"+board[5])
  print(board[6]+"|"+board[7]+"|"+board[8])


def main():
  #test if the game still going
  while game_still_going:
     # Display initial board 
    display_board()
    #handel a singele turm of an arbitary player 
    handel_tun(current_player)
    #check if the game has ended 
    check_if_game_over()
    #Flip to the other player 
    flip_player()

def check_number(position):
  global current_player
  print("Please Enter a Number:")
  position = input("It's %s Turn: Choose a position von 1-9: "%(current_player))
  return position

def check_space(position):
  global current_player
  print("Position is not empty!")
  position = input("It's %s Turn: Choose a position von 1-9: "%(current_player))
  return position

# handel the turn 
def handel_tun(player):
  global player_1
  global current_player

  position = input("It's %s Turn: Choose a position von 1-9: "%(current_player))
  
  while re.fullmatch('[1-9]',position)==None:
    position=check_number(position,current_player)

  while board[position] !='-':
    position = check_space(position) 

  #We have to subtract one to fit the array index
  if player==player_1:
    board[int(position)-1]="x"
  else:
    board[int(position)-1]="o"
  

def check_if_game_over():
  global winner
  check_for_winner()
  if winner == None:
    check_if_tie()

def check_for_winner():
  #set up global Variable
  global winner,current_player,game_still_going
  # check Row 
  is_row= check_rows()
  # check colom 
  is_column=check_columns()
  # check digonal 
  is_diagonal=check_diagonal()
  if is_row or is_column or is_diagonal:
    winner=current_player
    game_still_going=False
    display_board()
    print("Congratulations: %s won"%(current_player)) 
  

def check_rows():
  #check if any rows have all the same value 
  if board[0]==board[1]==board[2] and board[0]!='-':
    return True
  if board[3]==board[4]==board[5] and board[3] != '-':
    return True
  if board[6]==board[7]==board[8] and board[6] != '-':
    return True
  
  return False
  
def check_columns():
 #check if any columns have all the same value 
  if board[0]==board[3]==board[6] and board[0]!='-':
    return True
  if board[1]==board[4]==board[7] and board[1] != '-':
    return True
  if board[2]==board[5]==board[8] and board[2] != '-':
    return True
  return False
 
def check_diagonal():
  if board[0]==board[4]==board[8] and board[0]!='-':
    return True
  if board[2]==board[4]==board[6] and board[2] != '-':
    return True
  return False

def check_if_tie():
  global board,game_still_going
  if '-' not in board:
    game_still_going=False
    print("It's a Tie, Game Over!")

def flip_player():
  global current_player, player_1,player_2
  if current_player==player_1:
    current_player=player_2
  else:
    current_player=player_1

if __name__=="__main__":
  main()