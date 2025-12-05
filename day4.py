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


if __name__ == "__main__":
    partone()