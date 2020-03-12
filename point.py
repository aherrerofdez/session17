import inspect


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):  # getter method
        return self.x

    def distance_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def __str__(self):  # overwrites 'print'
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other):  # overwrites '=='
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other):  # overwrites '+'
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # overwrites '-'
        return Point(self.x - other.x, self.y - other.y)

    def __lt__(self, other):  # overwrites '<'
        if self.distance_origin() < other.distance_origin():
            return True
        else:
            return False

    def __len__(self):  # overwrites 'len'
        sig = inspect.signature(Point)
        return len(sig.parameters)


p = Point(3, 4)
p2 = Point(5, 6)
p3 = Point(8, 10)
p4 = Point(5, 10)
p5 = Point(5, 10)

print(p2.x, p3.y)  # 5 10
print(p.get_x())  # 3
print(p.distance_origin())  # 5.0
print(p.distance(p2))  # 2.828...
print(Point.distance(p, p2))  # 2.828...  Different syntax to call the same method as the previous one
print(p)  # <__main__.Point object at 0x0000023109AA5128>, need to create __str__ method -> (3,4)
print(p2 == p4)  # False
print(p3 == p4)  # False
print(p4 == p5)  # True
print(p + p2)  # (8, 10)
print(p3 - p2)  # (3, 4)
print((p + p2) == p3)  # True
print(p < p2)  # True
print(p3 < p)  # False
print(len(p))

# Create a list of points and print it
pts = [p, p2, p3, p4, p5]
pts_List = ''
for pt in pts:
    pts_List += pt.__str__() + ","
pts_List = pts_List[:-1]
print(pts_List)

# Sort the list of points and print it
pts.sort()
pts_List_Sorted = ''
for pt in pts:
    pts_List_Sorted += pt.__str__() + ","
pts_List_Sorted = pts_List_Sorted[:-1]
print(pts_List_Sorted)
