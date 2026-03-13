class Solution:
    def SumOfDigits(num):
        SOD = 0
        for i in str(num):
            SOD+=int(i)
        return SOD
    def addDigits(self, num: int) -> int:
        while(len(str(num))!=1):
            num = Solution.SumOfDigits(num)
        return num
        