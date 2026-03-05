class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        prod=1
        rem=0
        while n>0:
            rem=n%10
            n=n//10
            sum=sum+rem
            prod=prod*rem
        diff=prod-sum
        return diff
