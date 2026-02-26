class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        sum=0
        count=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            if(sum==0):
                count=count+1
            else:
                continue
        return count
