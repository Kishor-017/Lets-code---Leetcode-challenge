class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey=="type":
            key=0
        elif ruleKey=="color":
            key=1
        else:
            key=2
        count=0
        for i in range(len(items)):
            if items[i][key]==ruleValue:
                count+=1
            else:
                continue
        return count
            
        
