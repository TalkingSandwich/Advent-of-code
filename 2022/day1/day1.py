# getting data from file
data = []
with open("./2022/day1/day1_input.txt") as datafile:
    temporary_list = []
    for line in datafile:
        if line == "\n": # skip empty lines and add the inventory of one elf to final list
            data.append(temporary_list)
            temporary_list = []
            continue
        temporary_list.append(int(line.strip("\n")))

def findLargestTotal(list):
    largest = 0
    for i in range(len(list)):
        total = sum(list[i])
        if total > largest:
            largest = total
    return(largest)

def findThreeLargest(list):
    three_largest = [0, 0, 0]
    for i in range(3):
        three_largest[i] = sum(list[i])
    for i in range(3, len(list)):
        total = sum(list[i])
        if total > three_largest[0]:
            three_largest[2] = three_largest[1]
            three_largest[1] = three_largest[0]
            three_largest[0] = total
            continue
        if total > three_largest[1]:
            three_largest[2] = three_largest[1]
            three_largest[1] = total
            continue
        if total > three_largest[2]:
            three_largest[2] = total
            continue
    return(sum(three_largest))
    

print("Most number of calories is:", findLargestTotal(data))
print("Calories held by top three elfs:", findThreeLargest(data))