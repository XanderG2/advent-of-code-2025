import math

with open("inputs/day2.txt", "r") as f:
    INPUT: str = f.read()

def partone():
    """Check ranges of numbers for numbers that are made of another number repeating twice.
       For example, 123123, 22, 1515"""
    ranges: list[str] = INPUT.split(",") # whole list of ranges, as a list of strings like ["0-2", "5-8"]
    invalidIDsum: int = 0
    for rangeStr in ranges:
        twonums: list[int] = list(map(int, rangeStr.split("-"))) # the upper and lower bound of the range (like: [0, 2])
        nums: range = range(twonums[0], twonums[1]+1)
        for numberInt in nums:
            numberStr: str = str(numberInt)
            num1: str = numberStr[0:len(numberStr)//2] # the first half of the number
            num2: str = numberStr[len(numberStr)//2:] # the second half of the number
            if num1 == num2: # check if number is a doubly repeated number
                invalidIDsum += numberInt # if so, add the number to the sum
    print(invalidIDsum)

def parttwo():
    """Check ranges of numbers for numbers that are made of another number repeating twice or more.
       For example, 123123, 222, 131313"""
    ranges: list[str] = INPUT.split(",") # whole list of ranges, as a list of strings like ["0-2", "5-8"]
    invalidIDsum: int = 0
    for rangeStr in ranges:
        twonums: list[int] = list(map(int, rangeStr.split("-"))) # the upper and lower bound of the range (like: [0, 2])
        nums: range = range(twonums[0], twonums[1]+1)
        for num in nums:
            numberStr: str = str(num)  
            half: int = math.ceil(len(numberStr)/2) # Half the length of the number, rounded up
            for x in range(half):
                potStr: str = numberStr[:x+1] # Potential number that repeated, could make the full number, as a string (potential string)
                if len(numberStr) % len(potStr) == 0: # Check if the potential string can actually be multiplied to make the number
                    if numberStr == potStr*(len(numberStr)//len(potStr)) and len(numberStr)//len(potStr) != 1: # if the number is the potential string repeated,
                        invalidIDsum += num # add the number to the sum                                           and its not just the potential string repeated once
                        break
    print(invalidIDsum)


if __name__ == "__main__":
    partone()
    parttwo()