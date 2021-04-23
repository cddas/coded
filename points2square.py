class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distSq(a, b):
    return (a.x - b.x) ** 2 + (a.y - b.y) ** 2


def isSquare(quad):
    # If distance between (p1, p2) is same as (p1, p3) , then square of distance between (p1, p4) is twice the distance
    # between (p1,p2) and square of distance between (p2, p3) is twice the distance between (p2, p4)
    d1 = distSq(quad[0], quad[1])
    d2 = distSq(quad[0], quad[2])
    d3 = distSq(quad[0], quad[3])

    if any([d1, d2, d3]) == 0:
        return False
    else:
        if d1 == d2 and d3 == 2 * d1 and distSq(quad[1], quad[2]) == 2 * distSq(quad[2], quad[3]):
            return True
        elif d2 == d3 and d1 == 2 * d2 and distSq(quad[2], quad[3]) == 2 * distSq(quad[3], quad[1]):
            return True
        elif d3 == d1 and d2 == 2 * d3 and distSq(quad[1], quad[3]) == 2 * distSq(quad[1], quad[2]):
            return True
        else:
            return False


#Driver Code
if __name__=="__main__":
    points = []
    for i in range(0, 4):
        X = int(input("Enter X co-ordinates for point" + str(i + 1) + ": "))
        Y = int(input("Enter Y co-ordinates for point" + str(i + 1) + ": "))
        points.append(Point(X, Y))

    if isSquare(points):
        print("Given points form a square")
    else:
        print("Given points doesn't form a square")




