import math

with open("inputs/day2.txt", "r") as f:
    INPUT = f.read()

def partone():
    ranges = INPUT.split(",")
    invalidIDsum = 0
    for rangE in ranges:
        twonums = list(map(int, rangE.split("-")))
        nums = range(twonums[0], twonums[1]+1)
        for num in nums:
            Num = str(num) # me when trying to name variables: "how can i make this the most unreadable code possible?" 
            num1, num2 = Num[0:len(Num)//2], Num[len(Num)//2:]  #              (yes num and Num are seperate variables)
            if num1 == num2:
                invalidIDsum += num
    print(invalidIDsum)

def parttwo():
    ranges = INPUT.split(",")
    invalidIDsum = 0
    for rangE in ranges:
        twonums = list(map(int, rangE.split("-")))
        nums = range(twonums[0], twonums[1]+1)
        for num in nums:
            Num = str(num)  
            half = math.ceil(len(Num)/2)
            for x in range(half):
                potStr = Num[:x+1]
                if len(Num) % len(potStr) == 0:
                    if Num == potStr*(len(Num)//len(potStr)) and len(Num)//len(potStr) != 1:
                        invalidIDsum += num
                        break
    print(invalidIDsum)


if __name__ == "__main__":
    partone()
    parttwo()