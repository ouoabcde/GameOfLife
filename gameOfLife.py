import numpy as np
import matplotlib.pyplot as plt
import sys
import random

# setting up the values for the board 
ALIVE = 1
DEAD = 0
vals = [ALIVE, DEAD]

class GameOfLifeEngine:
    def __init__(self, board):
        self.state = board
    
    def countNeighbors(self):
        state = self.state
        total_neighbors = (state[0:-2, 0:-2] + state[0:-2, 1:-1] + state[0:-2, 2:] +
                            state[1:-1, 0:-2] + state[1:-1, 2:] + state[2:, 0:-2] +
                            state[2:, 1:-1] + state[2:, 2:])
        return total_neighbors

    def applyGameRules(self):
        total_neighbors = self.countNeighbors()
        state = self.state
        birth = (total_neighbors == 3) & (state[1:-1, 1:-1] == 0)
        survive = ((total_neighbors == 2) | (total_neighbors == 3)) & (state[1:-1, 1:-1] == 1)
        state[...] = DEAD
        state[1:-1, 1:-1][birth | survive] = ALIVE
        nBirth = np.sum(birth)
        self.nBirth = nBirth
        nSurvive = np.sum(survive)
        self.nSurvive = nSurvive
        return state

def makeBoardFromFile(initial_data):
    with open(initial_data, 'r') as initial_data:
        data = initial_data.readline()
        board_size = data.split()
        NUM_ROWS = int(board_size[0])
        NUM_COLS = int(board_size[1])
        board = np.zeros(NUM_ROWS * NUM_COLS).reshape(NUM_ROWS, NUM_COLS)
        print("NUM_ROWS: {}".format(NUM_ROWS))
        print("NUM_COLS: {}".format(NUM_COLS))
        count = 1
        while data:
            print("Line {}: {}".format(count, data))
            data = initial_data.readline()
            count += 1
            if count == 2:
                NUM_CELLS_INIT = int(data)
                print("NUM_CELLS_INIT: {}".format(NUM_CELLS_INIT))
            elif 2 < count <= NUM_CELLS_INIT + 2: # now it's spots
                location = data.split()
                row = int(location[0])
                col = int(location[1])
                board[row, col] = ALIVE
        return board

def visualize(board, generation):
    engine = GameOfLifeEngine(board)
    count = 0
    while True:
        plt.title("Jung Hyun's Game of Life - Generation: {}".format(count))
        if count == 0:
            plt.ion()
        count += 1
        # show board state after the given generation
        if count >= generation:
            plt.imshow(board, cmap='binary')
            plt.show()
        engine.applyGameRules()
        # set up animation
        print('Generation: {} Birth: {} Survive: {}'.format(count, engine.nBirth, engine.nSurvive))
        plt.pause(0.3)

def randomBoard(height, width): 
    """returns a board of width x height random values"""
    return np.random.choice(vals, width * height, p=[0.2, 0.8]).reshape(height, width)

def main():
    if len(sys.argv) == 2:
        board = makeBoardFromFile(sys.argv[1])
        generation = 0
        visualize(board, generation)
    elif len(sys.argv) == 1:
        while True:
            random_width = random.randint(0, 200)
            random_height = random.randint(0, 200)
            if random_width >= 80 and random_height >= 40:
                print("random_width: {}".format(random_width))
                width = random_width
                print("random_hegiht: {}".format(random_height))
                height = random_height
                break
        board = randomBoard(height, width)
        generation = 0
        visualize(board, generation)
    elif len(sys.argv) == 3:
        board = makeBoardFromFile(sys.argv[1])
        generation = int(sys.argv[2])
        visualize(board, generation)

if __name__ == '__main__':
    main()
