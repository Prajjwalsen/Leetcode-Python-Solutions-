class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst = [i*i for i in nums]
        lst.sort()
        return lst 
        