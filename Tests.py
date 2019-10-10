

def test_func(exp_result, new_result, test_id):
	if exp_result == new_result:
		print('PASSED', test_id)
	else:
		print('FAILED', test_id)
		print('Expected:')
		print(exp_result)
		print('Actual:')
		print(new_result)


if __name__ == '__main__':
	
	import engine as en
	import AI as ai

	#testing WINNER

	# playing = 'O'

	# clean_board = en.new_board()
	# en.render(clean_board)
	
	# res_1 = en.get_winner(clean_board, playing)
	# test_func(None, res_1, '1')
	
	# new_2 = [['O' for x in range(3)] for x in range(3)]
	# en.render(new_2)
	# res_2 = en.get_winner(new_2, playing)
	# test_func('O', res_2, '2')
	
	# new_3 = [['O', 'O', 'X'],
	# 		['X', 'X', 'O'],
	# 		['O', 'X', 'O']]
	# en.render(new_3)
	# res_3 = en.get_winner(new_3, playing)
	# test_func(None, res_3, '3')

	# #AI tests
	# print('4')
	# print(ai.random_ai(clean_board, 'X'))

	# print('5')

	# new_5 = [['O', 'O', 'X'],
	# 		['X', 'X', None],
	# 		['O', 'X', 'O']]

	# print(ai.random_ai(new_5, 'X'))

	# playing = 'X'

	
	# new_6 = [['O', 'O', 'X'],
	# 		['X', 'X', None],
	# 		['O', 'X', 'O']]


	# print('minmax_score X')
	# score = ai.minmax_score(new_6, playing, playing)
	# test_func(10, score, '6')
	
	# print('minmax_ai')
	# score =ai.minmax_ai(new_6, playing)
	# test_func((2, 3), score, '7')
	
	# playing = 'O'
	# print('minmax_score O')
	# score = ai.minmax_score(new_6, playing, playing)
	# test_func(0, score, '8')
	
	# print('minmax_ai O')
	# score = ai.minmax_ai(new_6, playing)
	# test_func((2 , 3), score, '9')

	new_7 = [['X', 'O', 'O'],
  			[None, 'O', 'X'],
  			['X', None, 'O']]


	en.render(new_7)
	playing = 'X'
	print('minmax_score X')
	score = ai.minmax_score(new_7, playing, playing)
	test_func(10, score, '10')
	
	print('minmax_ai')
	score =ai.minmax_ai(new_7, playing)
	test_func((2, 1), score, '11')
	print('\n')
	playing = 'O'
	print('minmax_score O')
	score = ai.minmax_score(new_7, playing, playing)
	test_func(10, score, '12')
	
	print('minmax_ai O')
	score = ai.minmax_ai(new_7, playing)
	test_func((3 , 2), score, '13')

