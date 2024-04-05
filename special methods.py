class Operators:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self):
        return self.x + self.y
    def __sub__(self):
        return self.x-self.y

v1 = Operators(3, 6).__add__(),Operators(3,6).__sub__()

print(v1)

