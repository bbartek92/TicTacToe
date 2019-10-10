import AI as ai
import engine as en

def new_board():
	new_board = [[None for a in range(3)] for x in range(3)]
	return new_board


def None_to_space(row):
	row_data =[None for a in range(3)]
	for cell in range(len(row)):

		if row[cell] == None:
			row_data[cell] = ' '
		else:
			row_data[cell] = row[cell]
	return row_data

def render(board):
	print(' ' * 3,'1', '2', '3')
	print('  ','--'  * len(board))
	for i in range(len(board)):
		print(i+1, '|', *None_to_space(board[i]), '|')
	print('  ','--'  * len(board))


def choose_x_o():
	pass

def get_move():

	while True:
		try:

			x = int(input("What is your move's X co-ordinate?: "))
			y = int(input("What is your move's Y co-ordinate?: "))
			if (x >= 1 and x <= 3) and (y >= 1 and y <= 3):
				break
		except:
			print('Incorrect input.', '\n', 'Please try again.')

	return x, y


def make_move(board, move_coords, playing):
	internal_board = [[None for a in range(3)] for x in range(3)]
	for i in range(len(board)):
		for j in range(len(board[i])):
			internal_board[i][j] = board[i][j]

	x, y = (move_coords[0]-1), (move_coords[1]-1)
	internal_board[x][y] = playing
	return internal_board


def is_valid_move(board, move_coords):
	x, y = move_coords
	return board[x-1][y-1] == None

def get_make_vali_move(board, playing, player_type):
	count = 0
	while True and count < 5:
		move_coords = player_switch(board, playing, player_type)
		if is_valid_move(board, move_coords):
			break
		else:
			print('Invalide move, try again')
			count += 1
	new_board = make_move(board, move_coords, playing)
	return new_board

def player_switch(board, playing, player_type):
	if player_type == 'H':
		return get_move()
	if player_type == 'A':
		return ai.random_ai(board, playing)
	if player_type == 'AI':
		return ai.minmax_ai(board, playing)


def change_turn(playing):
	if playing == 'X':
		playing = 'O'
	else:
		playing = 'X'
	return playing


def get_winner_ai_test(board, playing_current):
	
	for player in [playing_current, ai.get_opponent(playing_current)]:

		for i in [0, 1, 2]:
			if board[i][0] == player and board[i][1] == player and board[i][2] == player:
				return player
		for j in [0, 1, 2]:
			if board[0][j] == player and board[1][j] == player and board[2][j] == player:
				return player
		if board[0][0] == player and board[1][1] == player and board[2][2] == player:
			return player
		if board[0][2] == player and board[1][1] == player and board[2][0] == player:
			return player
	return None

def get_winner(board, playing):
		for i in [0, 1, 2]:
			if board[i][0] == playing and board[i][1] == playing and board[i][2] == playing:
				return playing
		for j in [0, 1, 2]:
			if board[0][j] == playing and board[1][j] == playing and board[2][j] == playing:
				return playing
		if board[0][0] == playing and board[1][1] == playing and board[2][2] == playing:
			return playing
		if board[0][2] == playing and board[1][1] == playing and board[2][0] == playing:
			return playing
		else:
			return None

def is_board_free(board):
	count_free = 0
	for i in [0, 1, 2]:
		for j in [0, 1, 2]:
			if board[i][j] == None:
				count_free += 1
	return count_free != 0
		

def lets_play(play_board, playing, player_type, waiting):
	while en.is_board_free(play_board):
	
		#make move
		print("It's",playing,"move")
		new_1 = en.get_make_vali_move(play_board, playing, player_type)
		en.render(new_1)
		#check winner
		if en.get_winner(new_1, playing) == playing:
			print('Player {0} wins the game!'.format(playing))
			break
		if en.is_board_free(new_1) == False:
			print('Its a draw :( \nIt was a great fight^^')

		#prepare for next iteration
		#Change player
		playing = en.change_turn(playing)
		#swap boards
		play_board = new_1.copy()
		#swap players
		player_type, waiting = waiting, player_type


if __name__ == '__main__':
	print('This is the Engine module')