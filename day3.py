with open("inputs/day3.txt", "r") as f:
    INPUT = f.readlines()

def partone():
    totalVoltage = 0
    for banK in INPUT:
        bank = banK.strip()
        nums = []
        for numI in range(len(bank)):
            num = bank[numI]
            for num2i in range(1, len(bank)-numI):
                num2I = numI + num2i
                num2 = bank[num2I]
                nums.append(int(num+num2))
        totalVoltage += max(nums)
    print(totalVoltage)


def parttwo(): # wow so readable (i have no clue what ive written but it works (at least its not my previous part 2 (it used 64+ GB of RAM and then memory errored)))
    def findNextDig(r, x):
        amountLeft = len(r) - x
        availableToCheck = r[:amountLeft+1]
        digit = max(availableToCheck)
        indeX = r.index(digit)
        return digit, r[indeX+1:]
    totalVoltage = 0
    for line in INPUT:
        remainingStr = line.strip()
        volt = ""
        for x in range(12, 0, -1):
            num, remainingStr = findNextDig(remainingStr, x)
            volt += num
        totalVoltage += int(volt)
    print(totalVoltage)


            

if __name__ == "__main__":
    partone()
    parttwo()