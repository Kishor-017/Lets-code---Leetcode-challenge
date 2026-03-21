class Solution:
    def hammingWeight(self, n: int) -> int:
        digit=0
        set=0
        while n>0:
            if n%2==1:
                digit=(digit*10)+n%2
                set+=1
            else:
                digit=digit*100
            n=n//2
