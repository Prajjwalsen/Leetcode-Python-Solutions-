class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False 
        mapping = {}
        for i,j in zip(s,t):
            mapping[i] = j
        if(len(set(mapping.values())) != len(mapping.values())):
            return False
        newstr = ''
        for i in s:
            newstr += mapping[i]
        if (newstr == t):
            return True
        else:
            return False
        