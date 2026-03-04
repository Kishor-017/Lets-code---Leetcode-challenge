class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count=0
        r=moves.count("R")
        l=moves.count("L")
        if r>=l or l==0:
            moves=moves.replace("_","R")
        else:
            moves=moves.replace("_","L")
        for i in range(len(moves)):
            if moves[i]=="R":
                count+=1
            else:
                count-=1
        if count>=0:
            return count
        else:
            return count*-1
