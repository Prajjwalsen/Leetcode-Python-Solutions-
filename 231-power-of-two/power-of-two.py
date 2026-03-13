class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        binary=bin(n).replace('0b','')
        if(n>=0 and binary.count('1')==1):
            return True
        return False
        