class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            if a == -1:  
                return 0
            ax, ay = divmod(a, 6)
            bx, by = divmod(b, 6)
            return abs(ax - bx) + abs(ay - by)

        n = len(word)
        dp = [0] * 26  
        
        for i in range(1, n):
            curr = ord(word[i]) - ord('A')
            prev = ord(word[i - 1]) - ord('A')
            
            new_dp = [float('inf')] * 26
            
            for j in range(26):
                
                new_dp[j] = min(new_dp[j], dp[j] + dist(prev, curr))
                
                new_dp[prev] = min(new_dp[prev], dp[j] + dist(j, curr))
            
            dp = new_dp
        
        return min(dp)