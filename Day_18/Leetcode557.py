class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split(" ")
        b=""
        for i in range(len(a)):
            b=b+a[i][::-1]+" "
        return b.strip()
