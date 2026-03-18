class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = dict(Counter(s))
        count2 = dict(Counter(t))
        if(count1 == count2):
            return True 
        else:
            return False
        