import itertools
from collections import deque

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

def parseline(line):
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
    joltage = [int(x) for x in line.split('{')[1].strip()[:-1].split(",")]
    return indicator, buttons, joltage

def partone():
    totalPresses = 0
    for line in INPUT:
        indicator, buttons, _ = parseline(line)
        totalPresses += pressButtons(indicator, buttons)
    print(totalPresses)

def pressButtonsJoltage(joltagerequirements, buttons): # incredible, INCREDIBLY slow; works
    totalreqs = len(joltagerequirements)
    buttonEffects = []
    for button in buttons:
        effect = [0]*totalreqs
        for i in button:
            effect[i] = 1
        buttonEffects.append(effect)
    start = tuple([0]*totalreqs)
    todo = deque([(start, 0)])
    seen = {start: 0}
    while todo:
        current, presses = todo.popleft()
        if current == tuple(joltagerequirements):
            return presses
        for eff in buttonEffects:
            newState = tuple(min(current[i] + eff[i], joltagerequirements[i]) for i in range(totalreqs))
            if newState not in seen or presses + 1 < seen[newState]:
                seen[newState] = presses + 1
                todo.append((newState, presses + 1))
    exit("This shouldnt happen btw (infinite presses ig?)")


def parttwo():
    totalPresses = 0
    for line in INPUT:
        _, buttons, targets = parseline(line)
        totalPresses += pressButtonsJoltage(targets, buttons)
    print(totalPresses)


if __name__ == "__main__":
    partone()
    parttwo()
