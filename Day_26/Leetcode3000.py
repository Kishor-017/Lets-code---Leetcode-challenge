class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        temp=0
        for i in range(len(dimensions)):
            diagonal=(((dimensions[i][0])**2)+((dimensions[i][1])**2))**1/2
            if diagonal>temp:
                temp=diagonal
                area=dimensions[i][0]*dimensions[i][1]
            elif diagonal==temp:
                area2=dimensions[i][0]*dimensions[i][1]
                if area2>area:
                    area=area2
            else:
                continue
        return area
