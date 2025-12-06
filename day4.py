with open("inputs/day4.txt", "r") as f:
    INPUT = f.readlines()

def partone():
    total = 0
    for rowI in range(len(INPUT)):
        row = INPUT[rowI]
        for charI in range(len(row)):
            char = row[charI]
            if char != "@":
                continue
            surrounding = 0
            #check horizointal:
            try:
                if row[charI-1] == "@" and charI != 0: surrounding += 1
            except IndexError:
                pass
            try:
                if row[charI+1] == "@": surrounding += 1
            except IndexError:
                pass
            #chek vertialca:
            try:
                if INPUT[rowI+1][charI] == "@": surrounding += 1
            except IndexError:
                pass
            try:
                if INPUT[rowI-1][charI] == "@" and rowI != 0: surrounding += 1
            except IndexError:
                pass
            # chjeck left diagonals:
            try:
                if INPUT[rowI+1][charI-1] == "@" and charI != 0: surrounding += 1
            except IndexError:
                pass
            try:
                if INPUT[rowI-1][charI-1] == "@" and charI != 0 and rowI != 0: surrounding += 1
            except IndexError:
                pass
            # chcek right diagonlas:
            try:
                if INPUT[rowI+1][charI+1] == "@": surrounding += 1
            except IndexError:
                pass
            try:
                if INPUT[rowI-1][charI+1] == "@" and rowI != 0: surrounding += 1
            except IndexError:
                pass
            if surrounding < 4:
                total += 1
    print(total)

def delete(grid):
    new = []
    for rowI in range(len(grid)):
        row = grid[rowI]
        newrow = []
        for charI in range(len(row)):
            char = row[charI]
            if char != "@":
                newrow.append(".")
                continue
            surrounding = 0
            #check horizointal:
            try:
                if row[charI-1] == "@" and charI != 0: surrounding += 1
            except IndexError:
                pass
            try:
                if row[charI+1] == "@": surrounding += 1
            except IndexError:
                pass
            #chek vertialca:
            try:
                if grid[rowI+1][charI] == "@": surrounding += 1
            except IndexError:
                pass
            try:
                if grid[rowI-1][charI] == "@" and rowI != 0: surrounding += 1
            except IndexError:
                pass
            # chjeck left diagonals:
            try:
                if grid[rowI+1][charI-1] == "@" and charI != 0: surrounding += 1
            except IndexError:
                pass
            try:
                if grid[rowI-1][charI-1] == "@" and charI != 0 and rowI != 0: surrounding += 1
            except IndexError:
                pass
            # chcek right diagonlas:
            try:
                if grid[rowI+1][charI+1] == "@": surrounding += 1
            except IndexError:
                pass
            try:
                if grid[rowI-1][charI+1] == "@" and rowI != 0: surrounding += 1
            except IndexError:
                pass
            char 
            if surrounding < 4:
                newrow.append(".")
                continue
            newrow.append("@")
        new.append(newrow)
    return new

def parttwo():
    total = 0
    grid = INPUT
    while True:
        newgrid = delete(grid)
        if newgrid == grid:
            break
        for rowi in range(len(newgrid)):
            row = newgrid[rowi]
            for coli in range(len(row)):
                if newgrid[rowi][coli] == "." and grid[rowi][coli] == "@":
                    total += 1
        grid = newgrid
    print(total)


if __name__ == "__main__":
    partone()
    parttwo()