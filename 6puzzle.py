from copy import deepcopy 
import heapq


class State:

    def __init__ (self, board, parent = None , distance = 0):
        self.board = board
        self.parent = parent
        self.f = 0
        self.g = distance
        self.h = 0

        if self.parent != None:
            self.g = parent.g + 1 

    def fScore(self):
        if self.parent != None:
            return (self.parent.g + 1) + (self.heuristic(self.board))
        else:
            return self.g + self.heuristic(self.board) 
 
    def printer(self):
        print("-----------------------------")
        print(f"| {self.board[0]} | {self.board[1]} | {self.board[2]} | {self.board[3]} | {self.board[4]} | {self.board[5]} | {self.board[6]} |")
        print("-----------------------------")

    def heuristic(self,current):

        count = 0

        if self.board[0] == "W":
            count = count + 1
        if self.board[1] == "W":
            count = count + 1
        if self.board[2] == "W":
            count = count + 1
        if self.board[4] == "B":
            count = count + 1
        if self.board[5] == "B":
            count = count + 1
        if self.board[6] == "B":
            count = count + 1

        return count

def generateMoveStates(state):

        temp = state.board
        que = []
        x = None

        # Finds the empty space
        for a in range(len(state.board)):
            if temp[a] == '_':
                x = a
                break        

        if x+1 <= 6:
            b = deepcopy(temp)
            b[x+1], b[x] = b[x], b[x+1]
            succ = State(b, state)
            que.append(succ)
        
        if x+2 <= 6: 
            b = deepcopy(temp)
            b[x+2], b[x] = b[x], b[x+2]
            succ = State(b, state)
            que.append(succ)
        
        if x+3 <= 6: 
            b = deepcopy(temp)
            b[x+3], b[x] = b[x], b[x+3]
            succ = State(b, state)
            que.append(succ)

        if x-1 >= 0:
            b = deepcopy(temp)
            b[x-1], b[x] = b[x], b[x-1]
            succ = State(b, state)
            que.append(succ)

        if x-2 >= 0: 
            b = deepcopy(temp)
            b[x-2], b[x] = b[x], b[x-2]
            succ = State(b, state)
            que.append(succ)
        
        if x-3 >= 0: 
            b = deepcopy(temp)
            b[x-3], b[x] = b[x], b[x-3]
            succ = State(b, state)
            que.append(succ)
    
        return que

def inClosedList(board,queue):

    for xy in queue:
        if board == xy.board:
            return True

    return False

def inOpenList(board,queue):

    for xy in queue:
        if board == xy[2].board:
            return True

    return False
 
def aStar(start):
    
    # Avoids class comparison
    compCounter = 0

    closedList = []
    openList = []

    heapq.heappush(openList,(start.fScore(), compCounter, start))
    compCounter = compCounter + 1

    # Loop while nodes are still available
    while openList:

        current = heapq.heappop(openList)
        closedList.append(current[2])

        # Exits if goal equals the current node
        if current[2].board == goal:
            print("done")
            global q 
            q = current[2]
            break 

        # Gets the possible moves (neighbours) of the current node and loops through them
        neighbours = generateMoveStates(current[2])
        for x in neighbours:

            # Skip neighbour if node is in closed
            if inClosedList(x.board,closedList):
                continue
            
            # Bulk of the algorithum
            if not inOpenList(x.board,openList):
                x.f = (current[2].g + 1) + x.heuristic(x.board)
                x.parent = current[2]
                if not inOpenList(x.board,openList):
                    heapq.heappush(openList,(x.fScore(),compCounter, x))
                    compCounter += 1

    # Output
    steps = 0
    cur = q
    while cur != start:
        cur.printer()
        cur = cur.parent
        steps += 1
        print("              |")
        print("              |")
        print("              v")
    
        
    start.printer()
    print(f"Steps To Goal: {steps}")
    
inital = ['B','B','B','_','W','W','W']
goal = ['W','W','W','_','B','B','B']

a = State(inital)
aStar(a)
