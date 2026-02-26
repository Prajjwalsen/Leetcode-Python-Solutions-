class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0

        # traverse from right to left (except first bit)
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i]) + carry

            if bit == 1:
                # odd → add 1 then divide
                steps += 2
                carry = 1
            else:
                # even → divide by 2
                steps += 1

        # if carry remains, one extra step
        return steps + carry