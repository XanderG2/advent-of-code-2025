with open("inputs/day6.txt", "r") as f:
    INPUT = f.readlines()

def partone():
    questions = zip(*([x.strip() for x in INPUT[y].split() if x.strip() != ""] for y in range(len(INPUT))))
    total = 0
    for question in questions:
        operator = question[-1]
        total += eval(operator.join(question[:-1]))
    print(total)


if __name__ == "__main__":
    partone()