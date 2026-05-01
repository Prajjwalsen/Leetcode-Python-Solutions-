class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        
        total_sum = sum(nums)
      
        f = 0
        for i in range(n):
            f += i * nums[i]
        
        max_value = f

        for k in range(1, n):
            f = f + total_sum - n * nums[n - k]
            max_value = max(max_value, f)
        
        return max_value