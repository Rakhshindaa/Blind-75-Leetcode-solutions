class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxarea=0
        while left<right:
            currarea=min(height[left],height[right])*(right-left)
            maxarea=max(maxarea,currarea)
            if height[left]<height[right]:
                left=left+1
            else:
                right=right-1
        return maxarea