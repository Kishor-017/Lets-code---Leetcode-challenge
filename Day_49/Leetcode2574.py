class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        finalnums=[]
        for i in range(len(nums)):
            leftsum=rightsum=0
            for j in range(i+1,len(nums)):
                rightsum+=nums[j]
            for j in range(i-1,-1,-1):
                leftsum+=nums[j]
            finalnums.append(abs(leftsum-rightsum))
        return finalnums
        
                
            
                
        
