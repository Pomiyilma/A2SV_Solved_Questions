import random

class RandomizedSet:                #exONnb

    def __init__(self):
        self.values = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False

        self.values.append(val)
        self.indices[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False

        remove_index = self.indices[val]
        last_val = self.values[-1]

        self.values[remove_index] = last_val
        self.indices[last_val] = remove_index

        self.values.pop()
        del self.indices[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
