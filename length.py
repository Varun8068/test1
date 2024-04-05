class Length:
    def __init__(self,data):
        self.data=data
    def __len__(self):
        return len(self.data)
result=Length([1,2,3,4,6,7,8,9])
print(len(result))