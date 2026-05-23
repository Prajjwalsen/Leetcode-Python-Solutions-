import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:

        if val in self.pos:
            return False

        self.pos[val] = len(self.nums)
        self.nums.append(val)

        return True

    def remove(self, val: int) -> bool:

        if val not in self.pos:
            return False

        idx = self.pos[val]
        last = self.nums[-1]

        # swap with last element
        self.nums[idx] = last
        self.pos[last] = idx

        # remove last
        self.nums.pop()

        # delete from hashmap
        del self.pos[val]

        return True

    def getRandom(self) -> int:

        return random.choice(self.nums)