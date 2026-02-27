class Solution:
    def isThree(self, n: int) -> bool:
        flag=0
        for i in range(1,n+1):
            if n%i==0:
                flag=flag+1
                if flag>3:
                    return False
                    break
            else:
                continue
        if flag==3:
            return True
        else:
            return False
