with open("inputs/day7.txt", "r") as f:
    INPUT = [x.strip() for x in f.readlines()]

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
    return grid

def parttwo():
    cache = {}
    def countRoutes(grid, r, c):
        if str([r, c]) in cache.keys():
            return cache[str([r, c])]
        char = grid[r][c]
        if char == ".":
            return 0
        if char != "|":
            exit(1)
        above = grid[r-1][c]
        if above == "S":
            return 1
        s = 0
        if above == "|":
            s += countRoutes(grid, r-2, c)
        if c > 0:
            l = grid[r-1][c-1]
            if l == "^":
                s += countRoutes(grid, r-2, c-1)
        if c < len(grid[r]) - 1:
            right = grid[r-1][c+1]
            if right == "^":
                s += countRoutes(grid, r-2, c+1)
        cache[str([r, c])] = s
        return s
    grid = partone()
    if len(grid) % 2 == 1:
        exit(1)
    r = len(grid) -1
    routes = 0
    for c in range(len(grid[-1])):
        routes += countRoutes(grid, r, c)
    print(routes)


if __name__ == "__main__":
    partone()
    parttwo()