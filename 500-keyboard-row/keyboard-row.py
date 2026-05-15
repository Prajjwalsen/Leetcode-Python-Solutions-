class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        row_num = {}

        for i in range(97,123):
            belongs = 0
            if(chr(i) in first):
                belongs = 1
            elif(chr(i) in second):
                belongs = 2
            else:
                belongs = 3
            row_num[chr(i)] = belongs

        for each_word in words:
            lwr = each_word.lower()
            count = set()
            for char in lwr:
                count.add(row_num[char])
            if(len(count) == 1):
                result.append(each_word)
        return result

        