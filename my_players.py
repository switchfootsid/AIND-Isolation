from isolation import Board 

player1 = RandomPlayer() # search algorithm, hacks, heuristic function
player2 = GreedyPlayer() # minimax with alpha-beta pruning, # my_moves

game = Board(player1, player2) #initialize the model of the Board

"""
1. Initialize game board and maintain player order = pass player1, player2 
2. Get legal moves for current player and algorithm it!
3. Maintain the player order
4. Print the game board 
5. Repeat until game ends
"""
#-----------#

def minimax(self, game, depth, maximizing_player=True):

	if maximizing_player==True:
		eval_func = max 
		score, best_move = float('-inf'), (-1,-1)
	else:
		eval_func = min
		score, best_move = float('inf'), (-1,-1)
	
	if depth == 0:
		#base case of recursion
		return self.scoring_func(game, player), (-1,-1)
	
	for move in game.get_legal_moves():
		new_game = game.forecast(move)
		maximizing_player = not maximizing_player #flip
		score_ret, move_ret = self.minimax(new_game, depth-1, maximizing_player)
		score, best_move = eval_func((score, best_move), (score_ret, move))
	return score, best_move


def min_value(self, game, depth, maximizing_player=True):



def max_value(self, game, depth, maximizing_player=True):

