with open("inputs/day1.txt", "r") as f:
    INPUT = f.readlines()

def partone():
    zeros = 0
    currentNum = 50
    for instruction in INPUT:
        direction = instruction[0]
        amount = int(instruction[1:])
        if direction == "L":
            amount = -amount
        currentNum += amount
        if str(currentNum)[-2:] == "00" or currentNum == 0: # probably like the strangest way i could think of, but it works!
            zeros += 1
    print(zeros)

if __name__ == "__main__":
    partone()