guide = []
with open("./2022/day2/day2_input") as datafile:
    for line in datafile:
        guide.append(tuple(line.strip("\n").split(" ")))

# point guidelines:
# loss=0, draw=3, win=6
# rock=1, paper=2, scissors=3
# points for round: shape + outcome

# shape guidelines:
# opponent: rock=A, paper=B, scissors=C
# player: rock=X, paper=Y, scissors=Z

# step 1
opponent_shape = ["A", "B", "C"]
player_shape = ["X", "Y", "Z"]
points = 0
for round in guide:
    loss = 0
    draw = 0
    win = 0
    opponent = opponent_shape.index(round[0])
    player = player_shape.index(round[1])
    if opponent == player: # check if opponent and player chose the same shape
        draw = 1
    elif opponent_shape[player-2] == round[0]: # player's shape loses if it's two spots "ahead of" the opponents
        loss = 1
    else: # if previous two conditions aren't met the only result left is win
        win = 1
    points += (player + 1) + draw*3 + win*6

print("Final score(step 1):", points)


# step 2

# new guidelines:
# player: X=loss, Y=draw, Z=win
round_result = ["X", "Y", "Z"]
points = 0
for round in guide:
    loss = 0
    draw = 0
    win = 0
    opponent = opponent_shape.index(round[0])
    result = round_result.index(round[1])
    if result == 0:
        loss = 1
        player = player_shape.index(player_shape[opponent - 1]) # converts possible negative index into one that can be used in the final calculation, not pretty but it works
    elif result == 1:
        draw = 1
        player = opponent
    else:
        win = 1
        player = player_shape.index(player_shape[opponent - 2])
    points += (player + 1) + draw*3 + win*6

print("Final score(step 2)", points)