

if __name__ == '__main__':
	import engine as en
	import random as rnd

	clean_board = en.new_board()
	
	en.render(clean_board)

	play_board = clean_board.copy()
	play_board = tuple(play_board)
	playing = 'O'
	game_mode = input('Human or AI game?\n1) for Human\n2) for Human v2s AI\n3) for AI vs AI\n')


	if game_mode == '1':
		
		player_1 = 3
		3

		player_2 = 'H'
		player_type = player_1
		waiting = player_2
		
		en.lets_play(play_board, playing, player_type, waiting)


	if game_mode == '2':
		ai_type = input('Choose AI type:\n1) for random\n2) for Pro\n')
		if ai_type == '1':
			ai_type = 'A'
		elif ai_type == '2':
			ai_type = 'AI'
		else:
			raise ValueError('Error, invalid AI type ', ai_type)
		#random choose sides
		options = ['H', ai_type]
		player_1 = rnd.choice(options)
		options.remove(player_1)
		player_2 = options[0]
		#1assign turn
		player_type = player_1
		waiting = player_2

		en.lets_play(play_board, playing, player_type, waiting)


	else:

		player_type = 'A'
		waiting = 'A'

		en.lets_play(play_board, playing, player_type, waiting)

