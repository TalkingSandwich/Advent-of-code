data = []
with open("./2022/day4/day4_input") as datafile:
    for line in datafile:
        line_string = line.strip("\n")
        data.append(tuple(line_string.split(",")))

def checkFullOverlap(pair1, pair2):
    pair1_startend = [int(i) for i in pair1.split("-")]
    pair2_startend = [int(i) for i in pair2.split("-")]
    
    # check if one elf's range contains the other's
    if pair1_startend[0] >= pair2_startend[0] and pair1_startend[1] <= pair2_startend[1] or pair1_startend[0] <= pair2_startend[0] and pair1_startend[1] >= pair2_startend[1]:
        return True
    return False


# perform checks for data and count how many times one elf has the other's whole range
overlap_count = 0
for pair in data:
    if checkFullOverlap(pair[0], pair[1]):
        overlap_count += 1

print("Overlap count:", overlap_count)


# step 2: check for even partial overlap

def checkPartialOverlap(pair1, pair2):
    pair1_startend = [int(i) for i in pair1.split("-")]
    pair2_startend = [int(i) for i in pair2.split("-")]

    # check for partial overlap
    pair1_range = [i for i in range(pair1_startend[0], pair1_startend[1]+1)]
    pair2_range = [i for i in range(pair2_startend[0], pair2_startend[1]+1)]

    for number in pair1_range:
        if number in pair2_range:
            return True

overlap_count = 0
for pair in data:
    if checkPartialOverlap(pair[0], pair[1]):
        overlap_count += 1

print("Partial overlap count:", overlap_count)