instructions = []

filepath = "./2022/day10/day10_input"
with open(filepath) as file:
    for line in file:
        instructions.append(line.strip("\n").split(" "))

cycle = 0
reg = 1
reg_dict = {}
for inst in instructions:
    if inst[0] == "noop":
        cycle += 1
        reg_dict[cycle] = reg
    elif inst[0] == "addx":
        # first cycle
        cycle += 1
        reg_dict[cycle] = reg
        # second cycle
        cycle += 1
        reg_dict[cycle] = reg
        reg += int(inst[1])

# find solution for step 1
signal_strengths = []
for i in range(20, 221, +40):
    strength = i * reg_dict[i]
    signal_strengths.append(strength)

print(sum(signal_strengths))

# step 2
crt_screen = []
row = ["." for _ in range(40)]
for key in reg_dict:
    if key % 40 == 0:
        crt_screen.append(row)
        row = ["." for _ in range(40)]
    sprite_loc = reg_dict[key]
    if (key % 40) -1 in [sprite_loc-1, sprite_loc, sprite_loc+1]:
        row[(key % 40) -1] = "#"

prt_screen = ""
for line in crt_screen:
    prt_line = ""
    for pixel in line:
        prt_line += pixel
    prt_line += "\n"
    prt_screen += prt_line

print(prt_screen)
