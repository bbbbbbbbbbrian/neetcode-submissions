class MinStack:

    def __init__(self):
        self.minimum = []
        self.data = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.minimum) == 0:
            self.minimum.append(val)
        elif self.minimum[len(self.minimum)-1] >= val:
            self.minimum.append(val)

    def pop(self) -> None:
        if len(self.minimum) == 0:
            raise IndexError
        val = self.data.pop()
        if val == self.minimum[len(self.minimum)-1]:
            self.minimum.pop()

    def top(self) -> int:
        return self.data[len(self.data)-1] 

    def getMin(self) -> int:
        return self.minimum[len(self.minimum)-1]
