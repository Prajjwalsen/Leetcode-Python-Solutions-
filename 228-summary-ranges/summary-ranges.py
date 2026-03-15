class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        result = []

        if len(nums) == 0:
            return []

        while i < len(nums):
            j = i + 1

            while j < len(nums) and nums[j-1] + 1 == nums[j]:
                j += 1

            if i == j - 1:
                result.append(str(nums[i]))
            else:
                result.append(str(nums[i]) + "->" + str(nums[j-1]))

            i = j

        return result