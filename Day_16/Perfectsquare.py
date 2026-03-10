class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqroot=num**0.5
        if sqroot%1==0:
            return True
        else:
            return False
