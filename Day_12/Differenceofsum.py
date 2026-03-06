class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum=0
        digsum=0
        diff=0
        for i in range(len(nums)):
            sum+=nums[i]
            while(nums[i]>0):
                digsum+=nums[i]%10
                nums[i]=nums[i]//10
        if(sum>digsum):
            diff=sum-digsum
        else:
            diff=digsum-sum
        return diff
