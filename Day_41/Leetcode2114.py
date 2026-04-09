class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        words=0
        list=[]
        for i in range(len(sentences)):
            list=sentences[i].split()
            if len(list)>words:
                words=len(list)
        return words
            
            
