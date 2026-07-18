
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        max_num = 0
        while(l < r):
            num = (r - l) * min(heights[l], heights[r])
            max_num = max(max_num, num)

            if(heights[l] < heights[r]):
                l += 1
            else:
                r -=1
            
        return max_num