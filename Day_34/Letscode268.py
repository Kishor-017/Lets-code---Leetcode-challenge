class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0]!=0:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i]-nums[i-1]>1:
                    return nums[i]-1
                    break
                elif i==len(nums)-1:
                    return nums[-1]+1
                else:
                    continue
            
        
