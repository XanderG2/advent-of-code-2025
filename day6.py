with open("inputs/day6.txt", "r") as f:
    INPUT = [line for line in f.readlines() if len(line) > 2]

def partone():
    questions = zip(*([x.strip() for x in INPUT[y].split() if x.strip() != ""] for y in range(len(INPUT))))
    total = 0
    for question in questions:
        operator = question[-1]
        total += eval(operator.join(question[:-1]))
    print(total)

def parttwo():
    #questions = zip(*[(INPUT[x][i:j] for i,j in zip(wheretosplit, wheretosplit[1:]+[None])) for x in range(len(INPUT))])
    #questions = zip(*([x for x in INPUT[y].split() if x.strip() != ""] for y in range(len(INPUT))))
    cols_to_split = []
    l = len(INPUT[0].strip())
    for i in range(l):
        okay = True
        for line in INPUT:
            try:
                if line[i] != " ":
                    okay = False
            except:
                print(line, i)
                exit()
        if okay:
            cols_to_split.append(i)
    cols_to_split.append(l+1)

    def splitLine(line, points):
        s = 0
        arr = []
        for point in points:
            arr.append(line[s:point])
            s = point+1
        return arr
    
    values = [splitLine(l, cols_to_split) for l in INPUT]
    questions = zip(*values)
    total = 0
    realquestions = []
    for question in questions:
        realquestion = []
        operator = question[-1]
        nums = question[:-1]
        for x in range(len(nums[0])):
            currentnum = []
            for num in nums:
                if len(num) >= x+1:
                    currentnum.append(num[-(x+1)])
            realquestion.append("".join(currentnum))
        realquestion.append(operator)
        realquestions.append(realquestion)
    for question in realquestions:
        operator = question[-1]
        answer = eval(operator.join(question[:-1]))
        total += answer
        print(question, answer)
    print(total)



if __name__ == "__main__":
    parttwo()