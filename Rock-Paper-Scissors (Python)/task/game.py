# Write your code here
import random

random.seed(999)

game_options = ["rock", "paper", "scissors"]
game_commands = ["!exit", "!rating"]

player_name = input("Enter your name: ")
print(f"Hello, {player_name}!")

user_game_choices = input()

if user_game_choices:
	game_options = user_game_choices.split(",")

if len(game_options) == 0:
	game_options = ["scissors", "paper", "rock"]

print("Okay, let's start")

rating_file = open('rating.txt')

score = 0

for line in rating_file:
	line = line.strip().split(' ')
	if line[0] == player_name:
		score = int(line[1])

rating_file.close()


def get_bot_winning_options(game_moves, player_move):
	max_index = (game_moves.index(player_move) + (len(game_moves) - 1) // 2) % len(game_moves)
	bot_winning_indices = [max_index - k for k in range((len(game_moves) - 1) // 2)]

	bot_winning_options = list()
	for index in bot_winning_indices:
		bot_winning_options.append(game_moves[index])

	return bot_winning_options


while True:
	player_input = input()

	if not (player_input in game_options or player_input in game_commands):
		print("Invalid input")
		continue

	if player_input == "!exit":
		print("Bye!")
		break

	if player_input == "!rating":
		print(f"Your rating: {score}")
		continue

	# playing a move
	bot_move = random.choice(game_options)

	if player_input == bot_move:
		# Draw
		print(f"There is a draw ({bot_move})")
		score += 50
	else:
		if bot_move in get_bot_winning_options(game_options, player_input):
			# User Defeated
			print(f"Sorry, but the computer chose {bot_move}")
		else:
			# User Wins
			score += 100
			print(f"Well done. The computer chose {bot_move} and failed")
