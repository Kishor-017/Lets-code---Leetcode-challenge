class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=""
        for i in range(len(digits)):
            num+=str(digits[i])
        num=int(num)+1
        digits=[]
        for i in str(num):
            digits.append(int(i))
        return digits
        
        
