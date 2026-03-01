class Solution:
    def isHappy(self, n: int) -> bool:
        mem=set()
        while(n != 1):
            sqrSum=0
            for i in str(n):
                sqrSum += int(i)**2
            n = sqrSum
            if(n in mem):
                return False
            else:
                mem.add(n)
        return True