class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum=0
        a=x
        while x>0:
            sum=sum+x%10
            x=x//10
        if a%sum==0:
            return sum
        else:
            return -1
