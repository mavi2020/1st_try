class Vector:

    def __init__(self, x, y):
        self.x = x

        self.y = y


    def __add__(a, b):
        # complete me
        new_x = a.x + b.x
        new_y = a.y + b.y
        return Vector(new_x, new_y)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x,new_y)

    def __neg__(self):
        if self.x>= 0 and self.y >=0:
            neg_x= self.x * -1
            neg_y = self.y *-1
        return Vector(neg_x, neg_y)

v1 = Vector(3, 4)

v2 = Vector(10, 1)

v3 = v1+v2
v4 = v2-v1
v5 = Vector(3,9)
v5.__neg__()
print(v4)
print(v5)
