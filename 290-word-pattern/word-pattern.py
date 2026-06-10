class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        if len(set(zip(pattern,words))) == len(set(pattern)) == len(set(words)):
            return True

        else:
            return False
        