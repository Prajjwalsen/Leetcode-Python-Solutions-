class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # total binary codes needed
        need = 1 << k   # 2^k
        
        # early pruning
        if len(s) - k + 1 < need:
            return False
        
        seen = set()
        
        # sliding window
        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])
            
            # early exit
            if len(seen) == need:
                return True
        
        return False