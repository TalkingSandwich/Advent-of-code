data = []
with open("./2022/day3/day3_input") as datafile:
    for line in datafile:
        data.append(line.strip("\n"))

# next split each line into two compartments that can then be compared
for i in range(len(data)):
    half = len(data[i]) // 2
    A = data[i][:half]
    B = data[i][half:]
    data[i] = (A, B)

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = []
for ch in alphabet:
    letters.append(ch)

# check if letter is found in both compartments and find the item's value
total_value = 0
for sack in data:
    for i in range(len(sack[0])):
        if sack[0][i] in sack[1]:
            item_value = letters.index(sack[0][i]) +1
            total_value += item_value
            break

print("Total value of misplaced items:", total_value)


# step 2
# find matching item in each group of three elves

# compartment split isn't needed anymore
for i in range(len(data)):
    data[i] = data[i][0] + data[i][1]

total_value = 0
for i in range(0, len(data), 3):
    for j in range(len(data[i])):
        if data[i][j] in data[i+1] and data[i][j] in data[i+2]:
            item_value = letters.index(data[i][j]) +1
            total_value += item_value
            break

print("Total value of identifying badges:", total_value)