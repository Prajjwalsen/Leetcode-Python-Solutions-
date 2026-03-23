from typing import List

class Solution:
    def uniformArray(self, nums: List[int]) -> bool:
        even = 0
        odd = 0
        
        for num in nums:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
        
        if even == 0 or odd == 0:
            return True
        
        return True