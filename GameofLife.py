'''This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).'''
def main():
    rows = len(board)
    cols = len(board[0])
    dupBoard = [[board[row][col] for col in range(cols)] for row in range(rows)]
    for i in range(rows):
        for j in range(cols):
            di = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1),
                  (i + 1, j + 1)]
            noOfOnes = 0
            for d in di:
                x = d[0]
                y = d[1]
                if (x >= 0 and x < rows) and (y >= 0 and y < cols) and (dupBoard[x][y] == 1):
                    noOfOnes += 1
            if noOfOnes == 3 and dupBoard[i][j] == 0:
                board[i][j] = 1
            elif (noOfOnes < 2 or noOfOnes > 3) and dupBoard[i][j] == 1:
                board[i][j] = 0
if __name__ == "__main__":
    main()