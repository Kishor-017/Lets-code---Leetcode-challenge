class Solution:
    def sumZero(self, n: int) -> List[int]:
        a = []
        i = 1

        if n % 2 == 1:
            a.append(0)

        while len(a) < n:
            a.append(i)
            a.append(-i)
            i += 1

        return a
        
