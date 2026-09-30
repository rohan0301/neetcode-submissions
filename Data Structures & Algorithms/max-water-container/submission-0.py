class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        area defined as j - i * min(arr[i], arr[j])
        two pointers left and right
        check which has the smaller height:
            move that pointer
        
        '''
        left, right = 0, len(heights) - 1
        maxArea = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            if maxArea < area:
                maxArea = area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea
