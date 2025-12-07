with open("inputs/day7.txt", "r") as f:
    INPUT = f.readlines()

def partone():
    grid = INPUT[:]
    start = grid[0].index("S")
    grid[1] = grid[1][:start] + "|" + grid[1][start+1:]
    splits = 0
    for row in range(1, len(grid)):
        newrow = list(grid[row])
        for col in range(len(newrow)):
            if grid[row-1][col] == "|":
                if newrow[col] == ".":
                    newrow[col] = "|"
                elif newrow[col] == "^":
                    splits += 1
                    newrow[col-1] = "|"
                    newrow[col+1] = "|"
        grid[row] = "".join(newrow)
    print(splits)

if __name__ == "__main__":
    partone()