from itertools import combinations
from shapely import Polygon, box

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

def parttwo():
    redTiles = [tuple(int(x) for x in line.split(",")) for line in INPUT]
    rects = []
    for xy, ab in combinations(redTiles, 2):
        x1 = xy[0]
        x2 = ab[0]
        y1 = xy[1]
        y2 = ab[1]
        smallX, largeX = min(x1, x2), max(x1, x2)
        smallY, largeY = min(y1, y2), max(y1, y2)
        rect = (smallX, smallY, largeX, largeY)
        rects.append(rect)
    areas = [rectSize((a, b), (x, y)) for (a, b, x, y) in rects]
    greenareapolygon = Polygon(redTiles)
    boxes = (box(smallX, smallY, largeX, largeY) for (smallX, smallY, largeX, largeY) in rects)
    isboxin = [greenareapolygon.contains(x) for x in boxes]
    squares = [d for d, s in zip(areas, isboxin) if s]
    print(max(squares))

if __name__ == "__main__":
    partone()
    parttwo()