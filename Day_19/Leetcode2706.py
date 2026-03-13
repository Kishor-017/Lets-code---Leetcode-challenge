class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        n=len(prices)
        amount=0
        for i in range(n):
            for j in range(i+1,n,1):
                temp=0
                temp+=prices[i]+prices[j]
                if amount==0:
                    amount=temp
                elif amount>temp:
                    amount=temp
                else:
                    continue
        if money-amount<0:
            return money
        else:
            return money-amount
        
                
