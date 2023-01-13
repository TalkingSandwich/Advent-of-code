data = []
with open("./2022/day7/day7_input") as datafile:
    for line in datafile:
        data.append(line.strip("\n"))


print(f"Total size of small directories: {sizes}")