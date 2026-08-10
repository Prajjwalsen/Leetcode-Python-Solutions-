class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        check_num = ''
        for i in num:
            check_num += i
        
        if(check_num == check_num[::-1]):
            return True
        
        return False