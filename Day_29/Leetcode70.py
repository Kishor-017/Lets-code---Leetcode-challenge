class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=2
        c=0
        count=2
        if n==1:
            return a
        if n==2:
            return b
        else:
            while count<n:
                c=a+b
                a=b
                b=c
                count+=1
        return c
