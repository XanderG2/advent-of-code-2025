import itertools

with open("inputs/day10.txt", "r") as f:
    INPUT = [x.strip() for x in f.readlines()]

def flip(indicator, button):
    indic = indicator[:]
    for switch in button:
        indic[switch] = not indic[switch]
    return indic

def pressButtons(indicator, buttons):
    possiblebuttonpresses = []
    for r in range(1, len(buttons) + 1):
        possiblebuttonpresses.extend(itertools.combinations(buttons, r))
    least = float('inf')
    for presses in possiblebuttonpresses:
        currentI = [False] * len(indicator)
        for press in presses:
            currentI = flip(currentI, press)
        if currentI == indicator:
            if len(presses) < least:
                least = len(presses)
    return least

def parse_line(line):
    indicator = [c == '#' for c in line.split(']')[0][1:]]
    buttonsstr = line.split(']')[1].split('{')[0].strip()
    buttons = []
    for b in buttonsstr.split(')'):
        b = b.strip()
        if not b:
            continue
        b = b[1:]
        indices = tuple(int(x) for x in b.split(','))
        buttons.append(indices)
    return indicator, buttons

def partone():
    totalPresses = 0
    for line in INPUT:
        indicator, buttons = parse_line(line)
        totalPresses += pressButtons(indicator, buttons)
    print(totalPresses)

if __name__ == "__main__":
    partone()
