with open("inputs/day1.txt", "r") as f:
    INPUT: list[str] = f.readlines()

def partone():
    """Digest INPUT into a direction and amount to turn.
       Count the amount of times that after turning in a certain direction, the dial hits 0.
       The dial is 0-99 and wraps around.
       Only count after turning, not during"""
    zeros: int = 0
    currentNum: int = 50
    for instruction in INPUT:
        direction: str = instruction[0]
        amount: int = int(instruction[1:])
        if direction == "L":
            amount = -amount
        currentNum += amount # increase by the whole amount at once
        if currentNum % 100 == 0: # check that amount is 0 or a multiple of 100
            zeros += 1
    print(zeros)

def parttwo():
    """Digest INPUT into a direction and amount to turn.
       Count the amount of times that during or after turning in a certain direction, the dial hits 0.
       The dial is 0-99 and wraps around.
       Count during and after turning."""
    zeros: int = 0
    currentNum: int = 50
    for instruction in INPUT:
        direction: str = instruction[0]
        amount: int = int(instruction[1:])
        i: int = 1 if direction == "R" else -1
        for _ in range(amount): # increase by 1 each time
            currentNum += i
            if currentNum % 100 == 0:
                zeros += 1
    print(zeros)

if __name__ == "__main__":
    partone()
    parttwo()