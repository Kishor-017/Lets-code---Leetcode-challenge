class Solution:
    def isPalindrome(self, x: int) -> bool:
        rem=0
        a=x
        num=0
        if x<0:
            return False
        else:
            while x>0:
                rem=x%10
                x=x//10
                num=num*10+rem
        if a==num:
            return True
        else:
            return False
