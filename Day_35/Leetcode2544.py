class Solution:
    def alternateDigitSum(self, n: int) -> int:
        num=str(n)
        sum=0
        for i in range(0,len(num),2):
            sum=sum+int(num[i])
        for i in range(1,len(num),2):
            sum=sum-int(num[i])
        return sum
