import random

# Function to implement the player strategy
def player(prev_play, opponent_history=[]):
    # Initialize some variables to keep track of strategy
    if prev_play == "":
        # If it's the first game, play randomly
        return random.choice(["R", "P", "S"])
    else:
        # Implement Counter Strategy
        if prev_play == "R":
            return "P"
        elif prev_play == "P":
            return "S"
        else:
            return "R"

# Function to play a match against a bot
def play_match(player1, bot, num_games):
    wins = 0
    for _ in range(num_games):
        player1_move = player1("", [])
        bot_move = bot("", [])
        result = play_round(player1_move, bot_move)
        if result == 1:
            wins += 1
    return wins / num_games

# Function to play a single round of Rock, Paper, Scissors
def play_round(move1, move2):
    if move1 == move2:
        return 0  # Tie
    elif (move1 == "R" and move2 == "S") or (move1 == "S" and move2 == "P") or (move1 == "P" and move2 == "R"):
        return 1  # Player 1 wins
    else:
        return -1  # Player 2 wins

# Bots to play against
def quincy(prev_play, opponent_history=[]):
    return "R"

def mrugesh(prev_play, opponent_history=[]):
    return random.choice(["R", "P", "S"])

def kris(prev_play, opponent_history=[]):
    most_frequent = max(["R", "P", "S"], key=opponent_history.count)
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[most_frequent]

def abbey(prev_play, opponent_history=[]):
    if len(opponent_history) == 0:
        return "R"
    else:
        return opponent_history[-1]

# Main function to test the program
def main():
    num_games = 1000
    player1 = player
    bots = [quincy, mrugesh, kris, abbey]
    for bot in bots:
        win_rate = play_match(player1, bot, num_games)
        print(f"Win rate against {bot.__name__}: {win_rate*100:.2f}%")

if __name__ == "__main__":
    main()
