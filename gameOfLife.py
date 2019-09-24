import numpy as np
import matplotlib.pyplot as plt
import sys

# setting up the values for the board 
ALIVE = 1
DEAD = 0
vals = [ALIVE, DEAD]

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as initialData:
            data = initialData.readline()
            boardSize = data.split()
            NUM_ROWS = int(boardSize[0])
            NUM_COLS = int(boardSize[1])
            board = np.zeros(NUM_ROWS * NUM_COLS).reshape(NUM_ROWS, NUM_COLS)
            print("NUM_ROWS: {}".format(NUM_ROWS))
            print("NUM_COLS: {}".format(NUM_COLS))
            count = 1
            while data:
                print("Line {}: {}".format(count, data))
                data = initialData.readline()
                count += 1
                if count == 2:
                    NUM_CELLS_INIT = int(data)
                    print("NUM_CELLS_INIT: {}".format(NUM_CELLS_INIT))
                elif 2 < count <= NUM_CELLS_INIT + 2: # now it's spots
                    location = data.split()
                    row = int(location[0])
                    col = int(location[1])
                    board[row, col] = ALIVE
    else:
        print("else")
        print("len(sys.argv): {}".format(len(sys.argv)))

    # set up animation
    plt.imshow(board, cmap='binary')
    plt.show()

main()