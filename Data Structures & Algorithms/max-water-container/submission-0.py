class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxi = 0
        while r > l:
            
            volume = min(heights[l] ,heights[r]) * (r - l)

            if volume > maxi:
                maxi = volume
            
            if heights[l] > heights [r]:
                r -= 1
            else:
                l += 1
        

        return maxi


        