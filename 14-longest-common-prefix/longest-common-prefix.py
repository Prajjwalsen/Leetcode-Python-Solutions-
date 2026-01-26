class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in strs:
            if len(i) < len(prefix):
                prefix = i

        need = len(strs)

        while prefix:
            count = 0
            for i in strs:
                if prefix == i[:len(prefix)]:
                    count += 1

            if count == need:
                return prefix

            prefix = prefix[:-1]

        return ""
