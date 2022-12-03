# A for rock, B for paper, C for scissors:
# X for rock, Y for paper, Z for scissors
# Score for a round is the shape chosen (Rock: 1, Paper: 2, Scissors: 3) plus the score for the outcome of the round (Loss: 0, draw: 3, win: 6)
#

def translate(move):
    if move == "A" or move == "X":
        return "rock"
    if move == "B" or move == "Y":
        return "paper"
    if move == "C" or move == "Z":
        return "scissors"


def translate_outcome(outcome):
    if outcome == "X":
        return "lose"
    if outcome == "Y":
        return "draw"
    if outcome == "Z":
        return "win"


def determine_move(opponent_move, outcome):
    print(f"Opponent plays: {translate(opponent_move)} we want to {translate_outcome(outcome)}")
    if outcome == "X":  # lose
        if opponent_move == "A":  # rock
            return("Z")           # scissors
        if opponent_move == "B":  # paper
            return("X")           # rock
        if opponent_move == "C":  # scissors
            return("Y")           # paper
    if outcome == "Y":  # draw
        if opponent_move == "A":  # rock
            return("X")           # rock
        if opponent_move == "B":  # paper
            return("Y")           # paper
        if opponent_move == "C":  # scissors
            return("Z")           # scissors
    if outcome == "Z":  # win
        if opponent_move == "A":  # rock
            return("Y")           # paper
        if opponent_move == "B":  # paper
            return("Z")           # scissors
        if opponent_move == "C":  # scissors
            return("X")           # rock


def match(opponent_move, player_move):
    match_score = 0
    # Score the invdividual moves
    if player_move == "X":
        match_score = match_score + 1
    if player_move == "Y":
        match_score = match_score + 2
    if player_move == "Z":
        match_score = match_score + 3
    # Score the outcome of the match
    if opponent_move == "A":
        if player_move == "X":
            match_score = match_score + 3
        if player_move == "Y":
            match_score = match_score + 6
    if opponent_move == "B":
        if player_move == "Y":
            match_score = match_score + 3
        if player_move == "Z":
            match_score = match_score + 6
    if opponent_move == "C":
        if player_move == "X":
            match_score = match_score + 6
        if player_move == "Z":
            match_score = match_score + 3
    return match_score


def run_strat(strategy):
    total_score = 0
    for line in strategy:
        opponent_move, outcome = line.split()[0], line.split()[1]
        player_move = determine_move(opponent_move, outcome)
        print(translate(player_move))
        total_score = total_score + match(opponent_move, player_move)
    return(total_score)


f = open("input.txt", "r")
print(run_strat(f))
