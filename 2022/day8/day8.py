forest = []
with open("./2022/day8/day8_input") as file:
    for line in file:
        trees = line.strip("\n")
        row = []
        for i in range(len(trees)):
            row.append(int(trees[i]))
        forest.append(row)

# step 1: count visible trees
visible_trees = 0

# count trees on the edges
visible_trees += len(forest) * 2
visible_trees += (len(forest[0])-2) * 2

# count visible trees inside grid
def isTreeVisible(i, j, forest):
    tree = forest[i][j]
    west_visible = True
    east_visible = True
    north_visible = True
    south_visible = True
    # west
    for h in range(j):
        if forest[i][h] >= tree:
            west_visible = False
            break
    for h in range(j+1, len(forest[i])):
        if forest[i][h] >= tree:
            east_visible = False
            break
    for k in range(i):
        if forest[k][j] >= tree:
            north_visible = False
            break
    for k in range(i+1, len(forest)):
        if forest[k][j] >= tree:
            south_visible = False
            break
    if west_visible or east_visible or north_visible or south_visible:
        return True
    else:
        return False

for i in range(1, len(forest)-1):
    for j in range(1, len(forest[i])-1):
        if isTreeVisible(i, j, forest):
            visible_trees += 1

print(f"Visible trees: {visible_trees}")

# step 2: find largest viewing area
def countViewScore(i, j, forest):
    tree = forest[i][j]
    west_view = 0
    east_view = 0
    north_view = 0
    south_view = 0
    # west
    for h in range(j-1, -1, -1):
        if forest[i][h] == tree or forest[i][h] > tree:
            west_view += 1
            break
        else:
            west_view += 1
    # east
    for h in range(j+1, len(forest[i])):
        if forest[i][h] == tree or forest[i][h] > tree:
            east_view += 1
            break
        else:
            east_view += 1
    # north
    for k in range(i-1, -1, -1):
        if forest[k][j] == tree or forest[k][j] > tree:
            north_view += 1
            break
        else:
            north_view += 1
    # south
    for k in range(i+1, len(forest)):
        if forest[k][j] == tree or forest[k][j] > tree:
            south_view += 1
            break
        else:
            south_view += 1
    return west_view * east_view * north_view * south_view

view_scores = []
for i in range(len(forest)):
    for j in range(len(forest[i])):
        view_scores.append(countViewScore(i, j, forest))
view_scores.sort()
print(f"Largest view score: {view_scores[-1]}")