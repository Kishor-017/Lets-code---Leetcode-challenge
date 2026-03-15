class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper()==True:
            return True
        elif word.islower()==True:
            return True
        elif word[0].isupper()==True:
            for i in range(1,len(word)):
                if word[i].isupper()==True:
                    return False
                    break
                elif i==len(word)-1:
                    return True
                else:
                    continue
        else:
            return False

        
