import random as rnd
import engine as en
import copy

def random_ai(board, playing):
	
	moves = list_moves(board)
	item = rnd.choice(moves)
	moves.remove(item)
	x, y = item
	return x, y

cache = {}

def minmax_score(board, playing_current, player):
	board_cache_key = hash_the_board(board)
	if board_cache_key in cache:
		return cache.get(board_cache_key)
	else:
		winner = en.get_winner_ai_test(board, playing_current)
		if winner is not None:
			if winner == player:
				return 10
			else:
				return -10
		elif en.is_board_free(board) == False:
				return 0
		else:
			moves = list_moves(board)
			scores = []
			for move in moves:
				new_board = en.make_move(board, move, playing_current) 
				opponent = get_opponent(playing_current)
				score = minmax_score(new_board, opponent, player)
				scores.append(score)
		if playing_current == player:
			cache[board_cache_key] = max(scores)
			# return max(scores)
		else:
			cache[board_cache_key] = min(scores)
			# return min(scores)
		return cache.get(board_cache_key)


def minmax_ai(board, playing):
	best_move = None
	best_score = None

	for move in list_moves(board):
		_board = copy.deepcopy(board)
		_board = en.make_move(_board, move, playing)
		opp = get_opponent(playing)
		score = minmax_score(_board, opp, playing)
		if best_score is None or score > best_score:
			best_move = move
			best_score = score

	return best_move


def get_opponent(playing):
	if playing == 'X':
		playing = 'O'
		return playing
	else:
		playing = 'X'
		return playing


def list_moves(board):
	moves_list = []

	for i in [0, 1, 2]:
		for j in [0, 1, 2]:
			if board[i][j] == None:
				moves_list.append((i+1, j+1))
	return moves_list


def hash_the_board(board):
	hashing = 'board_'
	for line in board:
		for cell in line:
			hashing += str(cell)
	return hashing


if __name__ == '__main__':
	print('This is AI module')