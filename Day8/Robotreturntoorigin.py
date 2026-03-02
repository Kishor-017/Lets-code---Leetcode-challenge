class Solution:
    def judgeCircle(self, moves: str) -> bool:
        a=[0,0]
        for i in range(len(moves)):
            if moves[i]=="R":
                a[0]+=1
            if moves[i]=="L":
                a[0]-=1
            if moves[i]=="U":
                a[1]+=1
            if moves[i]=="D":
                a[1]-=1
        if a[0]==0 and a[1]==0:
            return True
        else:
            return False
