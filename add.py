class Addition:
    def __init__ (self,x,y):
         self.x=x
         self.y=y
    def __add__(self):
        return self.x+ self.y
add1 = Addition(4,6)
result=add1.__add__()
print(result)

