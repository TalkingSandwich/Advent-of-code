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
        self.current_head = (0,0)
        self.current_tail = (0,0)
    
    def checkPosit(self): # get positions of Head and Tail of rope
        return self.current_head, self.current_tail
    
    def checkIfTailConnect(self): # check if Tail connects to the head
        head_loc, tail_loc = self.checkPosit()
        tail_sur_area = [] # list for positions surrounding Tail
        for i in range(tail_loc[0]-1, tail_loc[0]+2):
            for j in range(tail_loc[1]-1, tail_loc[1]+2):
                tail_sur_area.append((i,j))
        does_connect = head_loc in tail_sur_area
        return does_connect

    def updatePosit(self, direction):
        direction = direction
        head_loc, tail_loc = self.checkPosit()
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
        self.current_head = new_head_loc
        # update Tail position if needed
        does_connect = self.checkIfTailConnect()
        if does_connect == False:
            self.already_visited.add(self.current_tail)
            self.current_tail = head_loc
        
    
    # execute a move
    def executeMove(self, move):
        direction = move[0]
        amount = move[1]
        for i in range(amount):
            self.updatePosit(direction)
    
    # return amount of positions Tail visited
    def countTailVisits(self):
        return len(self.already_visited)

# carry out solution for step 1
moves = readMoves("./2022/day9/day9_input")
rope = Rope()
rope.addRope()
for move in moves:
    rope.executeMove(move)
print(rope.countTailVisits())