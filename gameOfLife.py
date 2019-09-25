import numpy as np
import matplotlib.pyplot as plt
import sys

# setting up the values for the board 
ALIVE = 1
DEAD = 0
vals = [ALIVE, DEAD]

class GameOfLifeEngine:
    def __init__(self, board):
        self.state = board
    
    def countNeighbors(self):
        cell = self.state
        total_neighbors = (cell[0:-2, 0:-2] + cell[0:-2, 1:-1] + cell[0:-2, 2:] +
                            cell[1:-1, 0:-2] + cell[1:-1, 2:] + cell[2:, 0:-2] +
                            cell[2:, 1:-1] + cell[2:, 2:])
        return total_neighbors

    def applyGameRules(self):
        total_neighbors = self.countNeighbors()
        cell = self.state
        birth = (total_neighbors == 3) & (cell[1:-1, 1:-1] == 0)
        survive = ((total_neighbors == 2) | (total_neighbors == 3)) & (cell[1:-1, 1:-1] == 1)
        cell[...] = DEAD
        cell[1:-1, 1:-1][birth | survive] = ALIVE
        nBirth = np.sum(birth)
        self.nBirth = nBirth
        nSurvive = np.sum(survive)
        self.nSurvive = nSurvive
        return cell

def main():
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as initial_data:
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
            engine = GameOfLifeEngine(board)
            generation = 0
            while True:
                if generation == 0:
                    plt.ion()
                generation += 1
                plt.imshow(board, cmap='binary')
                plt.show()
                engine.applyGameRules()
                # set up animation
                print('Generation: {} Birth: {} Survive: {}'.format(generation, engine.nBirth, engine.nSurvive))
                plt.pause(0.4)
    else:
        print("else")
        print("len(sys.argv): {}".format(len(sys.argv)))

main()
