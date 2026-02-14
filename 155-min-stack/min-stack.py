class MinStack:

    def __init__(self):
        self.stk=[]
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        

    def pop(self) -> None:
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        m = self.stk[0]
        for i in self.stk:
            if (i<m):
                m = i
        return m


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()