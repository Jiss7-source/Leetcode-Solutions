class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_1=0
        right=len(height)-1
        left=0
        while left<right:
            width=right-left
            area=width * min(height[left], height[right])
            max_1=max(area,max_1)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1    
        return max_1    

        