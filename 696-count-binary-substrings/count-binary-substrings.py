class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0          # previous group length
        curr = 1          # current group length
        result = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                result += min(prev, curr)
                prev = curr
                curr = 1

        # last group comparison
        result += min(prev, curr)

        return result
