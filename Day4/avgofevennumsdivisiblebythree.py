class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum=0
        count=0
        avg=0
        for i in range(len(nums)):
            if nums[i]%6==0:
                sum=sum+nums[i]
                count=count+1
            else:
                continue
        if count==0:
            return 0
        else:
            avg=sum/count
            return int(avg)
