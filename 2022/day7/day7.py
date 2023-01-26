data = []
with open("./2022/day7/day7_input") as datafile:
    for line in datafile:
        data.append(line.strip("\n"))

sizes = {}
path = []
for command in data:
    if command.startswith("$ ls") or command.startswith("dir"):
        continue
    if command.split()[0] == "$":
        current_dir = command.split()[2]
        if current_dir == "..":
            path.pop()
        else:
            if path:
                path.append(f"{path[-1]}/{current_dir}")
            else:
                path.append(current_dir)
    else:
        size, file = command.split()
        for dir in path:
            if dir in sizes:
                sizes[dir] += int(size)
            else:
                sizes[dir] = int(size)

total_small_sizes = 0
for dir in sizes:
    if sizes[dir] <= 100000:
        total_small_sizes += sizes[dir]

# step 1
print(total_small_sizes)

#step 2
required = 30000000 - (70000000 - sizes["/"])
viable_directories = []
for dir in sizes:
    if sizes[dir] >= required:
        viable_directories.append(sizes[dir])
viable_directories.sort()
print(viable_directories[0])


# Answer mostly stolen from reddit user silentwolf_01 https://github.com/silentw0lf/advent_of_code_2022/blob/main/07/solve.py