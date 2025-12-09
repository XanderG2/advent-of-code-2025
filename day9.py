with open("inputs/day9.txt", "r") as f:
    INPUT = f.readlines()

def rectSize(ab, xy):
    distanceInX = abs(ab[0] - xy[0]) +1
    distanceInY = abs(ab[1] - xy[1]) +1
    area = distanceInX * distanceInY
    return area

def partone():
    largest = 0
    for xy in [(int(a), int(b)) for a, b in [x.strip().split(",") for x in INPUT]]:
        for ab in [(int(a), int(b)) for a, b in [x.strip().split(",") for x in INPUT]]:
            if ab == xy:
                continue
            size = rectSize(ab, xy)
            if size > largest:
                largest = size
    print(largest)

if __name__ == "__main__":
    partone()