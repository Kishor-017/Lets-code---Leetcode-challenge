class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        small=nums[0]
        large=nums[-1]
        gcd=1
        for i in range(1,small+1):
            if small%i==0 and large%i==0:
                gcd=i
            else:
                continue
        return gcd
