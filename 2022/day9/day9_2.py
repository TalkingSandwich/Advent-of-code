import numpy as np

# read moves
def readMoves(filepath):
    moves = []
    with open(filepath) as file:
        for line in file:
            this_move = line.strip("\n").split(" ")
            this_move[1] = int(this_move[1])
            moves.append(tuple(this_move))
    return moves

# create rope object
class Rope():
    head = "H"
    tail = "T"

    def addRope(self):
        self.moves_made = 0
        self.already_visited = set()
        self.current_rope = []
        for i in range(10):
            self.current_rope.append((0,0))
    
    def checkPosit(self): # get positions of Head and Tail of rope
        return self.current_rope
    
    def checkIfRopeConnect(self, i): # check if Tail connects to the head
        rope_loc = self.checkPosit()
        knot_loc = rope_loc[i]
        prev_knot = rope_loc[i-1]
        knot_sur_area = [] # list for positions surrounding Tail
        for i in range(knot_loc[0]-1, knot_loc[0]+2):
            for j in range(knot_loc[1]-1, knot_loc[1]+2):
                knot_sur_area.append((i,j))
        does_connect = prev_knot in knot_sur_area
        return does_connect

    def updatePosit(self, direction):
        direction = direction
        head_loc = self.checkPosit()[0]
        # find new position for Head
        if direction == "U":
            new_head_loc = (head_loc[0]-1, head_loc[1])
        elif direction == "D":
            new_head_loc = (head_loc[0]+1, head_loc[1])
        elif direction == "R":
            new_head_loc = (head_loc[0], head_loc[1]+1)
        elif direction == "L":
            new_head_loc = (head_loc[0], head_loc[1]-1)
        # update Head position
        self.current_rope[0] = new_head_loc
        # update positions of knots if needed
        for i in range(len(self.current_rope)-1): # this finalised based on reddit user u/herpington 's solution
            dy = self.current_rope[i][0] - self.current_rope[i+1][0]
            dx = self.current_rope[i][1] - self.current_rope[i+1][1]
            if self.checkIfRopeConnect(i+1) == False:
                new_knot = (self.current_rope[i+1][0] + np.sign(dy), self.current_rope[i+1][1] + np.sign(dx))
                self.current_rope[i+1] = new_knot
        # add location of Tail
        self.already_visited.add(self.current_rope[-1])
        
    
    # execute a move
    def executeMove(self, move):
        direction = move[0]
        amount = move[1]
        for i in range(amount):
            self.updatePosit(direction)
    
    # return amount of positions Tail visited
    def countTailVisits(self):
        return len(self.already_visited)

# perform task for step 2
moves = readMoves("./2022/day9/day9_input")
long_rope = Rope()
long_rope.addRope()
i = 0
for move in moves:
    long_rope.executeMove(move)
print(long_rope.countTailVisits())