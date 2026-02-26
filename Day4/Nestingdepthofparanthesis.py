class Solution:
    def maxDepth(self, s: str) -> int:
        sum=0
        depth=0
        for i in range(len(s)):
            if s[i]=='(':
                sum=sum+1
                if sum>depth:
                    depth=sum
            elif s[i]==')':
                sum=sum-1
            else:
                continue
        return depth
