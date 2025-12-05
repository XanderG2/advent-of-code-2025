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



if __name__ == "__main__":
    partone()
