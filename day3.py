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



if __name__ == "__main__":
    partone()