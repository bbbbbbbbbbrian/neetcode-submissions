class MyHashMap:

    def __init__(self):
        self.vals = []
        self.keys = []

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.keys.append(key)
            self.vals.append([key,value])
        else:
            for i in range(len(self.vals)):
                if self.vals[i][0] == key:
                    self.vals[i][1] = value

    def get(self, key: int) -> int:
        for i in range(len(self.vals)):
            if self.vals[i][0] == key:
                return self.vals[i][1]
        return -1

    def remove(self, key: int) -> None:
        idx = 0
        while idx < len(self.vals):
            if self.vals[idx][0] == key:
                self.keys.remove(key)
                self.vals.pop(idx)
                idx -= 1
            idx += 1




# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)