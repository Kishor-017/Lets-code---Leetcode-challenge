class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        l=len(nums)
        Alice=[]
        Bob=[]
        nums.sort()
        for i in range(0,l,2):
            Alice.append(nums[i])
        for i in range(1,l,2):
            Bob.append(nums[i])
        for i in range(int(l/2)):
            arr.append(Bob[i])
            arr.append(Alice[i])
        return arr
