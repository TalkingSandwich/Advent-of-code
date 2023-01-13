def start():
    with open("./2022/day5/day5_input") as datafile:
        crates = []
        instructions = []
        split = False
        for line in datafile:
            if line == "\n":
                split = True
                continue
            if split == False:
                crates.append(str(line).strip("\n"))
            elif split == True:
                instructions.append(str(line).strip("\n"))
    return crates, instructions

# construct stacks
def makeStacks(crates):
    crate_numbers = crates.pop()
    stacks = []
    for i, line in enumerate(crate_numbers):
        if crate_numbers[i] != " ":
            stack = []
            for k, line in enumerate(crates):
                if line[i] != " ":
                    stack.append(line[i])
            stack.reverse() # stack gets read backwards so it needs to be reversed
            stacks.append(stack)
    return stacks

def interpretInstructions(instructions):
    new_instructions = []
    for line in instructions:
        instr = {} # why are they named like this?
        uction = line.split(" ") # because fuck you
        instr["move"] = int(uction[1])
        instr["from"] = int(uction[3])
        instr["to"] = int(uction[5])
        new_instructions.append(instr)
    return new_instructions

def performInstructionsOne(stacks, instructions):
    for line in instructions:
        for i in range(line["move"]):
            stacks[line["to"] - 1].append(stacks[line["from"] - 1].pop())

def performInstructionsTwo(stacks, instructions):
    for line in instructions:
        crane = []
        for i in range(line["move"]):
            crane.append(stacks[line["from"] - 1].pop())
        crane.reverse()
        stacks[line["to"] - 1].extend(crane)

def getAnswer(stacks):
    answer = ""
    for stack in stacks:
        answer += stack[-1]
    return answer

# step1
# initialise script
crates, instructions = start()
# process data
stacks = makeStacks(crates)
instructions = interpretInstructions(instructions)
# perform operations dictated in the input
""" performInstructionsOne(stacks, instructions)
print(f"Step 1 answer: {getAnswer(stacks)}") """

# step 2
performInstructionsTwo(stacks, instructions)
print(f"Step 2 answer: {getAnswer(stacks)}")